# Flask Toy Project

## Aim

You will implement the requirements which is written in the [USER-STORIES.md](https://gitlab.com/mountblue/cohort-14-python/rakshit_sarkheliya/flask-toy-project/-/blob/master/USERSTORIES.md).

## Requirements

* You have require a any browser like Chrome,Firefox,safari etc.
* Require internet connectivity.
* All requirements and dependencies run `pip3 install -r requirements.txt`

## How to run project

* Clone a repository in your system `git@gitlab.com:mountblue/cohort-14-python/rakshit_sarkheliya/flask-toy-project.git`

* You need to open postgres using this command `sudo -u postgres psql`

* Create a Role and Database in postgres using this script `\i script/createhelper.sql`

* Run command `export FLASK_APP=app.py` in the repository folder which register flaskapp.

* Run command `flask db upgrade` in the repository folder which create tables.

* Run command `flask saveadminuser` in the repository folder which create adminuser.

* Run command `flask dummyuser` in the repository folder which create dummyusers.

* Run command `flask dummypost` in the repository folder which create dummyposts.

* Run command `flask run` in the repository folder which run flask app.

* Open url [http://127.0.0.1:5000/] in Browser.

* Delete a Role and Database in postgres using this script `\i script/drophelper.sql`

### login as admin please login with:

* Email : admin@admin.com
* Password: admin

## Screenshot

1. Home Page <br>
<img src = "fiverr/static/webapp_img/homepage.png">

2. Registration Page<br>
<img src = "fiverr/static/webapp_img/register.png">

3. Login Page<br>
<img src = "fiverr/static/webapp_img/login.png">

4. User Dashbord Page<br>
<img src = "fiverr/static/webapp_img/currentuser_dash.png">

5. Account Page<br>
<img src = "fiverr/static/webapp_img/useraccount.png">

6. Create newpost Page<br>
<img src = "fiverr/static/webapp_img/createpost.png">
   
7. Admin home Page <br>
<img src = "fiverr/static/webapp_img/admin_home.png">

8. Admin freelancerlist Page <br>
<img src = "fiverr/static/webapp_img/freelancerlist.png">




