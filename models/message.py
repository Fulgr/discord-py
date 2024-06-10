messages = []

class Message:
    def __init__(self, data):
        self.type = data["type"]
        self.channel_id = data["channel_id"]
        self.content = data["content"]
        self.attachments = data["attachments"]
        self.embeds = data["embeds"]
        self.timestamp = data["timestamp"]
        self.edited_timestamp = data["edited_timestamp"]
        self.flags = data["flags"]
        self.components = data["components"]
        self.id = data["id"]
        self.author = data["author"]
        self.mentions = data["mentions"]
        self.position = data["position"]
        if data["referenced_message"]["id"] in [i.id for i in messages]:
            self.referenced_message = [i for i in messages if i.id == data["referenced_message"]["id"]][0]
        else:
            self.referenced_message = Message(data["referenced_message"])
        messages.append(self)