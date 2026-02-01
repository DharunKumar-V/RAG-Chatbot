import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import API from "../api";

export default function Register() {
  const nav = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const register = async () => {
    try {
      await API.post("/auth/register", { email, password });
      nav("/login");
    } catch {
      alert("User already exists");
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-[#0f0f0f] text-white">
      <div className="bg-gray-900 p-10 rounded-2xl w-96 space-y-4">

        <h2 className="text-2xl font-bold text-center">Register</h2>

        <input
          placeholder="Email"
          className="w-full p-3 bg-gray-800 rounded"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full p-3 bg-gray-800 rounded"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={register}
          className="w-full bg-green-600 p-3 rounded"
        >
          Register
        </button>

        <Link to="/login" className="text-sm text-blue-400">
          Back to login
        </Link>
      </div>
    </div>
  );
}



