### html

#### html元素
<p></p> 段落并会有空行
<br /> 换行
段落中加多个空格，使用空格的字符实体&nbsp;
<的字符实体为&lt；>的字符实体为&gt；
<div></div> 块元素
<span></span> 行内元素
<em></em> 语气中的强调词，有字体倾斜效果
<i></i> 表示专业词汇，有字体倾斜效果
<b></b> 表示文档中的关键字或产品名，有字体变粗效果
<strong></strong> 表示非常重要的内容，有字体变粗效果
<img src="../../pic.jpg" alt="加载失败显示"></img> alt用于盲人
<></>
<ul>
  <li>con1</li>
  <li>con2</li>
  <li>con3</li>  
</ul> 无序列表
<table></table> 表格
<form action="htttp://www.baidu.com">
  <label for="click_selection">user--name:</label>
  <input type="text" name="username" id="click_selection"/> 有name属性的会被提交,此时点击user--name:文字也会激活input
  <label>sexone:</label>
  <input type="radio" name="gender" value="man" /> 被选的name及value被提交  
  <input type="radio" name="gender" value="woman" />
  <input type="submit" name="" value="submit_values" />  
</form> 表单,会转到地址htttp://www.baidu.com?/username=input_content&gender=man

### css
1. 外联式<link rel="stylesheet" type="text/css" href="css/main.css" >
2. 嵌入式
<style type="text/css">
  h1{font-size:20px;}
</style>
3. 内联式<div style="font-size:20px;"></div>

#### 选择器
1. 标签选择器 div{}
2. id选择器 #idname{}
3. 类选择器(一个类用于多个元素，一个元素用多个类） .classformany{}
<div class="cname1 cname2 cname3">
4. 层级选择器（选择父元素下的元素,由外向内层级选择，4层以内） .box .red{}
5. 组选择器（公共样式） .c1,.c2,.c3{width:200;}
6. 伪类选择器（hover鼠标悬停) .xo:hover{color:red;}
7. 伪元素选择器（before,after,内容不可被选中) .xo:hover{content:"content befor";}

#### margin技巧
margin：50px auto; 左右居中
margin-top：-10px; 设置负值，元素位移其边框合并
margin-top：10px; margin-top合并：同层级元素都有margin，使用数值较大的margin的一个
margin-top：20px; margin-top塌陷：父子元素都有margin，使用数值较大的margin的一个
解决margin-top塌陷
1. 外部设置边框
2. 外部设置 overflow:hidden;
3. 再外部增加一个类，并设置类的伪类元素 .clearfix:before{content:'';}

inline-height：设置文字垂直居中
overflow
visible hidden scroll auto inherit(从父类继承overflow属性，较少使用）

#### display
元素就是标签
1. 块元素（又称行元素）：div, h1, p ,ul 等 支持全部样式，占据一行
2. 内联元素（又称行内元素）： a, span, em 不支持高宽，margin和padding的上下，不占一行，盒子间会产生间距（父级元素的font-size设为0，子元素设置font-size来取消间距）。父元素使用text-align设置子元素的水平对齐方式。
3. 内联块元素：img，input，使用display将其他转换为这种元素。支持全部样式，（可设置宽高），其他同内联元素

none: 元素隐藏且不占位置
block： 块元素显示
inline： 内联元素显示
inline-block： 内联块元素显示

#### float:left（变成内联块元素）
1. 碰到父元素边界或其他元素才停止
2. 相邻浮动的块元素可并在一行（且没有间隙）
3. 浮动元素后边没有浮动的元素会占据浮动元素的位置，没有浮动元素内的文字会环绕浮动元素。
4. 父元素如没有设置高度，父元素就需要加上overflow:hidden

或者父元素加上类.clearfix
.clearfix:before,.clearfix:after{
  content:"";
  display:table;}
.clearfix:after{
  clear:both;}
.clearfix{
  zoom:1}
  
  
####  定位（relative和absolute会变成内联块元素）
文档流：盒子按html标签的顺序一次从上到下，从左到右排列
使用position属性，设置position后，再设置left:20px，top:10px。
子元素可不设置position而设置left，top，此时默认使用父类元素的position属性。
1. relative:相对元素所在的原有文档流位置
2. absolute:元素脱离文档流，不占据文档流位置。相对于上一个设置了定位的父级元素定位，没有则相对于<body>
3. fixed:元素脱离文档流，不占据文档流位置。相对于浏览器窗口定位。/
4. static：默认值，没有定位，出现在文档流中，相当于取消定位属性或不设置定位。
5. inherit:从父级继承position属性。

使用z-index:6设置元素层级
