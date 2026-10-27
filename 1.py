import json
try:
    with open("users.json","r",encoding="utf-8") as f:
        users = json.load(f)
except FileNotFoundError:
    users=[]
def create_user(name, age, major):
    if not isinstance(age, int):
        return "请输入数字"
    if age < 0 or age > 100:
        return "请重新输入年龄"
    user={"name":name, "age":age, "major":major}
    return user
def show_users(users):
    if not users:
        print("没有学生信息")
    else:
        for user in users:
            print(user)
while True:
    choice=input("请选择功能：")
    if choice=="1":
        name = input("请输入姓名：(按q退出)")
        if name == "q":
            break
        try:
            age = int(input("请输入年龄："))
        except ValueError:
            print("输入错误请重新输入")
            continue
        else:
            major = input("请输入专业：")
        result = create_user(name, age, major)
        if isinstance(result, dict):
            users.append(result)
        with open("users.json","w",encoding="utf-8") as f:
            json.dump(users,f,ensure_ascii=False,indent=4)
        print(users)
    elif choice=="2":
        show_users(users)
    elif choice=="3":
        found=False
        name=input("请输入学生姓名：")
        for user in users:
            if user["name"]==name:
                found=True
                print(user)
        if found==False:
            print("未找到学生")
    elif choice=="4":
        break