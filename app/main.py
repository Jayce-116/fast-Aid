from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, guides
from app.database import engine, Base

# Ensure all tables are created on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FaST Aid API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # More permissive for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(auth.router)
app.include_router(guides.router)


@app.get("/")
def read_root():
    return {"message": "FaST Aid backend is running!"}


