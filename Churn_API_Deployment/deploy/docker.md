# Docker Deployment Guide
Customer Churn Prediction System

This guide explains how to deploy the churn prediction system using Docker containers.

---

## Overview

Docker allows packaging the ML application, dependencies, and runtime into a portable container.

Benefits:

- Reproducible deployment
- Environment isolation
- Easy scaling
- Production-ready deployment

---

## Prerequisites

Install Docker:

Linux:


sudo apt install docker.io -y


Verify:


docker --version


---

## Project Structure


Churn_API_Deployment/
│
├── app/
│ ├── main.py
│ ├── best_churn_model.pkl
│
├── streamlit/
│ ├── streamlit_app.py
│
├── docker/
│ ├── Dockerfile
│ ├── start.sh
│
├── requirements.txt


---

## Step 1: Navigate to Docker Folder


cd Churn_API_Deployment/docker


---

## Step 2: Build Docker Image


docker build -t churn-prediction .


Verify:


docker images


---

## Step 3: Run Docker Container


docker run -p 8000:8000 -p 8501:8501 churn-prediction


This exposes:

| Service | Port |
|--------|------|
| FastAPI | 8000 |
| Streamlit | 8501 |

---

## Step 4: Access Application

FastAPI:


http://localhost:8000/docs


Streamlit:


http://localhost:8501


---

## Docker Architecture


Docker Container
│
├── FastAPI Server
├── Streamlit Frontend
├── ML Model
└── Python Environment


---

## Stop Container

Find container:


docker ps


Stop container:


docker stop CONTAINER_ID


---

## Resume Description

Containerized ML inference system using Docker enabling portable and reproducible deployment of FastAPI and Streamlit-based churn prediction application.

---

## Production Deployment Options

Docker containers can be deployed on:

- AWS EC2
- AWS ECS
- Azure Container Instances
- Google Cloud Run
- Kubernetes

---
