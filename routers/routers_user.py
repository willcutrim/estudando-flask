from views.user_view import (
    UserAllUsersView, UserCreateUserView, UserGetUserView, UserUpdateUserView, UserDeleteUserView,
    UserReativarUserView
)

def router_user(app):
    app.add_url_rule('/users', view_func=UserAllUsersView.as_view('users'))
    app.add_url_rule('/create_users', view_func=UserCreateUserView.as_view('create_users'))
    app.add_url_rule('/user/<int:user_id>', view_func=UserGetUserView.as_view('user'))
    app.add_url_rule('/update_user/<int:user_id>', view_func=UserUpdateUserView.as_view('update_user'))
    app.add_url_rule('/delete_user/<int:user_id>', view_func=UserDeleteUserView.as_view('delete_user'))
    app.add_url_rule('/reativar_user/<int:user_id>', view_func=UserReativarUserView.as_view('reativar_user'))
