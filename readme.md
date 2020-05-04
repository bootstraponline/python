# Python Experiments

## Monorepo on GitHub

Monorepo allows for easier code sharing across projects. Standardization of software developement practices (such as lint rules) are easier when all code is in a single repo. One challenge the monorepo presents is access control. Multiple repositories on GitHub allow for fine grained access control (read/write) at the per repo level. In a monorepo, everyone has global read and write. To solve the write access problem, a land queue will be built to enforce access control. All users will still have global read, however merges will be done exclusively via the land queue. The land queue will enforce security policy.

## Land Queue

![](http://www.plantuml.com/plantuml/proxy?cache=no&fmt=svg&src=https://raw.githubusercontent.com/bootstraponline/python/master/overview.puml&foo=bar)

## Milestones

- Document the problem
- AppEngine Python 3.8 hello world
- App receives GitHub repo web hook for pull request label applied
  - Define webhook endpoint. Look into https://github.com/doodla/octohook
  - Create event listener for Cloud Pub/Sub
- App merges pull request when label is applied
  - Squash merge only. Commit title is PR title. Commit body is PR body + approved reviewers
- AppEngine firewall rules dynamically defined via [github meta](https://developer.github.com/v3/meta/) to only accept inbound from GitHub's IP ranges
- AppEngine deployed via Terraform
- Define access controls per directory. Code owners format (same as [git ignore](https://git-scm.com/docs/gitignore#_pattern_format)). Code can't be landed unless an owner has approved.
  - https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners
- Build out a testing strategy using a mock server
- Define a strategy for handling merge conflicts / providing feedback to PR owners

Consider [Weave Flux via Weave Cloud](https://www.weave.works/faq/weave-cloud-faq/#faq-4) free tier for GCP. Flux allows automatic terraform deploys.

Example GitHub webhook bot from Google deployed via terraform using Google App Engine. 

>Contribute Bot has two servers: a webhook endpoint and an event listener. The
webhook endpoint publishes events to a [Cloud Pub/Sub topic][pubsub] that are eventually
processed by the event listener. GitHub has a
[10 second webhook response time limit][github-async] combined with a
[5000 request/hour API rate limit][github-ratelimit], so this adds buffering
with the assumption that incoming events are bursty.

[github-async]: https://developer.github.com/v3/guides/best-practices-for-integrators/#favor-asynchronous-work-over-synchronous
[github-ratelimit]: https://developer.github.com/v3/#rate-limiting
[pubsub]: https://cloud.google.com/pubsub

- https://github.com/google/go-cloud/tree/master/internal/contributebot
- https://github.com/googleapis/repo-automation-bots

---

Python 3.8. AppEngine. Manual scaling. Size 1.

- https://cloud.google.com/appengine/docs/the-appengine-environments
- https://cloud.google.com/appengine/docs/standard/python3/runtime#python-3.8-beta
- https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls
- https://cloud.google.com/appengine/docs/standard/python3/quickstart

Store data.
- https://firebase.google.com/docs/firestore/quickstart#python

Code owners format (same as [git ignore](https://git-scm.com/docs/gitignore#_pattern_format)).
- https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners

Terraform. AppEngine. Weave Flux
- https://www.weave.works/oss/flux/
- https://www.terraform.io/docs/providers/google/r/app_engine_application.html

Cloud Run has a cold start cost of about ~2 seconds. Python has a initialization delay of [~1.6 seconds](https://medium.com/@shouldroforion/battle-of-the-serverless-part-2-aws-lambda-cold-start-times-1d770ef3a7dc). Total cold start time of Python on Cloud Run will be around 3.6 seconds.
- https://github.com/ahmetb/cloud-run-faq

## Notes

- https://stackoverflow.com/questions/48182967/is-there-a-way-to-create-firewall-rules-for-my-google-cloud-functions-http-endpo
  - Cloud Functions do not support firewall rules

- https://cloud.google.com/appengine/docs/standard/python/application-security#app_engine_firewall
  - "Ensure that only a certain range of IP addresses from specific networks can access your app. You are not billed for traffic or bandwidth that is blocked by the firewall."

- https://github.com/doodla/octohook
- https://developer.github.com/v3/meta/

- https://cloud.google.com/run/docs/triggering/webhooks#creating_a_webhook_target_in 
- https://codelabs.developers.google.com/codelabs/cloud-run-hello-python3/index.html#0
- https://cloud.google.com/run/docs/tips
- https://github.com/GoogleContainerTools/distroless
- https://medium.com/@shouldroforion/battle-of-the-serverless-part-2-aws-lambda-cold-start-times-1d770ef3a7dc
  - Rust has good cold start times
