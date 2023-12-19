import requests

class RequestDriver():
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, method, path, data=None, headers=None, params=None):
        try:
            url = self.base_url + path
            response = requests.request(method, url, data=data, headers=headers, params=params)

            # Si la respuesta es exitosa (código 2xx)
            response.raise_for_status()

            return response.json() if response.headers.get("Content-Type") == "application/json" else response.text

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud {method} {url}: {e}")
            return None

    def get(self, path, params=None, headers=None):
        return self.make_request("GET", path, params=params, headers=headers)

    def post(self, path, data=None, headers=None, params=None):
        return self.make_request("POST", path, data=data, headers=headers, params=params)

# # Ejemplo de uso
# base_url = "https://api.example.com"
# my_driver = RequestDriver(base_url)

# # Realizar una solicitud GET
# get_response = my_driver.get("/endpoint", params={"param1": "value1"}, headers={"Authorization": "Bearer token"})
# print(get_response)

# # Realizar una solicitud POST
# post_response = my_driver.post("/endpoint", data={"key": "value"}, headers={"Content-Type": "application/json"})
# print(post_response)
