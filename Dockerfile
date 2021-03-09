FROM wetransform/hale-cli:4.1.0-SNAPSHOT
ENV PATH="/hale/bin:${PATH}"
RUN apt-get update -y && apt-get install -y python3
WORKDIR /stnreg
COPY . .
ENTRYPOINT [ "python3", "./stnreg2gml.py" ]