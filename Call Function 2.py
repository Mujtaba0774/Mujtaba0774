from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()



@app.get("/posts")

def get_posts():
    return {"Hello I am MUJTABA"}


@app.get("/")

def root():
    return {"Hello"}

@app.posts("/createposts")
def create_posts(payload: dict = body(...)):
    print(payload)
    return{"new_post": f"title {payload['title']} content:{payload['content']}"}


 





