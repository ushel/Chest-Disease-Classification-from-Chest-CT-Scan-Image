#!bin/bash

sudo apt update

sudo apt install openjdk-8-jdk -y

https://pkg.jenkins.io/
https://pkg.jenkins.io/debian-stable/

sudo systemctl start jenkins

sudo systemctl enable jenkins

sudo systemctl status jenkins

## installing Docker

curl -fsSL https://get.docker.com -o get-docker.sh | sudo sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

sudo usermod -aG docker jenkins



newgrp docker

'''sudo apt install awscli -y '''

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install zip
unzip awscliv2.zip
sudo ./aws/install

sudo usermod -a -G docker jenkins


## AWS configuration & restarts jenkins

aws configure


## Now setup elastic IP on AWS as public ip will change



## For getting the admin password for jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword