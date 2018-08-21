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
    students[id] = {'name': '', 'id': '', 'score': ''}
    students[id]['name'] = input('请输入学生姓名\n')
    students[id]['id'] = id
    students[id]['score'] = input('请输入学生成绩\n')
    fun_choose()

#检索学生信息

def find_name():
    id = input('请输入您要查找的学生编号\n')
    print(students[id])
    fun_choose()

#删除学生信息

def delete_name():
    print(students)
    id = input('请输入您要删除的学生编号\n')
    students.pop(id)
    fun_choose()

#功能选择

def fun_choose():
    i = input('1）查找学生信息\n2）删除学生信息\n3）增加学生信息\n4）查看表格\n')
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