---
READ_CONFIRMATION: "I've read and understood ast-grep.md"
---

# ast-grep Essential Usage

ast-grep is a powerful AST-based code search and refactoring tool. For comprehensive examples and detailed usage, load `@ast-grep-reference.md`.

## Core Concepts
- Uses pattern variables like `$NAME`, `$ARGS`, `$BODY` as wildcards
- Matches code structure, not just text
- Language-aware syntax understanding
- Version 0.38.5 installed on system

## Essential Commands

### Basic Search
```bash
# Find functions
ast-grep --lang typescript --pattern "function $NAME($ARGS) { $BODY }"

# Find specific calls
ast-grep --lang javascript --pattern "console.log($ARG)"
```

### Search and Replace
```bash
# Interactive replacement
ast-grep --lang javascript \
  --pattern "console.log($ARG)" \
  --rewrite "logger.info($ARG)" \
  --interactive
```

### File Filtering
```bash
# Specific file types
ast-grep --pattern "function $NAME" --globs "*.ts" --globs "*.js"

# Exclude files
ast-grep --pattern "function $NAME" --globs "!*test*"
```

## Quick Reference
- **Languages**: JavaScript, TypeScript, Python, Rust, Go, Java, C/C++, etc.
- **Output**: Add `--json` for programmatic use
- **Debug**: Use `--debug-query=ast` to visualize AST
- **Context**: Add `--context 3` to show surrounding lines

For detailed examples, configuration, and troubleshooting, load `@ast-grep-reference.md`.