import React from "react";
import Button from "./Button";

const ScheduleCard = ({ schedule, onBook, onEdit, onDelete }) => {
  return (
    <div className="border rounded p-4 shadow-md mb-4">
      <h3 className="text-lg font-semibold">{schedule.route}</h3>
      <p>Date: {schedule.date}</p>
      <p>Time: {schedule.time}</p>
      <p>Seats Available: {schedule.seats}</p>
      <div className="mt-2 flex gap-2">
        {onBook && <Button onClick={() => onBook(schedule)}>Book</Button>}
        {onEdit && <Button onClick={() => onEdit(schedule)} variant="success">Edit</Button>}
        {onDelete && <Button onClick={() => onDelete(schedule)} variant="danger">Delete</Button>}
      </div>
    </div>
  );
};

export default ScheduleCard;