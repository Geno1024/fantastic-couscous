from Tkinter import *
import io
import os
import pickle
import hashlib

__pwdDB = {}
dbFilePath = "db.db"

def md5(str):
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()  
        m.update(str)
        return m.hexdigest()
    else:
        return ''
        
def alert(title, msg):
    alert = Tk()
    alert.title(title)
    Label(alert, text=msg).pack()
    Button(alert, text="OK", command=alert.destroy).pack()
    alert.mainloop()

def isFirst():
    if __pwdDB.get("mainKey") == None:
        __setPwdDBPwd()
    else:
        __chkPwdDBPwd()

def createPwd():
    def __addPassword():
        iUsername = username.get()
        iPassword = password.get()
        __pwdDB[iUsername] = iPassword
        __save()
        alert("Message", "Save finished.")
        sWnd.destroy()
    sWnd = Tk()
    sWnd.title("Save a password")
    Label(sWnd, text="Username:").pack()
    username = Entry(sWnd)
    username.pack()
    Label(sWnd, text="Password:").pack()
    password = Entry(sWnd)
    password.pack()
    Button(sWnd, text="OK", command=__addPassword).pack()
    
def retrvPwd():
    def __rtvPassword():
        if __pwdDB.get(name.get()) == None:
            alert("Error", "Name not found.")
        else:
            alert("Message", "The password for " + name.get + " is:\n" + __pwdDB[name.get()])
    rtvWnd = Tk()
    rtvWnd.title("Retrieve password")
    Label(rtvWnd, text="Input the username to retrieve:").pack()
    name = Entry(rtvWnd)
    name.pack()
    Button(rtvWnd, text="Confirm", command=__rtvPassword).pack()

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

def __load():
    global __pwdDB
    if not os.path.exists(dbFilePath) or os.path.getsize(dbFilePath) == 0:
        dbFile = io.FileIO(dbFilePath, "w")
        pickle.dump(__pwdDB, dbFile)
        dbFile.close()
    else:
        dbFile = io.FileIO(dbFilePath, "r")
        __pwdDB = pickle.load(dbFile)
        dbFile.close()

def __save():
    dbFile = io.FileIO(dbFilePath, "w")
    pickle.dump(__pwdDB, dbFile)
    dbFile.close()

def __setPwdDBPwd():
    def __setPwdDBPwdMain():
        dbEncPwd = inputedPwd.get()
        if len(dbEncPwd) == 0:
            alert("Error", "Password cannot be null")
        else:
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

def __chkPwdDBPwd():
    def __chkPwdDBPwdMain():
        dbInputedPwd = inputedPwd.get()
        if md5(dbInputedPwd) != __pwdDB["mainKey"]:
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

def mainWindow():
    m = Tk()
    m.title("Password Manager")
    Button(m, text="Create a new password", command=createPwd).grid()
    Button(m, text="Retrieve a password", command=retrvPwd).grid()
    Button(m, text="Update a password", command=updPwd).grid()
    Button(m, text="Delete a password", command=delPwd).grid()
    Button(m, text="Exit", command=m.destroy).grid()
    m.mainloop()

def main():
    __load()
    isFirst()
    mainWindow()
    

main()

