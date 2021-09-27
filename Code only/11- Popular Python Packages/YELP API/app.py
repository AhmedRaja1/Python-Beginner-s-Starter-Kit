import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "MnpPjs3wKcUvsqk96-BZOtMFIprPSRB3C6kx1SvpT3_IPduIfjXf9Y9rs1z-2QzNkF4q8JY7lJa7Ff_iwF69jZX4xPP86-G6yCJFq3N-0dB1oXgxXoOAZDdbbKq0YHYx"
headers = {
    "authorization": "Bearer " + api_key
}
params = {
    "location": "San Francisco",
    "term": "Hotel"
}
response = requests.get(url=url, headers=headers, params=params)
businesses = (response.json())["businesses"]
print(businesses)
