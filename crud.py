from models import db, Contact, Artwork
from sqlalchemy.exc import IntegrityError

def create_contact(name, email, phone, favorite_artwork):
    """Create a new contact."""
    try:
        new_contact = Contact(name=name, email=email, phone=phone, favorite_artwork=favorite_artwork)
        db.session.add(new_contact)
        db.session.commit()
        return new_contact
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return None

def get_all_contacts():
    """Retrieve all contacts from the database."""
    return Contact.query.all()

def get_contact_by_id(contact_id):
    """Fetches a specific contact by ID."""
    return Contact.query.get(contact_id)

def update_contact(contact_id, name, email, phone, favorite_artwork):
    """Updates an existing contact."""
    contact = Contact.query.get(contact_id)
    if contact:
        try:
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.favorite_artwork = favorite_artwork
            db.session.commit()
            return {"success": True, "message": "Contact updated successfully"}
        except IntegrityError:
            db.session.rollback()
            return {"success": False, "message": "Error: Could not update contact"}
    return {"success": False, "message": "Error: Contact not found"}

def delete_contact(contact_id):
    """Deletes a contact by ID."""
    contact = Contact.query.get(contact_id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        return {"success": True, "message": "Contact deleted successfully"}
    return {"success": False, "message": "Error: Contact not found"}

#-----------Artworks--------------

def get_all_artworks():
    """Retrieve all Artwork from the database."""
    return Artwork.query.all()
