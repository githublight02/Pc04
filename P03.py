import requests
url = 'https://images.unsplash.com/photo-1605725657590-b2cf0d31b1a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80'
response = requests.get(url)

with open('pastor.jpg', 'wb') as f:
    f.write(response.content)
    pass