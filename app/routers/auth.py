from fastapi import Response,status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from packages.database import engine,  get_db
from packages import  schema, models,utils,oauth2
router= APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model= schema.Token)
def login(user_creadentials: schema.UserLogin,db: Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.email == user_creadentials.email).first()
    if not user:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalidcredentials")
    if not utils.verify(user_creadentials.password,user.password):
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalidcredentials")
    access_token = oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}
# run pip install python-jose[cryptography] to be able to use jwt token



