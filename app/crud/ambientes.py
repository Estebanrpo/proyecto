
from fastapi import logger
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import logging
from app.schemas.ambientes import AmbienteCreate

logger = logging.getLogger(__name__)


def create_ambiente(db: Session, ambiente: AmbienteCreate) -> Optional[bool]:
    try:
        ambiente_data = ambiente.model_dump()
        query = text("""
            INSERT INTO ambiente_formacion(
                nombre_ambiente, num_max_aprendices, municipio,
                ubicacion, cod_centro, estado
            ) VALUES (
                :nombre_ambiente, :num_max_aprendices, :municipio,
                :ubicacion, :cod_centro, :estado
            )
        """)
        db.execute(query, ambiente_data)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al crear ambiente: {e}")
        raise Exception(f"Error al crear ambiente: {e}")