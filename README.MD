


This is a Sport listing app built with Python, Flask and SQLAlchemy. The app supports user authentication and authorization using OAuth 2.0 and the Google Login API. 
Logged in users can:
* Add, Edit and delete items that they have created. 
* Delete and Create Categories

The system is built in a way that a user is not authorized to delete categories or make changes to items created by another user. 
They only have read access.

Sporta also has a JSON endpoint at ``` \explore``` to view categories and items.

Users who are not logged in can view the contents of the listings 
but cannot make changes.

### Installation Prerequisites
* Python
* [Vagrant](https://www.vagrantup.com/downloads)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

### STEPS TO RUN THIS PROJECT
* Run: git clone https://github.com/udacity/fullstack-nanodegree-vm.git vagrant
(This will create a new directory titled vagrant that contains all of the necessary configurations to run this application.)
* Move to the vagrant folder by entering: cd ~/vagrant/
* Clone the github repository by running the command below:
* Run: git clone https://github.com/Ijebusoma/Sporta.git
(This will create a directory inside the vagrant directory titled catalog.)
* Run Vagrant by entering: vagrant up
* Log into Vagrant VM by entering: vagrant ssh
* Move to catalog directory by entering: cd /vagrant/CatalogApp/
* Run the main project file, run: python app.py
* View the app on your browser, go to: http://0.0.0.0:8000/

P.S: This application was intended for educational purposes only, app had to be paused on Amazon cloud due to unsustainable running charges however repo includes screenshot of working app.

