from flask_app.config.mysqlconnection import connectToMySQL

class Bird:
    db_name = 'ratebirds'
    def __init__(self, data):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        ratings = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM birds;"
        results = connectToMySQL('cls.db_name').query_db(query)
        lists = []
        for i in results:
            lists.append( cls(i))
        return lists
