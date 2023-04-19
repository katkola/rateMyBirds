from flask_app.config.mysqlconnection import connectToMySQL

class bird:
    def __init__(self, data):
        self.id = data['id']