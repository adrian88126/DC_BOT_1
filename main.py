import discord
import os
from discord.ext import commands
import configparser
from handle_message import handle_message
from member_handler import handle_member_join, handle_member_remove
# 初始化 channel_id 變數
channel_id = 1129987994590396468
# 創建 Discord Intents 物件並設定預設值
intents = discord.Intents.default()
# 開啟接收訊息內容的功能
intents.message_content = True
# 關閉接收「正在輸入」事件的通知
intents.typing = False
# 關閉接收其他用戶狀態更新的通知
intents.presences = False
# 啟用觀察成員列表的更改
intents.members = True
# 創建 Discord 機器人實例
bot = commands.Bot(command_prefix="[", intents=intents)
# @bot.event 是 Discord.py 中用於註冊事件處理函式的裝飾器（Decorator），讓你能夠以非同步的方式對 Discord 中的特定事件作出反應。
@bot.event
async def on_ready():
    print(">> bot online >>")
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(">> bot online")
        print('目前登入身份：', bot.user)
        game = discord.Game('Im py robot')
        # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
        await bot.change_presence(status=discord.Status.online, activity=game)
    else:
        print(f"找不到 ID 為 {channel_id} 的頻道")
@bot.command()  # 添加關閉機器人的指令
async def shutdown(ctx):
    print("收到關閉指令")
    await ctx.send("關閉機器人...")
    await bot.close()
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(channel_id)  # 獲取指定的頻道
    await handle_member_join(member, channel)  # 呼叫外部程式的成員加入處理函式並傳遞頻道參數
@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(channel_id)  # 獲取指定的頻道
    await handle_member_remove(member, channel)  # 呼叫外部程式的成員退出處理函式並傳遞頻道參數
@bot.command()
@bot.event
async def on_message(message):
    await handle_message(message)  # 呼叫外部程式的訊息處理函式
async def ping(ctx):
    print("bot.latency")
    await ctx.send(bot.latency)
# 創建 ConfigParser 對象並讀取配置文件
config = configparser.ConfigParser()
config.read('config.ini')
# 獲取機器人令牌
bot_token = config.get('Bot', 'token')
# 在這裡使用機器人令牌
bot.run(bot_token)
