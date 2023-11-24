# GitHub Actions Assignment

The CI workflow is designed to perform the following tasks whenever changes are pushed to the main branch:

- **Build and Test:**
  - Dependencies are installed.
  - Unit tests are executed to validate the integrity of the code.

- **Linting:**
  - Python code is linted using pylint to maintain high code quality.

## GitHub Actions CI

This repository includes a GitHub Actions workflow for continuous integration (CI). The workflow automates the build and test processes whenever changes are pushed to the main branch.

### Workflow Structure

The CI workflow consists of the following steps:

- **Build and Test:**
  - Installs dependencies.
  - Runs unit tests.

- **Lint:**
  - Lints the Python code using pylint.

### How to Contribute

We welcome contributions to improve and extend this project! Here's how you can contribute:

1. **Fork the repository:**
   - Click the "Fork" button at the top right of the repository.

2. **Clone your fork:**
   - Open a terminal and run:
     ```bash
     git clone https://github.com/your-username/your-repository.git
     cd your-repository
     ```

3. **Create a new branch:**
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature/new-feature
     ```

4. **Make your changes:**
   - Make the necessary changes to the code or documentation.

5. **Commit your changes:**
   - Stage and commit your changes:
     ```bash
     git add .
     git commit -m 'Add new feature or fix bug'
     ```

6. **Push your branch:**
   - Push your branch to your fork on GitHub:
     ```bash
     git push origin feature/new-feature
     ```

7. **Open a pull request (PR):**
   - Go to your fork on GitHub.
   - Click the "Compare & pull request" button next to your new branch.
   - Provide a meaningful title and description for your changes.
   - Click "Create pull request."

8. **Code Review:**
   - Your pull request will be reviewed by maintainers.
   - Make any requested changes and update the PR.

9. **Merge:**
   - Once your changes are approved, they will be merged into the main branch.

### GitHub Actions Status

[![CI Status](https://github.com/your-username/your-repository/workflows/CI/badge.svg)](https://github.com/amitc1712/GHA-Assignment/actions)

