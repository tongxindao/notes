# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import TextAreaField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import ValidationError

from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import URL
from wtforms.validators import NumberRange
from wtforms.validators import DataRequired as Required

from simpledu.models import db
from simpledu.models import User
from simpledu.models import Live
from simpledu.models import Course


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


class CourseForm(FlaskForm):
    name = StringField("课程名称",
            validators=[Required(message="请填写内容"), Length(5, 32,
                message="内容要在5～32个字符之间")])
    description = TextAreaField("课程简介",
            validators=[Required(message="请填写内容"), Length(20, 256,
                message="内容要在20～256个字符之间")])
    image_url = StringField("封面图片",
            validators=[Required(message="请选择图片"), URL(
                message="请填入合法链接")])
    author_id = IntegerField("作者ID",
            validators=[Required(message="请填写内容"),
                NumberRange(min=1, message="无效的用户ID")])
    submit = SubmitField("提交")

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError("用户不存在")

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course


class LiveForm(FlaskForm):
    name = StringField("直播名称",
            validators=[Required(message="请填写内容"), Length(15, 128,
                message="内容要在1～128个字符之间")])
    user_id = IntegerField("直播用户ID",
            validators=[Required(message="请填写内容"),
                NumberRange(min=1, message="无效的直播用户ID")])
    submit = SubmitField("提交")

    def validate_user_id(self, field):
        if not User.query.get(self.user_id.data):
            raise ValidationError("用户ID不存在")

    def validate_name(self, field):
        if Live.query.get(self.name.data):
            raise ValidationError("直播地址重复")

    def create_live(self):
        live = Live()
        self.populate_obj(live)
        db.session.add(live)
        db.session.commit()
        return live

    def update_live(self, live):
        self.populate_obj(live)
        db.session.add(live)
        db.session.commit()
        return live


class MessageForm(FlaskForm):
    message = StringField("系统消息",
            validators=[Required(message="请填写内容"), Length(3, 256,
                message="密码长度要在3～256个字符之间")])
    submit = SubmitField("提交")
