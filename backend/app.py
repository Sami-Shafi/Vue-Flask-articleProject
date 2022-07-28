from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/flask_backend"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
mm = Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class ArticleSchema(mm.Schema):
    class Meta:
        fields = ('id','title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many = True)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def get_articles():
    return jsonify({"Hello": "World!"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)