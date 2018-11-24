import search


local_song_namne = search.music_name()

local = search.save_path()

def lrc_save(lyric, Name):
    '''
    文件存储至.py所在目录
    :param lyric: 歌词
    :param Name: 歌曲名
    :return: 歌词文件
    '''
    file_name = local+'\\'+Name +'.lrc'
    file = open(file_name ,'w',encoding='utf-8')
    file.write(lyric)
    file.close()
    print("歌词文件"+Name+".lrc"+"已经创建")

for name in local_song_namne:
    ID = search.gainID(name)
    Lrc1 = search.lyric_get(ID)
    lrc_save(Lrc1, name)