# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (Xself, Xcls)

# METHOD
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.user = password

    # OBS: TODAS AS VEZES QUE EU PRECISO USAR ALGUMA COISA DE SELF, O MÉTODO SEMPRE SERÁ UMA INSTÂNCIA

c1 = Connection()
c1.set_user('Luiz')
c1.set_password('123')
print(c1.user)
