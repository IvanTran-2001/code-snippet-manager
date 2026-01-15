import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './store'
import { LoginPage, RegisterPage } from './pages/Auth'
import { Dashboard } from './pages/Dashboard'
import { CreateSnippet } from './pages/CreateSnippet'
import './App.css'

function App() {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated)
  const logout = useAuthStore((state) => state.logout)

  return (
    <Router>
      <div className="app">
        {isAuthenticated && (
          <nav className="navbar">
            <span>Code Snippet Manager</span>
            <div className="nav-links">
              <a href="/dashboard">Dashboard</a>
              <a href="/create">Create</a>
              <button onClick={logout} className="logout-btn">Logout</button>
            </div>
          </nav>
        )}
        <Routes>
          <Route
            path="/login"
            element={
              isAuthenticated ? <Navigate to="/dashboard" /> : <LoginPage />
            }
          />
          <Route
            path="/register"
            element={
              isAuthenticated ? <Navigate to="/dashboard" /> : <RegisterPage />
            }
          />
          <Route
            path="/dashboard"
            element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />}
          />
          <Route
            path="/create"
            element={
              isAuthenticated ? <CreateSnippet /> : <Navigate to="/login" />
            }
          />
          <Route
            path="/"
            element={
              isAuthenticated ? <Navigate to="/dashboard" /> : <Navigate to="/login" />
            }
          />
        </Routes>
      </div>
    </Router>
  )
}

export default App
