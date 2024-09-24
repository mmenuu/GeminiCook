from fastapi import APIRouter, HTTPException
from app.models.menu_model import MenuRequest
from app.services.menu_service import generate_menu

router = APIRouter()

@router.post("/generate-menu/")
def generate_menu_api(request: MenuRequest):
    try:
        # Call the service function to generate the menu
        menu_item = generate_menu(request.optional_dish, request.ingredients, request.supplies)
        return menu_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
