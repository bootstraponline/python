

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

- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`
- `pip3 install -r requirements-test.txt`
- `python3 main.py`
- http://localhost:8080


`gcloud app deploy`
`gcloud app browse`
`gcloud app logs tail -s default`

gcloud app versions describe -s default 20200503t100627

instanceClass: F1

https://cloud.google.com/appengine/docs/standard#second-gen-runtimes