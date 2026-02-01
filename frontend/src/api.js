import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000",
});

/* ======================================
   Attach JWT automatically
====================================== */
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  /* ⭐ CRITICAL FIX FOR FILE UPLOADS
     If FormData → let browser set boundary */
  if (config.data instanceof FormData) {
    delete config.headers["Content-Type"];
  }

  return config;
});

/* ======================================
   Auto logout on 401
====================================== */
API.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem("token");
      window.location.href = "/login";
    }
    return Promise.reject(err);
  }
);

export default API;


