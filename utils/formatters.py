#Utility functions for formatting messages and embeds
import discord
from datetime import datetime

def create_embed(title=None, description=None, color=None, footer=None, timestamp=True):
    """Create a standardized Discord embed.
    
    Args:
        title (str, optional): Embed title
        description (str, optional): Embed description
        color (discord.Color, optional): Embed color
        footer (str, optional): Footer text
        timestamp (bool, optional): Whether to add current timestamp
        
    Returns:
        discord.Embed: The created embed
    """
    embed = discord.Embed(
        title=title,
        description=description,
        color=color or discord.Color.blurple()
    )
    
    if timestamp:
        embed.timestamp = datetime.utcnow()
    
    if footer:
        embed.set_footer(text=footer)
    
    return embed

def format_channel_list(channels, show_ids=True, group_by_category=True):
    """Format a list of channels into a readable string.
    
    Args:
        channels (list): List of discord.Channel objects
        show_ids (bool): Whether to include channel IDs
        group_by_category (bool): Whether to group channels by category
        
    Returns:
        str: Formatted channel list
    """
    if not group_by_category:
        result = []
        for channel in channels:
            if show_ids:
                result.append(f"{channel.name}: {channel.id}")
            else:
                result.append(channel.name)
        return "\n".join(result)
    
    # Group by category
    categories = {}
    for channel in channels:
        category_name = str(channel.category) if channel.category else "No Category"
        if category_name not in categories:
            categories[category_name] = []
        categories[category_name].append(channel)
    
    result = []
    for category, channel_list in categories.items():
        result.append(f"== {category} ==")
        for channel in channel_list:
            if show_ids:
                result.append(f"  {channel.name}: {channel.id}")
            else:
                result.append(f"  {channel.name}")
        result.append("")  # Empty line between categories
    
    return "\n".join(result)