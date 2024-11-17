import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // To navigate to other pages after login
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap for styling

const LoginPage = () => {
    const [username, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const navigate = useNavigate(); // For redirecting after successful login

    // Handle form submission
    const handleLogin = async (event) => {
        event.preventDefault();

        // Clear previous errors
        setError(null);

        const credentials = {
            username,
            password,
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/api/v1/token/', { // Replace with your login API endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(credentials),
            });

            if (response.ok) {
                const data = await response.json();
                // Assuming the response contains a token (e.g., "access_token")
                localStorage.setItem('token', data.access); // Store token in localStorage or cookie
                navigate('/'); // Redirect to the homepage or any page after successful login
            } else {
                const errorData = await response.json();
                setError(errorData.message || 'Login failed. Please check your credentials.');
            }
        } catch (error) {
            setError('An error occurred. Please try again later.');
            console.error('Login error:', error);
        }
    };

    return (
        <div className="container d-flex justify-content-center align-items-center mt-5" style={{ height: '100vh' }}>
            <div className="row justify-content-center w-100">
                <div className="col-md-6 col-lg-4">
                    <div className="card shadow-lg p-4 rounded">
                        <h2 className="text-center mb-4">Login</h2>
                        <form onSubmit={handleLogin}>
                            <div className="mb-3">
                                <label htmlFor="email" className="form-label">Username</label>
                                <input
                                    id="email"
                                    className="form-control"
                                    value={username}
                                    onChange={(e) => setEmail(e.target.value)}
                                    required
                                    placeholder="Enter your username"
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
                                    placeholder="Enter your password"
                                />
                            </div>

                            {error && <div className="alert alert-danger">{error}</div>}

                            <button type="submit" className="btn btn-primary w-100">Login</button>
                        </form>
                        <p className="text-center mt-3">
                            Don't have an account?{' '}
                            <a href="/signup" className="text-primary">Sign Up</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;
