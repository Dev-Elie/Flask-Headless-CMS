from app import db,ma
from datetime import datetime


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return "<Articles %r>" % self.title

# Generate marshmallow Schemas from your models
class ArticlesShema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","title", "body", "date")


article_schema = ArticlesShema()
articles_schema = ArticlesShema(many=True)



class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300),nullable=False)

    def __repr__(self):
        return "<Authors %r>" % self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300),nullable=False)

    def __repr__(self):
        return "<Category %r>" % self.title