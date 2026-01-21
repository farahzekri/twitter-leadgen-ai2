# app/routers/leads.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database
from fastapi.responses import JSONResponse
import random

router = APIRouter(prefix="/leads", tags=["Leads"])

# Dépendance pour obtenir la session DB
def get_db_dep():
    db = next(database.get_db())
    return db

# Endpoint pour générer des idées de tweets pour contacter les leads
@router.get("/generate_ideas/", response_model=list[models.GeneratedTweet])
def generate_tweet_ideas(db: Session = Depends(get_db_dep)):
    # Récupère les tweets pertinents de la base (Agent 1)
    tweets = db.query(models.TweetDB).order_by(models.TweetDB.relevance_score.desc()).limit(5).all()

    ideas = []
    for t in tweets:
        # Génération simple : hook + contenu
        idea = f"Hey @{t.author}, j'ai vu votre tweet : '{t.content[:50]}...' et je pense que ça pourrait vous intéresser !"
        ideas.append(models.GeneratedTweet(content=idea))

    return ideas

# Endpoint pour envoyer / enregistrer un message envoyé à un lead
@router.post("/contact_lead/", response_model=models.Lead)
def contact_lead(lead_id: int, message: str, db: Session = Depends(get_db_dep)):
    lead = db.query(models.LeadDB).filter(models.LeadDB.id == lead_id).first()
    if not lead:
        return JSONResponse(status_code=404, content={"error": "Lead introuvable"})

    lead.message_sent = message
    db.commit()
    db.refresh(lead)
    return lead

@router.get("/contacted_leads/", response_model=list[models.Lead])
def get_contacted_leads(db: Session = Depends(get_db_dep)):
    # Récupérer tous les leads qui ont un message envoyé
    leads = db.query(models.LeadDB).filter(models.LeadDB.message_sent != None).all()
    
    # Si tu veux ajouter des champs mock pour CTR et conversion
    for lead in leads:
        if not hasattr(lead, "clicked"):
            lead.clicked = bool(random.getrandbits(1))  # True ou False aléatoire
        if not hasattr(lead, "converted"):
            lead.converted = bool(random.getrandbits(1))
    
    return leads