Patrick Bargoud
Sports Catalog Project
Full Stack Web Development Udacity Nanodegree

ABOUT
This project consists of developing an application that produces a list of Sports Equipment, categorized by sport. The items on the list can be read, edited, added, or deleted using a web application. The project also includes the use of Google login so that a user can use his/her Google account. 

REQUIREMENTS
This project requires Python, Vagrant, and VirtualBox in order to run. The download links are shown below.
Python: https://www.python.org/downloads/
Vagrant: https://www.vagrantup.com/downloads.html
VirtualBox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

RUNNING THE CODE
In order to run the code, you must first connect to the cirtual machine. Open your terminal and navigate to the vagrant folder. Run "vagrant up" and then "vagrant ssh" to access the VM. Then, run "cd /vagrant" and navigate to the project folder. Next, run "python database_setup.py" to create the database, followed by "python sportsequipment.py" to populate the database. To start the web application, run "python application.py" and then, through your browser, type in "localhost:5000".