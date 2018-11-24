import requests
import re
import tkinter as tk
from tkinter import filedialog    #窗口选取文件
import os
import json

'''
搜索歌曲API：
请求方式：post
请求地址：http://music.163.com/api/search/get/web?csrf_token=
请求数据：hlpretag=&hlposttag=&s=搜索歌曲名或歌手名&type=1&offset=0&total=true&limit=返回数据条数
请求头部：（仅供参考）数组形式
'Host: music.163.com',
返回数据：json数据格式

作者：Beck766
链接：https://www.jianshu.com/p/ccc81aa2b743
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
https://music.163.com/#/search/m/?s=fairy%20stage%20K2%20SOUND&type=1
'''#搜索歌曲API

'''
POST https://music.163.com/weapi/search/suggest/web?csrf_token= HTTP/1.1
Host: music.163.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://music.163.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 440
Connection: keep-alive
Cookie: JSESSIONID-WYYY=ORvP7xwUYXZZ5N4wzB6QYf9Hik0ssynFfuZPTJtaVjd%2FgmXx4isZ8VAvvv7BgTO1MuGtn6iUEDCu86bUVMvmTjX8%5Cn5yISAikV7CzUId0ryFogBVW8upT23R%2FkS1OZwJzdy0m8d9xdV5or9NwXZ8EgBjnREhccy%2F1knCumWPaBp%2FuQG%2B%3A1542994299908; _iuqxldmzr_=32; _ntes_nnid=4fecedf7b164cf3adfe5e6078b649778,1542870959532; _ntes_nuid=4fecedf7b164cf3adfe5e6078b649778; __utma=94650624.1287725957.1542870961.1542990727.1542993077.8; __utmz=94650624.1542953218.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=pN9VLRt%2FFjcCgVD%2Frdn1MWfyWUjGGfxEEa%2FvteQSa0b4ecYfA%2FHwDwi4icGi6P%2BEqJB5yWYo3iSN6kHm%2BPc4FtGQFi3D9V9Mz%2BbXFarVbwNGRuIaJrcPGLAP6NqFgAMyNXE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea2ce65ace7818af16d90868fb2d54e878a8baaf26ea5abe5b5e145a388899bf32af0fea7c3b92ab492f7b7cf5ab8f18a8be249a58a8cd0f170aeef83b8e573958ba6a8c66ebc9b8b82ae7eb8bb9fb4e43ca2ecab84dc6e83f18898c77dabeca784c663f690e5a6f44282ebb7b8dc65f1b79dafb5618cb3e5b1e24086ac89b2c563f19cf7b7bc47baf5aeb9c56bb28aae98cd4d92ab8782c97aa19089adc45cf692bfa7e64b8fa782b9c837e2a3; WM_TID=qAXyLHY1CB5EABAQFVZ8b0%2BINCzXbbE0; hb_MA-8EA5-1B4E54656795_source=www.baidu.com; __root_domain_v=.163.com; _qddaz=QD.oq3zpx.fuhvnm.jotpo1kp; __utmc=94650624; __utmb=94650624.3.10.1542993077

params=PppOWjiopGvjghmwwPS3vtswKzJcBA76aJKh%2B%2FicirROyVm5PfxsdkZ9Z36RL6rDucF699oWpGToVDS9DL0dP6MS0iRevH9wjD%2F1pwPvBRzSglO%2BeaK1nCW3KtSfi4D%2B2RpzLi45BOjmI8gDGW3P4A%3D%3D&encSecKey=cbcc2fe566c0f56aec13da1c9bb66ab34405615f5d78f053eac2d534f656f4f6d4332c640fbbb7b362813cbf20a0a8cb500cacef60847dae1e8d9cf9c59fa176ce32a8bb9d15db52f947c4156009173d96a5d0b86aaba3058855e222fa51373edc92e75cf6a79ba1f46ede643c599d6fa1304edba2f7d6dae8d4bdecbc9ea97c
'''#网页抓包Raw

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    'Host: music.163.com'
         }


def gainID(Name):
    '''

    :param Name: 搜索歌曲的名字，由music_name（）获得
    :return: 搜索到的歌曲ID
    '''
    search_url = r'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s=' + Name + '&type=1&offset=0&total=true&limit=1'
    search_temp = requests.post(search_url,headers=headers).text
    id_search = re.search("\"id\":.+?\,",search_temp)
    search_id_save = id_search.group()[5:-1]
    return search_id_save

def music_name():
    '''
    获取文件绝对路径
    获取文件名
    去除后缀
    :return:以列表返回文件名
    '''
    music_file_path= open_path()

    Music_Name = []

    for path in music_file_path:
        name_get = os.path.basename(path)
        name_split = name_get.split('.')[0]
        print(name_split)
        Music_Name.append(name_split)
    return Music_Name

def lyric_get(ID):
    '''

    :param ID: 歌曲ID
    :return: 歌词
    '''

    url = 'http://music.163.com/api/song/lyric?id=' + ID + '&lv=1&kv=1&tv=-1'
    r = requests.get(url)
    json_obj = r.text  # text作用
    j = json.loads(json_obj)
    if 'nolyric' in j:
        return '纯音乐，无歌词'
    else:
        temp = j['lrc']['lyric']
        return temp

def open_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilenames(title='选择歌曲文件')
    return file_path

def save_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory(title='选择歌词保存文件夹')
    return file_path
