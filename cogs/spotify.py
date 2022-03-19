import time
import discord

from discord.ext import commands

class Spotify(commands.Cog, name="spotify"):
	"""Show Spotify songs."""
	def __init__(self, bot):
		self.bot = bot

	def help_custom(self):
		emoji = "<:spotify:880896591756656641>"
		label = "Spotify"
		description = "Spotify status commands."
		return emoji, label, description

	@commands.command(name="spotify", aliases=["sy", "sp", "spy", "spot"])
	async def actual_calendar(self, ctx, user: discord.Member = None):
		"""Show the current Spotify song."""
		keeper = True
		if not user: user = ctx.author
		for activity in user.activities:
			if str(activity) == "Spotify":
				embed, keeper = discord.Embed(colour=activity.colour), False
				embed.set_author(name="Spotify", url=f"https://open.spotify.com/track/{activity.track_id}", icon_url="https://toppng.com/uploads/thumbnail//spotify-logo-icon-transparent-icon-spotify-11553501653zkfre5mcur.png")
				embed.add_field(name=activity.title, value=activity.artist, inline=False)
				embed.set_thumbnail(url=activity.album_cover_url)
				embed.set_footer(text=f"{str(activity.duration)[2:-7]} | Requested by : {ctx.message.author.name} at {time.strftime('%H:%M:%S')}", icon_url=ctx.message.author.display_avatar.url)
				await ctx.send(embed=embed)
		if keeper: await ctx.send(f"{user.name} is not currently listening to Spotify")

def setup(bot):
	bot.add_cog(Spotify(bot))
