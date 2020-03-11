from django.conf.urls import url

from admin.views import index,users,type,goods,orders

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="admin_index"),

    # 后台管理员路由
    url(r'^login$', index.login, name="admin_login"),
    url(r'^dologin$', index.dologin, name="admin_dologin"),
    url(r'^logout$', index.logout, name="admin_logout"),
    url(r'^verify$', index.verify, name="admin_verify"), #验证码

    # 会员信息管理路由
    url(r'^users/(?P<pIndex>[0-9]+)$', users.index, name="admin_users_index"),
    url(r'^users/add$', users.add, name="admin_users_add"),
    url(r'^users/insert$', users.insert, name="admin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="admin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="admin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="admin_users_update"),
    url(r'^users/resetpass/(?P<uid>[0-9]+)$', users.resetpass, name="admin_users_resetpass"),
    url(r'^users/doresetpass/(?P<uid>[0-9]+)$', users.doresetpass, name="admin_users_doresetpass"),

     # 商品类别信息管理路由
    url(r'^type/(?P<pIndex>[0-9]+)$', type.index, name="admin_type_index"),
    url(r'^type/add/(?P<tid>[0-9]+)$', type.add, name="admin_type_add"),
    url(r'^type/insert$', type.insert, name="admin_type_insert"),
    url(r'^type/del/(?P<tid>[0-9]+)$', type.delete, name="admin_type_del"),
    url(r'^type/edit/(?P<tid>[0-9]+)$', type.edit, name="admin_type_edit"),
    url(r'^type/update/(?P<tid>[0-9]+)$', type.update, name="admin_type_update"),

    # 商品信息管理路由
    url(r'^goods/(?P<pIndex>[0-9]+)$', goods.index, name="admin_goods_index"),
    url(r'^goods/add$', goods.add, name="admin_goods_add"),
    url(r'^goods/insert$', goods.insert, name="admin_goods_insert"),
    url(r'^goods/del/(?P<gid>[0-9]+)$', goods.delete, name="admin_goods_del"),
    url(r'^goods/edit/(?P<gid>[0-9]+)$', goods.edit, name="admin_goods_edit"),
    url(r'^goods/update/(?P<gid>[0-9]+)$', goods.update, name="admin_goods_update"),

    #订单管理
    url(r'^orders$', orders.index, name="admin_orders_index"),
    url(r'^orders/(?P<pIndex>[0-9]+)$', orders.index, name="admin_orders_index"),
    url(r'^orders/detail/(?P<oid>[0-9]+)$', orders.detail, name="admin_orders_detail"),
    url(r'^orders/state$',orders.state, name="admin_orders_state"),
]
