# Code Snippet Manager - Setup Guide

## Quick Start Guide

### Option 1: Local Development (Recommended for Development)

#### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your PostgreSQL connection string

# Run migrations and create tables
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"

# Start backend server
python main.py
```

Backend will run at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

#### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend will run at: `http://localhost:5173`

---

### Option 2: Docker Compose (Recommended for Production)

```bash
# Make sure you have Docker installed
docker --version

# Start all services
docker-compose up -d

# Stop services
docker-compose down
```

Services:
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- PostgreSQL: `localhost:5432`

---

## Environment Variables

### Backend (.env)

```
DATABASE_URL=postgresql://user:password@localhost:5432/snippet_manager
SECRET_KEY=your-super-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database Setup

### Using PostgreSQL Locally

```bash
# Install PostgreSQL (if not already installed)
# macOS: brew install postgresql
# Windows: Download from postgresql.org
# Linux: sudo apt-get install postgresql

# Create database
createdb snippet_manager

# Update .env with your connection string
# DATABASE_URL=postgresql://postgres:password@localhost:5432/snippet_manager
```

### Using Docker

```bash
docker run --name snippet-db \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=snippet_manager \
  -p 5432:5432 \
  -d postgres:15
```

---

## Running Tests

### Backend Tests

```bash
cd backend
pip install pytest httpx
pytest test_api.py -v
```

### Frontend Tests

```bash
cd frontend
npm test
```

---

## API Usage Examples

### Register

```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
  }'
```

### Login

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "password123"
  }'
```

### Create Snippet

```bash
curl -X POST http://localhost:8000/api/snippets \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Quick Sort",
    "code": "def quicksort(arr):\n  ...",
    "language": "python",
    "tags": ["algorithms", "sorting"]
  }'
```

---

## Deployment

### Deploy Backend (Heroku)

```bash
# Install Heroku CLI
# heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main
```

### Deploy Frontend (Vercel)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

---

## Troubleshooting

### PostgreSQL Connection Error

- Ensure PostgreSQL is running
- Check connection string in .env
- Verify database exists

### Frontend Can't Connect to Backend

- Ensure backend is running on port 8000
- Check CORS settings in backend (main.py)
- Update API_BASE_URL in frontend/src/services/api.js

### Port Already in Use

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :8000   # Windows
```

---

## Development Workflow

1. Backend changes don't require restart (uvicorn has reload enabled)
2. Frontend changes auto-reload (Vite dev server)
3. Database changes: Update models.py, then recreate tables

---

## Next Steps

- [ ] Add more programming languages
- [ ] Implement code execution
- [ ] Add team collaboration
- [ ] Set up CI/CD pipeline
- [ ] Add search functionality
- [ ] Implement dark mode

