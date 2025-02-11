<h1 align="center">
OTPify: Secure-Mail-Delivery-Service
</h1>
<h3 align="center">
A secure OTP and email delivery service built with Go Fiber, integrated with advanced AI/ML-based filtering using FastAPI to ensure accurate and reliable request processing.
</h3>

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
