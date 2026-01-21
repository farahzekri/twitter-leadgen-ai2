from fastapi import FastAPI
from .database import Base, engine
from .routers import tweets,leads  
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Genie Ops – Twitter Lead Gen Agent")

# Autoriser CORS pour ton frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # ou ["*"] pour tester mais pas recommandé en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tweets.router)
app.include_router(leads.router)
