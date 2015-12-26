# -*- coding:utf-8 -*-
# 这一段导入 Tkinter 库及各种……？
from Tkinter import *
import io
import os
import pickle
import hashlib

# 几个全局变量
__pwdDB = {}
dbFilePath = "db.db"

# MD5 哈希，加密数据库密码用
def md5(str):
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()  
        m.update(str)
        return m.hexdigest()
    else:
        return ''

# 提示信息的弹窗，貌似还挺常用的，于是把它单独出来
def alert(title, msg):
    alert = Tk()
    alert.title(title)
    Label(alert, text=msg).pack()
    Button(alert, text="OK", command=alert.destroy).pack()
    alert.mainloop()

# 检测是否为第一次使用
def isFirst():
# 检测依据是数据库密码是否存在
    if __pwdDB.get("mainKey") == None:
# 不是的话就设定它
        __setPwdDBPwd()
    else:
# 是的话就输入并检查它
        __chkPwdDBPwd()

# 建新账号 - 密码对的过程函数
"""----------------------------------------------------------------------------
顺便，将四个主方法的首字母提取出来，变成一个词，就是 CRUD
Create
Retrieve
Update
Delete
数据库的四种基本操作。
CRUD 翻译为“增删改查”。
函数名那样，是故意的。
也可以度一下 CRUD。
"""----------------------------------------------------------------------------
def createPwd():
    # 按钮按下时做的事
    def __addPassword():
        iUsername = username.get()
        iPassword = password.get()
        __pwdDB[iUsername] = iPassword
        __save()
        alert("Message", "Save finished.")
        sWnd.destroy()
    # 新建一个窗口
    sWnd = Tk()
    # 窗口标题
    sWnd.title("Save a password")
    # 一个文字控件
    Label(sWnd, text="Username:").pack()
    # 一个输入框控件
    username = Entry(sWnd)
    username.pack()
    
    Label(sWnd, text="Password:").pack()
    password = Entry(sWnd)
    password.pack()
    # 一个按钮控件，当按下时触发 __addPassword 方法
    Button(sWnd, text="OK", command=__addPassword).pack()
    
# 查账号 - 密码对
def retrvPwd():
    def __rtvPassword():
        # 当找不到的时候弹出警告窗口
        if __pwdDB.get(name.get()) == None:
            alert("Error", "Name not found.")
        # 否则显示
        else:
            alert("Message", "The password for " + name.get + " is:\n" + __pwdDB[name.get()])
    rtvWnd = Tk()
    rtvWnd.title("Retrieve password")
    Label(rtvWnd, text="Input the username to retrieve:").pack()
    name = Entry(rtvWnd)
    name.pack()
    Button(rtvWnd, text="Confirm", command=__rtvPassword).pack()

# 更新
def updPwd():
    def __updPassword():
        if __pwdDB.get(name.get()) == None:
            alert("Error", "Name not found.")
        else:
            __pwdDB[name.get()] = pwd.get()
            __save()
            alert("Message", "Updated.")
    updWnd = Tk()
    updWnd.title("Update Password")
    Label(updWnd, text="Input the username to update:").pack()
    name = Entry(updWnd)
    name.pack()
    pwd = Entry(updWnd)
    pwd.pack()
    Button(updWnd, text="Confirm", command=__updPassword).pack()

# 删除
def delPwd():
    def __delPassword():
        if __pwdDB.get(name.get()) == None:
            alert("Error", "Name not found.")
        else:
            __pwdDB.pop(name.get())
            __save()
            alert("Message", "Deleted.")
    delWnd = Tk()
    delWnd.title("Delete Password")
    Label(delWnd, text="Input the username to delete:").pack()
    name = Entry(delWnd)
    name.pack()
    Button(delWnd, text="Confirm", command=__delPassword).pack()

# 加载数据库文件
def __load():
    # 这里的 __pwdDB 用的是那个开头的全局变量，需要 global 关键字来……它
    global __pwdDB
    # 文件找不到，或者文件为空
    if not os.path.exists(dbFilePath) or os.path.getsize(dbFilePath) == 0:
        # 写它（事实上等于建）
        dbFile = io.FileIO(dbFilePath, "w")
        # 保存进去
        pickle.dump(__pwdDB, dbFile)
        # 关闭文件
        dbFile.close()
    # 否则（也就是文件找到且不为空）
    else:
        # 读它
        dbFile = io.FileIO(dbFilePath, "r")
        # 用 pickle 把它加载进去
        __pwdDB = pickle.load(dbFile)
        # 关闭文件
        dbFile.close()

