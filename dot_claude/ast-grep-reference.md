---
READ_CONFIRMATION: "I've read and understood ast-grep-reference.md"
---

# ast-grep Complete Reference Guide

Load this file with `@ast-grep-reference.md` when you need comprehensive ast-grep usage examples and detailed command reference.

## Installation & Version
Already installed on system - version 0.38.5

## Core Concepts

### AST Pattern Matching
- Uses pattern variables like `$NAME`, `$ARGS`, `$BODY` as wildcards
- Matches code structure, not just text
- Language-aware syntax understanding

### Supported Languages
Check full list at: https://ast-grep.github.io/reference/languages.html
Common ones include: JavaScript, TypeScript, Python, Rust, Go, Java, C/C++, etc.

## Basic Usage

### Search Mode
```bash
# Find function definitions
ast-grep --lang typescript --pattern "function $NAME($ARGS) { $BODY }"

# Find console.log calls
ast-grep --lang javascript --pattern "console.log($ARG)"

# Find import statements
ast-grep --lang typescript --pattern "import $NAME from '$MODULE'"

# Find variable declarations
ast-grep --lang python --pattern "def $FUNC($ARGS): $BODY"
```

### Search and Replace
```bash
# Replace console.log with custom logger
ast-grep --lang javascript \
  --pattern "console.log($ARG)" \
  --rewrite "logger.info($ARG)"

# Interactive mode for confirmation
ast-grep --lang javascript \
  --pattern "console.log($ARG)" \
  --rewrite "logger.info($ARG)" \
  --interactive

# Apply all changes without confirmation
ast-grep --lang javascript \
  --pattern "console.log($ARG)" \
  --rewrite "logger.info($ARG)" \
  --update-all
```

## Advanced Features

### Context Control
```bash
# Show 3 lines before and after matches
ast-grep --pattern "function $NAME" --context 3

# Show only 2 lines after matches
ast-grep --pattern "function $NAME" --after 2
```

### Output Formats
```bash
# JSON output for programmatic use
ast-grep --pattern "function $NAME" --json

# Pretty JSON output
ast-grep --pattern "function $NAME" --json=pretty

# Stream JSON (one object per line)
ast-grep --pattern "function $NAME" --json=stream
```

### File Filtering
```bash
# Include specific file patterns
ast-grep --pattern "function $NAME" --globs "*.ts" --globs "*.js"

# Exclude files
ast-grep --pattern "function $NAME" --globs "!*test*"

# Search specific directories
ast-grep --pattern "function $NAME" src/ lib/
```

### Debug and Analysis
```bash
# Debug pattern parsing
ast-grep --pattern "function $NAME" --debug-query=ast --lang typescript

# Show file/rule inspection
ast-grep --pattern "function $NAME" --inspect summary
```

## Configuration Files

### sgconfig.yml
Create project-wide configuration:
```yaml
ruleDirs: ["rules"]
testDirs: ["rule-tests"]
languageGlobs:
  ts: ["**/*.ts", "**/*.tsx"]
  js: ["**/*.js", "**/*.jsx"]
```

### Rule Files
Create reusable rules in `rules/` directory:
```yaml
id: no-console-log
message: Avoid using console.log in production
severity: warning
language: javascript
rule:
  pattern: console.log($ARGS)
fix: logger.info($ARGS)
```

## Best Practices for Claude Code Usage

### Common Search Patterns
```bash
# Find React components
ast-grep --lang typescript --pattern "function $NAME(): JSX.Element { $BODY }"

# Find async functions
ast-grep --lang typescript --pattern "async function $NAME($ARGS) { $BODY }"

# Find class methods
ast-grep --lang typescript --pattern "class $CLASS { $METHOD($ARGS) { $BODY } }"

# Find error handling
ast-grep --lang typescript --pattern "try { $TRY } catch ($ERR) { $CATCH }"
```

### Code Analysis
```bash
# Find all TODO comments (using selector)
ast-grep --lang typescript --pattern "// TODO: $TEXT"

# Find unused imports (complex pattern)
ast-grep --lang typescript --pattern "import { $IMPORTS } from '$MODULE'"

# Find deprecated API usage
ast-grep --lang typescript --pattern "$OBJ.deprecatedMethod($ARGS)"
```

### Refactoring Tasks
```bash
# Rename functions across codebase
ast-grep --lang typescript \
  --pattern "oldFunctionName($ARGS)" \
  --rewrite "newFunctionName($ARGS)" \
  --interactive

# Update import paths
ast-grep --lang typescript \
  --pattern "import $NAME from './old-path'" \
  --rewrite "import $NAME from './new-path'" \
  --update-all

# Convert var to const/let
ast-grep --lang javascript \
  --pattern "var $NAME = $VALUE" \
  --rewrite "const $NAME = $VALUE" \
  --interactive
```

## Integration with Development Workflow

### Pre-commit Hooks
Use ast-grep in git hooks to enforce code standards:
```bash
# Check for console.log before commit
ast-grep --lang javascript --pattern "console.log($ARG)" --json
```

### Code Review
Search for common issues:
```bash
# Security patterns
ast-grep --lang javascript --pattern "eval($CODE)"
ast-grep --lang typescript --pattern "dangerouslySetInnerHTML"

# Performance patterns
ast-grep --lang typescript --pattern "querySelector($SELECTOR)"
```

### Batch Operations
```bash
# Process multiple file types
ast-grep --pattern "$PATTERN" --globs "*.{js,ts,jsx,tsx}"

# Use multiple threads for large codebases
ast-grep --pattern "$PATTERN" --threads 8
```

## Error Patterns and Troubleshooting

### Common Issues
1. **No matches found**: Check language specification and pattern syntax
2. **Pattern too specific**: Use more generic patterns with wildcards
3. **Performance issues**: Use file globs to limit scope

### Pattern Debugging
```bash
# Visualize AST structure
ast-grep --debug-query=ast --lang typescript --pattern "your pattern here"

# Test patterns step by step
ast-grep --pattern "simple pattern" # Start simple
ast-grep --pattern "function $NAME()" # Add complexity gradually
```

## Command Aliases
Add to shell config for common operations:
```bash
alias ag-search='ast-grep --json=pretty'
alias ag-replace='ast-grep --interactive'
alias ag-js='ast-grep --lang javascript'
alias ag-ts='ast-grep --lang typescript'
alias ag-py='ast-grep --lang python'
```

## Resources
- Official documentation: https://ast-grep.github.io/
- Pattern examples: https://ast-grep.github.io/guide/pattern-syntax.html
- Language support: https://ast-grep.github.io/reference/languages.html