from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from forms import RegisterForm, LoginForm, EntryForm


# Configure the App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
db = SQLAlchemy(app)

# Lets Import the User and Entry Models

from models import User, Entry


# Calling the run function
if __name__ == '__main__':
    app.run(debug=True)
    
    