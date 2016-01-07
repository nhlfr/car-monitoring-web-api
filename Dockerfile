FROM centos:7
MAINTAINER Michal Rostecki <michal.rostecki@gmail.com>

RUN yum -y install \
        build-essential \
        epel-release \
        gcc \
        git \
        python-devel \
        sudo \
    && yum clean all

RUN yum -y install \
        python-virtualenv \
    && yum clean all


COPY car_monitoring_sudoers /etc/sudoers.d/car_monitoring_sudoers
ADD . /opt/car-monitoring-web-api

RUN mkdir -p /var/lib/car-monitoring/venv \
    && useradd --user-group obd \
    && chown -R obd: /opt/car-monitoring-web-api /var/lib/car-monitoring/venv

USER obd

RUN virtualenv /var/lib/car-monitoring/venv

RUN /var/lib/car-monitoring/venv/bin/pip install -e /opt/car-monitoring-web-api

COPY start.sh /

CMD ["/start.sh"]
