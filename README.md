# ideal-octo-robot

## Getting Started

### Anaconda
1. Download and install [Anaconda for Windows](https://www.anaconda.com/download).
2. Within the anaconda prompt, create a new environment called `airflow` and activate it:
```
conda create -n airflow python=3.8 pip setuptools git
conda activate airflow
```

### The Code
1. Fork this repostory.
2. Clone your forked repository and `cd` into it.
3. Install the packages in the requirements folder:
```
pip install -r requirements.txt
```
4. Install `pre-commit`
```
pre-commit install
```
4. Check to see if the code works:
```
python .\src\scrapes\movies\scrape.py
python .\src\scrapes\movies\etl.py
```

### Airflow
This is done using the instructions found [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
1. Install [Docker Desktop For Windows](https://www.docker.com/products/docker-desktop/).
    - Probably need to enable Windows Subsystem for Linux.
2. Within the repository directory, build the Dockerfile:
```
docker-compose build
```
3. Build the airflow instance
```
docker compose up airflow-init
```
4. Start airflow
```
docker compose up
```
5. Wait for airflow to load at `localhost:/8080` in your browser.

### Notes
- `src` contains the source code.
- `dags` contains the airflow DAGs.
- `data` is where the raw data will be saved.
