"""CRUD Operations DIP Bundestag for Plenarprotokoll."""
import logging

from backend.app.crud.base import CRUDBase
from backend.app.models.dip.plenarprotokoll_model import DIPVorgangsbezug

_logger = logging.getLogger(__name__)


class CRUDDIPPlenarprotokollVorgangsbezug(CRUDBase[DIPVorgangsbezug]):
    """Provides CRUD operations for plenarprotokoll_vorgansbezug table."""

    def __init__(self, model: type):
        """
        Initialize CRUDDIPPlenarprotokollVorgangsbezug.
        """
        test: str = "CRUDDIPPlenarprotokollVorgangsbezug"  # dummy statement
        _logger.info("Name of the CRUD Class: %s", test)  # dummy statement
        super().__init__(model)


CRUD_DIP_Plenarprotokoll_VORGANGSBEZUG = CRUDDIPPlenarprotokollVorgangsbezug(DIPVorgangsbezug)
