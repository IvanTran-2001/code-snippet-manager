import React, { useState, useEffect } from 'react';
import { snippetsAPI } from '../services/api';
import { useSnippetStore } from '../store';
import './Dashboard.css';

export const Dashboard = () => {
  const snippets = useSnippetStore((state) => state.snippets);
  const setSnippets = useSnippetStore((state) => state.setSnippets);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadSnippets();
  }, []);

  const loadSnippets = async () => {
    try {
      const response = await snippetsAPI.list();
      setSnippets(response.data);
    } catch (err) {
      console.error('Failed to load snippets:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="dashboard">
      <h1>My Snippets</h1>
      <div className="snippets-grid">
        {snippets.length === 0 ? (
          <p>No snippets yet. Create your first one!</p>
        ) : (
          snippets.map((snippet) => (
            <div key={snippet.id} className="snippet-card">
              <h3>{snippet.title}</h3>
              <p className="language">{snippet.language}</p>
              <p className="description">{snippet.description}</p>
              <div className="tags">
                {snippet.tags?.map((tag) => (
                  <span key={tag.id} className="tag">
                    {tag.name}
                  </span>
                ))}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
