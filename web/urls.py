from django.conf.urls import url

from web.views import index

urlpatterns = [
    # 前台首页
    url(r'^$', index.index, name="index"),	#商城首页
    url(r'^list$', index.lists, name="list"),# 商品列表
    #url(r'^list/(?P<pIndex>[0-9]+)$',index.lists,name="list"), #分页商品列表展示
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="detail"),#商品详情

    # 会员及个人中心等路由配置
    url(r'^login$', index.login, name="login"),
    url(r'^dologin$', index.dologin, name="dologin"),
    url(r'^logout$', index.logout, name="logout"),
]