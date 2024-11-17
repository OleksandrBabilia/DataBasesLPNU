import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import the useNavigate hook
import { getGenreName } from '../helpers/genreHelper';
import DatePicker from 'react-datepicker'; // Import the date picker
import "react-datepicker/dist/react-datepicker.css"; // Import the CSS for datepicker
import { Modal, Button } from 'react-bootstrap'; // Import Modal and Button components from React Bootstrap

const BookItem = ({ book, author, publisher }) => {
  const navigate = useNavigate(); // Initialize useNavigate hook
  const [isRented, setIsRented] = useState(book.rented); // Track book rental status
  const [showModal, setShowModal] = useState(false); // State to toggle modal visibility
  const [rentalDate, setRentalDate] = useState(new Date()); // Default rental date to current time
  const [returnDate, setReturnDate] = useState(new Date()); // Default return date to current time

  // Function to handle renting a book
  const handleRentBook = async () => {
    const rentalData = {
      rental_date: rentalDate.toISOString(), // Convert rentalDate to ISO string
      return_date: returnDate.toISOString(), // Convert returnDate to ISO string
    };

    // Retrieve the token from localStorage
    const token = localStorage.getItem('token');
    console.log(token);

    if (!token) {
      // If there's no token, prompt the user to log in or sign up
      alert('You are not logged in. Please log in first.');
      navigate('/login'); // Redirect to the login page
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/v1/books/${book.id}/rent/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(rentalData),
      });

      if (response.ok) {
        const result = await response.json();
        setIsRented(true); // Update rental status after successful rental
        alert('Book rented successfully!');
        console.log('Response:', result);
      } else if (response.status === 401) {
        // If the user is unauthorized (status code 401), redirect to /signup
        alert('You are not authorized. Please sign up.');
        navigate('/signup'); // Redirect to the signup page
      } else {
        alert('Failed to rent book. Please try again.');
        console.error('Error:', await response.json());
      }
    } catch (error) {
      console.error('Error occurred while renting the book:', error);
    }
  };

  return (
      <div className="col-md-3 mb-4">
        <div className="card h-100">
          <img
              src={book.cover || '/default_book_image.jpg'}
              className="card-img-top"
              alt={`${book.title} cover`}
          />
          <div className="card-body">
            <h5 className="card-title">{book.title}</h5>
            <p className="card-text">
              <strong>ISBN:</strong> {book.isbn}
            </p>
            <p className="card-text">
              <strong>Rented:</strong> {book.rented ? 'Yes' : 'No'}
            </p>
            <p className="card-text">
              <strong>Author(s):</strong>{' '}
              {book.author
                  .map((authorId) => author[authorId] || 'Unknown Author')
                  .join(', ')}
            </p>
            <p className="card-text">
              <strong>Publisher:</strong>{' '}
              {publisher[book.publisher] || 'Unknown Publisher'}
            </p>
            <p className="card-text">
              <strong>Genres:</strong> {getGenreName(book.ganres)}
            </p>

            {/* Availability indicator */}
            {!isRented ? (
                <p className="text-success"><strong>Available</strong> <span role="img" aria-label="check">✔️</span></p>
            ) : (
                <p className="text-danger"><strong>Not Available</strong> <span role="img" aria-label="cross">❌</span>
                </p>
            )}

            {/* Rent button (only show if the book is available) */}
            {!isRented && (
                <button onClick={() => setShowModal(true)} className="btn btn-primary">
                  Rent this Book
                </button>
            )}
          </div>
        </div>

        {/* Modal for picking rental and return dates */}
        <Modal show={showModal} onHide={() => setShowModal(false)}>
          <Modal.Header closeButton>
            <Modal.Title>Pick Rental and Return Dates</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <div className="mb-3">
              <label htmlFor="rental-date" className="form-label">Rental Date</label>
              <DatePicker
                  selected={rentalDate}
                  onChange={date => setRentalDate(date)}
                  showTimeSelect
                  dateFormat="Pp"
                  id="rental-date"
                  className="form-control"
              />
            </div>

            <div className="mb-3">
              <label htmlFor="return-date" className="form-label">Return Date</label>
              <DatePicker
                  selected={returnDate}
                  onChange={date => setReturnDate(date)}
                  showTimeSelect
                  dateFormat="Pp"
                  id="return-date"
                  className="form-control"
              />
            </div>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={() => setShowModal(false)}>
              Close
            </Button>
            <Button
                variant="primary"
                onClick={() => {
                  handleRentBook(); // Handle rent request on confirm
                  setShowModal(false); // Close modal after renting
                }}
            >
              Rent this Book
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
  );
};

export default BookItem;
