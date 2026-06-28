class usermanager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("username already exists.")
        else:
            self.users[username] = email

    def get_user(self, username):
        return self.users.get(username)


print("This is a basic function.")
# user_manager = usermanager()
# user_manager.add_user("jane_doe", "jane@example.com")
# user_manager.add_user("jane_doe", "jane@example.com")
