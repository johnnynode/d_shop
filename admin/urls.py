from django.conf.urls import url
from admin.views import index

urlpatterns = [
    # 后台首页
    url(r'^$', index, name="admin_index"),
]