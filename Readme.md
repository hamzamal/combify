Task no.1:
For data processing I used pyspark and all the processing was being performed on spark. For exploratory data analysis, I used google cloud too. In order to fetch the labels I performed sentimental analysis of data and sentimentintensityanalyzer library was used for this purpose. it can give sentiment scores based on feature that can be used as positive or negative sentiments i-e, indication of buing or selling shares.
The feature I used for sentimental analysis was headline of news. Exploratory data analysis was performed and I observed that length of the headline was an important parameter for prediction.

Task no.2:
I used multiple models for prediction i-e, logistic regression, naive bayes and deep neural network. I implemented logistic regression on spark however, it took alot of computation time to train the model as databricks community version donot provide enough cores so, I used google colab for naive bayes and deep neural networks as it provides GPU.
In the end LSTM model performed better in terms of classification evaluation and computational time so, I used the model from lstm for deployment and building a simple rest API.


Task no.3:
For packaging the container I have used docker to build up the image. I dumped the model and created the image using the model. Image was optimized by minimizing the number of layers and removing unnecessary packages. In order to to test the API docker image can be pulled using below command:
docker pull kiraan001/combify:test16
I have used below curl to test one case,
Request:
curl --location --request POST 'http://localhost:5000/predict' --header 'Content-Type:application/json' --data-raw '{ "filteredCleanedText": "stocks hit 52-week highs friday"}'
Below is the response I got from the curl request:
Response:
{"Prediction": [0.0]}
0.0 is an indication of not buying the shares.
Python Flask was used to expose the API through web interface. 


Task no.4: Deploying the Infrastructure:
I will host the API in cloud using Azure App Service. Azure App Service provides a highly scalable, self-patching web hosting service. Azure cloud shell can be used for deployment. First step is to create App Service resources using Azure CLI and then we can deploy the API to Azure using Git.
App Service has built-in support for user authentication and authorization.
I will use Auto-keras model to update the model continously as more data becomes available. it automatically trains a model on the data without having to tune the parameters. Array will be defined for training times and the model will be looped over this paprameter.
I wil be using whylogs logging agent for enabling logging, testing and monitoring the application. It is loght weight and can easily be used in python or spark environment. It can be used for collecting thousands of metrics from structured data, unstructured data, and ML model predictions with zero configuration.


