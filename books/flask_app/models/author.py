from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL("books_schema").query_db(query)
        authors = []

        for a in results:
            authors.append(cls(a))
        return authors

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        result = connectToMySQL("books_schema").query_db(query, data)
        return result
    
    @classmethod
    def unfavorited_authors(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        authors = []
        results = connectToMySQL("books_schema").query_db(query, data)
        for row in results:
            authors.append(cls(row))
        return authors
    
