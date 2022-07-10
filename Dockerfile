FROM python:latest
COPY entrypoint.sh .
COPY init_update.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT entrypoint.sh