from flask_app.config.mysqlconnection import connectToMySQL


class Rating:
    db_name = 'birds_schema'

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
    def get_one(cls,data):
        query = "SELECT * FROM ratings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        user = User.get_one({"id": results[0]["user_id"]})
        results[0]['user'] = user
        return cls(results[0])

    @classmethod
    def get_ratings_for_bird(cls,data):
        query= ''' SELECT *
                FROM Ratings
                WHERE   '''
        results = connectToMySQL(cls.db_name).query_db(query, data)

        ratings = []
        for rating in results:
            user = User.get_one({"id": rating[0]["user_id"]})
            rating['user'] = user
            ratings.append(cls(rating))
        return ratings


    @classmethod
    def get_average_rating(cls,data):
        query= ''' SELECT * FROM ratings WHERE ratings.bird_id = %(id)s;'''
        results = connectToMySQL(cls.db_name).query_db(query, data)

        ratings = []
        ratings_sum = 0
        ratings_count = 0
        rating_average = 0.0
        for rating in ratings:
            ratings_sum+= cls(rating).value
            ratings_count+=1
        ratings_total = ratings_sum/ratings_count
        return ratings_total
