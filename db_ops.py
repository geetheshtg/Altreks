from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
con = os.path.join(ROOT_FOLDER, 'db\\exam.db')


def StoreData(email, fname, lname, pno, password):
    conn = sqlite3.connect(globals()['con'])
    conn.execute(
        f"INSERT INTO USER (EMAIL,FIRSTNAME,LASTNAME,PHONE,PASSWORD) VALUES ( '{email}', '{fname}', '{lname}', {pno}, '{password}' )")
    conn.commit()
    return "User Registered Successfully"


def Validation(email, password):
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute("SELECT EMAIL,FIRSTNAME,LASTNAME,PHONE,PASSWORD from USER")
    message = "No such user"
    for row in cursor:
        if row[0] == email:
            if check_password_hash(row[4], password):
                message = "Login success"
            else:
                message = "Wrong Password"
    return message


def AddSchedule(email, date, time, examid, slot):
    conn = sqlite3.connect(globals()['con'])
    conn.execute(
        f"INSERT INTO SCHEDULE (EMAIL,EDATE,ETIME,EID,SLOT) VALUES ( '{email}', '{date}', '{time}', '{examid}', '{slot}' )")
    conn.commit()
    return "Schedule Added Successfully"


def ViewSchedule(email):
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute(f"SELECT EDATE,ETIME,EID,SLOT from SCHEDULE where EMAIL=='{email}'")
    lis = list()
    for row in cursor:
        temp = [
            row[0],  # date
            row[1],  # time
            row[2],  # examid
            row[3],  # exam slot
        ]
        lis.append(temp)
    return lis


def ViewAllSchedule():
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute(f"SELECT EMAIL,EDATE,ETIME,EID,SLOT from SCHEDULE")
    lis = list()
    for row in cursor:
        temp = [
            row[0],  # email
            row[1],  # date
            row[2],  # time
            row[3],  # examid
            row[4],  # exam slot
        ]
        lis.append(temp)
    return lis


def Viewfdb():
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute("SELECT email,name,feedback FROM fdbk")
    lis = list()
    for row in cursor:
        temp = [
            row[0],  # email
            row[1],  # name
            row[2]  # feeback
        ]
        lis.append(temp)
    return lis


def changeAvailability(email, eid, slot, availability):
    check = False
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute(f"SELECT EMAIL,EXAMID,SLOT,AVAILABLE from AVAILABILITY")
    for row in cursor:
        if row[0] == email and row[1] == eid and row[2] == slot:
            check = True

    if check is False:
        # no previous entry
        conn.execute(
            f"INSERT INTO AVAILABILITY (EMAIL,EXAMID,SLOT,AVAILABLE) VALUES ('{email}','{eid}','{slot}','{availability}')")
        conn.commit()
    else:
        # if some entry exists
        conn.execute(
            f"UPDATE AVAILABILITY SET AVAILABLE = '{availability}' WHERE EMAIL='{email}' AND EXAMID='{eid}' AND SLOT='{slot}'")
        conn.commit()


def ViewAvailable(email):
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute(
        "SELECT EMAIL FROM AVAILABILITY WHERE AVAILABLE='Available'")
    lis = list()
    for row in cursor:
        if row[0] != email:
            lis.append(row[0])
    return lis


def ViewRequests():
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute(f'SELECT * FROM REQUEST')
    lis = list()
    for row in cursor:
        temp = [
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6]
        ]
        lis.append(temp)
    return lis


def RequestSwap(email1, email, examid, date, time, slot):
    conn = sqlite3.connect(globals()['con'])
    conn.execute(
        f"INSERT INTO REQUEST (EMAILF,EMAILT,EXAMID,DATE,TIME,SLOT,APPROVED) VALUES ( '{email1}','{email}', '{examid}', '{date}', '{time}', '{slot}', 'N' )")
    conn.commit()
    return "Request sent"


def ReqStat(email):
    conn = sqlite3.connect(globals()['con'])
    cursor = conn.execute(f"SELECT * from REQUEST WHERE EMAILF='{email}'")
    lis = list()
    for row in cursor:
        lis.append([row[1], row[2], row[3], row[4], row[5], row[6]])
    return lis


def ApproveReq(emailf, emailt, examid, date, time, slot, approval):
    if approval == 'Y':
        conn = sqlite3.connect(globals()['con'])
        cursor = conn.execute(
            f"SELECT * from REQUEST WHERE EMAILF='{emailf}' AND EMAILT='{emailt}' AND EXAMID='{examid}' AND DATE='{date}' AND TIME='{time}' AND SLOT='{slot}'")
        lis = []
        for row in cursor:
            lis.append(row)
        if len(lis) == 0:
            res = "Enter valid input"
        else:
            # check if emailt is available during that time
            cur = conn.execute(
                f"SELECT EMAIL,EDATE,ETIME,SLOT FROM SCHEDULE WHERE EMAIL='{emailt}' AND EDATE='{date}' AND ETIME='{time}' AND SLOT='{slot}'")
            l1 = []
            for row in cur:
                l1.append(row)
            if len(l1) == 0:
                # available if no such entry in schedules table
                # change the approval to 'Y'
                conn.execute(
                    f"UPDATE REQUEST SET APPROVED = '{approval}' WHERE EMAILF='{emailf}' AND EMAILT='{emailt}' AND EXAMID='{examid}' AND DATE='{date}' AND TIME='{time}' AND SLOT='{slot}'")
                conn.commit()
                # remove the user with emailf from that schedule and replace with user with emailt
                conn.execute(
                    f"UPDATE SCHEDULE SET EMAIL = '{emailt}' WHERE EMAIL='{emailf}' AND EID='{examid}' AND EDATE='{date}' AND ETIME='{time}' AND SLOT='{slot}'")
                conn.commit()
                res = "Successfully updated the request of slot change"
            else:
                # otherwise not available
                res = f"Can't exchange slots with {emailt}"
        return res
    else:
        return None
