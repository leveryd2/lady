FROM ubuntu:14.04
MAINTAINER 1157599735@qq.com
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# apt and pip mirrors

RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && mkdir -p ~/.pip \
    && echo "[global]" > ~/.pip/pip.conf \
    && echo "timeout=60" >> ~/.pip/pip.conf \
    && echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf

# install requirements

RUN set -x \
    && apt-get update \
    && apt-get install -y wget unzip gcc libssl-dev libffi-dev python-dev libpcap-dev python-pip


# install this project
RUN mkdir -p /data/lady
COPY . /data/lady

RUN set -x \
    && pip install -r /data/lady/requirements.txt

# RUN set -x \
#     && chmod a+x /opt/xunfeng/masscan/linux_64/masscan \
#     && chmod a+x /opt/xunfeng/dockerconf/start.sh

WORKDIR /data/lady

# VOLUME ["/data"]

# ENTRYPOINT ["/opt/xunfeng/dockerconf/start.sh"]

EXPOSE 80

CMD ["/usr/bin/tail", "-f", "/dev/null"]