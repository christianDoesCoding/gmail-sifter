from flask import Flask, redirect, request
import requests
from oauthlib.oauth2 import WebApplicationClient

app = Flask(__name__)

