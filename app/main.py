from fastapi import FastAPI

from blog.database import engine
from blog.routers import authentication, blogs, users
from blog import models


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(authentication.router)
