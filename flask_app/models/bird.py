from flask_app.config.mysqlconnection import connectToMySQL


class Bird:
    db_name = 'birds-schema'

    def __init__(self, data):
        self.id = data['id']
        self.species = data['species']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO birds (species, description, user_id, created_at,updated_at) VALUES(%(species)s,%(description)s, %(user_id)s,NOW(),NOW())"
        return connectToMySQL(cls.db_name).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM birds;"
        results = connectToMySQL(cls.db_name).query_db(query)
        birds = []
        for i in results:
            birds.append(cls(i))
        return birds

    @classmethod
    def get_birds_by_user(cls, data):
        query = "SELECT * FROM birds WHERE birds.user_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        birds = []
        for bird in results:
            birds.append(cls(bird))
        return birds

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM birds WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
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
