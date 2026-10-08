# Security Policy

## Supported versions

The project is in early open-source development. Security updates are handled on the latest branch and on the latest release available in the repository.

## Reporting a vulnerability

If you discover a security issue, please do not open a public issue.

Report it privately by emailing the maintainers at `security@localhost` or by using a private GitHub security advisory if enabled for the repository.

Please include:

- a description of the issue
- affected versions or files
- steps to reproduce
- potential impact
- suggested fix if known

We will acknowledge receipt and determine the next steps within a reasonable time.

## Responsible disclosure

We ask that you give us a reasonable opportunity to address the issue before public disclosure.

## Best practices

- never expose private API keys or secrets in code or issue reports
- use environment variables or secret managers for production credentials
- validate all user-controlled inputs before using them in prompts or external APIs
