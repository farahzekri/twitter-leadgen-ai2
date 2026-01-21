import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // backend FastAPI

// Récupérer les idées de tweet (Agent 2)
export const getTweetIdeas = async () => {
  try {
    const response = await axios.get(`${API_URL}/leads/generate_ideas/`);
    return response.data; // retourne un tableau [{content: "..."}]
  } catch (error) {
    console.error("Erreur en récupérant les idées:", error);
    return [];
  }
};

// Récupérer les leads contactés
export const getLeads = async () => {
  try {
    const response = await axios.get(`${API_URL}/leads/contacted_leads/`);
    return response.data; // retourne un tableau de leads
  } catch (error) {
    console.error("Erreur en récupérant les leads:", error);
    return [];
  }
};
