from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)

engine = create_engine('postgresql://[username]:[password]@127.0.0.1/[DataBase name]')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()














if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
