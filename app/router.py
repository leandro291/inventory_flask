from app import app
from flask_restful import Api

from app.resources.category_resource import CategoryResource, ManagerCategoryResource
from app.resources.company_resource import CompanyResource, ManagerCompanyResource
from app.resources.role_resource import RoleResource, ManagerRoleResource
from app.resources.auth_resource import LoginResource, RegisterResource

api = Api(app, prefix="/api/v1")

api.add_resource(LoginResource, "/auth/login")
api.add_resource(RegisterResource, "/auth/register")

api.add_resource(CategoryResource, "/category")
api.add_resource(ManagerCategoryResource, "/category/<int:id_category>")

api.add_resource(RoleResource, "/role")
api.add_resource(ManagerRoleResource, "/role/<int:id_role>")

api.add_resource(CompanyResource, "/company")
api.add_resource(ManagerCompanyResource, "/company/<int:id_company>")