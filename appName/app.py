from distutils.command.config import config
import json
import os
from .functions import *
from werkzeug.utils import secure_filename
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from .apps import *


app = Flask(__name__,
            static_folder='./dist/static',
            template_folder='./dist/',
            )

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

###Apps###
app_auth = Auth(app)
app_auth.methods()

app_test =  Test(app)
app_test.methods()

__all__ = ['app']