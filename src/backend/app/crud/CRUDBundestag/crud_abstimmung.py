"""CRUD Operations DIP Bundestag for Drucksache."""
import datetime
import logging

from pydantic import BaseModel

from backend.app.crud.base import CRUDBase
from backend.app.models.bundestag.abstimmung_model import BTAbstimmung


class CRUDBundestagAbstimmung(CRUDBase[BTAbstimmung]):
    """Provides CRUD operations for bt.abstimmung table."""

    def __init__(self, model: type):
        """
        Initialize CRUDDIPDrucksache.
        """
        super().__init__(model)


CRUD_BUNDESTAG_ABSTIMMUNG = CRUDBundestagAbstimmung(BTAbstimmung)