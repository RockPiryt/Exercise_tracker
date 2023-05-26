import requests
from datetime import datetime
from dotenv import load_dotenv
import os

#####################################LOAD PASSWORDS########################################
load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")


USERNAME = os.getenv("pixela_username")
TOKEN = os.getenv("pixela_token")
GRAPH_ID = "graph1"


#####CREATE USER###################################
#url
pixela_endpoint = "https://pixe.la/v1/users"

#json - serializable Python object to send in the body of Request
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# #response
# response = requests.post(url=pixela_endpoint, json=user_params)

# #check response code
# print(response.status_code) #print 200

# #check response text
# print(response.text) # print JSON {"message":"Success. Let's visit https://pixe.la/@piryt , it is your profile page!","isSuccess":true} 

#####CREATE GRAPH###################################
#POST - /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "GRAPH_ID",
    "name": "Exercise Graph",
    "unit": "min",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# #response
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#####POST PIXEL###################################
#create before date
day = datetime(year=2023, month=5, day=18)
# print(yesterday)
formatted_day = day.strftime("%Y%m%d")#20230525
formatted_day_question = day.strftime("%Y-%m-%d")#2023-05-25

today = datetime.now()
# print(today)#2023-05-25 20:13:10.264573

formatted_today = today.strftime("%Y%m%d")
# print(formatted_today)#20230525

pixel_config = {
    "date": formatted_day, #20230525
    "quantity": input(f"How may minutes did you do exercise {formatted_day_question}? "),
}

# pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}" #better format of endpoint

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

#####UPDATE PIXEL###################################

update_config = {
    "quantity": "25.6",
}
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

#####DELETE PIXEL###################################
# create monday
monday = datetime(year=2023, month=5, day=22)
formatted_monday = monday.strftime("%Y%m%d")
# print(formated_monday)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_monday}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)