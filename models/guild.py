import discord.fetch as fetch

guilds = []

class Guild:
    def __init__(self, data):
        if data["id"] in [i.id for i in guilds]:
            return
        self.id = data["id"]
        self.name = data["name"]
        self.icon = data["icon"]
        self.owner = data["owner"]
        self.permissions = data["permissions"]
        self.features = data["features"]
        guilds.append(self)

    def channels(self, client):
        return client.channels(self.id)