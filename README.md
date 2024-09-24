# GeminiCook

**GeminiCook** is a backend repository that harnesses the power of generative AI, specifically utilizing **Gemini Pro** and **LangChain**, to create innovative and tailored recipes for culinary blogging. Built on **FastAPI**, this project aims to streamline the recipe generation process, enabling bloggers and food enthusiasts to produce unique content based on user inputs like ingredients, dietary preferences, and cooking styles.

## Features

- **Generative AI Integration:** Leverages Gemini Pro for advanced AI-driven recipe creation.
- **LangChain Support:** Utilizes LangChain to manage and integrate various components for seamless workflow and data handling.
- **FastAPI Framework:** Implements FastAPI for high-performance API development, ensuring quick responses and efficient handling of requests.
- **Customizable Inputs:** Users can input ingredients and preferences to generate personalized recipes.
- **Structured Output:** Recipes are generated in a structured format, ideal for easy integration into blogging platforms.

## Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/yourusername/GeminiCook.git
Replace yourusername with your GitHub username.

Navigate to the Project Directory

Change your directory to the cloned repository:

bash
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
cd GeminiCook
Install Dependencies

Install the required packages using pip:

bash
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
pip install -r requirements.txt
This will install Gemini Pro, LangChain, FastAPI, and any other dependencies listed in requirements.txt.

Configure Environment Variables

Create a .env file in the project root directory to store your environment variables. Here’s an example format:

plaintext
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
GEMINI_API_KEY=your_api_key
LANGCHAIN_SETTINGS=your_langchain_settings
Make sure to replace your_api_key and your_langchain_settings with the actual values.

Running the Application
Start the FastAPI Server

You can run the FastAPI application using Uvicorn. Execute the following command:

bash
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
uvicorn main:app --reload
Here, main refers to your main application file, and app is the FastAPI instance.

Access the API Documentation

Once the server is running, you can access the API documentation by visiting:

arduino
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
http://127.0.0.1:8000/docs
This interactive documentation allows you to test the endpoints directly from your browser.

Generating Recipes
To generate a recipe, send a POST request to the /generate-recipe endpoint with the following JSON structure:

json
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
{
    "optional_dish": "duck confit",
    "ingredients": ["duck", "thyme", "garlic"],
    "supplies": ["pan", "oven"]
}
Example Request Using curl
You can use the following curl command to test the recipe generation:

bash
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
curl -X POST "http://127.0.0.1:8000/generate-recipe" \\
-H "Content-Type: application/json" \\
-d '{ "optional_dish": "duck confit", "ingredients": ["duck", "thyme", "garlic"], "supplies": ["pan", "oven"] }'
Response
Upon successfully processing the request, you will receive a JSON response containing the generated recipe. The response format will look something like this:

json
แสดงรายละเอียดเสมอ

คัดลอกโค้ด
{
    "recipe_name": "Duck Confit",
    "instructions": [
        "Preheat the oven to 300°F (150°C).",
        "Season the duck with thyme and garlic.",
        "Place the duck in a pan and cook slowly in the oven for several hours."
    ],
    "cooking_time": "2 hours",
    "servings": 4
}
Note
Ensure that the server is running before sending the request. You can adjust the optional_dish, ingredients, and supplies fields to customize the recipe generation as needed.

Contributing
If you wish to contribute to this project, feel free to open issues or submit pull requests. We welcome improvements and new features!

License
This project is licensed under the MIT License - see the LICENSE file for details.
