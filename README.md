# ideal-octo-robot



install anaconda for windows

conda create -n airflow python=3.8 pip setuptools git
conda activate airflow

git clone repo

cd repo

pip install -r requirements




1. Fork this repository.
2. Clone the forked repository (through VSCode to add it to your workspace).
3. Install Docker Desktop For Windows https://www.docker.com/products/docker-desktop/
  - You may need to enable Windows Subsystem for Linux


4. cd into this repo

docker-compose build
docker compose up airflow-init
docker compose up

wait to load
localhost:/8080

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

Ctrl-C to quit


mamba create -n airflow python=3.8 pip setuptools git






Cron schedule https://crontab.guru/every-5-minutes
