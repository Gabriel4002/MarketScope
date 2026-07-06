import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="MarketScope API",
    description="API responsável pela integração entre o MarketScope e Marketplaces.",
    version="0.2.0"
)

CLIENT_ID = os.getenv("MERCADOLIVRE_CLIENT_ID")
REDIRECT_URI = os.getenv("MERCADOLIVRE_REDIRECT_URI")


@app.get("/")
async def root():

    return {
        "application": "MarketScope",
        "status": "online",
        "version": "0.2.0"
    }


@app.get("/health")
async def health():

    return JSONResponse(
        content={
            "status": "healthy"
        }
    )


# =====================================================
# LOGIN MERCADO LIVRE
# =====================================================

@app.get("/auth/login")
async def mercadolivre_login():

    authorization_url = (
        "https://auth.mercadolivre.com.br/authorization"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
    )

    return RedirectResponse(url=authorization_url)


# =====================================================
# CALLBACK
# =====================================================

@app.get("/auth/callback")
async def mercadolivre_callback(
    code: str = None,
    state: str = None
):

    return {

        "message": "Callback recebido com sucesso.",

        "authorization_code": code,

        "state": state,

        "next_step": "Trocar authorization_code por access_token"

    }


# =====================================================
# WEBHOOK
# =====================================================

@app.post("/webhooks/mercadolivre")
async def mercadolivre_webhook(payload: dict):

    print(payload)

    return {

        "received": True

    }
