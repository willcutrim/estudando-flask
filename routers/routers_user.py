from controllers.user_controller import (
    AllUsers, CreateUser, GetUser, UpdateUser, DeleteUser,
    TestDb, ReativarUser
)

def router_user(app):
    app.add_url_rule('/users', view_func=AllUsers.as_view('users'))
    app.add_url_rule('/create_users', view_func=CreateUser.as_view('create_users'))
    app.add_url_rule('/user/<int:user_id>', view_func=GetUser.as_view('user'))
    app.add_url_rule('/update_user/<int:user_id>', view_func=UpdateUser.as_view('update_user'))
    app.add_url_rule('/delete_user/<int:user_id>', view_func=DeleteUser.as_view('delete_user'))
    app.add_url_rule('/reativar_user/<int:user_id>', view_func=ReativarUser.as_view('reativar_user'))
    app.add_url_rule('/test_db', view_func=TestDb.as_view('test_db'))
