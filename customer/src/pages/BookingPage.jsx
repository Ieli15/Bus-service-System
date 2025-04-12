import React, { useState } from "react";
import { useParams } from "react-router-dom";
import toast from "react-hot-toast";

const BookingPage = () => {
  const { scheduleId } = useParams();
  const [name, setName] = useState("");
  const [seats, setSeats] = useState("");
  const [loading, setLoading] = useState(false);

  const handleBooking = (e) => {
    e.preventDefault();
    if (!name || !seats) {
      toast.error("Please fill in all fields");
      return;
    }
    setLoading(true);
    setTimeout(() => {
      toast.success("Booking successful!");
      setLoading(false);
      setName("");
      setSeats("");
    }, 1500);
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 border rounded-xl shadow-md">
      <h2 className="text-xl font-semibold mb-4">Book a Seat (ID: {scheduleId})</h2>
      <form onSubmit={handleBooking} className="space-y-4">
        <div>
          <label>Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div>
          <label>Number of Seats</label>
          <input
            type="number"
            min="1"
            value={seats}
            onChange={(e) => setSeats(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
        >
          {loading ? "Booking..." : "Confirm Booking"}
        </button>
      </form>
    </div>
  );
};

export default BookingPage;
