from flask import Flask, request, Response

import octohook
from octohook.events import PullRequestEvent
from octohook.models import PullRequest, Repository

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # X-GitHub-Event contains an event type defined here: https://developer.github.com/webhooks/
    github_event = request.headers.get('X-GitHub-Event')

    if github_event != 'pull_request':
        return '', 200, {}

    global last 
    last = request.json
    event : PullRequestEvent = octohook.parse(github_event, request.json)

    return '', 200, {}

last = 'no webhook data'

@app.route('/')
def hello():
    global last
    return str(last)

# https://cloud.google.com/appengine/docs/standard/python3/configuring-warmup-requests
@app.route('/_ah/warmup')
def warmup():
    return '', 200, {}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
