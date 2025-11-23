<!-- Copilot/AI instructions for contributors and coding agents -->

# Copilot instructions for PrimeraPruebaPython

Purpose

- Help AI coding agents quickly make safe, useful edits in this small tutorial-style Python repository.

Big picture

- This repository is a set of independent, single-file Python examples (00*\*.py .. 07*\*.py). Each file is a self-contained lesson (lists, tuples, dictionaries, etc.).
- There is no package/module structure, tests, or external dependencies.

How to run examples

- Use the local Python interpreter. Example: `python 07_diccionarios.py` (Windows PowerShell: `python 07_diccionarios.py`).

Project-specific conventions

- Filenames are prefixed with two-digit lesson numbers (e.g., `04_listas.py`, `07_diccionarios.py`) — preserve ordering when adding files.
- Code and comments are written in Spanish and example outputs are printed to stdout. Preserve Spanish text when modifying examples unless instructed otherwise.
- Keep changes minimal and focused: these are teaching snippets, not production services.

Editing guidance for AI

- Prefer small, targeted edits: fix typos, improve examples, or add short helper functions inside the same file.
- Do not introduce complex dependencies or restructure the repo into packages without user approval.
- Maintain the pattern of top-level script examples (simple prints and inline examples). If converting an example into functions, keep a short runnable `if __name__ == "__main__":` block.

Examples (how to modify)

- To clarify a dictionary example: update `07_diccionarios.py` by adding a small function and showing its output, e.g.:
  - Add `def imprimir_dic(dic):` then call it from the bottom of the file.
- To fix a typo in a filename or branch name, flag the issue in a PR description (don't rename branches automatically).

Branch/workflow notes

- The repo's default branch is `main`. Current working branch may contain a typo (`maiin`). Do not rename or change branches automatically; suggest a branch rename in the PR instead.
- PR title suggestions: `docs: fix typo in 07_diccionarios.py` or `chore(lesson): improve dictionary example`.

Testing & CI

- There are no tests or CI configured. When adding behavior changes, include a short runnable example or small script demonstrating the change.

When to ask the user

- If a change requires project-wide reorganization (adding packages, tests, or CI), ask before implementing.
- If you encounter missing information (Python version, intended audience language), request clarification.

Files to check for patterns

- `README.md` — repo-level description (currently minimal).
- `00_hello.py` .. `07_diccionarios.py` — primary source of coding patterns and examples.

Feedback

- If any section is unclear or you want additional rules (e.g., formatting, Python version pinning), please tell me and I'll update this file.
