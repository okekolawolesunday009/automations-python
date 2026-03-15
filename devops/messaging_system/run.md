# DevOps Stage 3 Task  
## Messaging System with RabbitMQ/Celery and Python Application behind Nginx

## Overview
This task requires deploying a **Python application behind Nginx** that interacts with **RabbitMQ and Celery** to perform background tasks such as **sending emails** and **logging messages**.

---

# Objective
Deploy a Python application that:

- Runs behind **Nginx**
- Uses **RabbitMQ + Celery** for background task processing
- Sends emails via **SMTP**
- Logs messages to a system log file
- Is exposed externally using **ngrok**

---

# Submission Deadline

**Submission Deadline:**  
Sunday, **7th July 2024**, at **11:59 PM GMT**

**Final Submission Cutoff:**  
Saturday, **12th July 2024**, by **11:59 PM GMT**

---

# Requirements

## 1. Local Setup

Install the following on your local machine:

- Python
- RabbitMQ
- Celery
- Nginx

Set up a **Python application** that exposes an endpoint capable of accepting the following parameters:

```
?sendmail
?talktome
```

---

# Endpoint Functionalities

## 1. `?sendmail`

When the endpoint is called with the parameter:

```
?sendmail=mailto:destiny@destinedcodes.com
```

The system should:

1. Queue an email sending task using **RabbitMQ/Celery**
2. Send the email using **SMTP**
3. Ensure the **Celery worker retrieves and processes the task from the queue**

### Flow

```
Client Request
      ↓
Python API
      ↓
Celery Task Queue
      ↓
RabbitMQ Broker
      ↓
Celery Worker
      ↓
SMTP Email Sent
```

---

## 2. `?talktome`

When the endpoint is called with:

```
?talktome
```

The system should:

Log the **current server time** into:

```
/var/log/messaging_system.log
```

Example log entry:

```
2024-07-07 15:42:10 - Request received from /talktome endpoint
```

---

# Nginx Configuration

Configure **Nginx** to serve the Python application.

Responsibilities of Nginx:

- Reverse proxy requests to the Python app
- Handle incoming HTTP requests
- Route requests properly to the application server

Example architecture:

```
Client Request
      ↓
Nginx Reverse Proxy
      ↓
Python Application (Flask/FastAPI/Django)
      ↓
RabbitMQ + Celery Worker
```

---

# Endpoint Exposure

Expose the application endpoint publicly using:

- **ngrok** or similar tunneling tools

Example:

```
https://abcd1234.ngrok.io
```

This endpoint should allow testers to access:

```
https://abcd1234.ngrok.io?talktome
https://abcd1234.ngrok.io?sendmail=mailto:test@example.com
```

---

# Documentation & Walkthrough

Record a **screen-captured walkthrough video** demonstrating the entire setup.

Your video must cover:

### 1. RabbitMQ Setup
- Installing RabbitMQ
- Running RabbitMQ locally

### 2. Celery Setup
- Installing Celery
- Connecting Celery to RabbitMQ

### 3. Python Application
- Code explanation
- Endpoint functionality

### 4. Nginx Configuration
- Reverse proxy configuration
- Application routing

### 5. SMTP Email Sending
- Demonstrate email being sent successfully

### 6. Logging System
- Show `/var/log/messaging_system.log` receiving entries

### 7. ngrok Exposure
- Expose the endpoint
- Demonstrate accessing it publicly

---

# Submission

Submit your work using the form below:

**Submission Link**

https://forms.gle/okhAFDnXQ5Dw6Ls39

---

# Submission Requirements

Your submission must include:

- **Public ngrok endpoint**
- **Screen recording walkthrough**
- Working **RabbitMQ + Celery integration**
- Working **email sending**
- Working **log system**
- Working **Nginx reverse proxy**

---

# Evaluation Criteria

## 1. Functionality
All required features must work correctly:

- Email sending
- Task queue processing
- Logging system
- Public endpoint access

---

## 2. Code Quality
- Clean structure
- Well-documented configurations
- Readable code

---

## 3. Presentation
- Clear walkthrough video
- Proper explanation of the setup

---

## 4. Deadline Adherence
Strict adherence to the deadline.

**Late submissions will not be accepted.**

---

# Expected System Architecture

```
                +-------------+
                |   Client    |
                +-------------
                
                       |
                       |
                       v
                +-------------+
                |    Nginx    |
                | Reverse Proxy|
                +-------------+
                       |
                       v
                +-------------+
                | Python App  |
                | (Flask/API) |
                +-------------+
                       |
                       v
                +-------------+
                |   RabbitMQ  |
                |   Broker    |
                +-------------+
                       |
                       v
                +-------------+
                |  Celery     |
                |  Worker     |
                +-------------+
                       |
                +-------------+
                | SMTP Server |
                +-------------+
```

---

# Good Luck 🚀
Make sure your solution is **fully functional**, **well documented**, and **properly demonstrated** in the walkthrough video.