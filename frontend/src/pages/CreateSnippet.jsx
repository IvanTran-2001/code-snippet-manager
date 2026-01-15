import React, { useState } from 'react';
import { snippetsAPI } from '../services/api';
import { useSnippetStore } from '../store';
import './CreateSnippet.css';

export const CreateSnippet = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');
  const [tags, setTags] = useState('');
  const [isPublic, setIsPublic] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const addSnippet = useSnippetStore((state) => state.addSnippet);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const tagsArray = tags
        .split(',')
        .map((t) => t.trim())
        .filter((t) => t);

      const response = await snippetsAPI.create({
        title,
        description,
        code,
        language,
        is_public: isPublic,
        tags: tagsArray,
      });

      addSnippet(response.data);
      setTitle('');
      setDescription('');
      setCode('');
      setTags('');
      setError('');
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to create snippet');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="create-snippet">
      <h1>Create New Snippet</h1>
      {error && <div className="error">{error}</div>}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Title *</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Description</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows="3"
          />
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Language *</label>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
            >
              <option value="python">Python</option>
              <option value="javascript">JavaScript</option>
              <option value="cpp">C++</option>
              <option value="java">Java</option>
              <option value="sql">SQL</option>
              <option value="html">HTML</option>
              <option value="css">CSS</option>
            </select>
          </div>

          <div className="form-group">
            <label>Tags (comma separated)</label>
            <input
              type="text"
              value={tags}
              onChange={(e) => setTags(e.target.value)}
              placeholder="e.g. async, utils, database"
            />
          </div>
        </div>

        <div className="form-group">
          <label>Code *</label>
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            required
            rows="10"
            className="code-input"
          />
        </div>

        <div className="form-group checkbox">
          <input
            type="checkbox"
            id="public"
            checked={isPublic}
            onChange={(e) => setIsPublic(e.target.checked)}
          />
          <label htmlFor="public">Make this snippet public</label>
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Creating...' : 'Create Snippet'}
        </button>
      </form>
    </div>
  );
};
