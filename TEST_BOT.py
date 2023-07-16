# import os
# bot_token = os.environ.get('BOT_TOKEN')
# print(bot_token)
import configparser
# 創建 ConfigParser 對象並讀取配置文件
config = configparser.ConfigParser()
config.read('config.ini')
# 獲取機器人令牌
bot_token = config.get('Bot', 'token')
# 在這裡使用機器人令牌
print(bot_token)
