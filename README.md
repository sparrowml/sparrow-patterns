# sparrow-patterns

A CLI for updating code patterns in Python projects

## Quick start

<!-- Put a code snippet here -->

## Development

This project is optimized for development in VS Code with the [Remote Containers](https://code.visualstudio.com/docs/remote/containers) extension.
With this setup, code will be linted, tested and executed inside a Docker container, defined at [`Dockerfile`](./Dockerfile).
Before you start writing code, you'll need to define a file at `.devcontainer/.env`. Any environment variables that you want to have accessible inside
your remote container should go in this file. You can see [`.devcontainer/.env.example`](.devcontainer/.env.example) for some example variables.

Once `.devcontainer/.env` is defined, you can open the code inside a container by opening the command palette and running:

```
Remote-Containers: Rebuild and Reopen in Container
```

After building, the VS Code window will reload inside the Docker container.

Inside the remote container, you should install the `pre-commit` hook, which will check code formatting before your commit new code to the repo.

By default, a GitHub Actions workflow will run on every push to GitHub. That configuration is defined at [`.github/workflows/build.yml`](./.github/workflows/build.yml) and can be edited or deleted.

### Poetry

Dependencies for this project are managed with a tool called [Poetry](https://python-poetry.org/docs/). The configuration file is [`pyproject.toml`](./pyproject.toml). This containers package dependencies, development dependencies and development tool settings.

To add another dependency, use the `poetry add` command. For example:

```
poetry add numpy@latest
```

### Makefile commands

Many useful dev commands are defined in the [`Makefile`](./Makefile).

For example, to build the Docker image:

```
make docker-build
```

To run unit tests and display coverage statistics:

```
make test
```

It's possible to use the `Makefile` both inside and outside of the Docker container, depending on your needs.
