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

## Python Tests

python -m venv .\myenv


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
