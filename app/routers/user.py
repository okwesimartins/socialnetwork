from fastapi import Response,status,HTTPException, Depends,APIRouter
from typing import Optional,List
from random import randrange
# import password hashing library
from packages import utils
from sqlalchemy.orm import Session
from packages import models, schema
from packages.database import engine,  get_db


models.Base.metadata.create_all(bind=engine)



router = APIRouter(
      # since all our api link starts with /posts we can use a prefix instead
    prefix="/users",
    # lets add tags to group the posts api so that it can appear grouped in swagger ui
    tags=['Users']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserCreate)
def create_user(user: schema.Users, db: Session = Depends(get_db)):

    # hash password
    hashed_password= utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    #save the data in the database
    db.add(new_user)
    db.commit()
    #retrive the newly created data
    db.refresh(new_user)  
    return new_user
@router.get("/{id}", response_model=schema.UserCreate)
def getUser(id: int, db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id: {id} does not exist here")
    return user