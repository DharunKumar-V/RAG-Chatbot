import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import API from "../api";

export default function Login() {
  const nav = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      const res = await API.post("/auth/login", { email, password });
      localStorage.setItem("token", res.data.token);
      nav("/chat");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-[#0f0f0f] text-white">
      <div className="bg-gray-900 p-10 rounded-2xl w-96 space-y-4">

        <h2 className="text-2xl font-bold text-center">Login</h2>

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
          onClick={login}
          className="w-full bg-blue-600 p-3 rounded"
        >
          Login
        </button>

        <Link to="/register" className="text-sm text-blue-400">
          Create account
        </Link>
      </div>
    </div>
  );
}







