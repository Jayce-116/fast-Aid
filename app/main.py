from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth
from app.routes import guides
from app.routes import guides


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include the auth routes
app.include_router(auth.router)
# Include the guides routes
app.include_router(guides.router)


@app.get("/")
def read_root():
    return {"message": "FaST Aid backend is running!"}


