

`brew install python@3.8`

Update `~/.bash_profile`
```bash
# python 3
export PATH="/usr/local/opt/python@3.8/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/python@3.8/lib"
export PKG_CONFIG_PATH="/usr/local/opt/python@3.8/lib/pkgconfig"
```

```
$ python --version
Python 3.8.2
```

- `pip install --upgrade pip`
- `pip install  -r requirements.txt`
- `pip install  -r requirements-test.txt`
- `python main.py`
- http://localhost:8080