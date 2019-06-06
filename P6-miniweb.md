### WSGI协议，miniweb框架介绍
> 配置服务器，用来处理动态请求。参考 [miniweb服务器]，[miniweb框架]。
miniweb框架用application(environ, start_response)函数处理外部动态请求

[miniweb服务器]: .\P6-miniweb\basic-miniweb\web-server.py
[miniweb框架]: .\P6-miniweb\basic-miniweb\dynamic\mini_web.py

### 闭包: 是一个函数，并且有传递数据的功能
方法1：实例对象：会传递所有参数
instance = NewClass(k, b)
instance(x)  # 会调用__call__
方法2：line函数内的局部变量k, b作为create_y的全局变量传入。

```python
def line(k, b):
    def create_y(x):  # 内部函数使用nonlocal k来改变k，内部直接改变k会出错
        print(k*x+b)
    return create_y  # 返回函数的引用

line1 = line(2, 3)
line1(5)  # 可创建多个
line1(6)
line1(10)
```

### 装饰器：传递函数与数据

```python
# 这个闭包是一个通用装饰器
def sf(func):
    def call_func(*args,**kwargs):
        print("new functions added")
        return func(*args,**kwargs)
    return call_func
    
@sf  # 等价于tes1 = sf(tes1),会直接执行sf（test1）中的代码
def tes1(param):
    print("old function")
    print(param)

tes1 = sf(tes1)  # 前边有@sf，这条就可以删除，原有调用不需修改

tes1(param)
```
多个装饰器由下往上被装载，tes1(param)时由上往下被执行

类装饰器

```python
class Ts(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, par):
        return self.func(par)
        
@Ts  # 等价于tes1 = Ts(tes1),会直接执行Ts（test1）中的代码
def tes1(param):
    print("old function")
    print(param)

tes1(param)
```


```python
# 这个闭包是一个权限限制的装饰器
def setlv(num):
    def sf(func):
        def call_func(*args,**kwargs):
            if num == 1:
                print("you have the privilege to run code in this part")
            print("new functions added")
            return func(*args,**kwargs)
        return call_func
    return sf
    
@setlv(4)  # 会执行tes1 = setlv(num)(tes1),等价于tes1 = sf(tes1)且num=4。
def tes1(param):
    print("old function")
    print(param)

# 此时外界调用时不用也不能,没有权限设置参数
tes1()
```

### url类型
静态url：类似.html，每个网页都有真实的物理地址
动态url：带有？id=5，是逻辑地址，不存在于服务器硬盘中
SEO：搜索引擎优化
伪静态（url rewrite）：和静态url类似，其实是动态伪装成静态
缺点：服务器要支持重写规则，负担增加。可以robots禁止掉动态地址