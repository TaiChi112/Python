from django.urls import path,include
urlpatterns =[
    path('',include('django.contrib.auth.urls')),
    # path("sign_up/", views.sign_up, name="sign_up"),
    # path("sign_in/", views.sign_in, name="sign_in"),
    # path("profile/", views.profile, name="profile"),
    # path("logout/", views.logout, name="logout"),
    # path("edit_profile/", views.edit_profile, name="edit_profile"),
    # path("change_password/", views.change_password, name="change_password"),
    # path("forgot_password/", views.forgot_password, name="forgot_password"),
    # path("reset_password/", views.reset_password, name="reset_password"),
    # path("reset_password/<str:token>/", views.reset_password, name="reset_password"),
    # path("test/<int:id>/<str:name>/", views.test, name="test"),
    # path("home/", views.home, name="home"),
    # path("product_list/", views.product_list, name="product_list"),
    # path("product_list/product_detail/<int:id>/", views.product_detail, name="product_detail"),
]