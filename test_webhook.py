import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "https://abdullaht2004.app.n8n.cloud/webhook-test/63abfc0b-e28e-43b9-815e-ba251bf43971"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])