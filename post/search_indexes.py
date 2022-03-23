#coding=UTF-8
from haystack import indexes
from post.models import *

#注意格式(模型类名+Index)
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #给title,content设置索引,搜索会从title和content中找
    title = indexes.NgramField(model_attr='title')   #这里框号里面的title以及下面框号里面的content都是models.py
    content = indexes.NgramField(model_attr='content')      #的，要和models.py一一对应

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')