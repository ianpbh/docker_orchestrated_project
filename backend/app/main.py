from fastapi import FastAPI
from app.routes import user, protected, topic, session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(protected.router)
app.include_router(topic.router)
app.include_router(session.router)