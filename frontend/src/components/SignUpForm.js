import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import libraryImage from '../assets/signup.webp';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const SignUpForm = ({ onSubmit, error }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');

  const navigate = useNavigate(); // Initialize navigate

  const handleSubmit = (e) => {
    e.preventDefault();

    // Assuming onSubmit returns a promise or handles redirection itself
    onSubmit(username, password, email, first_name, last_name)
        .then(() => {
          // If signup is successful, redirect to the homepage
          navigate('/'); // Redirect to the homepage
        })
        .catch((error) => {
          // Handle any error (this could show up if the signup fails)
          console.error('Signup error:', error);
        });
  };

  return (
      <div className="container mt-5">
        <div className="row align-items-center">
          {/* Signup Form Section */}
          <div className="col-md-6">
            <h2 className="text-center mb-4">Sign Up</h2>
            <p className="text-muted text-center">
              Welcome to our online library! Explore our vast catalog of books and rent your favorites.
              Upgrade to our <strong>premium subscription</strong> to access more books and enjoy faster approval.
              <a href="http://localhost:5000/" className="text-primary fw-bold"> Buy Premium</a>
            </p>
            <form onSubmit={handleSubmit} className="p-4 border rounded shadow">
              <div className="mb-3">
                <label htmlFor="username" className="form-label">Username</label>
                <input
                    type="text"
                    id="username"
                    className="form-control"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="password" className="form-label">Password</label>
                <input
                    type="password"
                    id="password"
                    className="form-control"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="email" className="form-label">Email</label>
                <input
                    type="email"
                    id="email"
                    className="form-control"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="firs_name" className="form-label">First Name</label>
                <input
                    type="text"
                    id="text"
                    className="form-control"
                    value={first_name}
                    onChange={(e) => setFirstName(e.target.value)}
                    required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="last_name" className="form-label">Last Name</label>
                <input
                    type="text"
                    id="text"
                    className="form-control"
                    value={last_name}
                    onChange={(e) => setLastName(e.target.value)}
                    required
                />
              </div>
              <button type="submit" className="btn btn-primary w-100">Sign Up</button>
            </form>
            {error && <p className="mt-3 text-danger text-center">{error}</p>}
            <p className="text-center mt-3">
              Already have an account?{' '}
              <a href="http://localhost:3000/login" className="text-primary fw-bold">Log In</a>
            </p>
          </div>

          {/* Image Section */}
          <div className="col-md-6 d-flex justify-content-center">
            <img
                src={libraryImage}
                alt="Online Library Illustration"
                className="img-fluid rounded shadow"
                style={{ maxHeight: '400px' }}
            />
          </div>
        </div>
      </div>
  );
};

export default SignUpForm;
