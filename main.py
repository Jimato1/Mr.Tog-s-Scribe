#Entry point for the discord bot

import asyncio
import logging
import os
from bot import create_bot
from config import CONFIG

# Set up logging - Console only for now
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # Only use console logging to avoid permission issues
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def main():
    """Main async entry point for the bot."""
    bot = create_bot()
    
    # Load all cogs
    logger.info("Loading cogs...")
    await bot.load_extensions()
    
    # Start the bot
    logger.info("Starting bot...")
    try:
        await bot.start(CONFIG.TOKEN)
    except Exception as e:
        logger.error(f"Error starting bot: {e}", exc_info=e)
    finally:
        if not bot.is_closed():
            await bot.close()

if __name__ == "__main__":
    # Check if TOKEN is set
    if not CONFIG.TOKEN:
        logger.error("No token provided. Set the DISCORD_TOKEN environment variable.")
        exit(1)
        
    logger.info("Initializing bot...")
    asyncio.run(main())