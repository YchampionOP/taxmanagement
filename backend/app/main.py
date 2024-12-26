# backend/app/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import Settings
from app.api.endpoints import auth, expenses, tax_alerts, forecasting

app = FastAPI(title="Tax Management System")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(expenses.router, prefix="/api/expenses", tags=["expenses"])
app.include_router(tax_alerts.router, prefix="/api/tax-alerts", tags=["tax-alerts"])
app.include_router(forecasting.router, prefix="/api/forecasting", tags=["forecasting"])