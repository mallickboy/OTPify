<h1 align="center">
Mail-Delivery-Service
</h1>
<h3 align="center">
Providing a OTP/Mail delivery service
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

``` pip install -r requirements.txt ```

``` cd OTPify ```

``` python manage.py runserver 8080 ```






### Stop Python Virtual Environment

``` deactivate ```

### Remove Python Virtual Environment ( ! CAUTION !)

``` Remove-Item -Recurse -Force .\venv ```
