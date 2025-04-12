import React, { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import Loader from "../components/Loader";
import ScheduleCard from "../components/ScheduleCard";

const DashboardPage = () => {
  const { user } = useAuth();
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBookings = async () => {
      try {
        // Mock fetch - replace with real API call
        const mockData = [
          { id: 1, bus: "Express 101", date: "2025-04-12", time: "10:00 AM" },
          { id: 2, bus: "InterCity 45", date: "2025-04-15", time: "2:00 PM" },
        ];
        setBookings(mockData);
      } catch (err) {
        console.error("Failed to fetch bookings");
      } finally {
        setLoading(false);
      }
    };

    fetchBookings();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Welcome, {user?.name}</h2>
      <h3 className="text-lg font-semibold mb-2">Your Bookings:</h3>
      {loading ? (
        <Loader />
      ) : bookings.length ? (
        <div className="space-y-4">
          {bookings.map((booking) => (
            <ScheduleCard key={booking.id} data={booking} showActions={false} />
          ))}
        </div>
      ) : (
        <p>You have no bookings yet.</p>
      )}
    </div>
  );
};

export default DashboardPage;
