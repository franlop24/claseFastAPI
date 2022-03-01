# Imports del Lenguaje Python
from typing import Optional

# Import de Pydantic
from pydantic import BaseModel, EmailStr, Field, HttpUrl

# Imports de fastAPI
from fastapi import Body, FastAPI, Path, Query

app = FastAPI()

# Modelos 
class Alumno(BaseModel):
    nombre: str = Field(
                        ...,
                        min_length=2,
                        max_length=30                
                    )
    apellidos: str = Field(
                            ...,
                            min_length=10,
                            max_length=50                    
                        )
    age: int = Field(
                        ...,
                        gt=10,
                        lt=100
                    )
    email: Optional[EmailStr] = None
    web_url: Optional[HttpUrl] = None


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

# PATH PARAMETERS son Obligatorios Required
@app.get("/alumnos/{id_alumno}")
def alumno_por_id(
                    id_alumno: int = Path(
                        ...,
                        gt=0,
                        title="ID del alumno",
                        description="Busca algun alumno por ID"
                    )
                ):
    return {id_alumno: "Este alumno sí existe"}

# QUERY PARAMETERS con Opcionales
@app.get("/alumno/query")
def query_alumnos(
                    grupo: Optional[str] = Query(
                        None,
                        min_length=1,
                        max_length=1,
                        title="Grupo",
                        description="Regresa los alumnos de un grupo"
                    ), 
                    cuatri: Optional[int] = Query(
                        None,
                        ge=1,
                        lt=12,
                        title="Cuatrimestre",
                        description="Cuatrimestre del grupo"
                    )
                ):
    return {
                "Grupo": grupo,
                "Cautri": cuatri
            }

@app.post("/alumno/new")
def add_alumno(alumno: Alumno = Body(...)):
    return alumno