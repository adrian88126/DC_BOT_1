async def handle_member_join(member, channel):
    # 在這裡進行成員加入的處理
    print(f"{member.name} 加入了伺服器")
    # 在指定的頻道中發送訊息
    await channel.send(f"{member.name} 加入了伺服器！歡迎！")
async def handle_member_remove(member, channel):
    # 在這裡進行成員退出的處理
    print(f"{member.name} 退出了伺服器")
    # 在指定的頻道中發送訊息
    await channel.send(f"{member.name} 退出了伺服器！掰掰！")
