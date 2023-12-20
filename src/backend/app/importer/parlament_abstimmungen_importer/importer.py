from backend.app.facades.bundestag_abstimmungen.parameter_model import (
    BundestagAbstimmungenParameter,
)
from backend.app.utils import get_data_folder
from backend.app.facades.bundestag_abstimmungen.facade import BundestagAbstimmungenFacade
from backend.app.core.config import settings
from datetime import date


class BundestagAbstimmungenImporter:
    def __init__(self):
        self.facade = BundestagAbstimmungenFacade.get_instance(settings)
        self.data_folder = get_data_folder()

    def get_abstimmungen(
        self, params: BundestagAbstimmungenParameter | None = None, response_limit: int = 1000
    ):
        for abstimmung in self.facade.get_bundestag_abstimmungen(
            params=params, response_limit=1000
        ):
            yield abstimmung


def main():
    importer = BundestagAbstimmungenImporter()

    params = BundestagAbstimmungenParameter(
        date_start=date(2021, 1, 1), date_end=date(2023, 12, 31)
    )

    for abstimmung in importer.get_abstimmungen(params=params):
        print(abstimmung)


if __name__ == '__main__':
    main()