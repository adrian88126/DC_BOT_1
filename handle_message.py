import discord
import requests
import pandas as pd
from bs4 import BeautifulSoup
async def handle_message(message):
    if message.content == '我好帥':
        # 刪除傳送者的訊息
        await message.delete()
        # 然後回傳訊息
        await message.channel.send('不要騙人')
    elif message.content == 'disp_news':
        url = "https://disp.cc/b/"
        web = requests.get('https://disp.cc/b/Joke')
        web.encoding = 'utf-8'
        soup = BeautifulSoup(web.text, 'html.parser')
        titles = soup.find_all('div', attrs={'class': 'row2'})[:12]
        records = []
        for i in titles:
            name = i.find('span', attrs={'class': 'L18'}).text[1:-2]
            title = i.find('span', attrs={'class': 'titleColor'}).text[:]
            P_date = i.find('span', attrs={'class': 'L12'})['title']
            destination_url = i.find(
                'span', attrs={'class': 'L34 nowrap listTitle'})
            destination_url = destination_url.find('a')['href']
            records.append((P_date, name, title, destination_url))
        max_records_per_embed = 6  # 每个嵌入消息中的最大记录数量
        num_embeds = (len(records) + max_records_per_embed -
                      1) // max_records_per_embed  # 计算所需的嵌入消息数量
        for i in range(num_embeds):
            embed = discord.Embed(title="Top 12 News",
                                  color=discord.Color.blue())
            start_index = i * max_records_per_embed
            end_index = min(start_index + max_records_per_embed, len(records))
            for j in range(start_index, end_index):
                record = records[j]
                embed.add_field(name="Time", value=record[0], inline=True)
                embed.add_field(name="Author", value=record[1], inline=True)
                embed.add_field(
                    name=record[2], value=f"[Click Here]({url + record[3]})", inline=False)
            remaining_fields = max_records_per_embed - \
                (end_index - start_index)
            for _ in range(remaining_fields):
                embed.add_field(name='\u200b', value='\u200b', inline=False)
                # 添加大的空白字段来增加宽度
            embed.add_field(name='\u200b', value='\u200b' * 10, inline=False)
            await message.channel.send(embed=embed)
