"""迁移当前目录下的所有MP3到指定目录"""
import os
import threading
from gevent import monkey

monkey.patch_all()


def open_and_write(mp3_name):
    # 迁移ing
    global path
    with open('./' + mp3_name, 'rb') as f:
        data = f.read()
    with open(path + mp3_name, 'wb') as f:
        f.write(data)


def handler(mp3_name):
    # 以线程进行迁移
    threading.Thread(target=open_and_write, args=(mp3_name,)).start()
    # 返回处理结果
    return mp3_name + '完成迁移'


def migrate(mp3_list):
    # 对每个文件进行处理并打印处理结果
    for i in map(handler, mp3_list):
        print(i)


def find_mp3():
    # 改变工作目录到工程文件夹所在的目录
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    # 获取所有mp3后缀的文件名
    mp3_list = [x for x in os.listdir('./') if x.endswith('.mp3')]
    # 返回结果
    return mp3_list


def main():
    # 获取文件名
    mp3_list = find_mp3()
    # 进行迁移
    migrate(mp3_list)


if __name__ == '__main__':
    # 指定迁移路径,以 / 结尾
    path = 'C:/Users/Maifeel/Music/'
    main()
