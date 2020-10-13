import os
import eel
import pygetwindow as pw
@eel.expose
def sendloginPage():
    dbWorker.giveuserPage()@eel.expose
def submituserPassword(passkey,login_stat):
    dbWorker.authenticateUser(passkey,login_stat)@eel.expose
def minWindow():
    pyWindow = pw.getWindowsWithTitle('Pygranthalaya')[0]
    pyWindow.minimize()
@eel.expose
def maxWindow():
    pyWindow = pw.getWindowsWithTitle('Pygranthalaya')[0]
    if pyWindow.isMaximized:
        pyWindow.restore()
    else:
        pyWindow.maximize()
@eel.expose
def submitaddTitleData(LACCNO, LTITLE, LAUTHOR, LISBN, LACCDATE, LTYPE, LNOC):
    dbWorker.submitaddTitleData(
        LACCNO, LTITLE, LAUTHOR, LISBN, LACCDATE, LTYPE, LNOC)
@eel.expose
def submitaddMembersData(LADMID, LNAME, LCLASS, LSECTION, LEMID):
    dbWorker.submitaddMembersData(LADMID, LNAME, LCLASS, LSECTION, LEMID)
@eel.expose
def issueTitle(UID, ACCNO):
    dbWorker.issueTitle(UID, ACCNO)
@eel.expose
def submitTitle(ACCNO):
    dbWorker.submitTitle(ACCNO)
@eel.expose
def deleteTitle(ACCNO):
    dbWorker.deleteTitle(ACCNO)
@eel.expose
def deleteMember(UID):
    dbWorker.deleteMember(UID)
@eel.expose
def optdb():
    dbWorker.optdb()
@eel.expose
def bkpdb():
    dbWorker.bkpdb()
@eel.expose
def installUP():
    import shutil
    from tkinter import filedialog
    userProfilepic = filedialog.askopenfilename()
    upP = r'{}\\resources\img\userPic.png'.format(os.getcwd())
    shutil.copyfile(userProfilepic, upP)
    eel.dUPB()
@eel.expose
def installIP():
    import shutil
    from tkinter import filedialog
    instProfilepic = filedialog.askopenfilename()
    ipP = r'{}\\resources\img\instPic.png'.format(os.getcwd())
    shutil.copyfile(instProfilepic, ipP)
    eel.dIPB()
@eel.expose
def installDB(userData, instData):
    dbSetup.createJSON(userData, instData)
    dbSetup.createDB()
    eel.installSuccess()
@eel.expose
def restartApp():
    import time
    os.rename(r'{}\\resources\index.html'.format(os.getcwd()),
              r'{}\\resources\install.html'.format(os.getcwd()))
    os.rename(r'{}\\resources\app.html'.format(os.getcwd()),
              r'{}\\resources\index.html'.format(os.getcwd()))
    eel.closeInstall()
    os.startfile('Pygranthalaya.py')
    exit()
def start():
    eel.init('resources')
    eel.start('index.html', mode='custom', port=12114,
              cmdline_args=['pga.exe', '.'])
def setup():
    if os.path.exists(r'{}\\resources\index.html'.format(os.getcwd())):
        os.rename(r'{}\\resources\index.html'.format(os.getcwd()),
                  r'{}\\resources\app.html'.format(os.getcwd()))
        os.rename(r'{}\\resources\install.html'.format(os.getcwd()),
                  r'{}\\resources\index.html'.format(os.getcwd()))
        eel.init('resources')
        eel.start('index.html', mode='custom', port=12114,
                  cmdline_args=['pga.exe', '.'])
    else:
        if os.path.exists(r'{}\\resources\install.html'.format(os.getcwd())):
            os.rename(r'{}\\resources\install.html'.format(os.getcwd()),
                      r'{}\\resources\index.html'.format(os.getcwd()))
            eel.init('resources')
            eel.start('index.html', mode='custom', port=12114,
                      cmdline_args=['pga.exe', '.'])
        else:
            from tkinter import messagebox
            messagebox.showerror(
                title="Critical Error!", message="App cannot install files corrupted or missing. Error triggered by frontend not found!")
if os.path.exists(r'{}\\resources\appdata\about.json'.format(os.getcwd())):
    if os.path.exists(r'{}\\resources\appdata\library.db'.format(os.getcwd())):
        if os.path.exists(r'{}\\resources\index.html'.format(os.getcwd())):
            from modules import dbWorker
            start()
        else:
            try:
                if os.path.exists(r'{}\\resources\app.html'.format(os.getcwd())):
                    os.rename(r'{}\\resources\app.html'.format(os.getcwd()),
                              r'{}\\resources\index.html'.format(os.getcwd()))
                    from modules import dbWorker
                    start()
            except:
                from tkinter import messagebox
                messagebox.showerror(
                    title="Critical Error!", message="App cannot start files corrupted or missing. Error triggered by frontend not found!")
    else:
        if os.path.exists(r'{}\\resources\index.html'.format(os.getcwd())):
            from tkinter import messagebox
            messagebox.showerror(
                title="Critical Error!", message="App cannot start files corrupted or missing library database not found!")
        else:
            from tkinter import messagebox
            messagebox.showerror(
                title="Critical Error!", message="App cannot start files corrupted or missing library database & frontend not found!")
else:
    if os.path.exists(r'{}\\resources\appdata\library.db'.format(os.getcwd())):
        from tkinter import messagebox
        messagebox.showerror(
            title="Critical Error!", message="App cannot start files corrupted or missing. Error triggered by user not found!")
    else:
        from modules import dbSetup
        setup()