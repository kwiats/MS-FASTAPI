from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

description = """
Managements system for users, employers or students 🚀

## Users - (_not implemented_)

You will be able to:

* **Create users** (_not implemented_).
* **Find users** (_not implemented_).
* **Get users** (_not implemented_).
* **Edit users** (_not implemented_).

"""

app = FastAPI(
    title="Management System API",
    description=description,
    version="Alpha 0.0.1",
    contact={
        "name": "Github repository: ",
        "url": "https://github.com/kwiats/MS-FastAPI/",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
