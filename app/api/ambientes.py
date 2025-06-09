
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import ambientes as crud_ambientes

from app.schemas.ambientes import AmbienteCreate, AmbienteOut
from core.database import get_db
from core.dependencies import get_current_user

router = APIRouter()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_ambiente_formacion(
    ambiente: AmbienteCreate,
    db: Session = Depends(get_db),
    current_user: AmbienteOut = Depends(get_current_user)
):
    
    if current_user.id_rol == 2:
        if current_user.id_rol == 1 or current_user.id_rol ==2:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")
        
    
    if current_user.id_rol == 3:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")

    try:
        crud_ambientes.create_ambiente(db, ambiente)
        return {"message": "Ambiente creado correctamente"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))