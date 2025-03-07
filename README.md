Mr.TOG's Scribe for The Old Guard Discord Bot
my_discord_bot/
│
├── main.py              # Entry point that runs the bot
├── config.py            # Configuration settings (token, prefix, etc.)
├── bot.py               # Bot setup and core functionality
│
├── cogs/                # Command categories as extensions
│   ├── __init__.py
│   ├── admin.py         # Admin commands
│   ├── channels.py      # Channel-related commands
│   ├── utility.py       # Utility commands
│   └── ...              # Other command categories
│
├── utils/               # Utility functions and helpers
│   ├── __init__.py
│   ├── formatters.py    # Message formatting helpers
│   ├── database.py      # Database interactions
│   └── ...              # Other utilities
│
└── .env                 # Environment variables (not in git repo)