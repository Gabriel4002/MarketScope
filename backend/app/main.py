from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="MarketScope API",
    description="API responsável pela integração entre MarketScope e os Marketplaces.",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "application": "MarketScope",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    return JSONResponse(
        content={
            "status": "healthy"
        }
    )


# ---------------------------------------------------
# OAuth Mercado Livre
# ---------------------------------------------------

@app.get("/auth/callback")
async def mercadolivre_callback(code: str = None, state: str = None):

    return {
        "message": "Autenticação realizada com sucesso.",
        "authorization_code": code,
        "state": state
    }


# ---------------------------------------------------
# Webhook Mercado Livre
# ---------------------------------------------------

@app.post("/webhooks/mercadolivre")
async def mercadolivre_webhook(payload: dict):

    print(payload)

    return {
        "received": True
    }