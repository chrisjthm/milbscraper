FROM python:2.7-slim
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y git
RUN apt-get install -y wget xvfb unzip
# install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 2.37
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
RUN chmod +x $CHROMEDRIVER_DIR/chromedriver*

ENV PATH $CHROMEDRIVER_DIR/chromedriver:$PATH

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
copy . /app
WORKDIR /app
RUN pip install flask
RUN pip install selenium
RUN pip install pyvirtualdisplay
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]