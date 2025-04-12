import React, { useState } from "react";

const AdminPanel = () => {
  const [buses, setBuses] = useState([]);
  const [form, setForm] = useState({
    busNumber: "",
    route: "",
    departure: "",
    arrival: "",
    seatsAvailable: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleAddBus = () => {
    const newBus = { ...form, id: Date.now() };
    setBuses([...buses, newBus]);
    setForm({ busNumber: "", route: "", departure: "", arrival: "", seatsAvailable: "" });
  };

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Admin Panel</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <input
          type="text"
          name="busNumber"
          value={form.busNumber}
          onChange={handleChange}
          placeholder="Bus Number"
          className="p-2 border rounded"
        />
        <input
          type="text"
          name="route"
          value={form.route}
          onChange={handleChange}
          placeholder="Route"
          className="p-2 border rounded"
        />
        <input
          type="text"
          name="departure"
          value={form.departure}
          onChange={handleChange}
          placeholder="Departure Time"
          className="p-2 border rounded"
        />
        <input
          type="text"
          name="arrival"
          value={form.arrival}
          onChange={handleChange}
          placeholder="Arrival Time"
          className="p-2 border rounded"
        />
        <input
          type="number"
          name="seatsAvailable"
          value={form.seatsAvailable}
          onChange={handleChange}
          placeholder="Seats Available"
          className="p-2 border rounded"
        />
      </div>
      <button onClick={handleAddBus} className="bg-blue-600 text-white px-4 py-2 rounded mb-6">
        Add Bus Schedule
      </button>
      <div>
        <h3 className="text-xl font-semibold mb-2">Existing Schedules</h3>
        {buses.length === 0 ? (
          <p>No schedules added yet.</p>
        ) : (
          buses.map((bus) => (
            <div key={bus.id} className="border p-4 mb-4 rounded shadow">
              <p><strong>Bus Number:</strong> {bus.busNumber}</p>
              <p><strong>Route:</strong> {bus.route}</p>
              <p><strong>Departure:</strong> {bus.departure}</p>
              <p><strong>Arrival:</strong> {bus.arrival}</p>
              <p><strong>Seats:</strong> {bus.seatsAvailable}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default AdminPanel;
