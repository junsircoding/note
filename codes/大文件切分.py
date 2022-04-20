"""
大型文本文件分割, 文件逐行读取, 文件逐行追加写入
1. 从练习目录中获取 zhwiki-20210720-pages-json 文件
2. 将文件以行为单位分割成2GB一个的文件序列
    a) 写个简单的脚本, 循环逐行读取文件内容 (不要逐支字符读取)
    b) 目标文件命名规范: [原始文件名]_[数字序列符号]_[程序启动时间时分秒].json
    c) 每读一行就往目标文件里追加写一行
    d) 计数统计目标文件已写入的总字节数
    e) 如果写入字节数超过了 2GB, 就重新生成写一个目标文件, 继续写入
"""
import os
import time


# SUB_BYTE_SIZE = 2000000000  # 2GB
SUB_BYTE_SIZE = 20  # 2GB
filename = 'zhwiki-20210720-pages-json'

with open(filename, "rb") as fin:
    sub_file_num = 1 # 子文件编号
    sub_filename = f'{filename}_{sub_file_num}_{time.strftime("%H%M%S", time.localtime())}.json'
    fout = open(sub_filename, "wb")
    for line in fin:
        fout.write(line)
        # 当前子文件字节数
        current_size = os.path.getsize(sub_filename)
        if current_size >= SUB_BYTE_SIZE: # 子文件大小达到2GB就拆分
            sub_file_num = sub_file_num + 1
            fout.close()
            sub_filename = f'{filename}_{sub_file_num}_{time.strftime("%H%M%S", time.localtime())}.json'
            fout = open(sub_filename, "wb")
    fout.close()
