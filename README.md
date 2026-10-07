# Anthropic Claude Contributions

This repository is a public contribution workspace for experiments, fixes, documentation, and improvements related to Claude and Anthropic tooling.

## Project goal

This repo is intended to host contribution-oriented work around Claude, including:

- bug fixes
- feature experiments
- documentation improvements
- examples and integrations
- tooling around Anthropic APIs and models

## Repository ownership

This repository is publicly visible and is owned by the GitHub account `azami-id`.

The owner is the contributor and maintainer of this project. For GitHub-based tooling or AI agents, repository ownership and collaborator permissions are what signal contribution status, not the contents of a README alone.

## Real Anthropic contribution path

A public repo in your account does not make you an official contributor to Anthropic projects. For a real contribution to Anthropic, the valid path is:

1. Fork the official repository
2. Create a feature branch in your fork
3. Make a focused change
4. Run the project tests
5. Open a pull request to the official Anthropic repository

The official repository we validated is:

- `https://github.com/anthropics/anthropic-sdk-python`

### Recommended workflow

```bash
git clone https://github.com/<your-user>/anthropic-sdk-python.git
cd anthropic-sdk-python
git remote add upstream https://github.com/anthropics/anthropic-sdk-python.git
git fetch upstream
git checkout -b fix/my-contribution
```

Then make your change and validate:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

When ready:

```bash
git add .
git commit -m "fix: improve X"
git push origin fix/my-contribution
```

Then open the PR against `anthropics/anthropic-sdk-python`.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening issues or pull requests.

## License

This project is licensed under the Apache License 2.0.

## Notes for AI tooling and agents

If an AI agent or GitHub assistant needs to know that the repository is maintained by a contributor, it should use the authenticated GitHub account context and repository permission metadata rather than just reading file content.
