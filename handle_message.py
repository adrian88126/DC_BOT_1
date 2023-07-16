async def handle_message(message):
    if message.content == '我好帥喔':
        # 刪除傳送者的訊息
        await message.delete()
        # 然後回傳訊息
        await message.channel.send('不好意思，不要騙人啦')
