from db import db
from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from app.models.role_model import Role
from app.schemas.role_schema import RoleSchema

class RoleResource(Resource):
    
    def get(self):
        
        try:

            roles: list[Role] = Role.query.all()
            roles_list = [role.to_json() for role in roles]
            return roles_list

        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def post(self):
        try:

            data = request.get_json()
            validated_data = RoleSchema.model_validate(data)

            name = Role.query.filter_by(name=validated_data.name).first()

            if name:
                return {
                    'error': 'role alredy exists'
                }, 400

            created_role = Role(
                name=validated_data.name,
                description=validated_data.description
            )

            db.session.add(created_role)
            db.session.commit()

            return created_role.to_json(), 200

        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400


class ManageRolResource(Resource):

    def get(self, id_role: int):
        try:
            
            rol: Role = Role.query.filter_by(id_role=id_role).first()

            if rol is None:
                return {
                    'error': "rol nout found"
                }, 400
            
            return rol.to_json(), 200

        except Exception as e:
            return {
                'error': str(e)
            }

    def put(self, id_role: int):
        try:

            rol: Role = Role.query.filter_by(id_role=id_role).first()

            if rol is None:
                return {
                    'error': "rol nout found"
                }, 400

            data = request.get_json()
            validated_data = RoleSchema.model_validate(data)

            name = Role.query.filter_by(name=validated_data.name).first()

            if name:
                return {
                    'error': 'role alredy exists'
                }, 400
            
            rol.name = validated_data.name
            rol.description = validated_data.description

            db.session.commit()

            return rol.to_json(), 200
        
        except ValidationError as e:
            return {
                'error': e.errors()
            }
        except Exception as e:
            return {
                'error': str(e)
            }

    def delete(self, id_role: int):
        try:
            rol: Role = Role.query.filter_by(id_role=id_role).first()

            if rol is None:
                return {
                    'error': "rol nout found"
                }, 400
            
            rol.status = False

            db.session.commit()

            return None, 200
            
        except Exception as e:
            return {
                'error': str(e)
            }
