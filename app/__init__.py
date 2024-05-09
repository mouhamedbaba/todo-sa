from flask import Flask, blueprints

app = Flask(__name__)
app.config.from_object('config')