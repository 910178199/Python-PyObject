# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test

# 数据库操作

#增
def insert(request):
    test1 = Test(name='runboot')
    test1.save()
    return HttpResponse("<p>数据添加成功!</p>")

#删
def delete(request):
    test1 = Test.objects.get(id = 1)
    test1.delete()

    #删除方式1
    # Test.objects.filter(id=1).delect()

    #删除所有
    # Test.objects.all.delect()
    return HttpResponse("<p>删除成功</p>")


#改
def update(request):
    #修改其中一个id=1的name字段，在save，相当于sql中的update
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    #另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    #修改所有的
    # Test.objects.all().update(name = 'Google')

    return HttpResponse("<p>修改成功</p>")



#查
def query(request):
    # 初始化
    response = ""
    response1 = ""

    # 获取所有数据行
    list = Test.objects.all()

    # filter相当于SQL中的Where,可设置过滤条件
    response2 = Test.objects.filter(id=1)
    # list = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # list = Test.objects.get(id=1)

    # 限制返回的数据 相当于SQL中的OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    # list = Test.objects.order_by('name')[0:10]

    # 数据排序
    Test.objects.order_by("id")
    # list = Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += str(var.id) + " "+var.name + "</br>"
    response = response1
    return HttpResponse("<p>"+response+"</p>")

