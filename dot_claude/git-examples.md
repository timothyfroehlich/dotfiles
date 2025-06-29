---
READ_CONFIRMATION: "I've read and understood git-examples.md"
---

# Git Workflow Examples and Detailed Command Reference

This file contains comprehensive examples and detailed command usage patterns. Load with `@git-examples.md` when you need detailed git guidance.

## Detailed Git Commands Summary

| Command | Description |
| :---- | :---- |
| git clone \<url\> | Downloads a remote repository. |
| git status | Shows working tree status, staged, unstaged, and untracked files. |
| git add \<file\> / git add . | Stages changes for the next commit. |
| git commit \-m "message" | Records staged changes to the repository. |
| git diff / git diff \--cached | Shows changes between working directory/staging area and last commit. |
| git log | Displays commit history. |
| git checkout \<branch-name\> | Switches to a different branch. |
| git checkout \-b \<new-branch\> | Creates and switches to a new branch. |
| git branch \-d \<branch-name\> | Deletes a local branch (only if merged). |
| git pull | Fetches and merges changes from the remote repository. |
| git push | Uploads local commits to the remote repository. |
| git push origin \--delete \<branch\> | Deletes a remote branch. |
| git reset \<file\> | Unstages a file. |
| git revert \<commit-hash\> | Creates a new commit that undoes the specified commit. |

## Complete Example Workflow

Let's say you need to implement a new login feature:

1. **Start a new branch**:  
   git checkout main  
   git pull origin main  
   git checkout \-b feature/implement-login

2. **First commit (initial structure)**:  
   \# Create login form HTML  
   git add src/components/LoginForm.html  
   git commit \-m "feat: Add basic login form HTML structure"

3. **Second commit (styling)**:  
   \# Add CSS for login form  
   git add src/styles/login.css  
   git commit \-m "style: Apply basic styling to login form"

4. **Third commit (JavaScript logic)**:  
   \# Add JavaScript for form submission handling  
   git add src/js/login.js  
   git commit \-m "feat: Implement client-side login form validation and submission"

5. **Staying up-to-date (fetch often)**:  
   git fetch origin \# To see if there are any new changes  
   git pull origin main \# To merge changes from main into your current branch  
   \# Resolve any conflicts if they arise

6. **Fourth commit (API integration with issue fix)**:  
   \# Integrate login form with backend API and fix a related bug  
   git add src/js/login.js src/services/auth.js  
   git commit \-m "fix: Connect login form to authentication API endpoint and resolve login bug

   Fixes \#456"

7. **Push and PR**:  
   git push \-u origin feature/implement-login  
   \# Open Pull Request on GitHub

8. **Merge & Cleanup**: After review and approval, the branch is merged using a Merge Commit.  
   git checkout main  
   git pull origin main  
   git branch \-d feature/implement-login  
   git push origin \--delete feature/implement-login

## Detailed Commit Message Examples

**Good commit messages following Conventional Commits:**

```
feat: Add user authentication system

- Implement JWT token-based authentication
- Add login/logout endpoints
- Create user session management
- Include password hashing with bcrypt

Fixes #123
```

```
fix: Resolve memory leak in WebSocket connections

The connection pool was not properly cleaning up closed connections,
causing memory usage to grow over time. Added proper cleanup in the
disconnect handler and implemented connection timeout.

Fixes #456
```

```
refactor: Restructure database connection handling

- Extract connection logic into separate module
- Add connection pooling for better performance
- Improve error handling and retry logic
- Update tests to reflect new structure
```

## Advanced Git Scenarios

### Handling Complex Merge Conflicts

When you encounter merge conflicts:

1. **Identify conflicted files:**
   ```bash
   git status  # Shows files with conflicts
   ```

2. **Resolve conflicts manually:**
   ```
   <<<<<<< HEAD
   Your current branch changes
   =======
   Incoming changes from other branch
   >>>>>>> feature/other-branch
   ```

3. **Complete the merge:**
   ```bash
   git add resolved-file.js
   git commit -m "resolve: Merge conflict in user authentication logic"
   ```

### Emergency Hotfix Workflow

```bash
# Save current work
git stash push -m "WIP: save current feature work"

# Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-security-fix

# Make fix
# ... edit files ...
git add .
git commit -m "fix: Patch critical security vulnerability in auth middleware

This addresses CVE-2024-XXXX by properly validating user input
before processing authentication tokens.

Fixes #999"

# Deploy hotfix
git push -u origin hotfix/critical-security-fix
# Create PR for immediate review

# Return to feature work
git checkout feature/your-feature
git stash pop  # Restore your work
```

### Conventional Commit Types with Examples

**feat: A new feature**
```bash
git commit -m "feat(auth): Add two-factor authentication support

- Implement TOTP-based 2FA
- Add QR code generation for mobile apps
- Create backup code system
- Update user settings interface"
```

**fix: A bug fix**
```bash
git commit -m "fix(api): Handle null values in user profile endpoint

Previously the API would crash when users had incomplete profiles.
Now returns default values for missing fields.

Fixes #234"
```

**docs: Documentation only changes**
```bash
git commit -m "docs: Add API authentication examples to README

- Include JWT token usage examples
- Add common error responses
- Update endpoint documentation"
```

**style: Formatting, missing semicolons, etc.**
```bash
git commit -m "style: Fix ESLint warnings in authentication module

- Add missing semicolons
- Fix indentation inconsistencies
- Remove unused imports"
```

**refactor: Code change that neither fixes a bug nor adds a feature**
```bash
git commit -m "refactor: Extract user validation logic into separate service

- Move validation functions to UserValidator class
- Improve code reusability across modules
- Add comprehensive unit tests for validation logic"
```

**test: Adding or correcting tests**
```bash
git commit -m "test: Add integration tests for payment processing

- Test successful payment flow
- Test failed payment handling
- Test payment timeout scenarios
- Mock external payment gateway"
```

**chore: Maintenance tasks**
```bash
git commit -m "chore: Update dependencies to latest versions

- Upgrade React to 18.2.0
- Update Express to 4.18.2
- Fix security vulnerabilities in deps
- Update package-lock.json"
```