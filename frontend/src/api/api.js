import axios from "axios";

const api = axios.create({
  baseURL: "https://carbonledger-api-4nrx.onrender.com/api/",
});

export default api;