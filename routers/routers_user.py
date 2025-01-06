from views.user_view import (
    AllUsersView, CreateUserView, GetUserView, UpdateUserView, DeleteUserView,
    TestDbView, ReativarUserView
)

def router_user(app):
    app.add_url_rule('/users', view_func=AllUsersView.as_view('users'))
    app.add_url_rule('/create_users', view_func=CreateUserView.as_view('create_users'))
    app.add_url_rule('/user/<int:user_id>', view_func=GetUserView.as_view('user'))
    app.add_url_rule('/update_user/<int:user_id>', view_func=UpdateUserView.as_view('update_user'))
    app.add_url_rule('/delete_user/<int:user_id>', view_func=DeleteUserView.as_view('delete_user'))
    app.add_url_rule('/reativar_user/<int:user_id>', view_func=ReativarUserView.as_view('reativar_user'))
    app.add_url_rule('/test_db', view_func=TestDbView.as_view('test_db'))
