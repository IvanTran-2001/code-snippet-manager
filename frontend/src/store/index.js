import { create } from 'zustand';

export const useAuthStore = create((set) => ({
  user: null,
  token: localStorage.getItem('access_token') || null,
  isAuthenticated: !!localStorage.getItem('access_token'),

  setUser: (user) => set({ user }),
  setToken: (token) => {
    localStorage.setItem('access_token', token);
    set({ token, isAuthenticated: true });
  },
  logout: () => {
    localStorage.removeItem('access_token');
    set({ user: null, token: null, isAuthenticated: false });
  },
}));

export const useSnippetStore = create((set) => ({
  snippets: [],
  publicSnippets: [],
  selectedSnippet: null,

  setSnippets: (snippets) => set({ snippets }),
  setPublicSnippets: (snippets) => set({ publicSnippets: snippets }),
  setSelectedSnippet: (snippet) => set({ selectedSnippet: snippet }),
  addSnippet: (snippet) =>
    set((state) => ({ snippets: [...state.snippets, snippet] })),
  updateSnippet: (id, updated) =>
    set((state) => ({
      snippets: state.snippets.map((s) => (s.id === id ? updated : s)),
    })),
  deleteSnippet: (id) =>
    set((state) => ({
      snippets: state.snippets.filter((s) => s.id !== id),
    })),
}));
