import os
import json
import sqlite3


def createDB():
    libdb = sqlite3.connect(
        '{}\\\\resources\\appdata\\library.db'.format(os.getcwd()))
    libcur = libdb.cursor()
    libcur.execute("CREATE TABLE library(ACCNO INT PRIMARY KEY UNIQUE NOT NULL,TITLE TEXT NOT NULL,AUTHOR TEXT DEFAULT '-',ACCDATE TEXT DEFAULT '-',TYPE TEXT DEFAULT 'Books',ISBN INT DEFAULT '-',ISSUED TEXT DEFAULT 'NO',NOC INT DEFAULT '1');")
    libcur.execute("CREATE TABLE members(UID INT PRIMARY KEY UNIQUE NOT NULL,NAME TEXT NOT NULL,CLASS TEXT NOT NULL,ADMID INT NOT NULL UNIQUE,EMID TEXT DEFAULT '-');")
    libcur.execute(
        'CREATE TABLE circulation(UID INT PRIMARY KEY NOT NULL,ACCNO INT UNIQUE NOT NULL,TITLE TEXT NOT NULL,NAME TEXT NOT NULL,CLASS TEXT NOT NULL);')
    libdb.commit()
    libdb.close()


def createJSON(userData, instData):
    firstName = userData['firstName'].strip()
    lastName = userData['lastName'].strip()
    userName = firstName + ' ' + lastName
    userEmail = userData['email'].strip()
    phoneNumber = userData['phoneNumber'].strip()
    userPassword = userData['password'].strip()
    instName = instData['instName'].strip()
    instAddress = instData['instAddress'].strip()
    instCity = instData['instCity'].strip()
    instPIN = instData['instPIN'].strip()
    instEmail = instData['instEmail'].strip()
    abtdataD = {'firstName': firstName,  'lastName': lastName,  'userName': userName,  'userEmail': userEmail,  'phoneNumber': phoneNumber,  'userPassword': userPassword,
                'instName': instName,  'instAddress': instAddress,  'instCity': instCity,  'instPIN': instPIN,  'instEmail': instEmail}
    with open('{}\\\\resources\\appdata\\about.json'.format(os.getcwd()), 'w') as (abtdataF):
        json.dump(abtdataD, abtdataF)
        abtdataF.close()