import React from "react";

const InputField = ({ label, type = "text", value, onChange, required = false }) => (
  <div>
    <label className="block text-sm font-medium mb-1">{label}</label>
    <input
      type={type}
      value={value}
      onChange={onChange}
      required={required}
      className="w-full p-2 border rounded"
    />
  </div>
);

export default InputField;