import os
import sqlite3
import json
import eel
try:
    with open('{}\\\\resources\\appdata\\about.json'.format(os.getcwd())) as (abtdataT):
        abtdataP = json.load(abtdataT)
        abtdataT.close()
    libdb = sqlite3.connect(
        '{}\\\\resources\\appdata\\library.db'.format(os.getcwd()))
    libcur = libdb.cursor()
except:
    pass
else:
    def giveuserPage():
        eel.loginPage(abtdataP['firstName'])

    def authenticateUser(passkey, login_stat):
        if passkey == abtdataP['userPassword']:
            libcur.execute('SELECT COUNT(*) FROM library;')
            tT = libcur.fetchall()[0][0]
            libcur.execute('SELECT SUM(NOC) FROM library;')
            tC = libcur.fetchall()[0][0]
            libcur.execute('SELECT COUNT(*) FROM members;')
            lM = libcur.fetchall()[0][0]
            eel.showLoadingBar()
            if login_stat == 1:
                if tT > 0:
                    eel.fillTitlesHead()
                    libcur.execute('SELECT * FROM library Order by ACCNO ASC;')
                    lLD = libcur.fetchall()
                    for rows in lLD:
                        eel.fillTitlesBody(
                            rows[0], rows[6], rows[1], rows[2], rows[4], rows[(-1)], rows[3], rows[(-3)])
                    else:
                        eel.queryTitlesTable(1)

                else:
                    eel.fillTitlesHead()
                    eel.queryTitlesTable(1)
                if lM > 0:
                    eel.fillMembersHead()
                    libcur.execute('SELECT * FROM members Order by UID ASC;')
                    lMD = libcur.fetchall()
                    for rows in lMD:
                        eel.fillMembersBody(
                            rows[0], rows[1], rows[2], rows[4], rows[3])
                    else:
                        eel.queryMembersTable(1)

                else:
                    eel.fillMembersHead()
                    eel.queryMembersTable(1)
                libcur.execute('SELECT COUNT(*) FROM circulation;')
                lenC = libcur.fetchall()[0][0]
                if lenC > 0:
                    eel.fillReturneesHead()
                    libcur.execute(
                        'SELECT * FROM circulation ORDER by UID ASC;')
                    lCD = libcur.fetchall()
                    for rows in lCD:
                        eel.fillReturneesBody(
                            rows[0], rows[1], rows[2], rows[3], rows[4])
                    else:
                        eel.queryReturnsTable(1)

                else:
                    eel.fillReturneesHead()
                    eel.queryReturnsTable(1)
            eel.triggerpasswordSuccess(abtdataP['userName'], abtdataP['instName'],
                                        abtdataP['instCity'], abtdataP['instPIN'], abtdataP['instEmail'], tT, tC, lM)
            eel.hideLoadingBar()
        else:
            eel.triggerpasswordError()

    def submitaddTitleData(LACCNO, TITLE, AUTHOR, ISBN, LACCDATE, LTYPE, LNOC):
        try:
            LTITLE = TITLE.strip()
            LAUTHOR = AUTHOR.strip()
            LISBN = ISBN.strip()
            if len(LAUTHOR) == 0:
                LAUTHOR = '-'
            if len(LISBN) == 0:
                LISBN = '-'
            lib_dataL = []
            lib_dataT = (
                int(LACCNO), LTITLE, LAUTHOR, LACCDATE,
                LTYPE, LISBN, 'NO', int(LNOC))
            lib_dataL.append(lib_dataT)
            libcur.execute(
                'INSERT INTO library VALUES(?, ?, ?, ?, ?, ?, ?, ?);', lib_dataT)
            libdb.commit()
            libcur.execute('SELECT COUNT(*) FROM library;')
            tT = libcur.fetchall()[0][0]
            libcur.execute('SELECT SUM(NOC) FROM library;')
            tC = libcur.fetchall()[0][0]
            libcur.execute('SELECT COUNT(*) FROM members;')
            lM = libcur.fetchall()[0][0]
            eel.queryTitlesTable(2)
            eel.fillTitlesHead()
            if tT > 0:
                libcur.execute('SELECT * FROM library order by ACCNO ASC;')
                lLD = libcur.fetchall()
                for rows in lLD:
                    eel.fillTitlesBody(
                        rows[0], rows[6], rows[1], rows[2], rows[4], rows[(-1)], rows[3], rows[(-3)])

            eel.queryTitlesTable(1)
            eel.triggeraddTitleDataSuccess(tT, tC, lM)
        except:
            eel.triggeraddTitleDataError()

    def submitaddMembersData(ADMID, NAME, CLASS, SECTION, EMID):
        try:
            LC = ''
            LS = ''
            LNAME = NAME.strip()
            LEMID = EMID.strip()
            if len(LEMID) == 0:
                LEMID = '-'
            LUID = int('{}'.format(CLASS) +
                        '{}'.format(SECTION) + '{}'.format(ADMID))
            if CLASS == '6':
                LC = 'VI '
            if CLASS == '7':
                LC = 'VII '
            if CLASS == '8':
                LC = 'VIII '
            if CLASS == '9':
                LC = 'IX '
            if CLASS == '10':
                LC = 'X '
            if CLASS == '11':
                LC = 'XI '
            if CLASS == '12':
                LC = 'XII '
            if SECTION == '1':
                LS = 'A'
            if SECTION == '2':
                LS = 'B'
            if SECTION == '3':
                LS = 'C'
            if SECTION == '4':
                LS = 'D'
            if SECTION == '5':
                LS = 'E'
            LCLASS = LC + ' ' + LS
            lib_Memb_dataL = []
            lib_Memb_dataT = (LUID, LNAME, LCLASS, ADMID, LEMID)
            lib_Memb_dataL.append(lib_Memb_dataT)
            libcur.execute(
                'INSERT INTO members VALUES(?, ?, ?, ?, ?);', lib_Memb_dataT)
            libdb.commit()
            libcur.execute('SELECT COUNT(*) FROM library;')
            tT = libcur.fetchall()[0][0]
            libcur.execute('SELECT SUM(NOC) FROM library;')
            tC = libcur.fetchall()[0][0]
            libcur.execute('SELECT COUNT(*) FROM members;')
            lM = libcur.fetchall()[0][0]
            eel.queryMembersTable(2)
            eel.fillMembersHead()
            libcur.execute('SELECT * FROM members order by UID ASC;')
            lMD = libcur.fetchall()
            for rows in lMD:
                eel.fillMembersBody(
                    rows[0], rows[1], rows[2], rows[4], rows[3])
            else:
                eel.queryMembersTable(1)
                eel.triggeraddMembersDataSuccess(LUID, tT, tC, lM)

        except:
            eel.triggeraddMembersDataError()

    def issueTitle(UID, ACCNO):
        libcur.execute(
            'SELECT ACCNO FROM circulation Where ACCNO=?;', (ACCNO,))
        tE = libcur.fetchall()
        if len(tE) == 0:
            libcur.execute(
                'SELECT ACCNO FROM library Where ACCNO=?;', (ACCNO,))
            vT = libcur.fetchall()
            libcur.execute('SELECT UID FROM members Where UID=?;', (UID,))
            vM = libcur.fetchall()
            if len(vT) == 1:
                if len(vM) == 1:
                    libcur.execute(
                        'SELECT UID FROM circulation Where UID=?;', (UID,))
                    mE = libcur.fetchall()
                    if len(mE) == 0:
                        try:
                            libcur.execute(
                                'SELECT * FROM library where ACCNO=?', (ACCNO,))
                            rLD = libcur.fetchall()[0]
                            libcur.execute(
                                'SELECT * FROM members where UID=?', (UID,))
                            rMD = libcur.fetchall()[0]
                            cir_dataT = (rMD[0], rLD[0],
                                            rLD[1], rMD[1], rMD[2])
                            libcur.execute(
                                'INSERT INTO circulation VALUES(?, ?, ?, ?, ?);', cir_dataT)
                            libcur.execute(
                                "UPDATE library set ISSUED = 'YES' WHERE ACCNO=?;", (ACCNO,))
                            libdb.commit()
                            eel.queryReturnsTable(2)
                            eel.fillReturneesHead()
                            libcur.execute(
                                'SELECT * FROM circulation ORDER by UID ASC;')
                            lCD = libcur.fetchall()
                            for rows in lCD:
                                eel.fillReturneesBody(
                                    rows[0], rows[1], rows[2], rows[3], rows[4])
                            else:
                                eel.queryReturnsTable(1)
                                eel.queryTitlesTable(2)
                                eel.fillTitlesHead()
                                libcur.execute(
                                    'SELECT * FROM library order by ACCNO ASC;')
                                lLD = libcur.fetchall()
                                for rows in lLD:
                                    eel.fillTitlesBody(
                                        rows[0], rows[6], rows[1], rows[2], rows[4], rows[(-1)], rows[3], rows[(-3)])
                                else:
                                    eel.queryTitlesTable(1)
                                    eel.issueTitleSuccess()

                        except:
                            eel.issueTitleError(6)

                    else:
                        eel.issueTitleError(5)
                else:
                    eel.issueTitleError(3)
            else:
                eel.issueTitleError(2)
        else:
            eel.issueTitleError(4)

    def submitTitle(ACCNO):
        try:
            libcur.execute(
                'SELECT ACCNO FROM circulation Where ACCNO=?;', (ACCNO,))
            vTc = libcur.fetchall()
            if len(vTc) == 1:
                try:
                    libcur.execute(
                        "UPDATE library set ISSUED = 'NO' WHERE ACCNO=?;", (ACCNO,))
                    libcur.execute(
                        'DELETE FROM circulation Where ACCNO=?;', (ACCNO,))
                    libdb.commit()
                    eel.queryReturnsTable(2)
                    eel.fillReturneesHead()
                    libcur.execute(
                        'SELECT * FROM circulation order by UID ASC;')
                    lCD = libcur.fetchall()
                    for rows in lCD:
                        eel.fillReturneesBody(
                            rows[0], rows[1], rows[2], rows[3], rows[4])
                    else:
                        eel.queryReturnsTable(1)
                        eel.queryTitlesTable(2)
                        eel.fillTitlesHead()
                        libcur.execute(
                            'SELECT * FROM library order by ACCNO ASC;')
                        lLD = libcur.fetchall()
                        for rows in lLD:
                            eel.fillTitlesBody(
                                rows[0], rows[6], rows[1], rows[2], rows[4], rows[(-1)], rows[3], rows[(-3)])
                        else:
                            eel.queryTitlesTable(1)
                            eel.submitTitleSuccess()

                except:
                    eel.submitTitleError(3)

            else:
                eel.submitTitleError(2)
        except:
            eel.submitTitleError(3)

    def deleteTitle(ACCNO):
        libcur.execute(
            'SELECT ACCNO FROM circulation Where ACCNO=?;', (ACCNO,))
        vTc = libcur.fetchall()
        if len(vTc) != 1:
            try:
                libcur.execute('DELETE FROM library Where ACCNO=?;', (ACCNO,))
                libdb.commit()
                libcur.execute('SELECT COUNT(*) FROM library;')
                tT = libcur.fetchall()[0][0]
                eel.queryTitlesTable(2)
                eel.fillTitlesHead()
                if tT > 0:
                    libcur.execute('SELECT * FROM library order by ACCNO ASC;')
                    lLD = libcur.fetchall()
                    for rows in lLD:
                        eel.fillTitlesBody(
                            rows[0], rows[6], rows[1], rows[2], rows[4], rows[(-1)], rows[3], rows[(-3)])

                eel.queryTitlesTable(1)
                libcur.execute('SELECT COUNT(*) FROM library;')
                tT = libcur.fetchall()[0][0]
                libcur.execute('SELECT SUM(NOC) FROM library;')
                tC = libcur.fetchall()[0][0]
                libcur.execute('SELECT COUNT(*) FROM members;')
                lM = libcur.fetchall()[0][0]
                eel.showLoadingBar()
                eel.triggerChangeSuccess(tT, tC, lM)
                eel.deleteTitleSuccess()
            except:
                eel.deleteTitleError(2)

        else:
            eel.deleteTitleError(1)

    def deleteMember(UID):
        libcur.execute('SELECT UID FROM circulation Where UID=?;', (UID,))
        vTc = libcur.fetchall()
        if len(vTc) != 1:
            try:
                libcur.execute('DELETE FROM members Where UID=?;', (UID,))
                libdb.commit()
                libcur.execute('SELECT COUNT(*) FROM members;')
                lM = libcur.fetchall()[0][0]
                eel.queryMembersTable(2)
                eel.fillMembersHead()
                if lM > 0:
                    libcur.execute('SELECT * FROM members order by UID ASC;')
                    lMD = libcur.fetchall()
                    for rows in lMD:
                        eel.fillMembersBody(
                            rows[0], rows[1], rows[2], rows[4], rows[3])

                eel.queryMembersTable(1)
                libcur.execute('SELECT COUNT(*) FROM library;')
                tT = libcur.fetchall()[0][0]
                libcur.execute('SELECT SUM(NOC) FROM library;')
                tC = libcur.fetchall()[0][0]
                libcur.execute('SELECT COUNT(*) FROM members;')
                lM = libcur.fetchall()[0][0]
                eel.showLoadingBar()
                eel.triggerChangeSuccess(tT, tC, lM)
                eel.deleteMemberSuccess()
            except:
                eel.deleteMemberError(2)

        else:
            eel.deleteMemberError(1)

    def optdb():
        libcur.execute('VACUUM;')
        libdb.commit()
        eel.operationSuccessMsg(1)

    def bkpdb():
        bkpPath = '{}\\\\resources\\appdata\\backup.db'.format(os.getcwd())
        if os.path.exists('{}\\\\resources\\appdata\\backup.db'.format(os.getcwd())):
            os.remove(bkpPath)
        libcur.execute('VACUUM main INTO ?;', (bkpPath,))
        eel.operationSuccessMsg(2)
        os.startfile('{}\\\\resources\\appdata\\'.format(os.getcwd()))
    def convtoExcel():
        try:
            if os.path.exists('{}\\\\resources\\appdata\\library.csv'.format(os.getcwd())):
                os.remove('{}\\\\resources\\appdata\\library.csv'.format(os.getcwd()))
            if os.path.exists('{}\\\\resources\\appdata\\members.csv'.format(os.getcwd())):
                os.remove('{}\\\\resources\\appdata\\members.csv'.format(os.getcwd()))
            if os.path.exists('{}\\\\resources\\appdata\\LIBRARY.xlsx'.format(os.getcwd())):
                os.remove(
                    '{}\\\\resources\\appdata\\LIBRARY.xlsx'.format(os.getcwd()))
            if os.path.exists('{}\\\\resources\\appdata\\MEMBERS.xlsx'.format(os.getcwd())):
                os.remove(
                    '{}\\\\resources\\appdata\\MEMBERS.xlsx'.format(os.getcwd()))
            libcur.execute(
                "SELECT ACCNO, TITLE, AUTHOR, ACCDATE, TYPE, ISBN, NOC From library ORDER BY ACCNO ASC;")
            library_sheet = libcur.fetchall()
            libcur.execute(
                "SELECT UID, NAME, CLASS, ADMID, EMID FROM members ORDER BY UID ASC;")
            members_sheet = libcur.fetchall()
            library_sheet_file = '{}\\\\resources\\appdata\\library.csv'.format(
                os.getcwd())
            members_sheet_file = '{}\\\\resources\\appdata\\members.csv'.format(
                os.getcwd())
            import numpy as np
            import pandas as pd
            import csv
            with open(library_sheet_file,'w') as out:
                csv_out=csv.writer(out)
                csv_out.writerow(['ACCNO', 'TITLE', 'AUTHOR','ACCDATE', 'TYPE', 'ISBN', 'NOC'])
                csv_out.writerows(library_sheet)
            with open(members_sheet_file,'w') as out:
                csv_out=csv.writer(out)
                csv_out.writerow(['UID', 'NAME', 'CLASS', 'ADMID', 'EMID'])
                csv_out.writerows(members_sheet)
            lb_new = pd.read_csv(
                '{}\\\\resources\\appdata\\library.csv'.format(os.getcwd()))
            mb_new = pd.read_csv(
                '{}\\\\resources\\appdata\\members.csv'.format(os.getcwd()))
            LBE = pd.ExcelWriter(
                '{}\\\\resources\\appdata\\LIBRARY.xlsx'.format(os.getcwd()))
            MBE = pd.ExcelWriter(
                '{}\\\\resources\\appdata\\MEMBERS.xlsx'.format(os.getcwd()))
            lb_new.to_excel(LBE, index=False)
            mb_new.to_excel(MBE, index=False)
            LBE.save()
            MBE.save()            
            library_sheet = None
            members_sheet = None
            os.remove('{}\\\\resources\\appdata\\library.csv'.format(os.getcwd()))
            os.remove('{}\\\\resources\\appdata\\members.csv'.format(os.getcwd()))
            os.startfile('{}\\\\resources\\appdata\\LIBRARY.xlsx'.format(os.getcwd()))
            os.startfile('{}\\\\resources\\appdata\\members.xlsx'.format(os.getcwd()))
            os.startfile('{}\\\\resources\\appdata\\'.format(os.getcwd()))
            eel.operationSuccessMsg(3)
        except:
            eel.operationErrorMsg()