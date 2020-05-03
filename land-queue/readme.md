

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

## Testing GitHub webhooks locally

Visit https://smee.io/new and copy the `Webhook Proxy URL`. Add a new webhook on GitHub.

The GitHub webhook content type must be `application/json`. If the content type is wrong, then `request.json` will return `None`.
The default content type is `application/x-www-form-urlencoded`. The user must select `application/json` from the webhook settings.

Run the smee CLI. This will forward GitHub webhooks to the local Python server.

```
$ smee -u https://smee.io/SECRET -t http://127.0.0.1:8080/webhook
```
