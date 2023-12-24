from flask import Flask, redirect, request
import requests
from oauthlib.oauth2 import WebApplicationClient
import json

app = Flask(__name__)

GOOGLE_CLIENT_ID = "1054406157740-qh53eu7qlugm13srihbrq93utei0vud3.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

"""
{"installed":{"client_id":"1054406157740-qh53eu7qlugm13srihbrq93utei0vud3.apps.googleusercontent.com","project_id":"gmail-sifter","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["http://localhost"]}}
"""


@app.route("/login")
def login():
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

"""callback"""
@app.route("/login/callback") 
def callback():
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for things on behalf of a user
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

 # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (access_token and refresh_token)
    # you can use them to make API requests to get user information
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        # Do something with this information!
        # e.g., Create a user in your db with the information provided
        # by Google

    return "User information retrieved successfully!"

"""For local development, using ssl_context="adhoc" in app.run() is okay, but for a production environment, you should use a proper SSL certificate."""
if __name__ == "__main__":
    app.run(ssl_context="adhoc")

"""Need to add logic"""
@app.errorhandler(ValueError)
def handle_value_error(e):
    print("{e.description}")
    return "Invalid input!", 400

@app.errorhandler(404)
def page_not_found(e):
    print("{e.description}")
    return "404 Page Not Found", 404

class OAuthError(Exception):
    def __init__(self, description):
        self.description = description

# Then, use the standard errorhandler to catch this exception
@app.errorhandler(OAuthError)
def handle_oauth_error(e):
    print("{e.description}")
    app.logger.error(f"OAuth error: {e.description}")

    # Redirect to a custom error page or return a custom error message
    return f"OAuth error: {e.description}", 500


@app.errorhandler(500)
def internal_server_error(e):
    print("{e.description}")
    return "500 Internal Server Error", 500

