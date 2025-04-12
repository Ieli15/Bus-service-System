import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const mockResults = [
  {
    id: 1,
    busNumber: "BUS101",
    route: "City A to City B",
    departure: "08:00 AM",
    arrival: "11:00 AM",
    seatsAvailable: 15,
  },
  {
    id: 2,
    busNumber: "BUS202",
    route: "City A to City B",
    departure: "01:00 PM",
    arrival: "04:00 PM",
    seatsAvailable: 10,
  },
];

const ResultsPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [buses, setBuses] = useState([]);

  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const source = params.get("source");
    const destination = params.get("destination");
    const date = params.get("date");

    // Simulate fetching data
    setTimeout(() => {
      setBuses(mockResults);
    }, 500);
  }, [location.search]);

  const handleBook = (scheduleId) => {
    navigate(`/book/${scheduleId}`);
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-xl font-semibold mb-4">Available Buses</h2>
      {buses.length === 0 ? (
        <p>Loading...</p>
      ) : (
        buses.map((bus) => (
          <div key={bus.id} className="border p-4 mb-4 rounded shadow">
            <p><strong>Bus Number:</strong> {bus.busNumber}</p>
            <p><strong>Route:</strong> {bus.route}</p>
            <p><strong>Departure:</strong> {bus.departure}</p>
            <p><strong>Arrival:</strong> {bus.arrival}</p>
            <p><strong>Seats Available:</strong> {bus.seatsAvailable}</p>
            <button
              onClick={() => handleBook(bus.id)}
              className="mt-2 bg-green-500 text-white p-2 rounded"
            >
              Book Now
            </button>
          </div>
        ))
      )}
    </div>
  );
};

export default ResultsPage;