# 保存数据库文件
def __save():
    # 加载为可写
    dbFile = io.FileIO(dbFilePath, "w")
    # 保存进去
    pickle.dump(__pwdDB, dbFile)
    # 关闭文件
    dbFile.close()

# 设置数据库密码的函数
def __setPwdDBPwd():
    # 按下按钮时触发的
    def __setPwdDBPwdMain():
        dbEncPwd = inputedPwd.get()
        if len(dbEncPwd) == 0:
            alert("Error", "Password cannot be null")
        else:
            # 我们保存它的 MD5 哈希而不是明文存储，增加数据的安全性
            __pwdDB["mainKey"] = md5(dbEncPwd)
            __save()
    
    dbPwd = Tk()
    dbPwd.title("Password DB file password")

    prompt = Label(dbPwd, text="This is the first time you use this password manager.\nPlease set a DB main key to encrypt this database.")
    inputedPwd = Entry(dbPwd)
    applyPwd = Button(dbPwd, text="Confirm", command=__setPwdDBPwdMain)

    prompt.pack()
    inputedPwd.pack()
    applyPwd.pack()

    dbPwd.mainloop()

# 检查数据库密码的函数
def __chkPwdDBPwd():
    def __chkPwdDBPwdMain():
        dbInputedPwd = inputedPwd.get()
        # 将输入的哈希跟保存的值比对
        if md5(dbInputedPwd) != __pwdDB["mainKey"]:
            # 相同的话就是输入正确，否则就是输入错误
            alert("Error", "Password incorrect.")
        else:
            dbPwd.destroy()
            return
    dbPwd = Tk()
    dbPwd.title("Password DB file password")
    
    prompt = Label(dbPwd, text="Please input the DB file encrypt password.")
    inputedPwd = Entry(dbPwd)
    confirmPwd = Button(dbPwd, text="Login", command=__chkPwdDBPwdMain)
    
    prompt.pack()
    inputedPwd.pack()
    confirmPwd.pack()
    
    dbPwd.mainloop()

# 这一段你说你看得懂
def mainWindow():
    m = Tk()
    m.title("Password Manager")
    Button(m, text="Create a new password", command=createPwd).grid()
    Button(m, text="Retrieve a password", command=retrvPwd).grid()
    Button(m, text="Update a password", command=updPwd).grid()
    Button(m, text="Delete a password", command=delPwd).grid()
    Button(m, text="Exit", command=m.destroy).grid()
    m.mainloop()

# 主方法
def main():
    # 从文件加载数据库
    __load()
    # 检查是不是第一次
    isFirst()
    # 然后这里是主方法
    mainWindow()
    
# 调用它
main()

"""----------------------------------------------------------------------------
最后。
现在那个账号 - 密码对的密码是明文存储的。
也就是说直接用记事本打开，什么都看到了。
这样绝对是不行的。
解决方案就是用一些带密钥的加密方案，例如 DES, AES; RSA, GPG 等。
（上一行的分号有特别的含义。两组加密算法在密钥方面有不同）
但是使用它们都需要加插件，太麻烦，对于你们这一群不用 Linux 的。
所以我还是放弃了。
虽然可以将这个算法自己写为一个文件然后调用，但是我感觉对你们来说不现实。
所以暂时搁置。
前面用来加密数据库密码的是 MD5，它是一种哈希算法。
如果把哈希算法比作 f(x) = y 中的 f 的话，那么它有如下特点：
1) 当 x1 不等于 x2 时，y1 不等于 y2。
2) 知道 x 很容易计算出 y，但是知道 y 要倒推出 x 是几乎不可能的。
（虽然在 2005 年王小芸院士的一篇论文证明 MD5 和 SHA-1（另外一种很常用的哈希算法）
  是不安全的，但是我们这个需求下，我还是用了 MD5，原因未知。
"""----------------------------------------------------------------------------

