FROM python:3.7

RUN pip install pandas
RUN pip install requests
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

COPY main.py .
COPY variables.py .
COPY run.sh .
COPY google_drive_key.json .
COPY gdrive.py .
RUN mkdir -p /outputs

CMD ["/bin/bash", "./run.sh"]