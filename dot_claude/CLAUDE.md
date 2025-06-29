# Claude Code Agent Instructions

If you've read this, say Hiya!

## Core Requirements
- All tests should pass before committing.

## User Information
- Name: Tim Froehlich
- Email: timothyfroehlich@gmail.com
- My name is Tim

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

## Conditional References (Load When Needed)

**For detailed examples and comprehensive guides:**
- `@git-examples.md` - Complete git workflow examples and command reference
- `@ast-grep-reference.md` - Comprehensive ast-grep usage guide with examples
- `@claude-worktrees-research.md` - Git worktrees research for multi-instance coordination
- `@project-lessons.md` - Detailed project lessons learned and historical context

## Important Instruction Reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.