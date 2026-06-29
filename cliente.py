import requests

class APIClient:
    def __init__(self,base_url,token):
        self.base_url = base_url
        self.token = token
    
    def get(self,endpoint):
        try:
            url = self.base_url + endpoint
            response = requests.get(
                url,
                headers = {"Authorization": f"Bearer {self.token}"},
                timeout = 3)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout: 
            print("Timeout : Servidor no respondió en 3 segundos")
        except requests.exceptions.HTTPError as e: 
            print(f"Error HTTP {response.status_code} : {e}")
        except requests.exceptions.RequestException: 
            print(f"Error de red: {e}")






