from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.rating import Rating
import json
import requests
from flask_app.config.config import api_key

class Bird:
    db_name = 'birds-schema'

    def __init__(self, data):
        self.id = data['id']
        self.species = data['species']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image_url = data['image_url']
        self.user = data["user"]
        self.avg_rating = 0

    @classmethod
    def save(cls,data):
        query = "INSERT INTO birds (species, description, user_id, created_at,updated_at, image_url) VALUES(%(species)s,%(description)s, %(user_id)s,NOW(),NOW(), %(image_url)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def update(cls,data):
            query = "UPDATE birds SET species=%(species)s,description=%(description)s WHERE id = %(id)s;"
            data = {
                "species": species,
                "description": description
            }
            return connectToMySQL(cls.db_user).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM birds LEFT JOIN users ON birds.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)

        birds = []

        for var in results:
            # birds.append(cls(var))
            calculated_rating = Rating.get_average_rating({'id': var['id']})
            var["user"] = User.get_one({"id": var["user_id"]})
            this_info = cls(var)
            this_info.avg_rating = calculated_rating
            birds.append(this_info)
        return birds

    @classmethod
    def get_birds_by_user(cls, data):
        query = "SELECT * FROM birds WHERE birds.user_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        birds = []
        for bird in results:
            bird['user'] = User.get_one({"id": bird["user_id"]})
            birds.append(cls(bird))
        return birds

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM birds WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        user = User.get_one({"id": results[0]["user_id"]})
        results[0]["user"] = user 

        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_bird(bird):
        is_valid = True
        if len(bird['species'])<3 :

            return False
        if len(bird['description'])<3 :

            return False
        return is_valid
        
    @staticmethod
    def get_bird_image(description):
        url = "https://api.unsplash.com/photos/random"
        parameters = {
            "query": description,
            "client_id": api_key
        }
        response = requests.get(url, params=parameters)
        print(type(json.loads(response.content)))
        return json.loads(response.content)['urls']['raw']

    @classmethod
    def update(cls,data):     
            query = "UPDATE birds SET species=%(species)s,description=%(description)s WHERE id = %(id)s;"
        

            return connectToMySQL(cls.db_name).query_db(query,data)
