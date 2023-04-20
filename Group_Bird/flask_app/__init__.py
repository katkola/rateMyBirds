from flask import Flask


# need to create a data base as a group? -QT
DATABASE = "login_reg_db"

app=Flask(__name__)


app.secret_key='juj'