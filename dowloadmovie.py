import requests
from multiprocessing import Pool

#用jx.618g.com/？url=网址来打开vip内容，就可以下载下来了
#最后在cmd中打开下载的路径将其拼接成一个完整的电影  指令：  copy /b *.ts name.mp4  就可以了

def download(i):
    url= 'https://youku.cdn1-letv.com/20180111/CxOfS5TG/800kb/hls/JHTB66451%03d.ts' % i
    print(url)
    r = requests.get(url)
    ret = r.content

    with open('./movie/{}'.format(url[-15:]),'wb') as f:    #以字节的形式写入文件夹
        f.write(ret)
if __name__== '__main__':
    pool = Pool(20)
    for i in range(1000):                                 #下载
        pool.apply_async(download,args=(i,))

    pool.close()
    pool.join()