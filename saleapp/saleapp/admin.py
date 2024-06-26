from saleapp.saleapp import app, db
from flask_admin import Admin, BaseView, expose
from saleapp.saleapp.models import Category, Product
from flask_admin.contrib.sqla import ModelView
from flask import redirect

admin = Admin(app, name='eCommerce Website', template_mode='bootstrap4')


class CategoryView(ModelView):
    column_list = ['id', 'name', 'products']


class ProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    can_export = True
    column_sortable_list = ['id', 'name']
    column_searchable_list = ['id', 'name']
    column_editable_list = ['name', 'price']
    column_filters = ['id', 'name', 'price']


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        return redirect('/admin')


admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name='Thống kê báo cáo'))
admin.add_view(LogoutView(name='Đăng xuất'))

