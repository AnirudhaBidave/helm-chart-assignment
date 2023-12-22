# helm-chart-assignment
The assignment is about to establish communication between two differnt pods deployed on kubernetes 
1. First I have created flask app of an simple web application on 'todo list' .
2. And create two different docker file for frontend and backend and push it to docker hub.
3. For frontend I use nginx as base image and change the default index.html with frontend html.
4. And configure it to listen on port 80 using nginx.conf file.
5. Then I create a helm chart using ```helm install <deployment-name> <dir-name>``` for both frontend and backend.
6. Then made the nessesory changes in value.yaml file.
7. And deploy it using helmfile to deploy both charts at ones ```helmfile sync```
