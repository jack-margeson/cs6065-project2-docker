FROM alpine:latest

RUN apk update && apk add --no-cache \
    bash \
    curl \
    python3

RUN mkdir -p /home/data/output

WORKDIR /home/data

COPY ./data/* /home/data/

#CMD ["/bin/bash"]
CMD ["python3", "/home/data/scripts.py"]

# Below is a command for testing the Kubernetes cluster for the extra credit.
#CMD ["sh", "-c", "while true; do python3 -c 'print(\"a\")'; sleep 1; done"]