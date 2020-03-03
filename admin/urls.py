from django.conf.urls import url
from admin.views import index, users

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="admin_index"),
    # 后台用户管理
    url(r'^users$', users.index, name="admin_users_index"),
    url(r'^users/add$', users.add, name="admin_users_add"),
    url(r'^users/insert$', users.insert, name="admin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="admin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="admin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="admin_users_update"),

    # 后台管理员路由
    url(r'^login$', index.login, name="admin_login"),
    url(r'^dologin$', index.dologin, name="admin_dologin"),
    url(r'^logout$', index.logout, name="admin_logout"),
]