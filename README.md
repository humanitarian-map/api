HUMANITARIAN MAP (API)
======================

Requirements:
- python3
- postgresql
- python-virtualenvwrapper


Setup

```
mkvirtualenv humanitarian-map-api
pip install -r requirements.txt
createdb humanitarianmap
```

Run the api

```
gunicorn --reload [-w4] [-b 0.0.0.0:8000] app
```

For developers only

```
pip install -r requirements-devel.txt
flake8 --install-hook git
git config --bool flake8.strict true
```
