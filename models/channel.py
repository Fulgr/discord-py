from discord.models.permission_overwrite import PermissionOverwrite

channels = []

class Channel:
    def __init__(self, data):
        if data["id"] in [i.id for i in channels]:
            return
        self.id = data["id"]
        self.type = data["type"]
        self.flags = data["flags"]
        self.guild_id = data["guild_id"]
        self.name = data["name"]
        self.parent_id = data["parent_id"]
        self.position = data["position"]
        self.permission_overwrites = []
        for i in data["permission_overwrites"]:
            self.permission_overwrites.append(PermissionOverwrite(i))
        channels.append(self)