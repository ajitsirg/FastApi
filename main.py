from fastapi import FastAPI


app= FastAPI()


@app.get('/')
def index():
    return { "hello" : {"ajit": "abhay"}}


@app.get('/about')
def about():
    return{"ansh":"ansh ka birthday aane wala h 14th april ko"}