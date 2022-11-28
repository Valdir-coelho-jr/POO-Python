# CLASSMETHOD
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.user = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    

# c1 = Connection()
c1 = Connection.create_with_auth('Luiz', '1234')
# c1.set_user('Luiz')
print(c1.user)
print(c1.password)