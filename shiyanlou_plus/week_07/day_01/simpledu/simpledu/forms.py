from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import ValidationError

from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import DataRequired as Required

from simpledu.models import db
from simpledu.models import User


class RegisterForm(FlaskForm):
    username = StringField("用户名",
            validators=[Required(message="请填写内容"), Length(3, 24,
                message="密码长度要在3～24个字符之间")])
    email = StringField("邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Required(message="请填写内容"), Length(6, 24,
                message="密码长度要在6～24个字符之间")])
    repeat_password = PasswordField("重复密码",
            validators=[Required(message="请填写内容"), EqualTo("password",
                message="密码不一致")])
    submit = SubmitField("提交")

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError("用户名必须由数字和字母组成")
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("用户名已经存在")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱已经存在")


class LoginForm(FlaskForm):
    username = StringField("用户名",
            validators=[Required(message="请填写内容"), Length(3, 24,
                message="密码长度要在3～24个字符之间")])
    # email = StringField("邮箱",
    #        validators=[Required(message="请填写内容"),
    #            Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Required(message="请填写内容"), Length(6, 24,
                message="请确认您输入的密码")])
    remember_me = BooleanField("记住我")
    submit = SubmitField("提交")

    def validate_username(self, field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError("请输入用户名")

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱未注册")

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError("密码错误")
