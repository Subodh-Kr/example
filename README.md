example
=======

An example project to help in teaching basics of Django.

1. In your nitrous instance, type the following in the terminal: git clone https://github.com/The-WebOps-Club/example.git
2. Now, you have the example code in a folder called 'example'
3. Then execute: python manage.py syncdb
This will create 'example.db' file and create all the required tables. When you make a new app, make sure you include in the INSTALLED_APPS list in 'settings.py'
4. Now you can do: python manage.py runserver 0.0.0.0:4000
This will run your server and you can view it by going to Preview>Port 4000 in Nitrous menu bar.
5. After this, change the code as you want and test it out.
6. The sequence of actions:
    i.  First check if you have got your models correctly. If there is any error, your tables will not get created when u run syncdb. Remember that it is Case-sensitive and hence you should use CharField and not charfield
    ii. If there is any error, try to google them and fix it. Otherwise, you can reply in the thread with a screenshot of the error.
    iii.Improvise on what's given and implement as many features as you can :)

All the best!