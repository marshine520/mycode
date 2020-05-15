
'''
author :zhangchao
date :20180503

'''

def getscreencap(filename,path):
    '''
    :param filename: 保存图片文件名
    :param path:图片保存路径
    :return:
    '''
    import subprocess
    import time
    begin = time.time()
    if not os.path.splitext(filename)[1]=='.jpg':
        filename= os.path.splitext(filename)[0]+'.jpg'
    pi = subprocess.Popen(
        "adb shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1920x1080@1920x1080/0 -s >/data/local/tmp/{}".format(filename),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in pi.stdout.readlines():
        # print(i.strip().decode('utf-8'))
        if 'Using' in line.strip().decode('utf-8'):
            p2 = subprocess.Popen("adb pull /data/local/tmp/{} {}".format(filename,path),
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line2 in p2.stdout.readlines():
                if 'pulled' in line2.strip().decode('utf-8'):
                    subprocess.Popen("adb shell rm /data/local/tmp/{}".format(filename), stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
                    end = time.time()
                    totaltime=end - begin
                    time1=str(totaltime)
                    print('截图完成，图片存储路径为 {}'.format(path))
            # break
if __name__ == '__main__':
    import os
    filename = input("请输入文件名:")
    path=os.getcwd()
    getscreencap(filename.strip(),path)
    pass