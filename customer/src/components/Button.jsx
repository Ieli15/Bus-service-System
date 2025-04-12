import React from "react";

const Button = ({ children, onClick, type = "button", disabled, className = "", variant = "primary" }) => {
  const base = "py-2 px-4 rounded text-white font-medium";
  const variants = {
    primary: "bg-blue-600 hover:bg-blue-700",
    danger: "bg-red-600 hover:bg-red-700",
    success: "bg-green-600 hover:bg-green-700",
  };
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`${base} ${variants[variant]} ${className}`}
    >
      {children}
    </button>
  );
};

export default Button;