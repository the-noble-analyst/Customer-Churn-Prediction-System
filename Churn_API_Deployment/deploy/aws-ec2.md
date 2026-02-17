
# AWS EC2 Deployment Guide
Customer Churn Prediction System (FastAPI + Streamlit)

This document explains how to deploy the churn prediction system on AWS EC2 for real-time inference.

---

## Overview

Architecture:

User → Streamlit Frontend → FastAPI Backend → ML Model → Prediction

Hosted on AWS EC2 Ubuntu Server.

---

## Prerequisites

Required:

- AWS account
- EC2 instance (Ubuntu 22.04 recommended)
- SSH key (.pem)
- Git installed locally

---

## Step 1: Launch EC2 Instance

1. Go to AWS EC2 Console
2. Click Launch Instance
3. Select:

   - Name: churn-server
   - AMI: Ubuntu Server 22.04 LTS
   - Instance type: t3.micro (Free Tier)

4. Create or select key pair

5. Configure Security Group:

Allow inbound ports:

| Port | Purpose |
|------|---------|
| 22   | SSH |
| 8000 | FastAPI |
| 8501 | Streamlit |

6. Launch instance

7. Copy Public IP

Example:

http://13.232.xxx.xxx


---

## Step 2: Connect to EC2 via SSH

From your local machine:


ssh -i churn-key.pem ubuntu@YOUR_PUBLIC_IP


Example:


ssh -i churn-key.pem ubuntu@13.232.xxx.xxx


---

## Step 3: Update Server


sudo apt update
sudo apt upgrade -y


---

## Step 4: Install Python and Dependencies


sudo apt install python3-pip python3-venv git -y


Verify:


python3 --version
pip3 --version


---

## Step 5: Clone GitHub Repository


git clone https://github.com/the-noble-analyst/Customer-Churn-Prediction-System.git

cd Customer-Churn-Prediction-System/Churn_API_Deployment


---

## Step 6: Install Project Requirements


pip3 install -r requirements.txt

pip3 install fastapi uvicorn streamlit scikit-learn pandas numpy


---

## Step 7: Run FastAPI Server


uvicorn app.main:app --host 0.0.0.0 --port 8000


Access API:


http://YOUR\_PUBLIC\_IP:8000/docs


Example:


http://13.232.xxx.xxx:8000/docs


---

## Step 8: Run Streamlit Frontend

Open new SSH terminal.

Navigate to project folder:


cd Customer-Churn-Prediction-System/Churn_API_Deployment


Run:


streamlit run streamlit/streamlit_app.py --server.port 8501 --server.address 0.0.0.0


Access UI:


http://YOUR\_PUBLIC\_IP:8501


---

## Step 9: Verify Deployment

Test:

FastAPI:

http://YOUR\_PUBLIC\_IP:8000/docs


Streamlit:

http://YOUR\_PUBLIC\_IP:8501


System is now live.

---

## Deployment Architecture


User Browser
↓
Streamlit Frontend (Port 8501)
↓
FastAPI Backend (Port 8000)
↓
Random Forest Model (.pkl)
↓
Prediction Response

Hosted on AWS EC2


---

## Stop Instance to Avoid Charges

Go to EC2 Console:

Instance → Stop

This stops compute billing.

---

## Resume Description

Deployed production ML inference system on AWS EC2 using FastAPI, Streamlit, and Uvicorn enabling real-time churn prediction via cloud-hosted REST API and web interface.

---
