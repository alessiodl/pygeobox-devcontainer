FROM ghcr.io/osgeo/gdal:ubuntu-small-3.9.0

RUN apt-get update && apt-get -y install python3-pip python3-venv --fix-missing

ENV VIRTUAL_ENV=/opt/geoenv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
