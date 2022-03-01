# Imports del Lenguaje Python
from typing import Optional

# Import de Pydantic

# Imports de fastAPI
from fastapi import FastAPI, Query

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

# PATH PARAMETERS
@app.get("/alumnos/{id_alumno}")
def alumno_por_id(id_alumno: int):
    return {id_alumno: "Este alumno sí existe"}

# QUERY PARAMETERS
@app.get("/alumno/query")
def query_alumnos(
                    grupo: Optional[str] = Query(
                        None,
                        min_length=1,
                        max_length=1
                    ), 
                    cuatri: Optional[int] = Query(
                        None,
                        ge=1,
                        lt=12
                    )
                ):
    return {
                "Grupo": grupo,
                "Cautri": cuatri
            }