repos:
-   repo: https//github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 24.2.0
    hooks:
    -   id: black

-   repo: https://github.com/charliemarsh/ruff-pre-commit
    rev: 'v0.6.4'
    hooks:
        - id: ruff
          args: ['--fix']
