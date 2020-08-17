FROM ubuntu:18.04

MAINTAINER Ahmed Barbouche <ahmed.barbouche1@gmail.com>

# Ignore APT warnings about not having a TTY
ENV DEBIAN_FRONTEND noninteractive
ENV DOCKER_DEV true

# install Dependecies
RUN \
apt-get update -qq && \
apt-get install -y \
build-essential \
apt-utils &&\
apt-get install -y \
aptdaemon \
ed git \
libcairo-dev \
libedit-dev \
libapparmor1 \
libpq-dev \
libedit2 \
libssl1.0.0 \
libcurl4-gnutls-dev \
libssl-dev \
curl \
sudo \
wget &&\
apt-get install -y \
libzbar-dev \
imagemagick \
zip \
unzip \
xvfb &&\
rm -rf /var/lib/apt/lists/*

# install Python libraries
RUN \
apt-get update -qq && \
apt-get install -y \
python3 python3-pip python3.6-venv python3-dev  libssl-dev &&\
pip3 --no-cache-dir install virtualenv --upgrade && \
#easy_install distribute && \
rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install binutils libproj-dev gdal-bin libgeoip1 postgis python-gdal -y &&\
    rm -rf /var/lib/apt/lists/*

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \
                                        libsndfile1 \
                                        ffmpeg 

#RUN gunicorn -b :5000 --access-logfile - --error-logfile - app:app

ENV SHELL /bin/bash

RUN useradd -m docker

RUN echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY docker-entrypoint.sh /

RUN chmod 777 /docker-entrypoint.sh

#USER docker

RUN mkdir -p /home/docker/app/

WORKDIR /home/docker/app

ENTRYPOINT ["/docker-entrypoint.sh"]


#RUN mkdir -p /home/docker/app/dependecies/
#RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb 
#RUN dpkg -i /chrome.deb || apt-get install -yf 
#RUN mkdir -p  ~/usr/lib/chromium-browser/
#RUN chmod +x -R  ~/usr/lib/chromium-browser/
#RUN curl https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip -o  ~/usr/lib/chromium-browser/chromedriver
#RUN unzip -o ~/usr/lib/chromium-browser/chromedriver

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
#RUN echo 'export PATH="/opt/conda/bin/:$PATH"' >> ~/.bashrc
ENV NVIDIA_REQUIRE_CUDA "cuda>=8.0"