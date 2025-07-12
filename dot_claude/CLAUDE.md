# Claude Code Agent Instructions

If you've read this, say some variation on "I'm Mr. Meeseeks, look at me!"

## Core Requirements
- All tests should pass before committing.
- ALWAYS run pre-commit hooks before attempting to commit. Pre-commit must be clean before committing.

## User Information
- Name: Tim Froehlich
- Email: timothyfroehlich@gmail.com

## Memory Management for Agents

### Claude Code Memory System
- **User memory location**: `~/.claude/CLAUDE.md` (this file)
- **Project memory location**: `./CLAUDE.md` (in project root)
- **NEVER use**: `~/.config/claude/` - this is incorrect and files won't auto-load
- **File references**: Use `@filename.md` syntax to reference other files for auto-loading
- **Import depth**: Maximum 5 hops for file imports
- **Memory hierarchy**: Project memory overrides user memory

### Required Actions for ~/.claude Changes
**CRITICAL**: Whenever you make ANY changes to files in the `~/.claude/` directory, you MUST immediately:
1. Stage the changes: `git -C /home/froeht/.claude add .`
2. Commit with descriptive message: `git -C /home/froeht/.claude commit -m "descriptive message"`
3. Push to GitHub: `git -C /home/froeht/.claude push`

This ensures all memory changes are version controlled and backed up to: https://github.com/timothyfroehlich/agents-md

### File Organization Best Practices
- Split large sections into separate files (e.g., `git-usage.md`, `ast-grep.md`)
- Reference files using `@` syntax for auto-loading
- Keep CLAUDE.md focused on core instructions and references
- Use descriptive filenames that clearly indicate content purpose

## Tool Documentation

@git-usage.md - Git workflow guidelines and best practices for agents

@ast-grep.md - AST-based code search and refactoring tool usage guide

## MCP Tools Configured
- **GitHub**: Repository operations, PRs, issues
- **Playwright**: Browser automation, E2E testing
- **Context7**: Get current library documentation - use `resolve-library-id` first to find library, then `get-library-docs` for up-to-date docs and patterns

## Conditional References (Load When Needed)

**For detailed examples and comprehensive guides:**

- `@ast-grep-reference.md` - Comprehensive ast-grep usage guide with examples

## Important Instruction Reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.

## Python Development Notes
- you must activate the python venv to run ruff

## Command Line Tools
- Use ripgrep (`rg`) instead of grep or find
