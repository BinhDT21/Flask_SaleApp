from saleapp.saleapp import db, app
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
    #     Lazy nghĩa là khi truy vấn Category cần nó mới lấy Product không thì thôi không tự lấy

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # create_all tạo script tạo database category

    # c1 = Category(name='Mobile')
    # c2 = Category(name='Laptop')
    # c3 = Category(name='Tablet')
    #
    # db.session.add_all([c1, c2, c3])
    # db.session.commit()
    # thêm dòng dữ liệu


        import json
        with open('data/products.json', encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
                prod = Product(name=p['name'], price=p['price'], image=p['image'], category_id=p['category_id'])
                db.session.add(prod)
            db.session.commit()

