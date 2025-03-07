#Configuration setting for the bot
import os
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@dataclass
class Config:
    """Bot configuration settings."""
    TOKEN: str = os.getenv("DISCORD_TOKEN", "")
    PREFIX: str = os.getenv("COMMAND_PREFIX", "!")
    COGS_DIR: str = "cogs"
    OWNER_IDS: List[int] = None  # List of owner user IDs
    
    def __post_init__(self):
        # Convert string of IDs to list of integers
        owner_ids = os.getenv("OWNER_IDS", "")
        self.OWNER_IDS = [int(id.strip()) for id in owner_ids.split(",") if id.strip()] if owner_ids else []
        
        # Validate configuration
        if not self.TOKEN:
            raise ValueError("Discord token not found. Set the DISCORD_TOKEN environment variable.")

# Create a global configuration instance
CONFIG = Config()