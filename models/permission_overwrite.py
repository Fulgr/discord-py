permission_overwrites = []

class PermissionOverwrite:
    def __init__(self, data):
        self.id = data["id"]
        self.type = data["type"]
        self.allow = data["allow"]
        self.deny = data["deny"]
        permission_overwrites.append(self)