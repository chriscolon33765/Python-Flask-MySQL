from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under_30 = data["under_30"]
        self.date_made = data["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) == 0:
            flash("Please fill in the Name field", "recipe")
            is_valid = False 
        elif len(recipe["name"]) < 3:
            flash("Name must have at least 3 characters", "recipe")
            is_valid = False
        if len(recipe["description"]) == 0:
            flash("Please fill in the Description field", "recipe")
            is_valid = False
        elif len(recipe["description"]) < 3:
            flash("Description must have at least 3 characters", "recipe")
            is_valid = False
        if len(recipe["instructions"]) == 0:
            flash("Please fill in the Instructions field", "recipe")
            is_valid = False
        elif len(recipe["instructions"]) < 3:
            flash("Instructions must have at least 3 characters", "recipe")
            is_valid = False
        if recipe["date_made"] == "":
            flash("Please fill in the date made", "recipe")
            is_valid = False 
        if "under_30" not in recipe:
            flash("Please click whether this was made in under 30 minutes", "recipe")
            is_valid = False 
        return is_valid
        

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date_made)s, %(user_id)s);"
        result = connectToMySQL("recipes").query_db(query,data)
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, date_made=%(date_made)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL("recipes").query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("recipes").query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s";
        result = connectToMySQL("recipes").query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes").query_db(query)
        all_recipes = []
        for row in results:
            print(row["date_made"])
            all_recipes.append(cls(row))
        return all_recipes
