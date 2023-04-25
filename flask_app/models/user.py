from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    db_name = 'birds-schema'
    def __init__(self,data):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.birds = []
        # birds=[]
        # ratings=[]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (firstname,lastname,email,password,created_at,updated_at) VALUES(%(firstname)s,%(lastname)s,%(email)s,%(password)s,NOW(),NOW())"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return User(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['firstname']) < 2:
            is_valid = False
            flash("First name must be at least 3 characters","user")
        if len(user['lastname']) < 2:
            is_valid = False
            flash("Last name must be at least 3 characters","user")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Invalid Email Address","user")
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters","user")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match!","user")

        return is_valid