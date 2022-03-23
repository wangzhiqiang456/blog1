#coding = utf-8
from django.db import connection
from django.db.models import Count

from post.models import Post

#分类
def getRightInfo(request):

    #获取分类信息
    r_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')
                                     #以类别名称和类别进行分组           #计算每一类的记录数量        #以记录数进行降序排列
    #获取近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]  #切片[:3]是去取近期的前三篇文章

    #获取日期归档信息
    cursor = connection.cursor()       #下方的c即count('*')改名为c    下面的sql语句是日期/时间转换为字符串
    cursor.execute("select created,count('*') c from t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c desc,created desc")
    r_filepost = cursor.fetchall()  #获取所有
    return({'r_catepost':r_catepost,'r_recpost':r_recpost,'r_filepost':r_filepost})
