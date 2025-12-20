# Currency Converter

A simple **Currency Converter** web application built using **FastAPI**.  
This project allows users to convert between different currencies easily.  

## 🌐 Live Demo
Check out the live project here: [https://sprintglobalpay.onrender.com](https://sprintglobalpay.onrender.com)

## 🛠 Technology Stack
- **Backend:** Python, FastAPI
- **Deployment:** Render
- **Dependencies:** See `requirements.txt`

## 🚀 Features
- Convert any currency to another.
- Fast and lightweight API.
- Easy to use interface (if you have a frontend).
- Deployed live on Render.

## 💻 Installation (for local development)
1. Clone the repository:
```bash
git clone https://github.com/Chhaviroy/currency_converter.git
```


## Navigate to the project folder:

cd currency_converter


# Create a virtual environment (optional but recommended):

python -m venv venv




# Activate the virtual environment:

- Windows: venv\Scripts\activate

- Mac/Linux: source venv/bin/activate



# Install dependencies:

pip install -r requirements.txt


# Run the app locally:

uvicorn main:app --reload


The API will be available at http://127.0.0.1:8000



# 🔧 Usage

- Make GET requests to endpoints for currency conversion.

- Example (replace with your actual endpoints if you have any):

- GET /convert?from=USD&to=INR&amount=10



# 📄 Contributing

Feel free to fork the project and make improvements. Pull requests are welcome!
