from app.models.product_model import Product
from app.schemas.product_schema import ProductSchema
from db import db

class ProductService:

    def get_all(self) -> list[Product]:
        products = Product.query.filter_by(status=True).all()
        return products
    
    def get_last(self) -> Product | None:
        product = Product.query.order_by(
            Product.id_product.desc()
        ).first()
        return product

    def create(
            self,
            data: ProductSchema,
            code: str,
            image: str
    ) -> Product:
        product = Product(
            name=data.name,
            code=code,
            description=data.description,
            image=image,
            brand=data.brand,
            purchase_price=data.purchase_price,
            sale_price=data.sales_price,
            id_category=data.id_category
        )
        db.session.add(product)
        db.session.commit()

        return product
    
product_service = ProductService()