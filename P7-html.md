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

选择器
1. 标签选择器 div{}
2. id选择器 #idname{}
3. 类选择器(一个类用于多个元素，一个元素用多个类） .classformany{}
<div class="cname1 cname2 cname3">
4. 层级选择器（选择父元素下的元素,由外向内层级选择，4层以内） .box .red{}
5. 组选择器（公共样式） .c1,.c2,.c3{width:200;}
6. 伪类选择器（hover鼠标悬停) .xo:hover{color:red;}
7. 伪元素选择器（before,after,内容不可被选中) .xo:hover{content:"content befor";}