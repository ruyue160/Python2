#list是不变数据类型，s.sort时候没有返回值，所以注释的代码写法不正确
s="ajldjlajfdljfddd"
s=set(s)
s=list(s)
s.sort(reverse=False)
#s=s.sort( reverse=False)
res="".join(s)
print(res)
