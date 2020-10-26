import discord
from datetime import datetime, timedelta
import random
from discord.ext import tasks
from discord.ext import commands
import ast
import re
import requests
#from bs4 import BeautifulSoup


bot = commands.Bot(command_prefix='$')

bot.remove_command('help')

@bot.event
async def on_voice_state_update(member, before, after):

	if before.channel != after.channel:
		now = datetime.utcnow() + timedelta(hours=9)
		alert_channel = bot.get_channel(635394005861138451)

		if before.channel is None:
			in_member = member.display_name.rstrip("[雑魚]")
			msg = now.strftime('%Y/%m/%d %H:%M:%S') + " : " + in_member + " が " +after.channel.name + " に参加しました。"
			await alert_channel.send(msg)

		elif after.channel is None:
			out_member = member.display_name.rstrip("[雑魚]")
			msg = now.strftime('%Y/%m/%d %H:%M:%S') + " : " + out_member + " が " + before.channel.name + " から退出しました。"
			await alert_channel.send(msg)

		else:
			moved_member = member.display_name.rstrip("[雑魚]")
			msg = now.strftime('%Y/%m/%d %H:%M:%S') + " : " + moved_member + " が " + before.channel.name + " から " + after.channel.name + " に移動しました。"
			await alert_channel.send(msg)


@bot.command()
async def perc(ctx):
	voice_channel = bot.get_channel(635849532894085140)
	vc_members = voice_channel.members
	l_stat = []
	if len(vc_members) == 0:
		await alert_channel.send("通話チャンネルには誰もいません。")

	else:
		for i in range(len(vc_members)):
      			l_stat.append(vc_members[i].voice.self_mute)
		sum_mute = sum(l_stat)
		sum_vc = len(l_stat)
		perc = sum_mute / sum_vc * 100
		perc_disp = round(perc, 2)
		await ctx.send("通話チャンネルのミュート率は " + str(perc_disp) + "% です。")


@bot.command()
async def m_vc(ctx):
	voice_channel = bot.get_channel(635849532894085140)
	vc_members = voice_channel.members
	num = str(len(vc_members)) + "人が通話チャンネルにいます。"
	await ctx.send(num)

@bot.command()
async def m_clan(ctx):
	zako = bot.get_guild(611163605198569475)
	clan_mem = zako.get_role(611164291193765888)
	sum_clan = len(clan_mem.members)
	msg_clan = "現在サーバー内で「クラメン」ロールを付与されているのは " + str(sum_clan) + "人 です。"
	await ctx.send(msg_clan)

"""@bot.command()
async def score(ctx, arg):
	user = arg
	r = requests.get("https://apiktracer.herokuapp.com/user/" + user)
	soup = BeautifulSoup(r.text, "html.parser")
	text = str(soup)

	try:
		start_num = [m.start() for m in re.finditer("{", text)]
		end_num = [m.start() for m in re.finditer("}", text)]
		info = text[start_num[1]:end_num[0]+1]
		info = info.replace("false", "'false'")
		info = info.replace("true", "'true'")
		dict = eval(info)
		score = dict["score"]
		await ctx.send(user + "のスコアは" + str(score) + "です。")
	
	except IndexError:
		await ctx.send("ユーザーが見つかりません。")"""

@bot.command()
async def sidkasu(ctx):
		if ctx.channel == bot.get_channel(636094557016031243):
			l_emojis = bot.emojis
			num1 = random.randrange(len(l_emojis))
			num2 = random.randrange(len(l_emojis))
			num3 = random.randrange(len(l_emojis))
			num4 = random.randrange(len(l_emojis))
			num5 = random.randrange(len(l_emojis))
			num6 = random.randrange(len(l_emojis))
			num7 = random.randrange(len(l_emojis))
			num8 = random.randrange(len(l_emojis))
			num9 = random.randrange(len(l_emojis))
			slot = str(l_emojis[num1]) + str(l_emojis[num2]) + str(l_emojis[num3]) + "\n" + str(l_emojis[num4]) + str(l_emojis[num5]) + str(l_emojis[num6]) + "\n" + str(l_emojis[num7]) + str(l_emojis[num8]) + str(l_emojis[num9]) + "\n by " + ctx.message.author.display_name.rstrip("[雑魚]")
			await ctx.send(slot)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="雑魚クラ雑用BOT", description="雑魚クラのすべて。 以下にコマンドを示します：", color=0xeee657)

    embed.add_field(name="$m_clan", value="クラメンの総数を返します。", inline=False)
    embed.add_field(name="$m_vc", value="通話チャンネルの人数を返します。", inline=False)
    embed.add_field(name="$perc", value="通話チャンネルのミュート率を返します。", inline=False)
    embed.add_field(name="$sydkasu", value="スロットチャンネルでのみ使用できます。絵文字を縦、横、または斜めに揃えたらB.Bodaにメンションしてください。", inline=False)
    embed.add_field(name="$help", value="これ。", inline=False)

    await ctx.send(embed=embed)

"""@tasks.loop(seconds=60)
async def loop():
	now = datetime.now().strftime("%M")
	if now == '55':
		ch_slot = bot.get_channel(636094557016031243)
		zako = bot.get_guild(611163605198569475)
		clan_mem = zako.get_role(611164291193765888)
		await ch_slot.set_permissions(clan_mem, send_messages=True)

	if now == '00':
		ch_slot = bot.get_channel(636094557016031243)
		zako = bot.get_guild(611163605198569475)
		clan_mem = zako.get_role(611164291193765888)
		await ch_slot.set_permissions(clan_mem, send_messages=False)"""

#loop.start()

bot.run("YOUR_TOKEN_HERE")
