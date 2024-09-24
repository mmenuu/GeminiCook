from fastapi import FastAPI
from app.routers import menu_router

app = FastAPI()

# Include the menu router
app.include_router(menu_router.router)

# You can also add other routes and configuration here
