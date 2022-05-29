# Solution for Question1 from homework1

## Introduction to the current files:

- docker-compose.yml: the docker-compose file that contains the infrastructure build for nifi
- prepareenv.sh: a bash script used to build the full infrastructure which are the below tasks:
    - Create the data  folder that will be used as bind mount inside /tmp of nifi
    - copy the csv2json.py script to ./data and set the proper permission
    - copy the data.csv (which are generated via faker) to ./data directory
    - Build the containers by running docker-compose up -d
    - Install the python interpreter and pandas module for nifi container using docker exec command
- data.csv: CSV data generated with faker
- csv2json.py: the script to convert the read CSV from previous process in Nifi and convert to json, then save it as data.json
- ibrahim_template_nifi.xml: the Nifi workflow exported template
- images: contains images used in section below.

---

## Steps to prepare the environment:

- Please run the script ./prepareenv.sh that should take care of having all folders, containers, scripts and data prepared
- Please login to nifi on http://localhost:8080
- Once logged, please click on upload template and uploaded the file "ibrahim_template_nifi.xml" as shown in screenshots below:
    - Upload template <br/>
        ![step1](./images/img1.png)
    - Select the template from local dirctory:<br/>
        ![step2](./images/img2.png)
    - Below how it looks like once images selected: <br/>
        ![step3](./images/img3.png)
    - When the workflow is uploaded successfully:<br/>
        ![step4](./images/img4.png)
    - Then click on use template from the top menu:<br/>
        ![step5](./images/img5.png)
    - Select the template that was just updated:<br/>
        ![step6](./images/img6.png)
    - The workflow should be loaded, select from navigation on the left the start button to start the workflow:<br/>
        ![step7](./images/img7.png)
    - Once the workflow will be show output as below, and a file named **data.json** should be in ./data directory contains the converted file:<br/>
        ![step8](./images/img8.png)
