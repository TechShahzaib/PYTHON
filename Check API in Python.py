import requests

def get_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# print(get_api("https://api.github.com/users"))   
    
 print(get_api("https://65d839bac96fbb24c1baf7ac.mockapi.io/api/v1/tasks")) 