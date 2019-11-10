[use selenium](http://www.santostang.com/2018/07/15/4-3-%E9%80%9A%E8%BF%87selenium-%E6%A8%A1%E6%8B%9F%E6%B5%8F%E8%A7%88%E5%99%A8%E6%8A%93%E5%8F%96/)
[代理IP](https://www.xicidaili.com/wt/)

全部资源链接： [github](https://github.com/DeathKing/Learning-SICP)

中文字幕视频： [计算机程序的构造和解释-视频（SICP）【中英字幕】【FoOTOo&HITPT&Learning-SICP】](https://www.bilibili.com/video/av8515129?t=1477)

原版：[Structure and Interpretation of Computer Programs](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/)

SICP书： [网页版本](https://mitpress.mit.edu/sicp/)

SICP书： [HTML5版本](https://sarabander.github.io/sicp/)

答案： http://community.schemewiki.org/?SICP-Solutions

Chez Scheme作为练习环境： [Chez Scheme](https://cisco.github.io/ChezScheme/)

其他资源：
> [伯克利的CS61A Python版](http://composingprograms.com/)
> [CS61AS Racket版](http://berkeley-cs61as.github.io/index.html)
> [新加坡大学的JavaScript版](https://www.comp.nus.edu.sg/~cs1101s/sicp/)


important
[1](##`Chris Strachey`将过程或是函数视为程序设计语言中的第一级元素)

[2](##intro)

 C.0 Layered System ( Compound data(复合数据))，每层皆可替换。

# A.0 the essense of computer science.
> computer it's not about computer or science,science/engineering is process.

The essense of computer science is how to formalize intuitions about process,how to do things.Starting to develop a way to talk precisely about how-to knowledge as opposed to geometry that talks about what is true.
计算机科学的本质：如何对计算过程进行形式化表述,如何解决问题，创造一套可以精确表述问题处理过程的方法。

## A.1 imperative knowledge 指令型知识
#### `procedures(过程/程序)` are going to be the way of talking about imperative knowledge.
a procedure will end up being another procedure，a general strategy that talks about a general strategy.
一种生成过程的过程,利用此递归性可讨论自身或所有新产生的过程.

## A.2 three techniques for controlling complexity 
### 1. black-box abstraction
* primitive objects
  1. primitive procedure ( exp: + - * / < = )
  2. primitive data ( exp: 22 23.4 )
* means of combinition
  1. procedure composition ( exp: [] composition, COND, IF )
  2. construction of compound data from primitive data
* means of abstraction ( from compound/combinition things )
  1. procedure definition ( exp: DEFINE )
  2. simple data abstraction( a technique for dealing with compound data )
* capturing common patterns
  1. high-order procedures ( 高阶过程，它的输入、输出、本身都是过程 ）
  2. data as procedures （ 模糊数据与过程的区别 ）

### 2. conventional interfaces ( 约定接口，可将符合接口标准的不同部分连接起来，并由此构建系统。）
> 例如对各种数据皆使用的`+`,`-`等基本符号

* generic operations
* large-scale structure and modularity
* metaphor 1:object-oriented programming
* metaphor 2:operations on aggregates ( 聚焦的操作，称作“流” ，用于数据的计算，如count，min，sum等)

### 3. metalinguistic abstraction 元语言抽象(make new languages)
>the purpose of the new designed languages will be to highlight different aspects of the system
设计意图：强调系统的某一方面,隐藏部分细节，强调其他细节。

* interpretion apply-eval
* example- logic programming
* register machines

##### `最终获得一种无关输入输出的过程，而仅关注元素间关系的语言`

##### The process of how lisp interprete itself? `eval and apply` constantly reduce expression to each other.(`eval and apply`不间断地交替进行）
> a magical symbol λ(lambda，用于表示无限)

>> 1. (define (pr x) (someprocess))
2. (define pr (λ (x) (someprocess))
3. (define pr ((define (anonymous x) (somefunc)) anonymous))
1,2,3作用相同，2是3地简写，定义一个匿名符号，并将其返回, 用pr这个符号代表这匿名符号。

# B.0 substitution Rule( 替换模型，适用于前几节课 )
> 
```
To evaluate an application
  Evaluate the operator to get procedure
  Evaluate the operands to get arguments
  Apply the procedure to the arguments
  Copy the body of the procedure,substituting the arguments applied
   for the formal parameters of the procedure.
  Evaluate the resulting new body.
```

****
# \* if you have the name of a spirit, you have the power of it. \*
****

## B.1 基本知识
#### O(),O is order: 表示复杂程度(时间，空间)的符号
```
(define (+ x y)
	(if (= x 0)
		y
		(+ (-1+ x) (1+ y))))
```

对于上边的过程
time = O(x)
space = O(1)

#### 迭代：iteration
每一层都与上一层无关,上几层的数据丢失也不影响获得最终结果。
#### 递归：recursion
每一层获得的值都需要传递回上一层。
> 1. linear recursion每次只调用自身1次
> 2. tail recursion
> 3. binary recursion每次调用自身2次-如斐波那契数列
>   * time = O(fib(n))
>   * space = O(n)

## `Chris Strachey`将过程或是函数视为程序设计语言中的第一级元素
### The rights and priviliges of first-class citizens(一级元素的权利)
* To be named by variables
* To be passed as argements to procedures
* To be returned as values of procedures
* To be incorporated into data structures

# C.0 Layered System ( Compound data(复合数据))，每层皆可替换。

### data abstraction(数据抽象)是一种通过假定的constructors(构造函数)和selectors(选择函数)将use(数据对象)与它的presentation(表示法)分隔开来的编程方法学。

使用wishful thinking strategy(愿望思维)，即假定复合结构中的某些部分(通常是较底层的功能)已被实现并可直接使用。

通过抽象层边界(abstrction layer，由constructors和selectors组成)分离对象的使用方法成use和presentarion

### *closure*(闭包): the means of combinition in system,put things together and then put together with the same means of combinition

## C.1 一种构建cons(序对)的过程

## intro
```
(define (cons x y)
	(λ (pick)
		(cond ((= pick 1) x)
			  ((= pick 2) y))))
(define (car p) (p 1))
(define cdr (λ (p) (p 2)))
((car st) 2)
```
