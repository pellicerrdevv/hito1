import requests

class APIClient:
    def __init__(self,base_url,token):
        self.base_url = base_url
        self.token = token
    
    def get(self,endpoint):
        try:
            url = self.base_url + endpoint
            response = requests.get(url, timeout = 3)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout: 
            print("Servidor no responde")
        except requests.exceptions.HTTPError: 
            print("Error 404 o 500")
        except requests.exceptions.RequestException: 
            print("Cualquier otro error dentro de red")






