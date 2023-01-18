FROM python:3.7
RUN pip install pandas

COPY main.py
COPY variables.py
COPY run.sh

CMD run.sh
