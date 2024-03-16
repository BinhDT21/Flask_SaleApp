from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route("/")
def index():
    kw = request.args.get("kw")
    cate_id = request.args.get("category_id")


    prods = dao.load_products(kw=kw, cate_id=cate_id);

    return render_template('index.html', products=prods)


@app.route('/login')
def process_login_user():
    return render_template('login.html')

@app.context_processor
def commont_attributes():
    return {
        'categories': dao.load_categories()
    }

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
