#Channel relation commands
import logging
import discord
from discord.ext import commands
from utils.formatters import create_embed

logger = logging.getLogger(__name__)

class ChannelsCog(commands.Cog, name="Channels"):
    """Commands for working with Discord channels."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="channels")
    async def list_channels(self, ctx):
        """List all channels in the current server with their IDs."""
        embed = create_embed(
            title=f"Channels in {ctx.guild.name}",
            color=discord.Color.blue()
        )
        
        # Group channels by category
        categories = {}
        for channel in ctx.guild.channels:
            category_name = str(channel.category) if channel.category else "No Category"
            if category_name not in categories:
                categories[category_name] = []
            categories[category_name].append(channel)
        
        # Add fields for each category
        for category, channels in categories.items():
            channel_list = "\n".join([f"{channel.name}: {channel.id}" for channel in channels 
                                     if not isinstance(channel, discord.CategoryChannel)])
            if channel_list:  # Only add non-empty categories
                embed.add_field(name=category, value=channel_list, inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name="channel_info")
    async def channel_info(self, ctx, channel_id: int = None):
        """Get detailed information about a specific channel."""
        # If no channel ID provided, use the current channel
        channel = ctx.channel
        if channel_id:
            channel = ctx.guild.get_channel(channel_id)
            if not channel:
                await ctx.send(f"Channel with ID {channel_id} not found.")
                return
        
        embed = create_embed(
            title=f"Channel Information: {channel.name}",
            color=discord.Color.green()
        )
        
        # Add basic information
        embed.add_field(name="ID", value=channel.id, inline=True)
        embed.add_field(name="Type", value=channel.type, inline=True)
        embed.add_field(name="Category", value=channel.category or "None", inline=True)
        
        # Add permissions if text channel
        if isinstance(channel, discord.TextChannel):
            embed.add_field(name="Topic", value=channel.topic or "No topic set", inline=False)
            embed.add_field(name="Slowmode Delay", value=f"{channel.slowmode_delay} seconds", inline=True)
            embed.add_field(name="NSFW", value=channel.is_nsfw(), inline=True)
            embed.add_field(name="News Channel", value=channel.is_news(), inline=True)
        
        await ctx.send(embed=embed)

# This is the setup function that discord.py expects
async def setup(bot):
    """Add the cog to the bot."""
    await bot.add_cog(ChannelsCog(bot))