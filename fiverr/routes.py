import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from fiverr import app, db, bcrypt
from fiverr.forms import (RegistrationForm,
                          LoginForm,
                          UpdateAccountForm,
                          PostForm)
from fiverr.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    '''
    Set home route
    '''
    # Featch all freelancer post
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    '''
    Create new freelancer account
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Password can decrypt and check in database using bcrypt
        hashed_password = bcrypt.generate_password_hash(form.password.data).\
            decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You able to login', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Freelancer can login and go home page
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if (user and bcrypt.check_password_hash(
                user.password, form.password.data)):
            if user.is_admin:
                login_user(user, remember=True)
                return redirect(url_for('home_admin'))
            else:
                if not user.is_valid:
                    flash('You have been block buy admin', 'danger')
                    return redirect(url_for('home'))
                else:
                    login_user(user, remember=True)
                    next_page = request.args.get('next')
                    return redirect(next_page) if next_page else redirect(
                        url_for('home'))

        else:
            flash('Login Unsuccessful.\
                 Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    ''' User can logout '''
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    '''
    Save profilepic profile_pics directory and resize image
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    '''
    Account in show the user information
    '''
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.user_image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    user_image_file = url_for(
        'static',
        filename='profile_pics/' + current_user.user_image_file)
    return render_template(
        'account.html',
        title='account',
        user_image_file=user_image_file,
        form=form)


def save_post_img(form_picture):
    '''
    Save post_pics in post_pics directory and image resize
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/post_pics', picture_fn)

    output_size = (680, 393)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    Freelancer can create new post
    '''
    form = PostForm()
    if form.validate_on_submit():
        if form.post_image.data:
            picture_file = save_post_img(form.post_image.data)
            post = Post(
                title=form.title.data,
                post_image_file=picture_file,
                content=form.content.data,
                category=form.category.data,
                author=current_user,
                price=form.price.data)
        else:
            post = Post(
                title=form.title.data,
                content=form.content.data,
                category=form.category.data,
                author=current_user,
                price=form.price.data)

        db.session.add(post)

        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='Create Post', form=form)


@app.route("/post/<int:post_id>")
def post(post_id):
    '''
    Show the post
    '''
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    '''
    Update previous post
    '''
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.post_image.data:
            picture_file = save_post_img(form.post_image.data)
            post.title = form.title.data
            post.content = form.content.data
            post.post_image_file = picture_file
            post.category = form.category.data
            post.price = form.price.data
            db.session.commit()
            flash('Your post has been updated!', 'success')
            return redirect(url_for('post', post_id=post.id))
        else:
            post.title = form.title.data
            post.content = form.content.data
            post.category = form.category.data
            post.price = form.price.data
            db.session.commit()
            flash('Your post has been updated!', 'success')
            return redirect(url_for('post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.category.data = post.category
        form.price.data = post.price
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    '''
    Delete post
    '''
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/dashboard")
@login_required
def dashboard():
    '''
    Show the currentuser post detail
    '''
    posts = Post.query.filter_by(author=current_user)\
        .order_by(Post.date_posted.asc())
    return render_template('dashboard.html', posts=posts, user=current_user)


@app.route("/user/<string:username>")
def user_posts(username):
    '''
    Show the particular user post detail
    '''
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\

    return render_template('dashboard.html', posts=posts, user=user)


@app.route("/home-admin", methods=['GET', 'POST'])
@login_required
def home_admin():
    '''
    Show the addmin homepage
    '''
    if current_user.is_admin:
        countuser = db.session.query(User).count()
        countuser -= 1
        countpost = db.session.query(Post).count()
        return render_template(
            'home_admin.html',
            title="Admin-home", countuser=countuser, countpost=countpost)
    else:
        abort(403)


@app.route("/freelancerlist", methods=['GET', 'POST'])
@login_required
def user_list():
    '''
    Only admin can show the all freelancer list
    '''
    if current_user.is_admin:
        users = User.query.filter(User.id != current_user.id)
        return render_template(
            'freelancerlist.html', title="Freelancers Detail", users=users)
    else:
        abort(403)


@app.route("/freelancerpost", methods=['GET', 'POST'])
@login_required
def user_post_list():
    '''
    admin can show the all post list
    '''
    if current_user.is_admin:
        posts = Post.query.all()
        return render_template(
            'freelancerpost.html', title="Freelancers Posts", posts=posts)

    else:
        abort(403)


@app.route("/userlist/<int:user_id>/", methods=['POST'])
@login_required
def user_vailded(user_id):
    '''
    admin can block user
    '''
    user = User.query.get_or_404(user_id)
    if current_user.is_admin:
        if user.is_valid:
            user.is_valid = False
            db.session.commit()
            flash('Your user has been Block', 'danger')
        else:
            user.is_valid = True
            db.session.commit()
            flash('Your user has been Unblock', 'success')
    return redirect(url_for('user_list_admin'))


@app.errorhandler(404)
def pagenotfound(error):
    '''
    Errorhandler 404
    '''
    return render_template('error.html', errortype="404",
                           title='Page Not Found'), 404


@app.errorhandler(403)
def error_403(error):
    '''
    Errorhandler 403
    '''
    return render_template('error.html', errortype="403",
                           title="You can't access page"), 403


@app.errorhandler(500)
def error_500(error):
    '''
    Errorhandler 500
    '''
    return render_template('error.html', errortype="403",
                           title='Something go wrong'), 500
