#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta


REMINDER_FILE = "/tmp/claude-stash-reminder-last"
COOLDOWN_MINUTES = 15


def run_git_command(cmd: str) -> tuple[bool, str]:
    """Run git command and return (success, output)"""
    try:
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            cwd=os.getcwd(),
            timeout=5
        )
        return result.returncode == 0, result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.SubprocessError):
        return False, ""


def is_git_repo() -> bool:
    """Check if we're in a git repository"""
    success, _ = run_git_command("git rev-parse --git-dir")
    return success


def get_stash_list() -> list[str]:
    """Get list of stash entries"""
    success, output = run_git_command("git stash list")
    if not success or not output:
        return []
    return [line.strip() for line in output.split('\n') if line.strip()]


def should_remind() -> bool:
    """Check if we should show stash reminder based on cooldown"""
    if not os.path.exists(REMINDER_FILE):
        return True

    try:
        with open(REMINDER_FILE, 'r') as f:
            last_reminder_time = float(f.read().strip())

        current_time = time.time()
        time_diff = current_time - last_reminder_time

        # Convert cooldown to seconds
        cooldown_seconds = COOLDOWN_MINUTES * 60

        return time_diff >= cooldown_seconds
    except (IOError, ValueError):
        return True


def update_reminder_time():
    """Update the last reminder timestamp"""
    try:
        with open(REMINDER_FILE, 'w') as f:
            f.write(str(time.time()))
    except IOError:
        pass  # Fail silently if we can't write


def format_stash_entry(entry: str) -> str:
    """Format a stash entry for display"""
    # Parse stash entry format: "stash@{0}: On branch-name: message"
    parts = entry.split(':', 2)
    if len(parts) >= 3:
        stash_ref = parts[0]
        message = parts[2].strip()
        return f"  • {stash_ref}: \"{message}\""
    return f"  • {entry}"


def get_stash_age(stash_ref: str) -> str:
    """Get human-readable age of stash entry"""
    success, output = run_git_command(f"git stash show --format='%cr' {stash_ref}")
    if success and output:
        return f" ({output})"
    return ""


def main():
    # This hook runs after any command, but we still need to consume stdin
    # to conform to the hook protocol.
    try:
        json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass  # Ignore malformed input, we don't use it anyway

    # Only run in git repositories
    if not is_git_repo():
        sys.exit(0)

    # Check if we should remind based on cooldown
    if not should_remind():
        sys.exit(0)

    # Get stash entries
    stash_entries = get_stash_list()

    if not stash_entries:
        sys.exit(0)  # No stashes, nothing to remind about

    # Show the reminder
    print("\n📚 Stash Reminder: You have stashed changes:", file=sys.stderr)

    # Show up to 5 most recent stash entries
    displayed_entries = stash_entries[:5]
    for entry in displayed_entries:
        stash_ref = entry.split(':')[0]
        age = get_stash_age(stash_ref)
        formatted_entry = format_stash_entry(entry)
        print(f"{formatted_entry}{age}", file=sys.stderr)

    if len(stash_entries) > 5:
        remaining = len(stash_entries) - 5
        print(f"  ... and {remaining} more", file=sys.stderr)

    print("\nActions: git stash pop, git stash apply, git stash drop, or git stash clear", file=sys.stderr)
    print("To disable: export CLAUDE_NO_STASH_REMINDER=1\n", file=sys.stderr)

    # Update the reminder timestamp
    update_reminder_time()

    sys.exit(0)


if __name__ == "__main__":
    # Check if user has disabled stash reminders
    if os.environ.get("CLAUDE_NO_STASH_REMINDER") == "1":
        sys.exit(0)

    main()
