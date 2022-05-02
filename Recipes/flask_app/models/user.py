from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import recipe
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.f_name = data["f_name"]
        self.l_name = data["l_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        email_matches = connectToMySQL("recipes").query_db(query, {"email": user["email"]})
        if len(email_matches) > 0:
            flash("That email is already in use", "register")
            is_valid = False
        if len(user["f_name"]) < 2:
            flash("Frist name  must be at least 2 characters", "register")
            is_valid = False
        if len(user["l_name"]) < 2:
            flash("Last name  must be at least 2 characters", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if user["password"] != user["confirm_password"]:
            flash("The passwords entered don't match", "register")
            is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (f_name, l_name, email, password) VALUES ( %(f_name)s, %(l_name)s, %(email)s, %(password)s);"
        results = connectToMySQL("recipes").query_db(query, data)
        return results 

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("recipes").query_db(query, data)
        if len(results) == 0:
            return False
        return cls(results[0])

    @classmethod
    def get_user_with_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL("recipes").query_db(query, data)
        this_user = cls(results[0])
        for row in results:
            data = {
                "id" : row["recipes.id"],
                "name" : row["name"],
                "description" : row["description"],
                "instructions" : row["instructions"],
                "under_30" : row["under_30"],
                "date_made" : row["date_made"],
                "created_at" : row["recipes.created_at"],
                "updated_at" : row["recipes.updated_at"],
                "user_id" : row["user_id"]
                }
            this_user.recipes.append(recipe.Recipe(data))
        return this_user
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("recipes").query_db(query, data)
        return cls(results[0])