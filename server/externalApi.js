import axios from "axios";

const BASE_URL = "http://localhost:4000";

const api = axios.create({
  baseURL: BASE_URL,
});

export const getFruits = async () => {
  try {
    const response = await api.get("/v1/fruits");
    return response.data;
  } catch (error) {
    console.error("Error fetching fruits:", error);
    throw error;
  }
};

export const getAnimals = async () => {
  try {
    const response = await api.get("/v1/animals");
    return response.data;
  } catch (error) {
    console.error("Error fetching animals:", error);
    throw error;
  }
};
