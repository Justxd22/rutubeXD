FROM debian:latest

ENV TZ=Asia/Riyadh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt upgrade -y && apt install ffmpeg python3 python3-pip -y

RUN mkdir /tube
COPY ./ /tube/

RUN pip3 install --no-cache-dir -r /tube/requirements.txt

CMD ["bash", "/tube/start.sh"]
