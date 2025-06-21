from fastapi import FastAPI
from app.routes import user, protected, topic, session

app = FastAPI()

app.include_router(user.router)
app.include_router(protected.router)
app.include_router(topic.router)
app.include_router(session.router)