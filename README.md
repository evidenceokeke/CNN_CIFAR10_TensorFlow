# CNN on CIFAR-10: Model Training, Flask API Deployment, and EC2 Hosting

In this project, I train a Convolutional Neural Network (CNN) on the CIFAR-10 dataset using TensorFlow. The trained model is then deployed as a Flask API in Docker and hosed on AWS EC2.

**Goal**: Achieve a test accuracy of > 70% on the CIFAR-10 dataset.

**Approach**

1. Model 1 (Custom CNN) : I first trained a custom CNN model from scratch, which achieved a test accuracy of 69%. This did not reach the goal. You can however, review the process in the notebook titled "Training a CNN on CIFAR-10 (1)".
2. Model 2 (Transfer Learning with ResNet50): I then used transfer learning with the pretrained ResNet50 model, achieving a test accuracy of 81%. I used this model to build a Flask API. Check out notebook "Training a CNN on CIFAR-10 (2)" on how it was done.

In main.py I built the Flask API.

**API Usage**

You can test the API using Postman (or cURL), by:
* Set the request type to POST.
* Use the following URL (or the one that comes up when you run main.py): http://127.0.0.1:5000/predict
* Under the "Body" tab, select "form-data" and upload the image you want to classify.
* The API will return a dictionary with the predicted class and its associated probability.

  **Dockerizing the Flask API**

  To deploy your Flask API in Docker, ensure you have the following files in your project directory:
  * Dockerfile
  * requirements.txt
  * .dockerignore

 Check them out in the repository. Ensure you have Docker installed on your system as well.

 *Steps to Dockerize*
 
 On your terminal run the following:
 1. Build the Docker image: ```docker build -t flask-api .```
 2. Run the container: ```docker run -p 5000:5000 flask-api```
 3. Test the API using Postman (or cURL) as described above.

If you are unsure of how to install the required python dependencies from ```requirements.txt```, you can use the following command:

```pip install -r requirements.txt```

**Deploying on AWS EC2**

1. Create an EC2 Instance. I followed this Youtube tutorial: https://youtu.be/YH_DVenJHII?si=P4ayk54JiNW3rsn8
2. Once the Instance is running and connected, copy the project from local machine to the Instance.
3. Open command prompt and navigate to the project directory.
4. Install all dependencies using: ```pip install -r requirements.txt```
5. Start the Flask app by running ```python main.py```

To allow external access to your Flask app on port 5000, you may need to confirgure the EC2 security group:
* In the EC2 Management Console, go to Security Groups.
* Click on "Edit the Inbound Rules", and add a rule for Custom TCP with port 5000 and source 0.0.0.0/0 (to allow all IP addresses).
* On the EC2 Instance, open Windows Firewall settings and add an inbound rule to allow connections on port 5000.

Now test the API from Postman on your local machine using the EC2's instance public IP address: ```http://<your-ec2-public-ip>:5000/predict```

After you're done with the instance, **remember to delete** it from the EC2 console to avoid incurring charges in the future.


   
