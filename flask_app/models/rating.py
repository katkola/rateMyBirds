from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Rating:
    db_name = 'birds-schema'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.bird_id = data['bird_id']
        self.value = data['value']
        self.user = data['user']

    
    @classmethod
    def save(cls,data):
        query = '''INSERT INTO ratings (value, bird_id, user_id, created_at,updated_at) 
            VALUES(%(value)s,%(bird_id)s, %(user_id)s,NOW(),NOW())'''
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query= """UPDATE ratings 
                SET value=%(value)s
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ratings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        user = User.get_one({"id": results[0]["user_id"]})
        results[0]['user'] = user
        return cls(results[0])
    
    @classmethod
    def get_user_rating(cls,data):
        print(data)
        query = """SELECT * FROM ratings
                WHERE ratings.user_id= %(user_id)s
                AND ratings.bird_id = %(bird_id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if not results:
            return False
        
        user = User.get_one({"id": results[0]["user_id"]})
        results[0]['user'] = user
        rating = results[0]

        return rating

    @classmethod
    def get_ratings_for_bird(cls,data):
        query= ''' SELECT *
                FROM Ratings
                WHERE bird_id= %(id)s'''
        results = connectToMySQL(cls.db_name).query_db(query, data)
        ratings = []
        if not results:
            return ratings
        for rating in results:
            user = User.get_one({"id": rating["user_id"]})
            rating['user'] = user
            ratings.append(cls(rating))
        return ratings


    @classmethod
    def get_average_rating(cls,data):
        query= ''' SELECT * FROM ratings WHERE ratings.bird_id = %(id)s;'''
        results = connectToMySQL(cls.db_name).query_db(query, data)
        ratings_sum = 0
        ratings_count = 0
        ratings_average = 0.0
        for rating in results:
            ratings_sum= ratings_sum + rating['value']
            ratings_count= ratings_count+1
        if ratings_count==0:
            return "No Ratings Yet"
        ratings_average = ratings_sum/ratings_count
        return ratings_average
