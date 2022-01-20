# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: 10 minuts

### Prerequisites:

- Something you should know beforehand...
    - The version can get messed up so be careful
- Something you will need installed beforehand...
    - You will need the LAMP stack

1. install wsgi
    ``` 
    sudo apt-get install libapache2-mod-wsgi-py3
    sudo a2enmod wsgi
    ```
2. make app - replace FlaskApp with nme of app - use this directory to add your code
    ```
    cd /var/www/
    sudo mkdir FlaskApp
    cd FlaskApp
    sudo mkdir FlaskApp
    cd FlaskApp
    sudo mkdir static templates
    ```
3. install flask
    ```
    sudo apt-get python3-pip
    sudo apt install python3.8-venv
    sudo python3 -m venv venv
    source venv/bin/activate
    chown user:user venv/ -R (not sure if necessary but i did)
    pip3 install flask
    deactivate
    ```
4. making config file and wsgi file (replace FlaskApp with your app name - get what to put in conf file in link in resources
   ```
   sudo nano /etc/apache2/sites-available/FlaskApp.conf (get what to put in here from website)
   sudo a2ensite FlaskApp
   cd /var/www/FlaskApp
   sudo nano flaskapp.wsgi (get what to put in here from website)
   service apache2 restart
   ```
5. CONGRATUALTIONS YOU SHOULD NOW HAVE A WORKING SITE!!!!

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

---

Accurate as of (last update): 2022-01-20

#### Contributors:  
Clyde "Thluffy" Sinclair  
Joshua Kloepfer, pd2  
Yoonah Chang, pd2  
Patrick Ging, pd2  
Rayat Roy, pd1  
