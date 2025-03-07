#Bot setup and core functionality
import os
import logging
import discord
from discord.ext import commands
from config import CONFIG

logger = logging.getLogger(__name__)

class DiscordBot(commands.Bot):
    """Custom Discord bot class with additional functionality."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        """Called when the bot is ready and connected to Discord."""
        logger.info(f"Logged in as {self.user.name} (ID: {self.user.id})")
        logger.info(f"Connected to {len(self.guilds)} guilds")
        await self.change_presence(activity=discord.Game(name=f"{CONFIG.PREFIX}help"))
        
        # Print all servers and channels for reference (can be removed in production)
        for guild in self.guilds:
            logger.info(f"\nServer: {guild.name} (ID: {guild.id})")
            logger.info("Channels:")
            for channel in guild.channels:
                logger.info(f"- {channel.name} (ID: {channel.id}, Type: {channel.type})")
    
    async def on_command_error(self, ctx, error):
        """Global error handler for command errors."""
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param.name}")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad argument: {error}")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")
        else:
            logger.error(f"Command error: {error}", exc_info=error)
            await ctx.send("An error occurred while executing the command.")
    
    async def load_extensions(self):
        """Load all cogs from the cogs directory."""
        loaded_count = 0
        
        # Get all Python files in the cogs directory
        for filename in os.listdir(CONFIG.COGS_DIR):
            if filename.endswith(".py") and not filename.startswith("__"):
                extension = f"{CONFIG.COGS_DIR}.{filename[:-3]}"
                try:
                    await self.load_extension(extension)
                    logger.info(f"Loaded extension: {extension}")
                    loaded_count += 1
                except Exception as e:
                    logger.error(f"Failed to load extension {extension}: {e}", exc_info=e)
        
        logger.info(f"Loaded {loaded_count} extensions")

def create_bot() -> DiscordBot:
    """Create and configure the Discord bot instance."""
    # Set up intents - ONLY USE BASIC INTENTS UNTIL PRIVILEGED INTENTS ARE ENABLED
    intents = discord.Intents.default()
    
    # These are the privileged intents - comment them out for now
    # intents.guilds = True
    # intents.message_content = True
    
    # Create bot instance
    bot = DiscordBot(
        command_prefix=CONFIG.PREFIX,
        intents=intents,
        owner_ids=set(CONFIG.OWNER_IDS) if CONFIG.OWNER_IDS else None,
        description="A modular Discord bot"
    )
    
    return bot