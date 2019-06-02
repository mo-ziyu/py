def meun():
    print('''*************************************************************************
*                               1.录入学生信息和成绩                    *
*                                                                       *
*                               2.显示学生信息                          *
*                                                                       *
*                               3.修改学生信息                          *
*                                                                       *
*                               4.查询学生信息                          *
*                                                                       *
*                               5.插入学生                              *
*                                                                       *
*                               6.删除学生                              *
*                                                                       *
*                               7.退出                                  *
*                                                                       *
*                       数字对应功能选择，请选1-8                       *
*                                                                       *
*************************************************************************
''')

def CreatLList():
    L = []
    num = int(input("请输入学生人数："))
    i = 1
    while True:
        if i > num:
            break
        n = input("请输入名字：")
        a = input("请输入年龄：")
        s = input("请输入成绩：")
        info = {"name":n,"age":a,"score":s}
        i = i + 1
        L.append(info)
    print("学生信息录入完毕！！！")
    return L

def OutputLList(student_info):
    for info in student_info:
        print("/***************************/")
        print("姓名：",info.get("name"))
        print("年龄：",info.get("age"))
        print("成绩：",info.get("score"))

def FindLList(student_info):
    flag = 0
    Find_name = input("请输入查找的学生姓名")
    for info in student_info:
        if Find_name == info.get("name"):
            print("/***************************/")
            print("姓名：",info.get("name"))
            print("年龄：",info.get("age"))
            print("成绩：",info.get("score"))
            flag = 1
    if flag == 0:
        print("没有该学生")

def ModifyOne(student_info):
    mod_name = input("请输入修改的学生姓名：")
    flag = 0
    i = 0
    for info in student_info:
        if mod_name == info.get("name"):
            student_info.pop(i)
            a = int(input("请输入年龄："))
            s = int(input("请输入成绩："))
            info = {"name":mod_name,"age":a,"score":s}
            student_info.append(info)
            flag = 1
            break
        i = i + 1
    if flag == 0:
        print("没有该学生")

def InsertLList(student_info):
    i = 1
    num = int(input("插入一个学生到第几个学生后："))
    for info in student_info:
        if i == num:
            n = input("请输入名字：")
            a = input("请输入年龄：")
            s = input("请输入成绩：")
            info = {"name":n,"age":a,"score":s}
            student_info.insert(i, info)
        i = i + 1

def DeleteLList(student_info):
    del_name = input("请输入删除的学生姓名：")
    i = 0
    for info in student_info:
        if del_name == info.get("name"):
            student_info.pop(i)
        i = i + 1

def main():
    student_info = []
    while True:
        meun()
        n = input("         数字对应实验题号，请选1-8:")
        if n == '1':
            student_info = CreatLList()
        elif n == '2':
            OutputLList(student_info)
        elif n == '3':
            ModifyOne(student_info)
        elif n == '4':
            FindLList(student_info)
        elif n == '5':
            InsertLList(student_info)
        elif n == '6':
            DeleteLList(student_info)
        elif n == '7':
            break
        else:
                print("请输入正确的值")
        input("回车显示菜单")

main()
