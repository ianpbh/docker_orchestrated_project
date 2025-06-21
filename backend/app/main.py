from fastapi import FastAPI
from app.routes import user, protected, topic

app = FastAPI()

app.include_router(user.router)
app.include_router(protected.router)
app.include_router(topic.router)