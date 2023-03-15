from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections

app = FastAPI(
    title="Fast API CMS",
    description="CMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "AT",
        "email": "AT@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
