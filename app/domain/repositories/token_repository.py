from utils.uuii import UniqueId
from db.driver import psql_driver
from domain.entities.token import Token

COLLECTION_NAME = 'token'

class TokenRepository:
    
    def __init__(self):
        self.driver = psql_driver()

    def get_token(self):
        token_data = self.driver.get_token(COLLECTION_NAME)
        if token_data is not None:
            return Token.list_to_json(token_data)
        else:
            return None

    def create_token(self, token):
        token_data = token.to_dict()
        token_response = self.driver.create(COLLECTION_NAME, token_data.keys(), list(token_data.values()))
        response = {
            "response" : token_response
        }
        return response
    
    def update_token(self, token):
        token_data = token.to_dict()
        token_info = {
            "token_key": token_data['tokenKey'],
            "expires_in": token_data['expiresIn']
        }
        self.driver.update(
            COLLECTION_NAME,
            token_info.keys(),
            list(token_info.values()),
            condition="",
        )
        return token_data