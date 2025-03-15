FROM ubuntu

RUN apt-get update
RUN apt install default-jdk -y

COPY BackendAddService.jar /opt/BackendAddService.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/opt/BackendAddService.jar"]
