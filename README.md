# ProjectAPI

*Turkish Text Classification with BERT*

API which uses a finetuned BERT model to classify Turkish text. 

This repo does not contain the model file because of the file size limitations of github. Working Docker Image with the model file
can be found at aatakansalar/projectapi

---
##### Status
To check the status of the API, send a get request to /status path.

```shell
>curl http://<domain>/status
>{"status":"ProjectAPI is up and running!"}
```

##### API Usage for Text Classification
To classify text, a POST request with the text attached in the request should 
be sent to /argument

```` python
import requests
argument = {"body": "Bu harika bir filmdi."}
response = requests.post("http://localhost:8000/argument", json = argument)

print(response.status_code) 
# Output: 200

print(response.json()) 
# Output: {'body': 'Bu harika bir filmdi.', 'evaluation': {'category': 'kultur'}}
````

###### Kullanılan Veriseti

- https://www.kaggle.com/datasets/savasy/ttc4900
