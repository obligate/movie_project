# coding:utf8
# Author: Peter
from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views
