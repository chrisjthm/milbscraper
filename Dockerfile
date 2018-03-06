FROM python:2.7-slim
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y git
RUN git clone https://github.com/chrismonsen/milbscraper.git
RUN cd milbscraper
RUN pip install -r requirements.txt
CMD ["python", "web-api.py"]