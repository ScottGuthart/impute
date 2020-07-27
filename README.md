# flaskloginapp
Flask App Template

Inspired by and modeled after [Miguel Grinberg's Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Links are included to corresponding sections in the tutorial if you want to learn more.

Includes:
* Login / User Registration with email confirmation ([Learn More](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins))
* Bootstrap 4 via [bootstrap-flask](https://github.com/greyli/bootstrap-flask)
* Heroku Procfile ([Learn More](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku))
* Redirect to HTTPS and Content Security Policy (CSP) Support* via [flask-talisman](https://github.com/GoogleCloudPlatform/flask-talisman)
* Blueprint app structure ([Learn More](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure))
* Easy database upgrades via [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)
    
**This template ships with a more relaxed CSP than included with flask-talisman by default in order to allow Bootstrap 4 to work properly. Please refer to flask-talisman documentation to decide what's right for your site.*

## Basic Setup
* Set up a virtual environment and install the requirements [more info](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* Create a .env file in the root directory (/.venv) [more info](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
    * Set up your gmail accout to allow third party sign-in. See above link for more info.
    * Sample .env file:
        ```
        FLASK_APP=flaskapp
        MAIL_SERVER=smtp.googlemail.com
        MAIL_PORT=587
        MAIL_USE_TLS=1
        MAIL_USERNAME=example@gmail.com
        MAIL_PASSWORD=examplepassword
        SECURITY_PASSWORD_SALT=put_your_password_salt_here
        SECRET_KEY=put_your_secret_key_here
        ```
