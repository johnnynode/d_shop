from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.paginator import Paginator

from common.models import Types,Goods
from PIL import Image
from datetime import datetime
import time,json,os

# 浏览商品信息
def index(request, pIndex):
    '''
    # 执行数据查询，并放置到模板中
    list = Goods.objects.all()
    for ob in list:
        ty = Types.objects.get(id=ob.typeid)
        ob.typename = ty.name
    context = {"goodslist":list}
    return render(request,'admin/goods/index.html',context)
    '''

    '''浏览信息'''
    #获取商品类别信息
    tlist = Types.objects.extra(select={'_has':'concat(path,id)'}).order_by('_has')
    for ob in tlist:
        ob.pname = '. . . ' * (ob.path.count(',')-1)

    #获取商品信息查询对象
    mod = Goods.objects
    mywhere=[] #定义一个用于存放搜索条件列表

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword",None)
    if kw:
        # 查询商品名中只要含有关键字的都可以
        list = mod.filter(goods__contains=kw)
        mywhere.append("keyword="+kw)
    else:
        list = mod.filter()
    # 获取、判断并封装商品类别typeid搜索条件
    typeid = request.GET.get('typeid','0')
    if typeid != '0':
        tids = Types.objects.filter(Q(id=typeid) | Q(pid=typeid)).values_list('id',flat=True)
        list = list.filter(typeid__in=tids)
        mywhere.append("typeid="+typeid)
    # 获取、判断并封装商品状态state搜索条件
    state = request.GET.get('state','')
    if state != '':
        list = list.filter(state=state)
        mywhere.append("state="+state)

    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list,5) #以5条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表

    #遍历商品信息，并获取对应的商品类别名称，以typename名封装
    for vo in list2:
        ty = Types.objects.get(id=vo.typeid)
        vo.typename = ty.name
    #封装信息加载模板输出
    context = {'typelist':tlist,"goodslist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere,'typeid':int(typeid)}
    return render(request,"admin/goods/index.html",context)

# 商品信息添加表单
def add(request):
    # 获取商品的类别信息
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    for ob in list:
        ob.pname = '. . . ' * (ob.path.count(',') -1)
    context = {"typelist":list}
    return render(request,'admin/goods/add.html', context)

#执行商品类别信息添加
def insert(request):
    try:
        # 判断并执行图片上传，缩放等处理
        myfile = request.FILES.get("pic", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        # 以时间戳命名一个新图片名称
        filename= str(time.time())+"."+myfile.name.split('.').pop()
        destination = open(os.path.join("./static/goods/",filename),'wb+')
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        # 执行图片缩放
        im = Image.open("./static/goods/"+filename)
        # 缩放到375*375:
        im.thumbnail((375, 375))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/"+filename, 'jpeg')
        # 缩放到220*220:
        im.thumbnail((220, 220))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/m_"+filename, 'jpeg')
        # 缩放到75*75:
        im.thumbnail((75, 75))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/s_"+filename, 'jpeg')

        # 获取商品信息并执行添加
        ob = Goods()
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.content = request.POST['content']
        ob.picname = filename
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':'添加成功！'}
    except Exception as err:
        print(err)
        context = {'info':'添加失败！'}

    return render(request,"admin/info.html",context)

# 执行商品信息删除
def delete(request,gid):
    try:
        # 获取被删除商品信的息量，先删除对应的图片
        ob = Goods.objects.get(id=gid)
        #执行图片删除
        os.remove("./static/goods/"+ob.picname)   
        os.remove("./static/goods/m_"+ob.picname)   
        os.remove("./static/goods/s_"+ob.picname)
        #执行商品信息的删除 
        ob.delete()
        context = {'info':'删除成功！'}
    except Exception as err:
        print(err)
        context = {'info':'删除失败！'}
    return render(request,"admin/info.html",context)

# 打开商品类别信息编辑表单
def edit(request,gid):
    try:
        # 获取要编辑的信息
        ob = Goods.objects.get(id=gid)
        # 获取商品的类别信息
        list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
        # 放置信息加载模板
        context = {"typelist":list,'goods':ob}
        return render(request,"admin/goods/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"admin/info.html",context)

# 执行商品类别信息编辑
def update(request,gid):
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)
            if not myfile:
                return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
            filename = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open(os.path.join("./static/goods/",filename),'wb+')
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()
            # 执行图片缩放
            im = Image.open("./static/goods/"+filename)
            # 缩放到375*375:
            im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/"+filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((220, 220))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/m_"+filename, 'jpeg')
            # 缩放到75*75:
            im.thumbnail((75, 75))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/s_"+filename, 'jpeg')
            b = True
            picname = filename
        else:
            picname = oldpicname
        ob = Goods.objects.get(id=gid)
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.content = request.POST['content']
        ob.picname = picname
        ob.state = request.POST['state']
        ob.save()
        context = {'info':'修改成功！'}
        if b:
            os.remove("./static/goods/m_"+oldpicname) #执行老图片删除  
            os.remove("./static/goods/s_"+oldpicname) #执行老图片删除  
            os.remove("./static/goods/"+oldpicname) #执行老图片删除  
    except Exception as err:
        print(err)
        context = {'info':'修改失败！'}
        if b:
            os.remove("./static/goods/m_"+picname) #执行新图片删除  
            os.remove("./static/goods/s_"+picname) #执行新图片删除  
            os.remove("./static/goods/"+picname) #执行新图片删除  
    return render(request,"admin/info.html",context)