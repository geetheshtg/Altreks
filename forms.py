from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, InputRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    phone = StringField('Phone number', validators=[Length(min=10, max=10)])
    register = SubmitField('Register')


class RequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    date = StringField('Date', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    examid = StringField('Exam-ID', validators=[DataRequired()])
    slot = SelectField('Slot', choices=[('Forenoon', 'Forenoon'), ('Afternoon', 'Afternoon')])
    submit = SubmitField('Submit')


class ContactUs(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    feedback = SelectField(choices=[('feedback', 'Feedback'), ('bug', 'Report bug')])
    message = TextAreaField()
    sendres = BooleanField('Send me a copy of this message')
    submit = SubmitField('Submit')


class ScheduleForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    # date = DateField('Date', format='%d/%m/%Y', validators=[DataRequired()])
    # time = TimeField('Time', format='%h-%m', validators=[InputRequired()])
    date = StringField('Date', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    examid = StringField('Exam-ID', validators=[DataRequired()])
    slot = SelectField('Slot', choices=[('Forenoon', 'Forenoon'), ('Afternoon', 'Afternoon')])
    submit = SubmitField('Submit')


class Availability(FlaskForm):
    availability = SelectField(
        choices=[('Available', 'Available'), ('Not Available', 'Not Available')])
    examid = StringField('Exam-ID', validators=[DataRequired()])
    slot = SelectField('Slot', choices=[('Forenoon', 'Forenoon'), ('Afternoon', 'Afternoon')])
    change = SubmitField('Change Availability')


class ApproveRequest(FlaskForm):
    emailf = StringField("Requester's Email:", validators=[DataRequired(), Email()])
    emailt = StringField("Substitute's Email", validators=[DataRequired(), Email()])
    examid = StringField('Exam-ID', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    slot = SelectField('Slot', choices=[('Forenoon', 'Forenoon'), ('Afternoon', 'Afternoon')])
    approval = SelectField('Approval', choices=[('Y', 'Y'), ('N', 'N')])
    submit = SubmitField('Submit')
