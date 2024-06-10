from discord.fetch import *

class Client:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "X-Super-Properties": "ewogICJvcyI6ICJXaW5kb3dzIiwKICAiY2xpZW50X2J1aWxkX251bWJlciI6IDE1MjQ1MAp9"
        }

    def guilds(self):
        return fetch_users_me_guilds(self.headers)
    
    def channels(self, guild_id):
        return fetch_guilds_id_channels(self.headers, guild_id)
    
    def messages(self, channel_id, limit=50, before=None):
        return fetch_channels_id_messages(self.headers, channel_id, limit, before)