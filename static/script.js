console.log("Script loaded successfully");


document.addEventListener("DOMContentLoaded", function () {
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const artworkContainer = document.querySelector(".artwork-container");
    const artworks = document.querySelectorAll(".artwork-card");
    let index = 0;

    function updateGallery() {
        artworks.forEach((artwork, i) => {
            artwork.style.display = i === index ? "block" : "none";
        });
    }

    prevBtn.addEventListener("click", function () {
        index = (index > 0) ? index - 1 : artworks.length - 1;
        updateGallery();
    });

    nextBtn.addEventListener("click", function () {
        index = (index < artworks.length - 1) ? index + 1 : 0;
        updateGallery();
    });

    updateGallery(); // Initialize gallery
});

// Show the Add Contact Form
function openAddContactForm() {
    document.getElementById("addContactForm").style.display = "block";
}

// Hide the Add Contact Form
function closeAddContactForm() {
    document.getElementById("addContactForm").style.display = "none";
}

// Handle Form Submission
document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch("/manage_contact", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            if (data.success) {
                location.reload(); // Refresh the page to show new contact
            }
        })
        .catch(error => console.error("Error:", error));
});

//delete contact: 
function deleteContact(contactId) {
    if (confirm("Are you sure you want to delete this contact?")) {
        fetch(`/delete_contact/${contactId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById(`contact-${contactId}`).remove();
                alert("Contact deleted successfully.");
            } else {
                alert("Error deleting contact.");
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

//update contact
function openEditContactForm(contactId) {
    fetch(`/get_contact/${contactId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success === false) {
                alert("Contact not found.");
                return;
            }

            document.getElementById('edit-contact-id').value = data.id;
            document.getElementById('edit-name').value = data.name;
            document.getElementById('edit-email').value = data.email;
            document.getElementById('edit-phone').value = data.phone;
            document.getElementById('edit-favorite-artwork').value = data.favorite_artwork;

            document.getElementById('editContactForm').style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
}

function closeEditContactForm() {
    document.getElementById('editContactForm').style.display = 'none';
}

document.getElementById('editForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const contactId = document.getElementById('edit-contact-id').value;
    const updatedData = {
        name: document.getElementById('edit-name').value,
        email: document.getElementById('edit-email').value,
        phone: document.getElementById('edit-phone').value,
        favorite_artwork: document.getElementById('edit-favorite-artwork').value
    };

    fetch(`/update_contact/${contactId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Contact updated successfully.");
            location.reload(); // Refresh page to update table
        } else {
            alert("Error updating contact.");
        }
    })
    .catch(error => console.error('Error:', error));
});