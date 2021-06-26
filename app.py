from fiverr import app

if __name__ == '__main__':
    app.run(debug=False)


@app.cli.command()
def saveadminuser():
    from fiverr.models import User
    from fiverr import db, bcrypt

    hashed_password = bcrypt.generate_password_hash("admin").decode('utf-8')
    admin = User(username="admin", email="admin@admin.com",
                 password=hashed_password, is_admin=True)
    db.session.add(admin)
    db.session.commit()


@app.cli.command()
def dummyuser():
    from fiverr.models import User
    from fiverr import db, bcrypt

    hashed_password1 = bcrypt.generate_password_hash("abc1").decode('utf-8')
    hashed_password2 = bcrypt.generate_password_hash("abc2").decode('utf-8')
    freelancer1 = User(username='freelancer1',
                   email="freelancer1@mail.com", password=hashed_password1)
    freelancer2 = User(username='freelancer2',
                   email="freelancer2@mail.com", password=hashed_password2)
    db.session.add(freelancer1)
    db.session.add(freelancer2)
    db.session.commit()


@app.cli.command()
def dummypost():
    from fiverr.models import User, Post
    from fiverr import db
    post1 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer1@mail.com')
                            .first().id)
    post2 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="one of the best places when you can find talented logo\
                designers, with a natural talent and ability to listen, to\
                absorb and visualize the needs of their clients. They give\
                you the possibility to choose from 2 kind of logos, in\
                different formats, different sizes a lifetime support\
                and if you don’t like it you can take your money back with\
                100 percentage guarantee.",
                category="Graphics & Design",
                price="100",
                user_id=User.query
                            .filter_by(email='freelancer2@mail.com')
                            .first().id)
    post3 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer2@mail.com')
                            .first().id)
    post4 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer2@mail.com')
                            .first().id)

    post5 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer1@mail.com')
                            .first().id)
    post6 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="one of the best places when you can find talented logo\
                designers, with a natural talent and ability to listen, to\
                absorb and visualize the needs of their clients. They give\
                you the possibility to choose from 2 kind of logos, in\
                different formats, different sizes a lifetime support\
                and if you don’t like it you can take your money back with\
                100 percentage guarantee.",
                category="Graphics & Design",
                price="100",
                user_id=User.query
                            .filter_by(email='freelancer2@mail.com')
                            .first().id)
    post7 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer1@mail.com')
                            .first().id)
    post8 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer1@mail.com')
                            .first().id)
    post9 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer2@mail.com')
                            .first().id)
    post10 = Post(title="I Will Do 2 Minimalist Logo Design",
                content="Hello there! I am srk, a professional graphic artist with\
                having experience of 8 years in the industry and I welcome you\
                to my gig for Brand guide and logo design. I have created this\
                gig to give a boost to your brand which is possible by having\
                a perfect logo design + brand style guide + stationary.",
                category="Graphics & Design",
                price="500",
                user_id=User.query
                            .filter_by(email='freelancer1@mail.com')
                            .first().id)

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.commit()
