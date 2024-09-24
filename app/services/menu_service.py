import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
from app.models.menu_model import MenuRequest

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI API with the API key from .env
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in environment variables")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to generate the menu
def generate_menu(optional_dish: str = None, ingredients: list = None, supplies: list = None):
    # Set default values if inputs are missing
    if optional_dish is None or optional_dish.strip() == "":
        optional_dish = "เมนูอาหารทำง่าย"  # Classic dish in Thai
    if ingredients is None or len(ingredients) == 0:
        ingredients = ["วัตถุดิบหาง่ายตามบ้าน"]  # Generic ingredient placeholder
    if supplies is None or len(supplies) == 0:
        supplies = ["อุปกรณ์ครัวทั่วไป"]  # Generic supplies placeholder
    
    # Define the template in Thai
    template = """
    คุณเป็นเชฟมืออาชีพ ช่วยสร้างเมนูอาหารตามข้อมูลที่ให้ไว้:
    - ชื่อเมนู: {optional_dish}
    - วัตถุดิบ: {ingredients}
    - อุปกรณ์ที่ต้องใช้: {supplies}

    เขียนเป็นบล็อกในรูปแบบ JSON:
    {{
        "MenuItem": {{
            "Name": "{optional_dish}",
            "Description": "คำอธิบายของเมนูที่ใช้ {ingredients} และ {supplies}",
            "EstimatedTimeCook": "60 นาที"
        }},
        "Recipe": {{
            "Ingredients": [
                {{"name": "วัตถุดิบตัวอย่าง", "quantity": "จำนวน", "preparation": "การเตรียม"}}
            ],
            "Instructions": [
                {{"step": 1, "description": "คำอธิบายขั้นตอนการทำ"}}
            ]
        }}
    }}
    """
    
    # Format the prompt
    prompt = template.format(
        optional_dish=optional_dish, 
        ingredients=", ".join(ingredients), 
        supplies=", ".join(supplies)
    )
    
    # Generate content using the language model
    response = model.generate_content(prompt)
    
    try:
        # Clean the generated content
        generated_content = response.text.strip("```json\n")
        
        # Try parsing the cleaned content as JSON
        json_response = json.loads(generated_content)
        return json_response
    except json.JSONDecodeError:
        # Handle JSON errors gracefully
        return {
            "error": "ERROR : Please Try Again!",
            "raw_response": generated_content
        }
