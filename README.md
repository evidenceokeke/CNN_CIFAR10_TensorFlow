#  Image Classifier API – CIFAR-10 (TensorFlow + Flask + AWS EC2)

Built a deep learning model to classify CIFAR-10 images using both a custom CNN and transfer learning with ResNet50. Deployed the model as a Flask API, containerized it with Docker, and hosted it on AWS EC2.

**Objective** : Achieve >70% test accuracy on CIFAR-10 and expose the trained model through a production-ready API.

**Approach**

*Model 1: Custom CNN*
* Trained a CNN from scratch using TensorFlow
* Reached 69% test accuracy
* See: Training a CNN on CIFAR-10 (1).ipynb

*Model 2: ResNet50 (Transfer Learning)*
* Used pretrained ResNet50
* Achieved 81% test accuracy
* Used this model for final API deployment
* See: Training a CNN on CIFAR-10 (2).ipynb

**Tech Stack**
* TensorFlow, Keras
* Flask (API)
* Docker
* AWS EC2
* Postman (for testing)

**API Overview**
* Endpoint: POST /predict
* Input: Image file (form-data)
* Output:
  ```
   {
    "prediction": "cat",
    "probability": 0.88
  }
  ```
  Test using Postman or cURL.


**Dockerrized Deployment**

Ensure you have:
* Dockerfile
* requirements.txt
* .dockerignore

Build and run:
```
# Build image
docker build -t flask-api .

# Run container
docker run -p 5000:5000 flask-api
```
Access the API at: http://127.0.0.1:5000/predict

**Deploying on AWS EC2**
* Launch EC2 Instance - Follow this tutorial -
* Transfer project files:
  ```
   scp -i your-key.pem -r ./project-folder ec2-user@<ec2-ip>:/home/ec2-user/
  ```
* On the instance:
  ```
  pip install -r requirements.txt
  python main.py
  ```
* Allow external access (Port 5000)
   * Update EC2 Security Group: Custom TCP → Port 5000 → Source: 0.0.0.0/0
   * Also update Windows Firewall (if applicable)
 * Test API remotely: http://<your-ec2-public-ip>:5000/predict

**Cleanup**
Terminate your EC2 instance to avoid unwanted AWS charges.
 
