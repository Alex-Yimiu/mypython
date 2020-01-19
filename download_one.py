import requests

url = 'https://52dy.hanju2017.com/20170610/Gjm6BXKH/hls/TTO8XK5326002.ts'
print(url)
r = requests.get(url)
ret = r.content

with open('./movie/{}'.format(url[-10:]), 'wb') as f:  # 以字节的形式写入文件夹
    f.write(ret)