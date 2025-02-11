<h1 align="center">
Mail-Delivery-Service
</h1>
<h3 align="center">
Providing a OTP/Mail delivery service using advanced ML algorithm and FastAPI 
</h3>

### Pull the code

``` mkdir OTPify  ```

``` cd OTPify ```

``` git init ```

``` git pull https://github.com/mallickboy/OTPify.git ```


### Create & Start Python Virtual Environment

``` cd backend ```

``` py -3.11 -m venv .venv ```

``` .venv\Scripts\activate ```


### Start the server

``` pip install --no-cache -r .\requirements.txt ```

``` uvicorn app.main:app --host "0.0.0.0" --port 8080 ```

``` uvicorn app.main:app --host "0.0.0.0" --port 8080 --reload ``` ( Optional for auto relaod )




### Stop Python Virtual Environment

``` deactivate ```

### Remove Python Virtual Environment ( ! CAUTION !)

``` Remove-Item -Recurse -Force .\venv ```
