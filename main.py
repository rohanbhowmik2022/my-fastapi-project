from fastapi import FastAPI

app = FastAPI()

@app.get('/profile/{userid}/comments') #Query parameters along with Path parameters
def profile(userid:int,commentid:int):
    return {f'Profile page for user with userid {userid} and commentid {commentid}'} 

@app.get('/products')
def products(id,price): #Query Paramaters
    return {f'Product with an id {id} and price: {price}'}

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

