# Python PEP8 Style Guide

\** [공부한 사이트](https://realpython.com/python-pep8/)



## 1. 왜 'PEP 8'이 필요한가

PEP 8은 파이썬 코드의 가독성을 향상시키기 위해 존재한다. 

코드는 쓰여지는 것보다 더 자주 읽혀지기 때문에 가독성은 중요하다. 

PEP8 규칙을 따르면 코드에서 논리적으로 따라가기도 쉽고 



## 2. Naming Conventions

서체에 따라 `1`또는 `0`과 헷갈릴 수 있는  `l`,`O`,`I`  문자 하나를 이름으로 사용하지 않는다.

:x: 

```python
O = 2	# 2를 0에 재할당하는 것처럼 보일 수 있다.
```

### 1. Naming Styles

##### 1\. 함수

소문자를 사용하고 `_`를 사용하여 띄어쓰기를 사용한다.

>  function , my_function



##### 2\. 변수

소문자를 사용하고 하나의 문자, 단어나 단어들을 사용한다. `_`를 사용하여 띄어쓰기를 사용한다.

> x, var, my_variable



##### 3\. 클래스

각각의 단어는 대문자로 시작한다. `_`를 사용하여 <u>띄어쓰기 하지 않는다</u>.  이러한 스타일은 *camel 표기법*이라 한다.(낙타 등처럼 생겨서)

> Model, MyClass



##### 4\. 메서드

단어나 단어들의 소문자를 사용하며 `_`를 사용하여 띄어쓰기를 한다.

> class_method, method



##### 5\. 상수

하나의 문자, 단어 또는 단어들의 대문자를 사용하며 `_`를 사용하여 띄어쓰기를 한다.

> CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT



##### 6\. 모듈

짧은 소문자의 단어나 단어들을 사용한다. `_`를 사용하여 띄어쓰기를 한다.

> module.py, my_module.py



##### 7\. 패키지

짧은 소문자의 단어나 단어들을 사용한다. `_`를 사용하여 <u>띄어쓰기를 하지 않는다</u>.

> package, mypackage



### 2. How to Choose Names

오브젝트가 나타내는 것을 **명확하게 하는 묘사하는 이름**들을 사용한다. 

위와 유사한 의미로, **약어를 사용하기 보다 이해하기 쉬운 이름**을 사용한다.

```python
# 1.1 Not recommended
x = 'John Smith'
y, z = x.split()

# 1.2 Recommended
name = 'John Smith'
first_name, last_name = name.split()


# 2.1 Not recommended
def db(x):
    return x * 2

# 2.2 Recommended
def muliply_by_two(x):
    return x * 2
```

항상 가능한 가장 간단하지만 설명하는 이름을 사용하도록 하자.

