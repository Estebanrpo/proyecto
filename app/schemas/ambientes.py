from pydantic import  BaseModel, Field
from typing import Optional

class AmbienteBase(BaseModel):
    nombre_ambiente: str = Field(min_length=3, max_length=80)
    num_max_aprendices: int
    municipio: str = Field(min_length=6, max_length=30)
    ubicacion: str = Field(min_length=6, max_length=80)
    cod_centro: int

class AmbienteCreate(AmbienteBase):
    estado: bool

class AmbienteUpdate(BaseModel):
    nombre_ambiente: Optional[str] = Field(default=None, min_length=3, max_length=80)
    municipio: Optional[str] = Field(default=None, min_length=6, max_length=30)
    ubicacion: Optional[str] = Field(default=None, min_length=6, max_length=80)
    # estado: Optional[bool] = None

class AmbienteOut(AmbienteBase):
    id_ambiente: int