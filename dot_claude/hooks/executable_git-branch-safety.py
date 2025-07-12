#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys


def run_git_command(cmd: str) -> tuple[bool, str]:
    """Run git command and return (success, output)"""
    try:
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            cwd=os.getcwd(),
            timeout=10
        )
        return result.returncode == 0, result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.SubprocessError):
        return False, ""


def has_uncommitted_changes() -> bool:
    """Check for uncommitted changes (staged or unstaged)"""
    success, output = run_git_command("git status --porcelain")
    return success and bool(output.strip())


def has_untracked_files() -> bool:
    """Check for untracked files"""
    success, output = run_git_command("git status --porcelain")
    if not success:
        return False
    
    # Look for lines starting with '??' (untracked files)
    for line in output.split('\n'):
        if line.startswith('??'):
            return True
    return False


def get_unmerged_commits() -> list[str]:
    """Get commits on current branch not in main"""
    success, output = run_git_command("git log origin/main..HEAD --oneline")
    if not success or not output:
        return []
    return [line.strip() for line in output.split('\n') if line.strip()]


def get_unpushed_commits() -> list[str]:
    """Get commits not pushed to remote"""
    # First get current branch
    success, branch = run_git_command("git branch --show-current")
    if not success or not branch:
        return []
    
    # Check for unpushed commits
    success, output = run_git_command(f"git log origin/{branch}..HEAD --oneline")
    if not success or not output:
        return []
    return [line.strip() for line in output.split('\n') if line.strip()]


def has_open_pr() -> bool:
    """Check if current branch has an open PR using gh CLI"""
    try:
        result = subprocess.run(
            ["gh", "pr", "view", "--json", "state"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("state") == "OPEN"
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, json.JSONDecodeError):
        pass
    return False


def check_force_override() -> bool:
    """Check if user wants to force override the safety check"""
    return os.environ.get("CLAUDE_FORCE_BRANCH_SWITCH") == "1"


def is_git_checkout_command(command: str) -> bool:
    """Check if command is a git checkout or switch operation"""
    patterns = [
        r'\bgit\s+checkout\s+\S+',
        r'\bgit\s+switch\s+\S+',
    ]
    return any(re.search(pattern, command) for pattern in patterns)


def validate_git_operation(command: str) -> list[str]:
    """Validate git operation and return list of issues"""
    if not is_git_checkout_command(command):
        return []
    
    # Check for force override first
    if check_force_override():
        return []
    
    issues = []
    
    # Check for uncommitted changes
    if has_uncommitted_changes():
        issues.append("You have uncommitted changes. Consider: git commit, git stash, or git add + git commit")
        return issues  # Early return - this is always blocking
    
    # Check for untracked files
    if has_untracked_files():
        issues.append("You have untracked files. Consider: git add + git commit, or git clean -f if unwanted")
        return issues  # Early return - this is always blocking
    
    # Check for unmerged commits
    unmerged_commits = get_unmerged_commits()
    if unmerged_commits:
        has_pr = has_open_pr()
        
        if not has_pr:
            issues.append(f"Branch has {len(unmerged_commits)} unmerged commits but no PR. Consider creating PR or merging to main")
        else:
            # Has PR, check for unpushed commits
            unpushed_commits = get_unpushed_commits()
            if unpushed_commits:
                issues.append(f"Branch has PR but {len(unpushed_commits)} unpushed commits. Consider: git push")
    
    # Add override hint if we're blocking
    if issues:
        issues.append("To override: CLAUDE_FORCE_BRANCH_SWITCH=1 " + command)
    
    return issues


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    if tool_name != "Bash" or not command:
        sys.exit(0)  # Not our concern

    # Validate the git operation
    issues = validate_git_operation(command)

    if issues:
        print("🚨 Git Branch Safety Check:", file=sys.stderr)
        for issue in issues:
            print(f"• {issue}", file=sys.stderr)
        # Exit code 2 blocks tool call and shows stderr to Claude
        sys.exit(2)

    # All good, allow the operation
    sys.exit(0)


if __name__ == "__main__":
    main()