from discord.fetch import *
import discord.models.guild as guild
import discord.models.channel as channel

class Client:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "X-Super-Properties": "ewogICJvcyI6ICJXaW5kb3dzIiwKICAiY2xpZW50X2J1aWxkX251bWJlciI6IDE1MjQ1MAp9"
        }

    def guilds(self):
        guild.guilds = []
        data = fetch_users_me_guilds(self.headers)
        for i in data:
            guild.Guild(i)
        return guild.guilds
    
    def channels(self, guild_id):
        channel.channels = []
        data = fetch_guilds_id_channels(self.headers, guild_id)
        for i in data:
            channel.Channel(i)
        return channel.channels
    
    def messages(self, channel_id, limit=50, before=None):
        return fetch_channels_id_messages(self.headers, channel_id, limit, before)