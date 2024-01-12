import json
import pathlib

import pandas as pd
from loguru import logger


class ETL(object):
    name = "movies"

    @property
    def path_data(self) -> pathlib.Path:
        """
        So that we can access the data folder
        """
        path = pathlib.Path(__file__).parent
        for i in range(20):
            if (path / "data/").exists():
                return path / f"data/raw/scrapes/{self.name}"
            path = path.parent
        raise FileNotFoundError()

    def run(self):

        # Find all raw saved files for this task
        files = [f for f in self.path_data.glob("**/*") if f.is_file()]
        for file in files:

            # Transform raw data to dataframe
            self.transform(file)

            # TODO load into SQL database? Not yet implemented

    def transform(self, file: pathlib.Path) -> pd.DataFrame:

        # Open file
        with open(file.resolve(), "r") as f:
            data = json.load(f)

        # Convert to dataframe
        df = pd.DataFrame(data)

        # Change best_picture from True/NaN to True/False
        df["best_picture"] = df["best_picture"].fillna(False)

        logger.info(f"\n{df}")
        return df


def main():
    etl = ETL()
    etl.run()


if __name__ == "__main__":
    main()
