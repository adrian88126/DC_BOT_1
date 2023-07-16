import requests
import pandas as pd
from bs4 import BeautifulSoup
import discord
async def call_bug(ctx):
    # 以下皆捨棄
    '''
    channel_id = ctx.channel.id
    channel = ctx.guild.get_channel(channel_id)
    # from tabulate import tabulate
    url = "https://disp.cc/b/"
    web = requests.get('https://disp.cc/b/Joke')
    web.encoding = 'utf-8'
    soup = BeautifulSoup(web.text, 'html.parser')
    titles = soup.find_all('div', attrs={'class': 'row2'})
    records = []
    for i in titles:
        name = i.find('span', attrs={'class': 'L18'}).text[1:-2]
        title = i.find('span', attrs={'class': 'titleColor'}).text[:]
        popularity = i.find('span', attrs={'class': 'R0 bgB'}).text
        P_date = i.find('span', attrs={'class': 'L12'})['title']
        # print(P_date)
        # title
        destination_url = i.find(
            'span', attrs={'class': 'L34 nowrap listTitle'})
        destination_url = destination_url.find('a')['href']
        destination_url = url + destination_url
        records.append((P_date, name, title, popularity, destination_url))
    # pd.set_option('max_rows', None) # 显示最多行数
    # pd.set_option('max_columns', None) # 显示最多列数
    pd.set_option('expand_frame_repr', False)  # 当列太多时显示不清楚
    # pd.set_option('display.unicode.east_asian_width', False) #设置输出右对齐
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    df = pd.DataFrame(records, columns=['時間', '作者', '標題', '人氣', '網址'])
    # 將 DataFrame 轉換為文字格式
    table_str = df.to_string(index=False)
    # 在 Discord 頻道中發送 DataFrame 文字
    await ctx.send("```\n" + table_str + "\n```")
    '''
