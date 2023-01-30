```sh
git clone https://github.com/grewn0uille/base.git

cd base

python -m venv venv

# Linux
venv/bin/pip install -e .

venv/bin/pip install ".[test]"

venv/bin/pytest

venv/bin/pytest --cov

# Windows
venv/Scripts/pip install -e .

venv/Scripts/pip install ".[test]"

venv/Scripts/pytest

venv/Scripts/pytest --cov
```
