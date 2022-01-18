# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: _

### Prerequisites:

- Make sure your flask app (app.py) is renamed to ``` __init__.py ```
- Something you will need installed beforehand...

1. Install and enable mod_wsgi (changed to reflect python3!) with
    ```
    sudo apt-get install libapache2-mod-wsgi-py3 python-dev
    ```
    and
    ```
    sudo a2enmod wsgi 
    ```
2. Create and place flask app in /var/www directory with ``` cd /var/www ```
3. Install flask
4. 
   
1. Step, with [hyperlink](https://xkcd.com)s...


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

---

Accurate as of (last update): 2022-01-18

#### Contributors:  
Joshua Kloepfer, pd2  
Pat Ging, pd2  
Yoonah Chang, pd2  
