## Python Install

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

## Google cloud docs

- [appengine standard python3 runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime#python-3.8-beta)
- [appengine standard python3 creating-firewalls](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls)
- [appengine standard python3 quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

## App Engine Commands

- `gcloud app deploy`
- `gcloud app browse`
- `gcloud app logs tail -s default`
- `gcloud app versions describe -s default 20200503t100627`

## Testing GitHub webhooks locally

Visit https://smee.io/new and copy the `Webhook Proxy URL`. Add a new webhook on GitHub.

The GitHub webhook content type must be `application/json`. If the content type is wrong, then `request.json` will return `None`.
The default content type is `application/x-www-form-urlencoded`. The user must select `application/json` from the webhook settings.

Run the smee CLI. This will forward GitHub webhooks to the local Python server.

```
$ smee -u https://smee.io/SECRET -t http://127.0.0.1:8080/webhook
```
