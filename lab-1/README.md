## Run with Docker
```bash
cd labs/cs361-hello-service/src
docker build -t cs361-hello-service:lab1 -f ../docker/Dockerfile .
docker run --rm -p 8080:8080 --name cs361-hello-service cs361-hello-service:lab1
