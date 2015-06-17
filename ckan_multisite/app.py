# Copyright 2015 Boxkite Inc.

# This file is part of the ckan-multisite package and is released
# under the terms of the MIT License.
# See LICENSE or http://opensource.org/licenses/MIT

from flask import Flask, redirect
from flask.ext.admin import Admin
from ckan_multisite.api import bp as api_bp
from ckan_multisite.admin import admin
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
admin.init_app(app)
db.init_app(app)
app.register_blueprint(api_bp)

@app.route('/')
def index():
    return redirect('/admin')


if __name__ == '__main__':
    app.run(debug=True)
