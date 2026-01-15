import axios from 'axios';

// Auto-detect the backend URL based on current hostname
const host = window.location.hostname;
const API_BASE_URL = `http://${host}:8000/api`;

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth endpoints
export const authAPI = {
  register: (username, email, password) =>
    api.post('/auth/register', { username, email, password }),
  login: (username, password) =>
    api.post('/auth/login', { username, password }),
  getMe: () => api.get('/auth/me'),
};

// Snippets endpoints
export const snippetsAPI = {
  create: (snippet) => api.post('/snippets', snippet),
  list: () => api.get('/snippets'),
  getPublic: () => api.get('/snippets/public'),
  get: (id) => api.get(`/snippets/${id}`),
  update: (id, snippet) => api.put(`/snippets/${id}`, snippet),
  delete: (id) => api.delete(`/snippets/${id}`),
};

// Tags endpoints
export const tagsAPI = {
  list: () => api.get('/tags'),
};

export default api;
