from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.register import User


# Brainstormed some ideas and used an old file here. check out whats going on. Friday we are doing the group meet - QT
class Bird:
    db_user = 'birds'
    def __init__(self, data):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.reason = data['reason']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM birds;"
        results = connectToMySQL('cls.db_user').query_db(query)
        lists = []
        for i in results:
            lists.append( cls(i))
        return lists

    @classmethod
    def save(cls, data):
        query = "INSERT INTO trees (species,location,reason,created_at,user_id) VALUES (%(species)s,%(location)s,%(reason)s,Now(),%(user_id)s);" 
        result = connectToMySQL(cls.db_user).query_db(query,data)
        return result

        
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM trees WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_user).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_them(cls,data):
        query  = "SELECT * FROM trees WHERE user_id = %(id)s;"
        result = connectToMySQL(cls.db_user).query_db(query,data)
        lists = []
        for i in result:
            lists.append( cls(i))
        return lists

    @classmethod
    def update(cls,data):
        print(data)
        query = "UPDATE trees SET species=%(species)s,location=%(location)s,reason=%(reason)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_user).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM trees WHERE id = %(id)s;"
        return connectToMySQL(cls.db_user).query_db(query,data)

    # @classmethod
    # def get_mine( cls , data ):
    #     query = "SELECT * FROM trees JOIN users ON trees.user_id = users.id WHERE users.id=%(id)s ;"
    #     results = connectToMySQL(cls.db_user).query_db( query , data )

    #     trees = []
        
    #     for row_from_db in results:
    #         this_tree = cls(row_from_db)

    #         data_user = {
    #             # **row_from_db,
    #             "id": row_from_db['users.id'],
    #             "first_name": row_from_db['first_name'],
    #             "last_name": row_from_db['last_name'],
    #             "email": row_from_db['email'],
    #             "password": row_from_db["password"],
    #             "created_at": row_from_db["users.created_at"],
    #             "updated_at": row_from_db["users.updated_at"]
    #         }
    #         this_user = User(data_user)
    #         this_tree.planter=this_user
    #         trees.append(this_tree)
    #     return trees



    @classmethod
    def get_everybodys(cls):
        query= "SELECT * FROM trees JOIN users ON trees.user_id = users.id;"
        results = connectToMySQL(cls.db_user).query_db(query)

        trees = []
        
        for row_from_db in results:
            this_tree = cls(row_from_db)

            data_user = {
                **row_from_db,
                "id": row_from_db['users.id'],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            this_user = User(data_user)
            this_tree.planter=this_user
            trees.append(this_tree)
        return trees


    @staticmethod
    def validate_plant(plant):
        is_valid_plant = True
        if len(plant['species']) < 2:
            is_valid_plant = False
            flash("species must be at least 2 characters.",'species')
        if len(plant['location']) < 2:
            is_valid_plant = False
            flash("Location must be at least 3 characters.",'location')
        if len(plant['reason']) < 5:
            is_valid_plant = False
            flash("reason must be more than 5 characters.",'reason')
        return is_valid_plant