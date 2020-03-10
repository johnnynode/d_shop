from django.conf.urls import url

from web.views import index,cart,orders

urlpatterns = [
    # 前台首页
    url(r'^$', index.index, name="index"),	#商城首页
    url(r'^list$', index.lists, name="list"),# 商品列表
    url(r'^list/(?P<pIndex>[0-9]+)$',index.lists,name="list"), #分页商品列表展示
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="detail"),#商品详情

    # 会员及个人中心等路由配置
    url(r'^login$', index.login, name="login"),
    url(r'^dologin$', index.dologin, name="dologin"),
    url(r'^logout$', index.logout, name="logout"),

    # 购物车路由
    url(r'^cart$', cart.index,name='cart_index'), #浏览购物车
    url(r'^cart/add/(?P<gid>[0-9]+)$', cart.add,name='cart_add'), #添加购物车
    url(r'^cart/del/(?P<gid>[0-9]+)$', cart.delete,name='cart_del'), #从购物车中删除一个商品
    url(r'^cart/clear$', cart.clear,name='cart_clear'), #清空购物车
    url(r'^cart/change$', cart.change,name='cart_change'), #更改购物车中商品数量

    # 订单处理
    url(r'^orders/add$', orders.add,name='orders_add'), #订单的表单页
    url(r'^orders/confirm$', orders.confirm,name='orders_confirm'), #订单确认页
    url(r'^orders/insert$', orders.insert,name='orders_insert'), #执行订单添加操作
]