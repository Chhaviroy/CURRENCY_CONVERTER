from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from exchange_rates import exchange_rates

app = FastAPI(title="CurrencyConverterWebService")#fastapi object

templates = Jinja2Templates(directory="templates")

# ---------------- FRONTEND PAGES ----------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/converter", response_class=HTMLResponse)
def converter_page(request: Request):
    return templates.TemplateResponse("converter.html", {"request": request})

# ---------------- BACKEND LOGIC ----------------

def get_exchange_rate(from_currency, to_currency):
    try:
        # Convert from source currency to USD
        amount_in_usd = 1 / exchange_rates[from_currency]
        # Convert from USD to target currency
        rate = amount_in_usd * exchange_rates[to_currency]
        return rate
    except KeyError:
        return None



@app.get("/rate")
def exchange_rate(fromCurrency: str, toCurrency: str):
    rate = get_exchange_rate(fromCurrency, toCurrency)

    if rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")

    return {
        "from": fromCurrency,
        "to": toCurrency,
        "rate": rate
    }


@app.get("/convert")
def convert_currency(fromCurrency: str, toCurrency: str, amount: float):
    rate = get_exchange_rate(fromCurrency, toCurrency)

    if rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")

    converted_amount = amount * rate

    return {
        "from": fromCurrency,
        "to": toCurrency,
        "amount": amount,
        "convertedAmount": converted_amount
    }
