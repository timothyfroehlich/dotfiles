---
READ_CONFIRMATION: "I've read and understood git-usage.md"
---

# Git Workflow Guidelines for Coding Agents

Essential Git workflow and best practices for coding agents. For detailed examples and commands, load `@git-examples.md`.

## Core Principles

1. **Feature Branching is Mandatory (Short-Lived)**: All work must be performed on dedicated feature branches. Never commit directly to main.
   * Isolates changes, enables parallel development, facilitates code review
   * Short-lived branches reduce merge complexities

2. **Small, Atomic Commits**: Make frequent, small commits representing single logical changes.
   * Improves history readability, simplifies debugging, makes reverts easier
   * Each commit should ideally pass tests independently

3. **Meaningful Commit Messages (Conventional Commits)**: Follow Conventional Commits specification.
   * **Format**: `type(scope): description` (e.g., "feat: Add user profile API")
   * **Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
   * **GitHub Integration**: Include `Fixes #<issue-number>` to auto-close issues
   * Use imperative mood in subject line

4. **Never Rewrite Shared History**: Once pushed to shared branches, never rewrite history.
   * Avoid `git rebase -i` or `git push --force` on shared branches
   * Prevents collaboration issues and lost work

5. **Continuous Synchronization**: Regularly fetch/pull from main to minimize conflicts.
   * Keep feature branches up-to-date with main branch changes
   * Resolve conflicts early and often

## Standard Workflow

### Basic Flow
1. **Setup**: `git clone <repo>` and `cd <repo>`
2. **New Feature**: Create branch from updated main
   ```bash
   git checkout main && git pull origin main
   git checkout -b feature/descriptive-name
   ```
3. **Development**: Make changes, commit frequently with conventional commits
   ```bash
   git add . && git commit -m "feat: Add feature description"
   ```
4. **Stay Current**: Regularly sync with main
   ```bash
   git fetch origin && git pull origin main
   ```
5. **Submit**: Push branch and create PR
   ```bash
   git push -u origin feature/descriptive-name
   ```
6. **Merge**: Approved PRs merged with merge commit (--no-ff)
7. **Cleanup**: Delete feature branch after merge

### Branch Naming
Use prefixes: `feature/`, `fix/`, `hotfix/`, `chore/` + kebab-case description

## Best Practices for Agents

* **Commit frequently**: Every logical change should be committed
* **Test before committing**: Ensure changes work and pass tests
* **Fetch regularly**: Stay synchronized with remote changes
* **Keep branches short-lived**: Complete features quickly to avoid conflicts
* **Use proper .gitignore**: Prevent unwanted files from being tracked

## Key Terms
* **HEAD**: Current repository snapshot
* **origin**: Default remote repository
* **main**: Primary development branch

For detailed examples, commands, and troubleshooting, load `@git-examples.md`.