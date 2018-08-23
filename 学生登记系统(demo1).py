#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:23:07 2018
学生登记系统，可实现以下功能
1）查找学生信息
2）删除学生信息
3）增加学生信息
4）查看表格
@author: Lancelot
"""
#学生信息添加

def add_name():
    id = input("请输入您要添加的学生编号\n")
    #若原始表格中包含将要输入的id，输出提示消息，并可选择重新录入还是覆盖
    if id in students:
        print("您已添加过此学生:",students[id])
        flag = input('是否重新登记（y/n）')
        #覆盖记录
        if flag == 'y' : 
            students[id] = {'name': '', 'id': '', 'score': ''}
            students[id]['name'] = input('请输入学生姓名\n')
            students[id]['id'] = id
            students[id]['score'] = input('请输入学生成绩\n')
            print('您已成功添加学生信息： ',students[id])
            fun_choose()
       #重新录入信息
        else :
            add_name()
    #正确输入id
    else:
        students[id] = {'name': '', 'id': '', 'score': ''}
        students[id]['name'] = input('请输入学生姓名\n')
        students[id]['id'] = id
        students[id]['score'] = input('请输入学生成绩\n')
        print('您已成功添加学生信息： ',students[id])
        fun_choose()

#检索学生信息

def find_name():
    try:
        id = input('请输入您要查找的学生编号: ')
        print(students[id])
        fun_choose()
    except BaseException:#排除错误输入类型
        print('您输入的类型有误，或表格中没有该条信息，表格中的数据为：', students)
        find_name()
#删除学生信息

def delete_name():
    print(students)
    try:
        id = input('请输入您要删除的学生编号: ')
        print('您已成功删除学生信息：',students[id])
        flag = input('是否需要撤销(y/n)')#防误删
        if flag != 'y':
            students.pop(id)
        fun_choose()
    except BaseException:#排除错误输入类型
         print('输入有误，请重新输入')
         delete_name()
        
#功能选择

def fun_choose():
    i = input('-------------------\n1）查找学生信息\n2）删除学生信息\n3）增加学生信息\n4）查看表格\n-------------------')
    if i == '1' or i == '2' or i == '3' or i =='4':
        if i == '1':
            find_name()
        elif i == '2':
            delete_name()
        elif i == '3':
            add_name()
        elif i == '4':
            print(students)
            fun_choose()
    else:
        print("输入信息有误，请不要输入1,2,3以外的数字\n")
        fun_choose()

#运行程序

print('\n欢迎光临本系统，请选择你要做的事情\n')        
students = {'1':{'name': 'lily', 'id': 1, 'score': 67}}#初始化示例数据
fun_choose()