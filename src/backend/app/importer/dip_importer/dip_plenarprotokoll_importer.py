"""Class for DIP Bundestag Plenarprotokoll Importer."""

from typing import Iterator

from backend.app.core.config import Settings
from backend.app.crud.CRUDDIPBundestag.crud_plenarprotokoll import CRUD_DIP_PLENARPROTOKOLL
from backend.app.facades.deutscher_bundestag.model import Plenarprotokoll
from backend.app.facades.deutscher_bundestag.parameter_model import PlenarprotokollParameter
from backend.app.facades.util import ProxyList
from backend.app.importer.dip_importer.base import DIPImporter

# import from all models to ensure they are registered
from backend.app.models.deutscher_bundestag.models import (
    DIPFundstelle,
    DIPPlenarprotokoll,
    DIPVorgangsbezug,
)


class DIPBundestagPlenarprotokollImporter(
    DIPImporter[Plenarprotokoll, PlenarprotokollParameter, DIPPlenarprotokoll]
):
    """Class for DIP Bundestag Plenarprotokoll Importer."""

    def __init__(self):
        """
        Initialize DIPImporter.
        """
        super().__init__(CRUD_DIP_PLENARPROTOKOLL)

    def transform_model(self, data: Plenarprotokoll) -> DIPPlenarprotokoll:
        """Transform data."""

        dip_fundstelle = DIPFundstelle(**data.fundstelle.model_dump(exclude={"fk_id"}))

        dip_vorgangsbezug = (
            [
                DIPVorgangsbezug(
                    **vorgangsbezug.model_dump(exclude={'id'}), vorgang_id=vorgangsbezug.id
                )
                for vorgangsbezug in data.vorgangsbezug
            ]
            if data.vorgangsbezug
            else []
        )

        return DIPPlenarprotokoll(
            **data.model_dump(exclude={'fundstelle', 'vorgangsbezug'}),
            fundstelle=dip_fundstelle,
            vorgangsbezug=dip_vorgangsbezug,
        )

    def fetch_data(
        self,
        params: PlenarprotokollParameter | None = None,
        response_limit=1000,
        proxy_list: ProxyList | None = None,
    ) -> Iterator[Plenarprotokoll]:
        """Fetch data."""

        return self.dip_bundestag_facade.get_plenarprotokolle(
            params=params,
            response_limit=response_limit,
            proxy_list=proxy_list,
        )


def import_dip_bundestag():
    importer = DIPBundestagPlenarprotokollImporter()

    params = PlenarprotokollParameter(dokumentnummer=['20/8626', '20/9345'])

    importer.import_data(
        params=params,
        response_limit=1,
    )


if __name__ == '__main__':
    import_dip_bundestag()