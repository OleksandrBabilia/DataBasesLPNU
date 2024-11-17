import React, { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe('pk_test_51QLYRgFovu7WKbeEPK2MR1ggwY9R7vv3F6iSQyHrx3iCFSO36TRQlphDbqpQmKhU8FCmsTmbnlAKV50KJC7hp0At00hA9cNfTP'); // Replace with your Stripe public key

const StripeCheckout = () => {
    const [loading, setLoading] = useState(false);

    const handleCheckout = async () => {
        setLoading(true);
        const jwtToken = localStorage.getItem('token');
        try {
            // Request a session from your backend to create the checkout session
            const response = await fetch('http://localhost:5000/create-checkout-session', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${jwtToken}`  // Pass JWT in Authorization header
                },
            });
            const sessionId = await response.json();

            const stripe = await stripePromise;

            // Redirect to Stripe Checkout
            const result = await stripe.redirectToCheckout({ sessionId: sessionId.id });

            if (result.error) {
                alert(result.error.message);
            }
        } catch (error) {
            console.error('Error during checkout:', error);
            alert('An error occurred while processing your checkout.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Stripe Checkout</h1>
            <button
                id="checkout-button"
                onClick={handleCheckout}
                disabled={loading}
            >
                {loading ? 'Loading...' : 'Checkout'}
            </button>
        </div>
    );
};

export default StripeCheckout;
