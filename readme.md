# Python Experiments

## Monorepo on GitHub

Monorepo allows for easier code sharing across projects. Standardization of software developement practices (such as lint rules) are easier when all code is in a single repo. One challenge the monorepo presents is access control. Multiple repositories on GitHub allow for fine grained access control (read/write) at the per repo level. In a monorepo, everyone has global read and write. To solve the write access problem, a land queue will be built to enforce access control. All users will still have global read, however merges will be done exclusively via the land queue. The land queue will enforce security policy.

## Land Queue

![](http://www.plantuml.com/plantuml/proxy?cache=no&fmt=svg&src=https://raw.githubusercontent.com/bootstraponline/python/master/overview_0.puml&githubcachefoo)

The [GitHub meta](https://developer.github.com/v3/meta/) API is used to fetch a list of GitHub's IP addresses. The [AppEngine firewall](https://cloud.google.com/appengine/docs/standard/python/creating-firewalls) is configured to drop traffic not coming from GitHub.

> Favor asynchronous work over synchronous
>
> GitHub expects that integrations respond within 10 seconds of receiving the webhook payload. If your service takes longer than that to complete, then GitHub terminates the connection and the payload is lost.
> https://developer.github.com/v3/guides/best-practices-for-integrators/#favor-asynchronous-work-over-synchronous

After a webhook payload is processed by Flask, it's submitted to [Cloud Pub/Sub](https://cloud.google.com/pubsub). An event listener then picks up the payload and processes it. 

## Tech Stack

- AppEngine Standard
- Python 3.8
- Flask

## User stories

As an engineer, I want to merge my pull request by adding a `land requested` label so that the code is merged automatically.
As a security engineer, I want to ensure access control on folders in the monorepo so that engineers don't have global write access.
As an infrastructure engineer, I want to calculate productivity metrics (such as diff land time) to understand the health of the land queue.

## Feature backlog

- Deploy a webhook server using [doodla/octohook](https://github.com/doodla/octohook) to parse the payload.
- Create an event listener for Cloud Pub/Sub.
  - See [contributebot](https://github.com/google/go-cloud/tree/master/internal/contributebot) for Pub/Sub example
- Define terraform rules to deploy AppEngine infrastructure automatically.
  - See [main.tf](https://github.com/google/go-cloud/blob/master/internal/contributebot/main.tf) as an example.
- When a `land requested` label is applied to a pull request, squash merge the pull request.
  - The pull request title represents the commit title. The pull request body is the commit body.
  - Ensure there's at least 1 non-author reviewer that has approved the pull request before merging.
- Dynamically apply AppEngine firewall rules via [github meta](https://developer.github.com/v3/meta/) to only accept inbound from GitHub's IP ranges
- Define access controls per directory. Store a file in `.github/.landqueue` using the code [owners format]( https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners) (same as [git ignore](https://git-scm.com/docs/gitignore#_pattern_format)). Code can't be landed into a protected folder unless an owner has approved.
- Build out a testing strategy using a mock server
- Define a strategy for handling merge conflicts / providing feedback to PR owners
  - Detect when merges will conflict with other pull requests. Prefer to keep master stable by merging in a stack.

