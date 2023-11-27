"""Contains endpoints for importing PLENARPROTOKOLLE from DIP Bundestag API with DIP Bundestag facade."""
import logging

import fastapi

import backend.app.schemas.schema_example as schema_example  # pylint: disable=consider-using-from-import
from backend.app.crud.crud_example import CRUD_EXAMPLE
from backend.app.importer.dip_plenarprotokoll_importer import (
    DIPBundestagPlenarprotokollImporter,
)

_logger = logging.getLogger(__name__)

router = fastapi.APIRouter()


@router.post(
    "/plenarprotkolle",
    tags=["plenarprotokoll"],
)
def import_plenarprotkolle():
    DIPBundestagPlenarprotokollImporter().import_plenarprotokoll_vrogangsbezuege()