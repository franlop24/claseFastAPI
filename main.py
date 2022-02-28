from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola():
    return {"hola": "Mundo!"}

@app.get("/alumnos")
def alumnos():
    alumnos = [{
            "name": "Alumno1",
            "age": 19
        },
        {
            "name": "Francisco",
            "age": 28        
        }]
    return alumnos