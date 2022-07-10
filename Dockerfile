FROM python:latest
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
COPY init_update.py /init_update.py
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ENTRYPOINT ["/entrypoint.sh"]