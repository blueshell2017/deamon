#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys

# 初始化进程名称和命令路径

# 使用参数方式传递程序名称和程序路径
# p_name = sys.argv[1]
# p_path = sys.argv[2]

# Linux
# p_name = ""
# p_path = ""


# Windows
p_name = "TeamViewer.exe"
p_path = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"


# Linux平台调用ps命令/Win平台调用tasklist命令，判断进程是否存在，传入进程名称，返回为查询得到的进程个数
def process_exit(process_name):
    # Linux
    # p_checkresp = os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines()

    # Windows，为避免进程名称被截断，输出格式为csv，使用tasklist /fo csv
    p_checkresp = os.popen('tasklist /fo csv | find "' + process_name + '"').readlines()
    return len(p_checkresp)


# Linx平台调用os.system方法启动命令/Win平台调用os.startfile方法启动命令，传入命令路径，无返回值
def process_exec(process_path):
    # 将工作目录切换到启动脚本所在目录，解决部分进程启动时依赖工作目录问题
    os.chdir(os.path.dirname(process_path))

    # Linux
    #os.system(process_path)

    # Windows
    os.startfile(process_path)


# 主函数
if __name__ == '__main__':

    # 查询进程个数大于1，返回0，不做任何操作，退出
    if process_exit(p_name) >= 1:
        print(0)
        sys.exit(0)

    # 查询进程个数等于0
    elif process_exit(p_name) == 0:
        # 执行启动命令
        process_exec(p_path)
        # 查询进程个数大于1，返回1，启动成功，退出
        if process_exit(p_name) >= 1:
            print(1)
            sys.exit(0)
        # 启动失败，返回2，退出
        else:
            print(2)
            sys.exit(0)

    # 其他问题，返回2，退出
    else:
        print(2)
        sys.exit(0)