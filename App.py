from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
import sys, fsdk, math, ctypes, time
import mysql.connector
import easyocr
import cv2 as cv
import re
import random
import os

app = Flask(__name__)

app.config['DEBUG']
app.config['SECRET_KEY'] = 'san'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')

    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()

    return render_template('AdminHome.html', data=data, data1=data1)


@app.route("/NewLoan")
def NewLoan():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data = cur.fetchall()
    return render_template('NewLoan.html', data=data)


@app.route("/ALoanInfo")
def ALoanInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM loantb ")
    data = cur.fetchall()
    return render_template('ALoanInfo.html', data=data)


@app.route("/newloan1")
def newloan1():
    id = request.args.get('id')
    session['id'] = id

    import random
    fnew = random.randint(11111, 99999)

    return render_template('NewLoan1.html', lid="LoanID" + str(fnew))


@app.route("/LoanWaiver")
def LoanWaiver():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Waivertb ")
    data = cur.fetchall()
    return render_template('LoanWaiver.html', data=data)


@app.route("/Waiver", methods=['GET', 'POST'])
def Waiver():
    if request.method == 'POST':
        Type = request.form['Type']
        amt = request.form['amt']
        file = request.files['file']
        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename
        file.save("static/upload/" + savename)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into Waivertb values('','" + Type + "','" + amt + "','" + savename + "')")
        conn.commit()
        conn.close()
        flash("Record Save..!")
        return LoanWaiver()


@app.route("/Remove")
def Remove():
    id = request.args.get('lid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("Delete from  Waivertb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    return LoanWaiver()


@app.route("/newloanreg", methods=['GET', 'POST'])
def newloanreg():
    if request.method == 'POST':
        LoanId = request.form['LoanId']
        Type = request.form['Type']
        amt = request.form['amt']
        date = request.form['date']
        info = request.form['info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where id='" + session['id'] + "' ")
        data = cursor.fetchone()
        if data:
            uname = data[1]
            Mobile = data[3]
            Email = data[4]
            Aadhar = data[12]
            Accno = data[6]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cursor = conn.cursor()
            cursor.execute(
                "insert into loantb values('','" + uname + "','" + Mobile + "','" + Email + "','" + Aadhar + "','" + Accno + "','" + LoanId + "','" + Type + "','" +
                amt + "','" + date + "','" + info + "','Active','')")
            conn.commit()
            conn.close()

        return NewLoan()


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['Password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where status='waiting'")
            data = cur.fetchall()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where status='Active'")
            data1 = cur.fetchall()
            return render_template('AdminHome.html', data=data, data1=data1)
        else:
            flash("UserName or Password Incorrect!")

            return render_template('AdminLogin.html')


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']

        age = request.form['age']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        accno = request.form['accno']
        username = request.form['username']
        Password = request.form['Password']
        aadhar = request.form['aadhar']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' or AccountNo='" + accno + "'")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cursor = conn.cursor()
            cursor.execute(
                "insert into regtb values('','" + name + "','" + age + "','" + mobile + "','" + email + "','" + address + "','" + accno + "','" + username + "','" + Password + "','nill','waiting','0.00','" + aadhar + "')")
            conn.commit()
            conn.close()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cursor = conn.cursor()
            cursor.execute(
                "insert into multitb values('','" + accno + "','" + username + "')")
            conn.commit()
            conn.close()

        else:
            flash('Already Register Account Number or Username')
            return render_template('NewUser.html')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')

    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Approved'")
    data1 = cur.fetchall()

    return render_template('AdminHome.html', data=data, data1=data1)


@app.route("/Approved")
def Approved():
    try:
        import LiveRecognition as liv
        liv.att()
        del sys.modules["LiveRecognition"]

        id = request.args.get('lid')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute("Update regtb set Status='Active'  where id='" + id + "' ")
        conn.commit()
        conn.close()

        return Approved1()
    except Exception as e:
        flash("Face verification failed. Please try again.")
        return Approved1()


@app.route("/Approved1")
def Approved1():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()

    return render_template('AdminHome.html', data=data, data1=data1)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['Password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:

            session['acc'] = data[6]
            session['aadhar'] = data[12]

            return render_template('Aadhar.html')


@app.route("/verifyaadhar", methods=['GET', 'POST'])
def verifyaadhar():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        session['aadhar'] = aadhar

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where AadharNo='" + aadhar + "' ")
        data = cursor.fetchone()
        if data:
            session['uname'] = data[7]

            uname, Email, Phone, Accountno = loginvales1()

            session['mob'] = Phone

            import random
            n = random.randint(111111, 999999)
            sendmsg(Phone, "Your OTP " + str(n))
            session['otp'] = str(n)
            mmmsg = "Your OTP " + str(n);

            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            fromaddr = "projectmailm@gmail.com"
            toaddr = Email

            # instance of MIMEMultipart
            msg = MIMEMultipart()

            # storing the senders email address
            msg['From'] = fromaddr

            # storing the receivers email address
            msg['To'] = toaddr

            # storing the subject
            msg['Subject'] = "Alert"

            # string to store the body of the mail
            body = mmmsg

            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login(fromaddr, "qmgn xecl bkqv musr")

            # Converts the Multipart msg into a string
            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, toaddr, text)

            # terminating the session
            s.quit()
            return render_template('OTP.html')
        else:
            flash('Aadhar No  is wrong')
            return render_template('Aadhar.html')


def sendmsg(targetno, message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


def loginvales1():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM regtb where username='" + uname + "'")
    data = cursor.fetchone()

    if data:
        Email = data[4]
        Phone = data[3]
        Accountno = data[6]



    else:
        return 'Incorrect username / password !'

    return uname, Email, Phone, Accountno


@app.route("/verifyotp", methods=['GET', 'POST'])
def verifyotp():
    if request.method == 'POST':
        votp = request.form['votp']
        # num = int(session['otp'])

        if str(session['otp']) == votp:
            uname = session['uname']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + uname + "'  ")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data)

        else:
            flash('OTP Incorrect')
            return render_template('OTP.html')


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + uname + "'  ")
    data = cur.fetchall()

    return render_template('UserHome.html', data=data)


@app.route("/ULoanStatus")
def ULoanStatus():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("truncate table temploantb ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from waivertb ")
    data = cursor.fetchall()

    # Check if data exists and print it
    if data:
        for row in data:
            type = row[1]
            Amount = row[2]
            Doc = row[3]
            print(type)
            print(Amount)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from  loantb where type ='" + type + "' and Amt <= '" + Amount + "'  and Status='Active' ")
            row = cursor.fetchall()
            for data1 in row:
                print(data1)
                loanid = data1[0]
                Name = data1[1]
                Mobile = data1[2]
                Email = data1[3]
                Aadhar = data1[4]
                AccNo = data1[5]
                LoanId = data1[6]
                type = data1[7]
                Amt = data1[8]
                date = data1[9]
                Info = data1[10]
                Status = "Eligible"

                print(loanid)

                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='1loanverficationdb')
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * from  temploantb where LoanId ='" + LoanId + "'  ")
                data1 = cursor.fetchone()
                if data1:
                    print("hao")
                else:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1loanverficationdb')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into temploantb values('" + str(
                            loanid) + "','" + Name + "','" + Mobile + "','" + Email + "','" + Aadhar + "','" + AccNo + "','" + LoanId + "','" + type + "','" +
                        str(Amt) + "','" + str(date) + "','" + Info + "','" + Status + "','" + Doc + "')")
                    conn.commit()
                    conn.close()



    else:
        print("No data found.")

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from temploantb  where Aadhar='" + session['aadhar'] + "'")
    data = cursor.fetchall()

    return render_template('ULoanStatus.html', data=data)


