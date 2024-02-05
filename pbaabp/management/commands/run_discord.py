import os

from django.core.management.base import BaseCommand

from discord.bot import bot


class Command(BaseCommand):
    help = "Run the PBA Discord bot"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting discord bot..."))
        discord_token = os.environ.get("DISCORD_BOT_TOKEN", "")
        bot.run(discord_token)
