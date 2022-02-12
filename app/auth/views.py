from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login_manager
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import Cart, CartProduct, Users
from app.products.models import ProductCategory

auth = Blueprint('auth',
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 static_url_path='/home-static')


@login_manager.user_loader
def load_user(user_id):
    g.user = Users.get_user(user_id)
    return g.user


@auth.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.psw, form.psw.data):
                session['userLogged'] = user.email
                if form.remember.data:
                    login_user(user)
                    session.permanent = True
                else:
                    login_user(user)
                return redirect(url_for('home.index'))
            else:
                flash("User not found", category="error")
        else:
            for error in form.errors.items():
                flash(message=error, category="error")
    return render_template("auth/login.html",
                           categories=ProductCategory.get_all_categories(),
                           form=form,
                           price=CartProduct.get_price_and_count()['price'],
                           count=CartProduct.get_price_and_count()['count'])


@auth.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():
            if form.email.data in [user.email for user in Users.query.all()]:
                flash("Пользователь с таким email зарегистрирован",
                      category="error")
                return render_template("auth/register.html",
                                       title="Register",
                                       form=form)
            try:
                hash_psw = generate_password_hash(form.psw1.data)
                u = Users(email=form.email.data, psw=hash_psw,
                          name=form.name.data, address=form.address.data)
                db.session.add(u)
                db.session.flush()
                cart = Cart(customer_id=u.id)
                db.session.add(cart)
                db.session.commit()
                flash("Success", category="success")
            except Exception as e:
                db.session.rollback()
                print("Ошибка добавления в БД", e)
        else:
            for error in form.errors.items():
                flash(message=error, category="error")

    return render_template("auth/register.html",
                           categories=ProductCategory.get_all_categories(),
                           form=form,
                           price=CartProduct.get_price_and_count()['price'],
                           count=CartProduct.get_price_and_count()['count'])


@auth.route('/logout')
def logout():
    if 'userLogged' in session:
        del session['userLogged']
        session.permanent = False
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('auth.login'))
