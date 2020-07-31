# Ссылки для проверки:
# https://tranquil-escarpment-45744.herokuapp.com/success
# https://tranquil-escarpment-45744.herokuapp.com/fail

import os
import sentry_sdk

from bottle import route, run, HTTPError, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://36bcda97367647a3b8ba67436f3297eb@o427857.ingest.sentry.io/5372543",
    integrations=[BottleIntegration()]
)

@route("/")
def main():
    result = HTTPResponse(status=200, body="OK")
    return result

@route("/success")
def success():
    result = HTTPResponse(status=200, body="OK")
    return result

@route("/fail")
def fail():
    raise RuntimeError("There is an error!")

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
