#利用global在函数声明修改全局变量a=5
def fn():
    global a
    a=4
fn()
print(a)
