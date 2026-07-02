from flask import request
from pydantic import ValidationError
from flask_restful import Resource
from app.models.category_model import Category
from app.schemas.category_schema import CategorySchema
from app.services.category_service import category_service  

class CategoryResource(Resource):
    
    def get(self):
        try:

            categories = category_service.get_all()
            categories_list = [category.to_json() for category in categories]
            return categories_list, 200

        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def post(self):
        try:
            
            data = request.get_json()
            validated_data = CategorySchema.model_validate(data)

            category = category_service.get_by_name(validated_data.name)

            if category:
                return {
                    'error': "category already exists"
                }, 400
            
            create_category = category_service.create(validated_data)

            return create_category.to_json(), 200
            
        except ValidationError as e:
            return {
                'error': str(e)
            }
        except Exception as e:
            return {
                'error': str(e)
            }, 400

class ManagerCategoryResource(Resource):
    
    def get(self, id_category: int):
        try:
            
            category = category_service.get_by_id(id_category)

            if category is None:
                return {
                    'error': "category not found"
                }, 404
            
            return category.to_json(), 200

        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def put(self, id_category: int):
        try:
            category = category_service.get_by_id(id_category)

            if category is None:
                return {
                    'error': "category not found"
                }, 404
            
            data = request.get_json()
            validated_data = CategorySchema.model_validate(data)
            update_category = category_service.update(category, validated_data)

            return update_category.to_json(), 200
        
        except ValidationError as e:
            return {
                'error': str(e)
            }
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def delete(self, id_category: int):
        try:
            category = category_service.get_by_id(id_category)

            if category is None:
                return {
                    'error': "category not found"
                }, 404
            
            category_service.delete(category)

            return None, 200

        except Exception as e:
            return {
                'error': str(e)
            }, 400
