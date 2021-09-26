# Python PEP8 Style Guide

\** [공부한 사이트](https://realpython.com/python-pep8/)



## 3. Code Layout

#### 1\. Blank Lines

- **최상단 레벨의 함수나 클래스는 두 줄의 빈 라인으로 묶습니다.**

  ```python
  class MyFirstClass:
      pass
  
  
  class MySecondClass:
      pass
  
  
  def top_level_function():
      return None
  ```

- **클래스 내부의 함수 정의 시 한 개의 빈 라인으로 묶습니다.**

  ```python
  class MyClass:
      def first_method(self):
          return None
      
      def second_method(self):
          return None
      
  ```

- **함수 내에서 명확한 절차를 보여주기 위해 빈 라인을 드물게 사용합니다.**

  `반환문` 전에 여러 단계의 절차를 거치는 복잡한 함수 사용 시, 사용자의 함수내 로직 이해를 돕기 위해 각 단계 사이에 빈 라인을 사용하는 것이 도움이 될 수 있습니다.

  ```python
  def calculate_variance(number_list):
      sum_list = 0
      for number in number_list:
          sum_list = sum_list + number
      mean = sum_list / len(number_list)
      # 단계 하나 완료
      
      sum_squares = 0
      for number in number_list:
          sum_squares = sum_squares + number**2
      mean_squares = sum_squares / len(number_list)
      # 단계 하나 완료 # return 문 전에 blank line 하나 추가
      
      return mean_squares - mean**2 
      
  ```



#### 2\. Maximum Line Length and Line Breaking

PEP8은 줄을 **79자**로 제한해야한다고 제안한다. 이는 여러 파일을 나란히 열 수 있게 하기도 하고 줄 바꿈을 피하게 하기 때문이다.

79자 이내로 문장을 유지하는 게 항상 가능하지 않기 때문에 PEP8은 여러줄로 문장이 실행할 수 있도록 하는 방법에 대해 설명한다.

(코드의 **연속성**을 표현하는 방법들에 대해 설명한다.)

- **괄호, 대괄호 또는 중괄호 안에 코드가 포함되어 있을 때**

  ```python
  def function(arg_one, arg_two,
              art_three, arg_four):
      retunr art_one
      
  ```

- **백슬래시를 사용하여 줄 바꿈을 할 때**

  ```python
  from mypkg import example1, \
  	example2, example3
      
  ```

- **이진 연산자(`+`, `*`) 주변에서 줄바꿈이 발생할 경우 연산자 전에 줄 바꿈 해야 한다.**

  ```python
  total = (first_variable
          + second_variable
          - third_variable)
  
  ```

