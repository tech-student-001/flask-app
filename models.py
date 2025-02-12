from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.String(10))
    style = db.Column(db.String(100))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    favorite_artwork = db.Column(db.String(100)) 
