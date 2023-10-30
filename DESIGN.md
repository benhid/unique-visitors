The number of unique visits in any period of time is the number of total visits minus the number of repeat visits from the same users. To get an accurate result, you need to track repeat visits somehow.

# Tracking repeat visits

Cookies represent the most common method to trace repeat visits. When users access a website, their computer stores a cookie. Upon revisiting, the cookie is sent to the server and the server knows that this is a repeat visit from the same user. Nonetheless, within the EU, obtaining explicit consent for cookies is mandatory. Privacy tools frequently block them, and their storage can pollute the user's browser with unwanted data.

## Privacy implications

An alternative method involves leveraging the user's IP address and other data, like the user agent, to discern their identity. This Client ID might be look like this: `clientId=(SiteID+UserAgent+UserIP+...)`. The Client ID is then stored in a database and checked every time the user visits the website to see if they've visited it before. But fingerprinting users poses numerous privacy concerns and has the potential to reveal someone's identity if the data is leaked or stolen.

Many privacy-focuses services will store a hash of the fingerprint instead of the fingerprint itself. This looks like a step in the right direction, yet leaked or stolen hashes can still be used to reconstruct the browsing history of a user.

For our project, we wanted to find a way to track repeat visits without storing any personal information directly.

Goals:
- Estimate unique website visitors (we don't typically need exact numbers).
- Avoid storing identifiable information.
- Avoid using cookies.

Non-goals:
- Tracking beyond a single browser session.

## Approximating unique visitors

The idea is to use a probabilistic data structure, i.e., HyperLogLog, to estimate the number of unique visitors of a website.

When a user visits a website, we first check whether the `referer` header matches our site. Cross-site visits are discarded. 
Then, a Client ID, derived from available server data (like user agent and IP address), is generated and incorporated into a HyperLogLog sketch.

The HyperLogLog can be queried to get an estimate of the number of elements (visits) in it. This estimate is not exact, but it is very close to the real number of elements.

To prevent data loss during server restarts, we persist the HyperLogLog sketches in a PostgreSQL database (via the `postgresql-hll` extension).
Databases like Redis [natively](https://redis.io/docs/data-types/probabilistic/hyperloglogs/) support HyperLogLog sketches, posing an interesting alternative to PostgreSQL.

## Advanced use cases

HyperLogLog sketches can be merged together to get an estimation of the combined elements. This is useful when estimating the number of unique visitors across multiple websites or for a single website over any period of time.

For more advanced queries, we can create a table with the following columns:

* Date (YYYY-MM-DD)
* Location (Country)
* Unique visitors (HLL)

This works well to get the number of unique visitors from a specific country on a specific date. 

To get the number of unique visitors from a specific country over any period of time, we can merge the daily sketches.

# Monitoring

> This section is a work in progress. Not all the systems are in place yet.

The server exposes a `/metrics` endpoint that can be scraped by Prometheus. The endpoint returns the following metrics:

* `http_requests_total`: the total number of HTTP requests received by the server.
* `http_requests_duration_seconds`: the duration of HTTP requests.
* `http_errors_total`: the total number of HTTP errors returned by the server.

The server also exposes a `/healthz` endpoint that can be scraped by Kubernetes. This endpoint returns a 200 status code if the server is healthy and can be used for liveness probes.

## Logging

The server logs all the requests and emits structured output (JSON) to `stdout`, so it can be collected by a log aggregator.
