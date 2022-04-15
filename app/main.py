from fastapi import FastAPI,Response,status,HTTPException, Depends
from typing import Optional,List
# add cors
from fastapi.middleware.cors import CORSMiddleware
##import pydantic to be able 
##to define  or set the input params that are allowed
from packages import config
from random import randrange

# import password hashing library


from routers import post, user, auth, vote


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




   
    # rating: Optional[int] = None

# try:
#     conn=psycopg2.connect(host='localhost',database='myonlineshop',user='postgres', password='okwesijune30#',cursor_factory=RealDictCursor )
#     cursor = conn.cursor()
#     print("database connected successfully")
# except Exception as error:
#     print("connection to database failed")
#     print("error: ", error)
#want to start storing data in the my_post dictionary below


#the find_post function loops through the my_post
#dictionary and locates the post with the id that was passed into it


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts """)
#     posts = cursor.fetchall()
#     print(posts)
#     return {"message":posts}




