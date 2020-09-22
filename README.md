# Inter-process communication

This Python application launches a couple of processes which communicate with each other using the publish-subscribe 
messaging pattern.  


There are 4 main objects : 
* MotionDetector (Publisher) : Gets a message from the Flask API, creates an object of the class MotionVector and adds 
this object to the queue
* SingleShotDetector (Publisher-Subcriber) : Gets the messages from the MotionVector's queue, process them and puts them 
in the DetectionVector's queue.
* Logger (Subscriber) : Reads messages from the both queues and logs them to the standard output.
* MotionVector (Topic) : Class which allows us to create messages under a specific format
* DetectionVector (Topic) : Class which allows us to create messages under a specific format


To be able to correctly share data between processes, the decision to use Queues was made.  
Queues are using pipes and a few locks/semaphores, so this guarantees us that data will not be corrupted.

## Test the application
Flask is using PORT 5000, make sure that the port is not already in use.    
* 1 : Open to the folder `inter_process_communication` in a terminal window

* 2 : Copy and past this shell command in the terminal window :
`docker-compose -f devops/docker_compose_inter_process_comm.yml up --build`  
If everything went good you should see something similar to this in your terminal window : 
![alt text](img/docker_run.png?raw=true "Terminal result")

* 3 : It's time to open the Swagger ! (API's documentation)   
Copy and paste this link into your web browser : `http://0.0.0.0:5000/doc`
The swagger must open in your web browser : 
![alt text](img/swagger.png?raw=true "Swagger in the web browser")

* 4 : Click on "POST" row, it will open, click on `try it out`  
Write a message and click on `Execute`
If everything went good flask has returned **201 : created** 
![alt text](img/try_it_out.png?raw=true "Swagger result")

In your terminal window you should see this message printed 2 times, logger consumes 2 queues, first 
the message will be taken from the first queue and printed and then when the process SingleShotDetector will process 
the message it will exist in the second queue and the logger will print it a second time.  

![alt text](img/message_terminal.png?raw=true "Terminal result with message printed")

### To stop the docker container :
Please use the command `docker stop $(docker ps -a -q)` to stop the application.  
If you will try to stop it only with the `CTRL + C` it won't stop correctly as the application has not only 
one process running.
