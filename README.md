<h1 align="center">
OTPify – AI-Driven Fast OTP & Email Service
</h1>
<!-- <h3 align="center">
A secure OTP and email delivery service built with Go Fiber, integrated with advanced AI/ML-based filtering using FastAPI to ensure accurate and reliable request processing.
</h3> -->

## Overview

**OTPify** is an AI-driven OTP and email delivery service designed to provide high-performance, scalable, and secure user authentication. The service is built using **Go Fiber** to handle OTP and email dispatch, ensuring excellent performance, especially in database management and high-concurrency scenarios. Additionally, **FastAPI** is integrated as a microservice to enable advanced AI-driven functionalities, including fraud detection and email classification using **OpenAI API** and **LLMs**.

## Key Features

- **Fast and Scalable OTP Delivery**:  
  Using **Go Fiber** for efficient OTP and email dispatch, optimizing system performance and scalability.
  
- **AI-Driven Insights**:  
  Leveraging machine learning and AI to detect fraud, generate rejection summaries, and provide real-time security insights through an interactive dashboard.
  
- **Microservices Architecture**:  
  **Go Fiber** powers the core OTP delivery functionality, while **FastAPI** serves as a microservice to process AI-based email analysis.
  
- **Future Domain-Based Authentication**:  
  Planned extension to offer serverless authentication services, allowing users to validate and authenticate using domain names for sending OTPs and emails securely.

## Technologies Used

- **Go Fiber**  
- **FastAPI**  
- **Python**  
- **Docker**  
- **JWT**  
- **Redis**  
- **Machine Learning**: TensorFlow, PyTorch, OpenAI API, LLMs

## Project Goal

With a focus on scalability, fraud prevention, and real-time analytics, **OTPify** is designed to meet the needs of modern applications that require secure and efficient OTP and email delivery solutions.

## Future Plans

- **Serverless Architecture**: Expanding to a serverless solution with domain-based authentication, enabling easy integration and enhanced security.

---

Feel free to contribute, report issues, or fork the repository to improve **OTPify**.

# Get OTPify

### Pull the code

``` mkdir OTPify  ```

``` cd OTPify ```

``` git init ```

``` git pull https://github.com/mallickboy/OTPify.git ```


### Start the Go Fiber server

``` cd backend/go_fiber ```

``` go mod tidy ```  (Installing the dependencies)

``` go run main.go ``` (Running Go Fiber Server)

``` air ``` (Run using reload for debugging)


### Start the FastAPI server

#### Create & Start Python Virtual Environment

``` cd backend/app ```

``` py -3.11 -m venv .venv ```

``` .venv\Scripts\activate ```

#### Install dependencies and Start the server
``` pip install --no-cache -r .\requirements.txt ```

``` uvicorn app.main:app --host "0.0.0.0" --port 8080 ```

``` uvicorn app.main:app --host "0.0.0.0" --port 8080 --reload ``` ( Optional for auto relaod )

#### Stop Python Virtual Environment

``` deactivate ```

#### Remove Python Virtual Environment ( ! CAUTION !)

``` Remove-Item -Recurse -Force .\venv ```
