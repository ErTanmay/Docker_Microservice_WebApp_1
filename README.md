🐳 Microservices with Python (Flask) and Java (Spring Boot)
This project demonstrates a microservices-based architecture using Python (Flask) and Java (Spring Boot), containerized with Docker. The primary goal is to showcase seamless communication between services built with different tech stacks.

💡 Project Architecture
The application consists of two microservices:

1. Client App (Python + Flask) 🐍
Accepts two numbers from the user via an API endpoint.
Forwards the numbers to the Host App for addition.
Receives and displays the result from the Host App.
2. Host App (Java + Spring Boot) ☕
Exposes a REST endpoint to perform the addition of two numbers.
Sends the result back to the Client App.

🐋 Docker Integration
Both apps are containerized using Docker and are connected using the --link argument to enable inter-container communication.

📝 Prerequisites
Docker installed on your system.
📦 Pull the Docker images:
docker pull tanmaylokhande/host_app:latest
docker pull tanmaylokhande/client_app:latest

🚀 Running the Containers:
Start the Host App container:
docker run -d -p 8080:8080 --name host-app tanmaylokhande/host_app:latest

Start the Client App container (linking it to the Host App):
docker run -d -p 5000:5000 --name client-app --link host-app:host-app tanmaylokhande/client_app:latest

Access the Client App:
http://localhost:5000/proxyAdd/2/5

This will trigger the addition of numbers 2 and 5, and you will see the result returned from the Host App.

🚦 API Endpoints
Client App (Flask)
Addition Endpoint:
GET /proxyAdd/{n1}/{n2}
Parameters:
n1 (int): First number
n2 (int): Second number
Response: JSON with the addition result.

Host App (Spring Boot)
Addition Endpoint:
GET /add/{n1}/{n2}
Parameters:
n1 (int): First number
n2 (int): Second number
Response: Integer result of the addition.

📸 Screenshots
Client App (Python + Flask)
<img width="952" alt="ClientApp" src="https://github.com/user-attachments/assets/6aa10bdf-0806-4dea-ac23-91bcda0c9f34" />

Host App (Java + Spring Boot)
<img width="952" alt="HostApp" src="https://github.com/user-attachments/assets/24bf63b5-cb45-4802-9b92-1bb471a56bb5" />

Docker Containers and Output
<img width="1010" alt="Example" src="https://github.com/user-attachments/assets/dfe239cf-2c7a-4436-9f9a-875db1448439" />

🌟 Technologies Used
Python (Flask)
Java (Spring Boot)
Docker
REST APIs


