# sonarfun
Docker with SonarQube and exporter test

# Start Running

```
sudo docker-compose up -d 
```

Follow logs with
```
sudo docker-compose logs --follow
```

## Python Debugging

Create Virtual Environment for vscode. This can also be done in vsCode IDE

```
python -m venv .venv
```

Debug locally using python 3.10 using the .vscode launch.json file. Options available
1. Python: Debug Exporter" - for local debugging without using going through Docker
   - For this option though you will need to comment out sqexporter from docker-compose.yml file
     and use: "targets: ['host.docker.internal:9120']" instead of  "targets: ['sqexporter:9120']"
      
2. Remote Debugging: ... TO DO

## Jave Unit Tests
After starting up SonarQube, register the project as "junit-mockito-spring-boot"

mvn clean verify sonar:sonar \
  -Dsonar.projectKey=junit-mockito-spring-boot \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=sqp_6237bb62be62f21e668221c3298a0020e183e6dc

## Sonar Plugin

Original Source code from here: https://github.com/vinicelms/sonarqube-prometheus-exporter

To Debug You need to following Variables

```
SONAR_URL=https://localhost:9001
SONAR_USER={USER}
SONAR_PASSWORD={PASSWORD}
```

The project retrieves all the metrics from SonarQube using the "Web API"

e.g.
http://localhost:9000/api/measures/component?component=junit-mockito-spring-boot&metricKeys=tests
