from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Artwork, Contact
import crud

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.route('/')
def index():
    artworks = Artwork.query.all()
    return render_template('index.html', artworks=artworks)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    artworks = Artwork.query.all()
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        favorite_artwork = request.form.get('favorite_artwork') or None 
        
        try:
            new_contact = Contact(name=name, email=email, phone=phone, favorite_artwork=favorite_artwork)
            db.session.add(new_contact)
            db.session.commit()
            flash('Contact added successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')

    return render_template('contact.html', artworks=artworks)


@app.route('/manage_contact', methods=['GET', 'POST'])
def manage_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        favorite_artwork = request.form.get('favorite_artwork') or None 

        new_contact = crud.create_contact(name, email, phone, favorite_artwork)

        if new_contact:
            return jsonify({'success': True, 'message': 'Contact added successfully!'})
        else:
            return jsonify({'success': False, 'message': 'Failed to add contact!'})

    contacts = crud.get_all_contacts()
    artworks = crud.get_all_artworks()

    return render_template('manage_contact.html', contacts=contacts, artworks=artworks)

@app.route('/get_contact/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = crud.get_contact_by_id(contact_id)
    if contact:
        return jsonify({
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'favorite_artwork': contact.favorite_artwork
        })
    return jsonify({'success': False, 'message': 'Contact not found'})

@app.route('/update_contact/<int:contact_id>', methods=['POST'])
def update_contact(contact_id):
    data = request.json
    result = crud.update_contact(contact_id, data['name'], data['email'], data['phone'], data['favorite_artwork'])
    return jsonify(result)

@app.route('/delete_contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    result = crud.delete_contact(contact_id)
    return jsonify(result)





@app.route('/manage_artwork', methods=['GET', 'POST'])
def manage_artwork():
    artworks = Artwork.query.all()
    return render_template('manage_artwork.html', artworks=artworks)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
