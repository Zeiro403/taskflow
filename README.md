# TaskFlow — GitHub CI/CD Learning Project

A small Python CLI task manager with automatic tests, linting, and tagged releases.

## Run locally

Requires Python 3.10+.

```bash
python -m pip install -e . pytest ruff build
python -m taskflow add "Learn GitHub Actions"
python -m taskflow list
python -m taskflow done 1
python -m taskflow delete 1
```

## Run CI checks yourself

```bash
ruff check .
python -m pytest -v
```

## Publish to GitHub

Create an empty GitHub repository named `taskflow`, then run:

```bash
git init
git add .
git commit -m "Initial TaskFlow project with CI/CD"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/taskflow.git
git push -u origin main
```

The CI workflow runs on pushes and pull requests to `main`, and can be started manually from Actions.

## Try a pull request

```bash
git checkout -b feature/my-change
# Make a change, then:
git add .
git commit -m "Try a feature"
git push -u origin feature/my-change
```

Open a pull request into `main` on GitHub and inspect the CI checks. Try breaking a test to see a failure.

## Create a release

After merging and confirming CI passes on `main`:

```bash
git checkout main
git pull
git tag v0.1.0
git push origin v0.1.0
```

The release workflow tests the project, builds wheel/source archives, and attaches them to a GitHub Release. Ensure repository Actions permissions allow creating releases. For production, pin third-party actions to reviewed commit SHAs.
