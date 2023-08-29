# DevOps : Pipeline CI-CD

## Table of Contents
- [sequencing_module](#sequencing_module)
  - [Table of Contents](#table-of-contents)
  - [General Info](#general-info)
    - [1.Contextualization of the project](#1contextualization-of-the-project)
    - [2.Presentation of the project](#2presentation-of-the-project)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [FAQs](#faqs)
    - [2. Contact the developers](#2-contact-the-developers)


## General Info
***
### 1.Contextualization of the project
We always struggle to deploy an app automatically because of the intervention of the human being in the process of automation but 
we want to diminish the intervention of the human . So our project aims to have a pipeline for delivering the app build with django

### 2.Presentation of the project
this project is just having a view rendering users saved on the postgres sql database

### 3. Configuration

#### Dockerfile
we need to create a custom image that contains Python but also installs our code and has additional configuration details. To build our own image we create a special file known as a Dockerfile that defines the steps to create and run the custom image.

#### .dockerignore
A **.dockerignore** file is a best practice way to specify certain files and directories that should not be included in a Docker image. This can help reduce overall image size and improves security by keeping things that are meant to be secret out of Docker.

#### docker-compose.yml
Our fully-built custom image is now available to run as a container. In order to run the container we need a list of instructions in a file called **docker-compose.yml**



## Technologies
***
A list of technologies used within the project:
* [Django](https://www.djangoproject.com): Version 12.3
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): Version 2.9.7


## Installation
***

### 1. A little intro about the installation.
```
$ git clone https://github.com/mamoudousow098/sequencing_module.git
$ cd ../path/to/the/file
$ docker-compose up -d --build
$ after instatllation you can access the django project [home page](http://127.0.0.1:8000/)
```


## FAQs
***

###  Contact the developers
For further information you can directly contact the two developers of the project
* [Mamoudou Mamadou Sow](<MAILTO:smamadoumamoudou@ept.sn>)
* [Mouhamed Abdoulaye Sadji](<MAILTO:sadjiabdoulaye@ept.sn>)
* [Aissatou Baldé](<MAILTO:baldeaissatou@ept.sn>)
* [Farimata Ngom](<MAILTO:ngfarimata@ept.sn>)

