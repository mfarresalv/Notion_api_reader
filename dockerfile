FROM python:3.7
RUN pip install pandas
RUN pip install requests

COPY main.py .
COPY variables.py .
COPY run.sh .
RUN mkdir -p /outputs

CMD ["/bin/bash", "./run.sh"]