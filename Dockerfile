FROM python:2.7-slim
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y git
RUN git clone https://github.com/chrismonsen/milbscraper.git
WORKDIR milbscraper
RUN pip install flask
RUN pip install selenium
CMD ["python", "web-api.py"]