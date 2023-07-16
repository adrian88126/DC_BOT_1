import discord
import os
from discord.ext import commands
import configparser
from member_handler import handle_member_join, handle_member_remove
# 創建 Discord Intents 物件並設定預設值
intents = discord.Intents.default()
# 關閉接收「正在輸入」事件的通知
intents.typing = False
# 關閉接收其他用戶狀態更新的通知
intents.presences = False
# 創建 Discord 機器人實例
bot = commands.Bot(command_prefix="[", intents=intents)
# @bot.event 是 Discord.py 中用於註冊事件處理函式的裝飾器（Decorator），讓你能夠以非同步的方式對 Discord 中的特定事件作出反應。
@bot.event
async def on_ready():
    print(">> bot online >>")
@bot.event
async def on_member_join(member):
    handle_member_join(member)  # 呼叫成員加入處理副程式
@bot.event
async def on_member_remove(member):
    handle_member_remove(member)  # 呼叫成員退出處理副程式
# 創建 ConfigParser 對象並讀取配置文件
config = configparser.ConfigParser()
config.read('config.ini')
# 獲取機器人令牌
bot_token = config.get('Bot', 'token')
# 在這裡使用機器人令牌
print(bot_token)
bot.run(bot_token)
