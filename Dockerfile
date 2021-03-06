# This Dockerfile

# Base image
FROM centos

# Maintainer
MAINTAINER songjun songjun0810@163.com

# Commands
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
#RUN dpkg-reconfigure -f noninteractive tzdata

# For complie
#RUN yum install -y git
#RUN yum install -y make
#RUN yum install -y gcc-c++
#RUN yum install -y python36-setuptools
#RUN yum install -y python36-devel

# Install 
RUN yum install -y net-tools.x86_64
RUN yum install -y gdb
RUN yum install -y epel-release
RUN yum install -y python36
RUN yum install -y python36-pip
RUN pip3 install mongo
RUN pip3 install six

# Add folders and files
ADD lib /app/lib
ADD scripts /app/scripts
ADD libskynet.so /app/libskynet.so
ADD skynet /app/skynet
ADD game.conf /app/game.conf
RUN mkdir /app/log

# Set env
ENV LD_LIBRARY_PATH /app:/app/lib:$LD_LIBRARY_PATH

WORKDIR /app

EXPOSE 15001
EXPOSE 9999

ENTRYPOINT ["./skynet", "game.conf"]
#ENTRYPOINT ["/bin/bash", "./docker-start.sh"]
