from flask import Flask
from models import db, Artwork, Contact

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

artworks_data = [
    {"title": "Starry Night", "year": "2010", "style": "Post-Impressionism", "description": "A famous painting by Vincent van Gogh. A swirling night sky filled with stars over a quiet town.", "image_url": "https://saudigazette.com.sa/uploads/images/2021/07/01/1818162.jpeg"},
    {"title": "Caravan in the Desert", "year": "2012", "style": "Impressionist/Realist Painting", "description": "A vibrant painting of camels walking along a golden desert beside a blue sea.", "image_url": "https://images.joseartgallery.com/8493/conversions/landscape-painting-caravan-saudi-arabia-thumb900.jpg"},
    {"title": "Hijazi architecture", "year": "2014", "style": "Expressionism", "description": "A detailed depiction of traditional Hijazi architecture with ornate wooden balconies (Rawashin).", "image_url": "https://www.saudigazette.com.sa/uploads/images/2019/02/18/1160113.JPG"},
    {"title": "Spiral Motif", "year": "2015", "style": "Abstract textile art", "description": "Abstract spiral with earthy tones, stitched textures, and flowing curves.", "image_url": "https://www.saudigazette.com.sa/uploads/images/2019/02/18/1160112.JPG"},
    {"title": "Mural", "year": "2020", "style": "Mural painting", "description": "A wall mural illustrating rural agricultural life with a serene atmosphere.", "image_url": "https://saudigazette.com.sa/uploads/images/2019/10/07/1379075.jpg"}
]

contacts_data = [
    {"name": "Alice Johnson", "email": "alice@example.com", "phone": "1234567890", "favorite_artwork": "Starry Night"},
    {"name": "Bob Smith", "email": "bob@example.com", "phone": "9876543210", "favorite_artwork": "Caravan in the Desert"},
    {"name": "Charlie Brown", "email": "charlie@example.com", "phone": "5551234567", "favorite_artwork": "Hijazi architecture"}
]

with app.app_context():
    db.create_all()

    # Add artworks
    for art in artworks_data:
        existing = Artwork.query.filter_by(title=art["title"]).first()
        if not existing:
            db.session.add(Artwork(**art))
    db.session.commit()

    # Add contacts without artwork reference
    for contact in contacts_data:
        existing = Contact.query.filter_by(email=contact["email"]).first()
        if not existing:
            db.session.add(Contact(**contact))
    
    db.session.commit()
    print("Sample data added successfully!")