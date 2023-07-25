FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y python3.9
RUN apt update && apt install python3-pip -y
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN apt-get install -y ca-certificates wget 

    
COPY . /home/site/wwwroot

WORKDIR /home/site/wwwroot

CMD ["python3","app.py"]