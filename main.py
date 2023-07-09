import requests
from datetime import datetime

USERNAME = "jdaise"
TOKEN = "ifaliq8fq8hf3q"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# post_pixel_params = {
#     "date": "20230709",
#     "quantity": "2",
# }

today = datetime(year=2023, month=7, day=8)
# print(today.strftime("%Y%m%d"))
datetime_string = today.strftime("%Y%m%d")

pixel_data = {
    "date": datetime_string,
    "quantity": "6.252",
}


# Add Pixel
# response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
# response.raise_for_status()
# print(response.text)


# Update Pixel

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime_string}"

# response = requests.put(url=put_pixel_endpoint, json=pixel_data, headers=headers)
# response.raise_for_status()
# print(response.text)


delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime_string}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
response.raise_for_status()
print(response.text)
