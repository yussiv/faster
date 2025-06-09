FROM python:3.13-slim-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src tests log_conf.yaml ./

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload", "--log-config", "log_conf.yaml" ]