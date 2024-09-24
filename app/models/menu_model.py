from pydantic import BaseModel

# Pydantic model for the menu generation request
class MenuRequest(BaseModel):
    optional_dish: str
    ingredients: list
    supplies: list
