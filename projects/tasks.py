from asgiref.sync import async_to_sync, sync_to_async
from celery import shared_task
from django.conf import settings
from django.urls import reverse
from interactions.models.discord.enums import AutoArchiveDuration

from pba_discord.bot import bot
from projects.models import ProjectApplication


async def _add_new_project_message_and_thread(project_application_id):
    application = await ProjectApplication.objects.filter(id=project_application_id).afirst()
    if application is None or application.draft or application.thread_id:
        return

    await bot.login(settings.DISCORD_BOT_TOKEN)
    guild = await bot.fetch_guild(settings.NEW_PROJECT_REVIEW_DISCORD_GUILD_ID)
    selection_channel = await guild.fetch_channel(settings.NEW_PROJECT_REVIEW_DISCORD_CHANNEL_ID)
    mention_role = await guild.fetch_role(settings.NEW_PROJECT_REVIEW_DISCORD_ROLE_MENTION_ID)
    submitter = await sync_to_async(lambda: application.submitter)()
    profile = await sync_to_async(lambda: submitter.profile)()
    discord = await sync_to_async(lambda: profile.discord)()
    discord_username = discord.extra_data["username"]
    thread = await selection_channel.create_thread(
        name=f"{application.data['shortname']['value']}",
        reason=f"Project Application submitted by {discord_username}",
        auto_archive_duration=AutoArchiveDuration.ONE_WEEK,
    )
    if not application.markdown:
        await sync_to_async(application.render_markdown)()
    msg = ""
    in_response = False
    for line in application.markdown.split("\n"):
        if line == "```":
            if in_response:
                in_response = False
            else:
                in_response = True
        if len(msg) + len(line) >= 1990:
            if in_response:
                msg += "```\n"
            await thread.send(msg)
            msg = ""
            if in_response:
                msg += "```\n"
        msg += line + "\n"
    await thread.send(msg)
    link = reverse("project_application_view", kwargs={"pk": application.id})
    link = f"https://apps.bikeaction.org{link}"
    await thread.send(
        f"{mention_role.mention} please review!\n\n"
        f"You can view the application online [here]({link}) after logging in."
    )
    application.thread_id = thread.id
    await application.asave()


@shared_task
def add_new_project_message_and_thread(project_application_id):
    async_to_sync(_add_new_project_message_and_thread)(project_application_id)
