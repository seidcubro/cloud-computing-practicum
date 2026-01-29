# Lab 1 – Hello Service (Toolchain Setup)

## Overview
This lab establishes the baseline development environment and repository structure that will be reused throughout the Cloud Computing Practicum. A minimal HTTP API service was implemented, run locally, and containerized using Docker. The lab demonstrates the distinction between an application, a container image, and a running container while verifying correct toolchain setup.

The service exposes simple endpoints to confirm functionality and includes basic request logging. Evidence of successful execution is captured and included in the repository.

---

## Objectives
- Verify installation and configuration of Git, Docker, and a Linux development environment (WSL)
- Implement a minimal HTTP API service
- Run the service locally (non-containerized)
- Containerize the service using Docker
- Build and run the container locally
- Verify endpoints using a browser and `curl`
- Establish a clean, reusable repository structure

---

## Repository Structure
lab-1/
├── README.md
├── .gitignore
├── docker/
│ ├── Dockerfile
│ └── .dockerignore
├── images/
│ └── Evidence screenshots
├── report/
│ └── Lab 1 report files
└── src/
├── app.py
└── requirements.txt


---

## API Endpoints
| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/health` | Returns service health status |
| GET | `/` | Returns a basic service response |

Example response:
```json
{ "status": "ok" }
Running the Service Locally
From the src/ directory:

python app.py
The service runs on port 8080.

Test the service:


curl http://localhost:8080/health
Running the Service with Docker
Build the image
From the src/ directory:


docker build -t cs361-hello-service:lab1 -f ../docker/Dockerfile .
Run the container
bash
Copy code
docker run -p 8080:8080 cs361-hello-service:lab1
Verify container execution
bash
Copy code
docker images
docker ps
Test the running container:

curl http://localhost:8080/health

Evidence
Screenshots demonstrating tool installation, local execution, Docker image creation, running containers, and successful endpoint responses are stored in the images/ directory and referenced in the lab report.

Notes
Virtual environments and generated files are intentionally excluded from the repository.

Docker is used to ensure reproducible execution across systems.

This repository structure will be reused for future labs.

Technologies Used
Python

Flask

Docker

Git

WSL (Ubuntu)


---

This README is **100% appropriate for grading** and **clean enough for a portfolio**.
- prep **Lab 2** so it doesn’t turn into chaos again
::contentReference[oaicite:0]{index=0}
