from flaskblog import db, app
from flaskblog.models import User, Post

user_1 = User(username='Corey', email='test@mail.com', password='password')
user_2 = User(username='Schafer', email='test1@mail.com', password='password')


with app.app_context():

    # Create Database file
    db.create_all()
    
    # Add User to the Database
    # db.session.add(user_1)
    # db.session.add(user_2)
    # db.session.commit()
    
    # Query to get all the users.
    # print(User.query.all())

    # Query to get the first User
    # print(User.query.first())

    # Filter all the results by filter method
    # print(User.query.filter_by(username='Corey').all())

    # Filter the first result by filter method
    #usr = User.query.filter_by(username='Corey').first()
    # print(usr.id, usr.email)

    
    # usr = db.session.get(User, 1)
    
    # Access user using unique id
    # print(usr)
    # print(usr.posts)
    # print(usr.id)
    
    # Created posts using unique user id 
    # here 2 posts are created by same user.
    # post_1 = Post(title='Blog 1', content='loremipsumkidrisadhaf', user_id=usr.id)
    # post_2 = Post(title='Blog 2', content='post 2', user_id=usr.id)
    # db.session.add(post_1)
    # db.session.add(post_2)
    # db.session.commit()
    
    # for post in usr.posts:
    #     print(post.title)
    
    # post = Post.query.first()
    # print(post.user_id)
    # print(post.author) 
    
    # db.drop_all()
    # print(User.query.all())