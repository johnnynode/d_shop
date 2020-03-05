from django.conf.urls import url
from admin.views import index, users, type, goods

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
    url(r'^verify$', index.verify, name="admin_verify"), #验证码

    # 后台商品类别信息管理
    url(r'^type$', type.index, name="admin_type_index"),
    url(r'^type/add/(?P<tid>[0-9]+)$', type.add, name="admin_type_add"),
    url(r'^type/insert$', type.insert, name="admin_type_insert"),
    url(r'^type/del/(?P<tid>[0-9]+)$', type.delete, name="admin_type_del"),
    url(r'^type/edit/(?P<tid>[0-9]+)$', type.edit, name="admin_type_edit"),
    url(r'^type/update/(?P<tid>[0-9]+)$', type.update, name="admin_type_update"),

    # 后台商品信息管理
    url(r'^goods/(?P<pIndex>[0-9]+)$', goods.index, name="admin_goods_index"),
    url(r'^goods/add$', goods.add, name="admin_goods_add"),
    url(r'^goods/insert$', goods.insert, name="admin_goods_insert"),
    url(r'^goods/del/(?P<gid>[0-9]+)$', goods.delete, name="admin_goods_del"),
    url(r'^goods/edit/(?P<gid>[0-9]+)$', goods.edit, name="admin_goods_edit"),
    url(r'^goods/update/(?P<gid>[0-9]+)$', goods.update, name="admin_goods_update"),
]