@app.route("/Download")
def Download():
    fid = request.args.get('lid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  temploantb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        fname = data[12]

    else:
        return 'Incorrect username / password !'

    filepath = "./static/upload/" + fname

    return send_file(filepath, as_attachment=True)


@app.route("/Action1")
def Action1():
    fid = request.args.get('lid')
    uname = request.args.get('uname')
    session['fid'] = fid

    return render_template('UploadAadhar.html')


@app.route("/uploaaadhar", methods=['GET', 'POST'])
def uploaaadhar():
    if request.method == 'POST':

        aadhar = request.files['file']
        pn = random.randint(1111, 9999)
        file_path = f"static/upload/{pn}.png"
        aadhar.save(file_path)

        reader = easyocr.Reader(['en'])
        img = cv.imread(file_path)
        result = reader.readtext(img)
        del reader

        # Collect all text
        full_text = ' '.join([detection[1] for detection in result])
        print("Full Text:", full_text)

        # Initialize all fields as 'Not Found'
        name = 'Not Found'
        aadhar_number = 'Not Found'
        dob = 'Not Found'
        gender = 'Not Found'

        # Extract Aadhar Number (12 digits)
        aadhar_number_match = re.search(r'\d{4}\s?\d{4}\s?\d{4}', full_text)
        if aadhar_number_match:
            aadhar_number = aadhar_number_match.group().replace(" ", "")

        # Extract DOB (Date of Birth)
        dob_match = re.search(r'\d{2}/\d{2}/\d{4}', full_text)
        if dob_match:
            dob = dob_match.group()

        # Extract Gender
        gender_match = re.search(r'\b(MALE|FEMALE|Male|Female|Transgender|male|female)\b', full_text, re.IGNORECASE)
        if gender_match:
            gender = gender_match.group().title()

        # Improved Name Extraction
        name_patterns = [
            r'Name\s*[:]?\s*([A-Za-z\s\.]+)\b',  # Matches "Name: John Doe" or "Name John Doe"
            r'([A-Z][a-z]+\s[A-Z][a-z]+)\s*(?=\d{2}/\d{2}/\d{4})',  # Matches name before DOB
            r'([A-Z][a-z]+\s[A-Z][a-z]+)\s*(?=(MALE|FEMALE|Male|Female|Transgender))',  # Matches name before gender
            r'^\s*([A-Z][a-z]+\s[A-Z][a-z]+)\s*$'  # Standalone name in a line
        ]

        for pattern in name_patterns:
            name_match = re.search(pattern, full_text, re.IGNORECASE)
            if name_match:
                name = name_match.group(1).strip()
                # Clean up any remaining special characters or numbers
                name = re.sub(r'[^A-Za-z\s\.]', '', name).strip()
                break

        # If still not found, try to find the largest text block that looks like a name
        if name == 'Not Found':
            potential_names = []
            for detection in result:
                text = detection[1].strip()
                # Check if text looks like a name (at least two words, starts with capital letters)
                if re.match(r'^[A-Z][a-z]+\s+[A-Z][a-z]+', text):
                    potential_names.append(text)

            if potential_names:
                # Select the longest potential name
                name = max(potential_names, key=len)

        print("Aadhar Number:", aadhar_number)
        print("Date of Birth:", dob)
        print("Gender:", gender)
        print("Name:", name)

        if aadhar_number == session['aadhar']:

            return render_template('Verfication.html')
        else:
            sendmsg(session['mob'], "unknown User Access your Account..! ")
            flash("AadharCard  Incorrect..!")
            return ULoanStatus()


@app.route("/selectlogin", methods=['GET', 'POST'])
def selectlogin():
    if request.method == 'POST':

        if request.form["submit"] == "Alive":
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cursor = conn.cursor()
            cursor.execute("truncate table temptb")
            conn.commit()
            conn.close()

            import LiveRecognition1  as liv1
            liv1.att()
            del sys.modules["LiveRecognition1"]
            return facelogin()

        elif request.form["submit"] == "Death":

            return render_template('UploadCertificate.html')


@app.route("/facelogin")
def facelogin():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from temptb where UserName='" + uname + "' ")
    data = cursor.fetchone()
    if data is None:

        flash('Face  is wrong')
        return render_template('Verfication.html')


    else:

        # flash('Face  is Correct..!')

        

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
        cursor = conn.cursor()
        cursor.execute("Update loantb set Status='Close' ,Reason='Face' where id='" + session['fid'] + "' ")
        conn.commit()
        conn.close()
        flash("Loan Waived Off Completed..!")
        return UserLoanStatus()


@app.route("/uploddeath", methods=['GET', 'POST'])
def uploddeath():
    if request.method == 'POST':
        aadhar = request.files['file']
        pn = random.randint(1111, 9999)
        file_path = f"static/upload/{pn}.jpeg"
        aadhar.save(file_path)

        #file_path = "WhatsApp Image 2025-05-06 at 11.41.24 AM.jpeg"

        reader = easyocr.Reader(['en'])
        img = cv.imread(file_path)
        result = reader.readtext(img)
        del reader

        full_text = ' '.join([detection[1] for detection in result])
        print("Full Text:", full_text)
        pass

        pattern = r'\b\d{2}-\d{5}-\d{6}\b'

        match = re.search(pattern, full_text)
        if match:
            number = match.group()
            print("Extracted Number:", number)



            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
            cursor = conn.cursor()
            cursor.execute("SELECT * from dtable where dno='" + str(number) + "' ")
            data = cursor.fetchone()

            if data:


                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='1loanverficationdb')
                cursor = conn.cursor()
                cursor.execute(
                    "Update loantb set Status='Close' ,Reason='" + file_path + "' where id='" + session['fid'] + "' ")
                conn.commit()
                conn.close()
                flash("Loan Waived Off Completed..!")

            else:

                flash(" Certificate Number Incorrect..!")



        else:
            print("No matching number found.")
            flash("Loan Waived Off Not Completed Certificate Number Incorrect..!")


        return UserLoanStatus()


@app.route("/UserLoanStatus")
def UserLoanStatus():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1loanverficationdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM loantb where Aadhar='" + session['aadhar'] + "'  ")
    data = cur.fetchall()

    return render_template('UserLoanStatus.html', data=data)


@app.route("/Support")
def Support():
    return render_template('Support.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
