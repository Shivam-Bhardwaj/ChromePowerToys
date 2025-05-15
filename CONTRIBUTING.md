# Contributing to ChromePowerToys

First off, thank you for considering contributing to ChromePowerToys! We're excited to build a vibrant community around making Chrome even more powerful and personalized. Your help is essential for creating a great set of tools.

This document provides guidelines for contributing to the project. Please read it carefully to ensure a smooth and effective collaboration process.

## Table of Contents

* [How Can I Contribute?](#how-can-i-contribute)
    * [Reporting Bugs](#reporting-bugs)
    * [Suggesting Enhancements or New PowerToys](#suggesting-enhancements-or-new-powertoys)
    * [Working on Existing Issues](#working-on-existing-issues)
    * [Submitting Code Contributions](#submitting-code-contributions)
    * [Improving Documentation](#improving-documentation)
    * [Providing Feedback](#providing-feedback)
* [Setting Up Your Development Environment](#setting-up-your-development-environment)
* [Coding Style & Conventions](#coding-style--conventions)
* [Commit Message Guidelines](#commit-message-guidelines)
* [Pull Request Process](#pull-request-process)
* [Code of Conduct](#code-of-conduct)
* [Questions?](#questions)

## How Can I Contribute?

There are many ways to contribute, and not all of them involve writing code!

### Reporting Bugs
If you find a bug in one of the PowerToys:
1.  **Search existing issues:** Check if the bug has already been reported on our [GitHub Issues page](https://github.com/YOUR_USERNAME/ChromePowerToys/issues).
2.  **If not found, create a new issue:** Use the "Bug Report" template if available. Provide as much detail as possible:
    * Steps to reproduce the bug.
    * Expected behavior.
    * Actual behavior.
    * Screenshots or GIFs if helpful.
    * Your Chrome version and Operating System.
    * The specific PowerToy and its version (if applicable).

### Suggesting Enhancements or New PowerToys
Have an idea for a new PowerToy or an improvement to an existing one?
1.  **Check the [Project Roadmap](PROJECT_ROADMAP.md):** See if your idea aligns with our existing plans or if something similar is already listed.
2.  **Open a "Feature Request" issue:** Clearly describe your idea, its benefits, and potential implementation thoughts. This allows for community discussion.

### Working on Existing Issues
1.  Browse the [GitHub Issues page](https://github.com/YOUR_USERNAME/ChromePowerToys/issues).
2.  Look for issues tagged `help wanted`, `good first issue`, or `status:todo`.
3.  Comment on the issue to indicate you'd like to work on it. This helps avoid duplicated effort.
4.  If it's a larger feature, discuss your proposed approach in the issue before starting significant coding.

### Submitting Code Contributions
This is the core of building new PowerToys!
1.  Follow the [Setting Up Your Development Environment](#setting-up-your-development-environment) guide below.
2.  Adhere to our [Coding Style & Conventions](#coding-style--conventions) and [Commit Message Guidelines](#commit-message-guidelines).
3.  Ensure your PowerToy is **safe, secure, and easy to use**. Request minimal permissions.
4.  Include or update relevant documentation for your contribution.
5.  Submit a [Pull Request](#pull-request-process) with your changes.

### Improving Documentation
Clear documentation is crucial. You can help by:
* Improving this `CONTRIBUTING.md` file.
* Enhancing the main `README.md`.
* Adding or improving the `README.md` for individual PowerToys.
* Correcting typos or clarifying instructions.

### Providing Feedback
Your feedback on existing PowerToys, ideas, and the project direction is highly valuable. Participate in discussions on GitHub Issues and Pull Requests.

## Setting Up Your Development Environment

1.  **Fork the Repository:** Create your own copy of `ChromePowerToys` by clicking the "Fork" button on GitHub.
2.  **Clone Your Fork:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ChromePowerToys.git](https://github.com/YOUR_USERNAME/ChromePowerToys.git)
    cd ChromePowerToys
    ```
3.  **Set Upstream Remote (Optional but Recommended):** This helps keep your fork synced with the main repository.
    ```bash
    git remote add upstream [https://github.com/YOUR_USERNAME/ChromePowerToys.git](https://github.com/YOUR_USERNAME/ChromePowerToys.git)
    ```
    *(Replace `YOUR_USERNAME` in the upstream URL with the actual owner of the main ChromePowerToys repository if it's not you.)*
4.  **Create a New Branch:** Before making changes, create a descriptive branch:
    ```bash
    git checkout -b feature/my-new-powertoy
    # or fix/bug-in-xyz-powertoy
    ```
5.  **Develop Your PowerToy:**
    * Each PowerToy will typically be a Chrome extension in its own subdirectory (e.g., `code_examples/my_powertoy/`).
    * Follow standard Chrome extension development practices (HTML, CSS, JavaScript, `manifest.json`).
    * Load your extension as "unpacked" in `chrome://extensions` (with Developer Mode enabled) for testing.

## Coding Style & Conventions

* **JavaScript:** We generally follow modern JavaScript (ES6+) practices. Consider using a linter like ESLint with a common style guide (e.g., Airbnb, StandardJS - to be decided and configured).
* **HTML/CSS:** Write clean, semantic HTML and well-organized CSS.
* **Comments:** Add comments to explain complex logic or non-obvious code sections.
* **Readability:** Prioritize clear and readable code.
* **Permissions:** Only request the minimum permissions necessary for your PowerToy to function. Clearly justify why each permission is needed in the PowerToy's documentation or PR.
* **AI Integration:** If using LLMs (preferably Google Gemini):
    * Clearly indicate to the user when AI is being used and what data is being sent.
    * Handle API keys securely (e.g., users provide their own keys in settings, do not hardcode keys).
    * Minimize data sent to the LLM.

*(More detailed style guides might be added later.)*

## Commit Message Guidelines

We use a commit message template (`.gitmessage.txt`) to encourage consistent and informative commit messages. Please follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

**Basic Format:**
[optional scope]: [optional body][optional footer(s)]Example: `feat(summarizer): Add option for summary length`

If you haven't configured the template locally, refer to the `.gitmessage.txt` file in the project root.

## Pull Request Process

1.  Ensure your code lints (if a linter is set up) and any tests pass.
2.  Update your fork's branch with the latest changes from the main repository's `main` branch (rebase if possible to keep history clean):
    ```bash
    git fetch upstream
    git rebase upstream/main
    # or git merge upstream/main
    ```
3.  Push your changes to your forked repository:
    ```bash
    git push origin feature/my-new-powertoy
    ```
4.  Open a Pull Request (PR) from your branch to the `main` branch of the official `ChromePowerToys` repository.
5.  **Fill out the PR template thoroughly:**
    * Provide a clear title and description of your changes.
    * Explain the "why" and "what" of your contribution.
    * Link to any relevant GitHub Issues (e.g., `Closes #123`).
    * Include screenshots or GIFs if your changes affect the UI.
6.  Be prepared for a code review and respond to feedback constructively.
7.  Once your PR is approved and passes any checks, it will be merged!

## Code of Conduct

All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please ensure you read and understand it. We are committed to a welcoming and inclusive community.

## Questions?

If you have questions, feel free to:
* Open an issue on GitHub with the `question` label.
* Join our community discussion forum (if/when one is set up).

Thank you for contributing to ChromePowerToys!
