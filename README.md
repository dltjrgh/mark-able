<div align="center">
  <img src="https://cdn.discordapp.com/attachments/381812425906716674/872453476788101180/77e635d998ef8c24.png" alt="Responsively Logo" width="150">
  <h1>Mark-able <a href="https://github.com/2021-summer-program/MarkAble" target="_blank"></a></h1>
  <strong>Trademark Similarity Calculation Application 🔎</strong>
  <h6>A web service that determines the distinctiveness of given trademarks, based on a previously registered trademark dataset.</h6>
</div>
<br><br>

## **📝 Introduction**

- Choose up to two <i>Similarity code groups</i>.
- Then, enter your trademark to search for similar trademarks among the selected groups.
- Data visualization is provided as wordcloud.

<br>

**Demo Video** : 
[Mark-able Demo](https://drive.google.com/file/d/1iXJ6pz-P7uPYEriTwBZTbhvKo2NARdkB/view?usp=sharing)
<br>
<p><img src = "https://user-images.githubusercontent.com/52441906/127099647-acf124f8-645a-4d7c-8dab-f0f59a079f3d.png" width="500px"></p>
<p><img src = "https://user-images.githubusercontent.com/52441906/127078511-02e08cf2-30e2-4bf9-93b4-2e34538eac70.png" width="500px"></p>
</br>
</br>

## **💡 System Architecture**</br>

</br>![image](https://user-images.githubusercontent.com/75110752/127173731-ab57644e-2b31-4ecc-baa5-c411e1f1c990.png)
</br></br></br>

## **🖇 Tech Stack**
```
frontend : React 
backend : Flask 
database : MongoDB
model : Elasticsearch
web server : nginx
middle ware: gunicorn
monitoring : Prometheus, Grafana 
api documentation/test : swagger, postman
images server : s3 bucket 
cloud : aws ec2 
```
| frontend                                                                                                                                                                                                                   | backend                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | etc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://img.shields.io/badge/React-92CAFB?style=flat-square&logo=React&logoColor=white"/></a>  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a> </br> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/></a> <img src="https://img.shields.io/badge/Axios-AE68D1?style=flat-square&logo=Axios&logoColor=white"/></a> | <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a> <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/></a> </br> <img src="https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=Elasticsearch&logoColor=white"/></a> <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white"/></a> <img src="https://img.shields.io/badge/Gunicorn-A1DCDA?style=flat-square&logo=Gunicorn&logoColor=white"/></a> | <img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/> </br><img src="https://img.shields.io/badge/S3-569A31?style=flat-square&logo=Amazon S3&logoColor=white"/> <img src="https://img.shields.io/badge/EC2-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> <img src="https://img.shields.io/badge/Swagger-85EA2D?style=flat-square&logo=Swagger&logoColor=white"/> <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white"/> </br> <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=Prometheus&logoColor=white"/> <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=Grafana&logoColor=white"/>  <img src="https://img.shields.io/badge/Ubuntu 20.04-E95420?style=flat-square&logo=Ubuntu&logoColor=white"/></a> </br> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> </br>
</br>
</br>

## **💻  Installation**

### a. Install Docker.

Follow the guidelines in the [official website](https://docs.docker.com/engine/install/) to install Docker.

### b. Clone Repository.
```shell
git clone https://github.com/2021-summer-program/Trademark_verification
```
### c. Set Kipris API KEY.

1. Access [KIPRIS Plus website](https://plus.kipris.or.kr/portal/bbs/view.do?bbsId=B0000004&nttId=683&menuNo=200019)

2. Sign Up

3. [KIPRIS Plus](https://plus.kipris.or.kr/portal/main.do) Main page <i>Data Services</i> -> OpenAPI -> apply for <b>Trademark Registration API</b></br>
      </br>
      <img src = "https://user-images.githubusercontent.com/52441697/128177546-766e6bb4-f340-4d78-96ff-dabf825a4769.png" width="400px">

4. Create <i>backend/codes/api_key.txt</i> file, and paste your REST API KEY to <i>api_key.txt</i>.</br>
      </br>
      <img src = "https://user-images.githubusercontent.com/52441697/128176181-f8cecd98-185e-427d-9806-168bb6282ad0.png" width="300px">
      <img src = "https://user-images.githubusercontent.com/52441697/128176708-f5760812-f41a-4492-b36e-3f5a961af1e5.png" width="400px">

### d. Download Dataset

Download <i>data.json</i> from the [link](https://drive.google.com/file/d/121MmzB5duG_PS5bt442Q35wAM_R1pkaO/view?usp=sharing) and add the file to the <i>root/mongo-seed/</i> folder.

### e. Build

[docker-compose.yml] Execute the following in the root folder.
```shell
docker-compose build
```
</br>
</br>

## **💻  Execution**

**[docker-compose.yml] Execute the following in the root folder.**

```shell
docker-compose up
```

**Container Ports** 

Tool | port |
--- | --- | 
Frontend | 3000 |
Backend | 5000 |
ElasticSearch | 9200 |
MongoDB | 27017 |
Prometheus | 9090 |
Grafana | 3001 |
      
**Delete container after execution**

```shell
docker-compose down
``` 
