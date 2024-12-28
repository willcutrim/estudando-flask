from controllers.user_controller import AllUsers, CreateUser

def router_user(app):
    app.add_url_rule('/users', view_func=AllUsers.as_view('users'))
    app.add_url_rule('/create_users', view_func=CreateUser.as_view('create_users'))
