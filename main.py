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

@app.get("/alumnos/{id_alumno}")
def alumno_por_id(id_alumno: int):
    return {id_alumno: "Este alumno sí existe"}

@app.get("/alumno/query")
def query_alumnos(grupo: str, cuatri: str):
    return {"grupo": grupo, "cuatrimestre": cuatri}