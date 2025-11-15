# Discord Bot Project

## Overview
This is a Discord bot built with discord.py that responds to commands. The bot includes a Flask web server to keep it alive on hosting platforms like Replit.

## Project Structure
- `main.py` - Main Discord bot code with command handlers
- `keep_alive.py` - Flask web server that runs on port 5000 to keep the bot alive
- `requirements.txt` - Python dependencies (discord.py, flask)

## Setup
1. Python 3.11 is installed
2. Dependencies are installed via pip
3. Discord bot TOKEN is stored in Replit Secrets

## Bot Commands
- `$ping` - Bot responds with "pong!"

## Current State
- Bot uses discord.py library
- Flask server runs on port 5000
- Bot requires TOKEN environment variable to connect to Discord
- Command prefix is `$`

## Recent Changes
- November 15, 2025: Initial setup for Replit environment
  - Installed Python 3.11
  - Installed discord.py and flask packages
  - Updated Flask port from 8080 to 5000
  - Added .gitignore for Python projects
  - Created replit.md documentation
