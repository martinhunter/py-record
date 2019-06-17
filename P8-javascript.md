事件： onclick, onmouseover

解决兼容性问题：document.getElementById('div1')而不直接使用div1

设置变量： var oVarname = document.getElementById('div1')

onmouseover="document.getElementById('div1').display='none';"

<script>
  function func_name(){
  document.getElementById('div1').display='none';
  }
</script>
onmouseover="func_name()"

#### 操作属性
传入的参数name和value都是值，name不能直接传入style.name，需要加[]。
所有以.property调用的属性都可用['property']代替
function setStyle(name, value){
  var oDiv=document.getElementById('div1');
  oDiv.style.name=value; /\*此处的name是style的属性而非传入的变量name\*/
  oDiv.style.['name']=value; /\*此处的name依然是style的属性而非传入的变量name\*/
  oDiv.style.[name]=value; /正确方法：\*变量name可以当作style的属性使用\*/
}
onclick="setStyle('width', '400px')"
  
#### 提取行间事件：
oBtn.clock=func_name;
oBtn.clock=function(){
}

window.onload=function(){}  页面加载完成后运行
aDiv=document.getElementByTagName('div') 获得一个数组
aDiv[0].style.background='red' 选取数组中的1个元素
aDiv[i].index=i 设置元素的序列
 
this: 当前发生事件的元素
aBtn[i].onclick=function(){
  for(var i=0;i<aBtn.length;i++){
  aBtn[i].className='';
  }
  this.className='active';
};

aBtn[i].innerHTML='<h2>'+(this.index+1)+'月活动</h2><p>'+cont[this.index]+'</p>';

***

***

### 数据类型
interger(i)
function(fn)
object(o)
array(a)
regexp(re)
variant(v)

数字类型转换：往右直到非数字。parseInt(var_name),parseFloat()
判断是否为数字： isNaN()

#### 函数传参
arguments等同于python中的args，是一个数组。
arguments.length

取非行间样式（不能用来设置）
* obj.currentStyle[attr]  // 仅适用IE
* getComputedStyle(obj, false)[attr]  // false处可以是任意值。

#### 数组的使用
定义： var arr=[12, 8, 5, 9];
属性： arr.length=0; 可以清空数组

arr.push(element); 从尾部添加
arr.unshift(element); 从头部添加
arr.pop(element); 从尾部删除
arr.shift(element); 从头部删除
arr.splice(起始位置, 要删除的元素数量,'要添加的元素1' ,'要添加的元素2','要添加的元素3');
arr.sort(function(n1, n2){return n1-n2;}); 返回值负数则前后不交换，否则交换来达到排序的目的
arr.concat(arr2); 连接2个数组
arr.join(分隔符);  元素组成字符串

### 变量类型
number、string‘boolean、undefined、object、array、function

类型抓换 parseInt(var)

字符串兼容性问题：
str[0]改为str.charAt(0)

***

## DOM(document)
标签=元素=节点

选取子节点-> children
选取父节点-> parentNode
获得由position属性的父节点对象（默认为body）：offsetParent

选取首尾节点：firstElementChild,lastElementChild
选取相邻节点：nextElementSibling，previousElementSibling


```html
<script>
    var oUl=document.getElementById('uul');
    oUl.childNodes[i].nodeType;  //childNodes有兼容性问题
    oUl.children[i].nodeType;  //只取元素节点，无兼容性问题
    oUl.children[i].style.width='200px';
    //nodeType==3 -> 文本节点
    //nodeType==1 -> 元素节点
    
    if(oUl.firstElementChild){
        oUl.firstElementChild.style.width='200px'  //用于chrome，IE9
    }
    else{
        oUl.firstChild.style.width='200px'  //用于IE7
    }
    
    //获取子节点中所有符合类名的元素
    function gbClass(oParent, sClass){
        var aResult=[];
        var aEle=oParent.getElementByTagName('*');  // *获得所有
        for(var i=0;i<aEla.length; i++){
            if(aEle[i].className==sClass){
                aResult.push(aEle[i]);
            }
        }
        return aResult;
    }
    
    var aClassNeeded=gbClass(oUl, 'oneClass');
</script>
<body>
    asbda  ->文本节点
    <div></div>  -> 元素节点
</body>
```

操纵元素属性3种方式：
* oDiv.style.display="block"
* oDiv.style["display"]="block"
* oDiv.setAttribute("display","block")

获取：getAttribute("display")
移除：removeAttribute("display")

### 插入元素（改变了innerHTML）
父级创建子节点： document.createElement('li');
父级插入子节点（到最后，会先把元素从原有父节点删除，然后插入新父节点，也可以是原有父节点）： oLis.appendChild(oLis); 
父级插入子节点（再制定位置前）： oUl.insertBefore(新节点,在谁之前); 
父级删除子节点： oUl.removeChild(子节点);  

```html
<script>
    var oUl=document.getElementById('uul');
    
    var oLis=document.createElement('li');
    oLis.innerHTML=oTextarea.value;  // 为新元素添加值。
    oLis.appendChild(oLis);  //创建元素并插入到需要的位置，但与innerHTML不同，不改变原有的其他元素。
    oUl.insertBefore(oLis,aLi[0]);  //在oUl中插入oLias，位于aLi[0]之前
    
</script>
<body>
    maincont
</body>
```

### 文档碎片：提高dom操作性能
> 创建完新元素插入文档碎片，最后再插入页面（避免多次页面重新渲染）

类似1个array,先将要增加的元素加入到oFrag中，然后传递给父级元素

```html
<script>
window.onload=function(){
    var oFrag=document.createDocumentFragment();
    for（var i=0;i<10000; i++){
        pass
        oFrag.appendChild(newelement);
    }
    oUl.appendChild(oFrag);
};
    
</script>
<body>
    <ul id="ull">
    </ul> 
</body>
```

var stri=document.getElementByTag('liId').[1];
str.toLowerCase();
str.search('匹配字符');  //返回匹配到的字符起始位置，是正数，没找到返回-1
str.split('分隔符');  //可以是空格，返回array

排序：
aLi是元素集合，并不完全是array,无法直接使用sort。

```html
array[i]=aLi[i];  // array=[aLi[0],aLi[1],aLi[2]...]
array.sort(function (li1,li2){
    var n1=parseInt(li1.innerHTML);
    var n2=parseInt(li2.innerHTML);
    return n1-n2;
});
// 此时array中的成员已重新排列。例如array=[aLi[2],aLi[1],aLi[4]...]
oUL1.appendChild(array[i]); 

```

### 表单

```html
<form action="http://www.baodu.com/">
    usname:<input type="text" name="user" /><br>
    
    <input type="submit" />
    <input type="reset" />
</form>
```
表单事件 onsubmit, onreset

表单内容验证
* 组织用户输入非法字符 -> 阻止事件
* 输入时、失去焦点时验证 -> onkeyup、onblur
* 提交时检查 -> onsubmit
* 后台数据检查 


## js运动
setInterval：多次点击时，可以开启多个定时器，导致setInterval中的函数被执行多次
先执行一次cleatInterval（yourtimer）确保只有1个定时器。

缓冲运动：speed=（目标值-当前值）/缩放系数 -> 注意：
speed=speed>0?Math.ceil(speed):Math.floor(speed);
为避免speed在-1~1之间时停止运动，需要向上取整和向下取整数。
Math.abs() 获取绝对值。，。/mn
bvasdfghjkltyuiopSD  

#### 页面滚动
offsetWidth: 返回数值，width+padding+border
clientHeight：页面可视区域高度

```html
window.onscroll=function (){
    var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;  //写2种以兼容不同浏览器。
};