import json
import pathlib

import pandas as pd
from loguru import logger


class ETL(object):
    name = "movies"

    @property
    def path_data(self) -> pathlib.Path:
        path = pathlib.Path(__file__).parent
        for i in range(20):
            if (path / "data/").exists():
                return path / f"data/raw/scrapes/{self.name}"
            path = path.parent
        raise FileNotFoundError()

    def run(self):
        files = [f for f in self.path_data.glob("**/*") if f.is_file()]
        for file in files:
            self.transform(file)

            # TODO load into SQL database? Not yet implemented

    def transform(self, file: pathlib.Path) -> pd.DataFrame:
        with open(file.resolve(), "r") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        df["best_picture"] = df["best_picture"].fillna(False)
        logger.info(f"\n{df}")
        return df


def main():
    etl = ETL()
    etl.run()


if __name__ == "__main__":
    main()
