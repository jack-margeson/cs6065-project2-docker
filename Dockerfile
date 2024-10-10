FROM alpine:latest

RUN apk update && apk add --no-cache \
    bash \
    curl

WORKDIR /app

COPY . /app

CMD ["bash"]