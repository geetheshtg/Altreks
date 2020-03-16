# Package Imports
from flask import Flask, render_template, redirect, url_for, flash, session, g, request

from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, RegisterForm, ContactUs, ScheduleForm, Availability, RequestForm, ApproveRequest

from db_ops import StoreData, Validation, AddSchedule, ViewSchedule, ViewAllSchedule, changeAvailability, ViewRequests, Viewfdb, ViewAvailable, RequestSwap, ReqStat, ApproveReq

import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey148-3tothe3tothe6tothe9'


cur_user = ''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactUs()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        msg = form.message.data
        conn = sqlite3.connect('db\\exam.db')
        print("connected")
        cl = conn.cursor()
        cl.execute(f'''
        insert into fdbk values('{email}','{name}','{msg}')
                ''')
        conn.commit()
        return "FeedBack sent successfully", render_template("contact.html", form=form)
        # return "The feedback has been submitted"
    return render_template("contact.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('user', None)
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.email.data, form.password.data
        res = Validation(email, password)
        if res == "Login success" and email != "admin@gmail.com":
            flash(res)
            session['user'] = globals()['cur_user'] = email
            return render_template("user.html", name=globals()['cur_user'], ddtext='Modules')
        elif res == "Login success" and email == "admin@gmail.com":
            flash(res)
            session['user'], globals()['cur_user'] = email, "admin"
            return redirect(url_for("admin"))
            # return render_template("admin.html", name=globals()['cur_user'])
        elif res == "Wrong Password":
            flash(res)
            return redirect(url_for("login"))
        else:
            flash("Email does not exist.\nCreate account")
            return redirect(url_for("register"))
    return render_template('login.html', form=form, ddtext='Modules')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email, fname, lname, pno = form.email.data, form.firstname.data, form.lastname.data, form.phone.data
        password = generate_password_hash(form.password.data)
        res = StoreData(email, fname, lname, pno, password)
        if res == "User Registered Successfully":
            flash(res)
            return redirect(url_for('login'))
        else:
            flash("Unable to create User")
            return redirect(url_for("register"))
    return render_template('register.html', form=form)

# user form functionalities below
@app.route('/user')
def user():
    if g.user:
        return render_template('user.html', ddtext='Modules')
    return redirect(url_for("login"))


@app.route('/user/view_slot')
def view_slot():
    email = globals()['cur_user']
    if email == '':
        flash("Login as user to view schedule.")
        return redirect(url_for('login'))
    else:
        lis = ViewSchedule(email)  # list of list containing schedules
        return render_template('display_slot.html', lis=lis, email=email, ddtext='View Slot')


@app.route('/user/view_available')
def viewAvailable():
    email = globals()['cur_user']
    if email == '':
        flash("Login as user to view schedule.")
        return redirect(url_for('login'))
    else:
        lis = ViewAvailable(email)  # list of list containing schedules
        return render_template('view_available.html', lis=lis, ddtext='View Available Faculty')


@app.route('/user/request_swap', methods=['GET', 'POST'])
def RequestSwapp():
    email1 = globals()['cur_user']
    if email1 == '':
        flash("Login as user to view schedule.")
        return redirect(url_for('login'))
    else:
        form = RequestForm()
        if form.validate_on_submit():
            email, examid, date, time, slot = form.email.data, form.examid.data, form.date.data, form.time.data, form.slot.data
            if email != email1:
                print(email, examid, date, time, slot)
                res = RequestSwap(email1, email, examid, date, time, slot)
                flash(res)
                return redirect(url_for("RequestSwapp"))
            elif email == email1:
                flash("you can't enter your own email!")
                return redirect(url_for("RequestSwapp"))
        return render_template('request_swap.html', form=form, ddtext='Request Swap')


@app.route("/user/view_req_stat")
def viewreqstatus():
    email = globals()["cur_user"]
    if email == '':
        flash("Login to view request status")
        return redirect(url_for("login"))
    else:
        lis = ReqStat(email)
        return render_template('reqstat.html', lis=lis, ddtext="View Request Status")


@app.route("/user/availability", methods=['GET', 'POST'])
def availability():
    email = globals()['cur_user']
    if email == '':
        flash("Login as user to change availability.")
        return redirect(url_for('login'))
    else:
        form = Availability()
        if form.validate_on_submit():
            examid = form.examid.data
            slot = form.slot.data
            availability = form.availability.data
            email = globals()['cur_user']
            changeAvailability(email, examid, slot, availability)
            flash("updated availability")
            return redirect(url_for("availability"))
        return render_template('availability.html', form=form, ddtext='Change Availability')

# admin form functionalities below
@app.route('/admin')
def admin():
    if g.user:
        return render_template('admin.html', ddtext='modules')
    return redirect(url_for("login"))


@app.route('/admin/add_slot', methods=["GET", "POST"])
def addSchedule():
    if globals()['cur_user'] == "admin":
        form = ScheduleForm()
        if form.validate_on_submit():
            email, date, time, examid, slot = form.email.data, form.date.data, form.time.data, form.examid.data, form.slot.data
            res = AddSchedule(email, date, time, examid, slot)
            flash(res)
            return redirect(url_for("addSchedule"))
        return render_template('add_slot.html', form=form, ddtext='Add Slot')
    else:
        flash("Login as admin to add schedule.")
        return redirect(url_for("login"))


@app.route('/admin/view_all_schedule')
def viewAllSchedule():
    email = globals()['cur_user']
    if email != 'admin':
        flash("Login as admin to view schedule.")
        return redirect(url_for('login'))
    else:
        lis = ViewAllSchedule()  # list of list containing schedules
        return render_template('display_all_schedule.html', lis=lis, ddtext='View All Schedules')


@app.route('/admin/view_request')
def viewRequest():
    email = globals()['cur_user']
    if email != 'admin':
        flash("Login as admin to view schedule.")
        return redirect(url_for('login'))
    else:
        lis = ViewRequests()  # list of list containing schedules
        return render_template('view_request.html', lis=lis, ddtext='View Request')


@app.route('/admin/view_requests')
def viewRequests():
    email = globals()['cur_user']
    if email != 'admin':
        flash("Login as admin to view requests.")
        return redirect(url_for('login'))
    else:
        lis = Viewfdb()  # list of list containing schedules
    return render_template('display_requests.html', lis=lis, ddtext='View All Request')


@app.route('/admin/view_fdb')
def viewfdb():
    email = globals()['cur_user']
    if email != 'admin':
        flash("Login as admin to view requests.")
        return redirect(url_for('login'))
    else:
        conn = sqlite3.connect("exam.db")
        cursor = conn.execute("SELECT email,name,feedback FROM fdbk")
        lis = list()
        for row in cursor:
            temp = [
                row[0],  # email
                row[1],  # name
                row[2]  # feeback
            ]
            lis.append(temp)  # list of list containing schedules
    return render_template('display_fdb.html', lis=lis, ddtext='View Feedback')


@app.route('/admin/app_req', methods=["GET", "POST"])
def approve():
    email = globals()['cur_user']
    if email != 'admin':
        flash("Login as admin to view requests.")
        return redirect(url_for('login'))
    else:
        form = ApproveRequest()
        if form.validate_on_submit():
            emailf, emailt, eid, date, time, slot, approval = form.emailf.data, form.emailt.data, form.examid.data, form.date.data, form.time.data, form.slot.data, form.approval.data
            # print(emailf, emailt, eid, time, slot, approval)
            res = ApproveReq(emailf, emailt, eid, date, time, slot, approval)
            flash(res)
            return redirect(url_for("approve"))
        return render_template("approve.html", form=form, ddtext='Approve Request')


# @app.route('/guest')
# def guest():
#     return render_template('user.html', ddtext='Modules')
#
#
# @app.route('/guest2')
# def guest2():
#     email = 'ashwin99@gmail.com'
#     lis = ViewSchedule(email)  # list of list containing schedules
#     return render_template('display_slot.html', lis=lis, email=email, ddtext='View Slot')
#
#
# @app.route('/guest3', methods=['GET', 'POST'])
# def guest3():
#     email = 'ashwin99@gmail.com'
#     lis = ViewSchedule(email)  # list of list containing schedules
#     form = Availability()
#     if form.validate_on_submit():
#         availability = form.availability.data
#         changeAvailability(email, availability)
#         flash("updated availability")
#         return redirect(url_for("guest3"))
#     return render_template('availability.html', form=form, ddtext='Availability Status')
#
#
# @app.route('/guest4')
# def viewAvailable1():
#     email = 'ashwin99@gmail.com'
#     lis = ViewAvailable()
#     return render_template('view_available.html', lis=lis, ddtext='View Available')

# other session handling code below
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    globals()['cur_user'] = ''
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
