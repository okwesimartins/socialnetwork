from fastapi import Response,status,HTTPException, Depends, APIRouter
from typing import Optional,List
from random import randrange
# import password hashing library
from packages import utils
from sqlalchemy.orm import Session
from packages import models, schema, oauth2
from packages.database import engine,  get_db
# the import func will give us access to some special function like count
from sqlalchemy import func

models.Base.metadata.create_all(bind=engine)



router = APIRouter(
    # since all our api link starts with /posts we can use a prefix instead
    prefix="/posts",
    # lets add tags to group the posts api so that it can appear grouped in swagger ui
    tags=['Posts']
)



@router.post("/",status_code=status.HTTP_201_CREATED)
def create_posts(post: schema.Post, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    ##post is a variable that stores the pydantic data from the post class
    ##convert the post data to a dictionary
    # post_dict=post.dict()
    #add an id key to the dictionary and store random numbers
    # post_dict['id'] = randrange(0, 1000000)
    # my_post.append(post_dict)

    new_post = models.Post(owner_id=current_user.id, **post.dict())
    #save the data in the database
    db.add(new_post)
    db.commit()
    #retrive the newly created data
    db.refresh(new_post)      
    
                                                                          
   
    return new_post

@router.get("/{id}", response_model=schema.Postout) 
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))

    # post = cursor.fetchone() 
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    return post

@router.delete("/{id}") 
def delete_post(id: int, db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)
# update a post
@router.put("/{id}")
def update_post(id: int,updated_post:schema.Post,db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return {"status":"success"}
@router.get("/",response_model=List[schema.Postout])
def get_posts(db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user), Limit:int = 10, skip:int = 0, search: Optional[str] = ""):
    # posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    result = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    return  result