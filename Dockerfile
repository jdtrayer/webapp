# webapp
FROM openshift/base-centos7

# TODO: Put the maintainer name in the image metadata
MAINTAINER Jeb Trayer <jdtrayer@gmail.com>

RUN yum install -y python-flask && yum clean all -y

ADD ./src/ /opt/app-root/
RUN chown -R 1001:0 /opt/app-root

RUN ls -al /opt/app-root/

# This default user is created in the openshift/base-centos7 image
USER 1001

# TODO: Set the default port for applications built using this image
EXPOSE 80

# TODO: Set the default CMD for the image
CMD ["python", "/opt/app-root/app.py"]
