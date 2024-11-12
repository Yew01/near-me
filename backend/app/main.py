from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import json
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import routes.account
import routes.services


# Override JSONResponse to pretty-print by default
class PrettyJSONResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(content, indent=4).encode("utf-8")

app = FastAPI(default_response_class=PrettyJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.account.router)
app.include_router(routes.services.router)

@app.get("/")
def read_root():
    return {"message" : "Welcome to near-me, inspired by ZANA"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/maincategory")
# def get_maincategory(db: Session = Depends(get_db)):
#     maincategory = db.query(models.MainCategory).all()
#     return maincategory


# @app.get("/subcategory")
# def get_subcategory(db: Session = Depends(get_db)):
#     subcategory = db.query(models.SubCategory).all()
#     return subcategory

# @app.get("/freelancer")
# def get_freelancer(db: Session = Depends(get_db)):
#     freelancer = db.query(models.Freelancer).all()
#     return freelancer

# @app.get("/business")
# def get_business(db: Session = Depends(get_db)):
#     business = db.query(models.Business).all()
#     return business