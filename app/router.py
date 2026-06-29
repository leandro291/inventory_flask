from app import app
from flask_restful import Api
from app.resources.role_resource import RoleResource, ManageRolResource

api = Api(app, prefix="/api/v1")

api.add_resource(RoleResource, "/role")
api.add_resource(ManageRolResource, "/role/<int:id_role>")