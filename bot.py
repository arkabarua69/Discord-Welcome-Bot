import discord
from discord.ext import commands
from discord import PartialEmoji
import os

# ----- Bot Token and Channel -----
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# ----- Intents -----
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


# ----- Welcome Buttons -----
class WelcomeButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        youtube_emoji = PartialEmoji(name="youtube", id=1162772349993635911)
        self.add_item(
            discord.ui.Button(
                label="YouTube Channel",
                emoji=youtube_emoji,
                style=discord.ButtonStyle.link,
                url="https://www.youtube.com/@mac_GunJon",
            )
        )

        tiktok_emoji = PartialEmoji(name="tiktok", id=1162772344973049876)
        self.add_item(
            discord.ui.Button(
                label="Follow on TikTok",
                emoji=tiktok_emoji,
                style=discord.ButtonStyle.link,
                url="https://www.tiktok.com/@mac_gunjon",
            )
        )


# ----- Bot Events -----
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    guild = member.guild
    member_count = guild.member_count

    embed = discord.Embed(
        title="Mac GunJon Gaming",
        description=(
            f"Welcome {member.mention} to the **𝐌𝐀𝐂 𝐆𝐔𝐍𝐉𝐎𝐍 𝐆𝐀𝐌𝐈𝐍𝐆 Community!** 🎉\n\n"
            f"You're our **{member_count}ᵗʰ** member.\n"
            f"Thanks for being part of the squad!"
        ),
        color=discord.Color.blue(),
    )
    embed.set_thumbnail(url=member.display_avatar.url)

    # Channel mentions
    embed.add_field(name="⚡ Welcome", value="<#1417049467290386523>", inline=False)
    embed.add_field(
        name="📢 Announcements", value="<#1417049475335065794>", inline=False
    )
    embed.add_field(name="📜 Rules", value="<#1417049470943625256>", inline=False)
    embed.add_field(name="🔥 Chat", value="<#1417049495434428467>", inline=False)

    # GIF
    embed.set_image(
        url="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnJneXB4aWZ4azJkeWQ5MnRndDMwZGVwZDFyM3lzN3V2Y3dsOHFkNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZoGstMtBFzRqJhZ3w8/giphy.gif"
    )
    embed.set_footer(text="Made With Love BY - Mac GunJon")

    # Send embed + buttons
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(embed=embed, view=WelcomeButtons())


# ----- Run Bot -----
bot.run(TOKEN)
