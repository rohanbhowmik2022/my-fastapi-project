from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Hello World"

@app.get('/property/{id}') #Path Parameters
def property(id): #Parameters passed on to the function
    return {f"This is a property page {id}"} #Returned as a JSON response

@app.get('/movies')
def movies():
    return {'movie list':{'movie 1', 'movie 2', 'movie 3'}}

