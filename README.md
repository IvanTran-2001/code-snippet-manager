# Code Snippet Manager

A modern, full-stack web application for storing, organizing, and sharing code snippets. Built with **Python FastAPI** backend and **React** frontend.

## 🚀 Features

- **User Authentication** - Secure registration and login with JWT tokens
- **Snippet Management** - Create, read, update, and delete code snippets
- **Public Sharing** - Make snippets public for the community to view
- **Tagging System** - Organize snippets with custom tags
- **Language Support** - Multiple programming languages (Python, JavaScript, C++, Java, SQL, HTML, CSS)
- **Syntax Highlighting** - Beautiful code display with syntax highlighting
- **View Tracking** - Track how many times public snippets are viewed

## 📋 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Robust relational database
- **SQLAlchemy** - ORM for database operations
- **JWT** - Secure token-based authentication
- **Pydantic** - Data validation

### Frontend
- **React** - UI library
- **Vite** - Build tool and dev server
- **Zustand** - Lightweight state management
- **Axios** - HTTP client
- **React Router** - Client-side routing
- **Highlight.js** - Syntax highlighting

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL 12+

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env and add your PostgreSQL connection string
   ```

5. **Create database tables:**
   ```bash
   python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

6. **Run backend server:**
   ```bash
   python main.py
   ```
   Server runs at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run development server:**
   ```bash
   npm run dev
   ```
   App runs at `http://localhost:5173`

## 📡 API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get token
- `GET /api/auth/me` - Get current user
- `POST /api/snippets` - Create snippet
- `GET /api/snippets` - Get user's snippets
- `GET /api/snippets/public` - Get all public snippets
- `GET /api/snippets/{id}` - Get specific snippet
- `PUT /api/snippets/{id}` - Update snippet
- `DELETE /api/snippets/{id}` - Delete snippet
- `GET /api/tags` - Get all tags

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

## 🐳 Docker Deployment

### Build Docker image:
```bash
docker build -t snippet-manager-backend ./backend
```

### Run container:
```bash
docker run -p 8000:8000 --env-file .env snippet-manager-backend
```

## 📦 Project Structure

```
code-snippet-manager/
├── backend/
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database setup
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── auth.py             # Authentication logic
│   ├── main.py             # FastAPI app
│   └── routers/
│       ├── auth.py         # Auth endpoints
│       ├── snippets.py     # Snippet endpoints
│       └── tags.py         # Tags endpoints
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API client
│   │   ├── store/          # State management
│   │   ├── App.jsx         # Root component
│   │   └── main.jsx        # Entry point
│   └── package.json        # Dependencies
└── README.md
```

## 🚀 Deployment

### Backend (Heroku/Railway)
1. Set environment variables
2. Use `Procfile` with gunicorn
3. Deploy PostgreSQL database

### Frontend (Vercel/Netlify)
1. Build: `npm run build`
2. Deploy the `dist` folder

## 📝 Future Enhancements

- [ ] Code execution/testing
- [ ] Snippet forking and versioning
- [ ] Search and filtering improvements
- [ ] Dark mode
- [ ] Snippet templates
- [ ] Team collaboration features
- [ ] API key authentication for developers

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📄 License

MIT License - feel free to use this project as a reference or starting point!

## 👤 Author

Ivan Tran - [Portfolio](https://ivantran-2001.github.io)

---

Made with ❤️
