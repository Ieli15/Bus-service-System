import React, { useState, useEffect } from "react";

const mockBookings = [
  {
    id: 1,
    busNumber: "BUS101",
    route: "City A to City B",
    seat: 5,
    date: "2025-04-15",
  },
  {
    id: 2,
    busNumber: "BUS202",
    route: "City A to City B",
    seat: 12,
    date: "2025-04-20",
  },
];

const ProfilePage = () => {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    // Simulate fetching user bookings
    setTimeout(() => {
      setBookings(mockBookings);
    }, 500);
  }, []);

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-xl font-bold mb-4">My Bookings</h2>
      {bookings.length === 0 ? (
        <p>Loading...</p>
      ) : (
        bookings.map((booking) => (
          <div key={booking.id} className="border p-4 mb-4 rounded shadow">
            <p><strong>Bus Number:</strong> {booking.busNumber}</p>
            <p><strong>Route:</strong> {booking.route}</p>
            <p><strong>Seat:</strong> {booking.seat}</p>
            <p><strong>Date:</strong> {booking.date}</p>
          </div>
        ))
      )}
    </div>
  );
};

export default ProfilePage;
