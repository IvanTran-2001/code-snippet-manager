from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import auth, snippets, tags

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Code Snippet Manager API",
    description="A modern API for managing and sharing code snippets",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(snippets.router, prefix="/api/snippets", tags=["Snippets"])
app.include_router(tags.router, prefix="/api/tags", tags=["Tags"])


@app.get("/")
async def root():
    return {
        "message": "Code Snippet Manager API",
        "version": "1.0.0",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
