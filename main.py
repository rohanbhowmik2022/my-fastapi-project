from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Hello World"

@app.get('/property/{id}') #Path Parameters
def property(id:int): #Path Parameters passed on to the function
    return {f"This is a property page {id}"} #Returned as a JSON response

@app.get('/user/{username}')
def profile(username:str):
    return {f"This is a profile page for user {username}"}

@app.get('/user/admin')
def admin():
    return {'This is an admin panel'}

@app.get('/movies')
def movies():
    return {'movie list':{'movie 1', 'movie 2', 'movie 3'}}

