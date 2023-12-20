from datetime import datetime

class Token():

    def __init__(self, tokenKey=None, expiresIn=None) -> None:
        self.tokenKey = tokenKey
        self.expiresIn = expiresIn

    @classmethod
    def from_dict(cls, data):
        return cls(
            tokenKey=data.get('tokenKey'),
            expiresIn=data.get('expiresIn')
        )

    def to_dict(self):
        return {
            'tokenKey': self.tokenKey,
            'expiresIn': self.expiresIn.isoformat() if self.expiresIn else None,
        }
    
    @staticmethod
    def list_to_json(values):
        token = Token()
        token.tokenKey = values[0]
        token.expiresIn = values[1]
        return token

    def update_token(self, item):
        # Update attributes with values from 'item' if provided, otherwise retain existing values
        self.tokenKey = item.tokenKey if item.tokenKey else self.tokenKey
        self.expiresIn = item.expiresIn if item.expiresIn else self.expiresIn

        return self
