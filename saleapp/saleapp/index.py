from flask import Flask, render_template, request
import dao


app = Flask(__name__)


@app.route("/")
def index():
    kw = request.args.get("kw")
    cate_id = request.args.get("category_id")

    cates = dao.load_categories()
    prods = dao.load_products(kw=kw, cate_id=cate_id);

    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

