# 3주차 2022 07 11
</br>

## 📌 Python 기초

### Python 개발 환경

- python 설치
- anaconda 는 처음 배우는 단계에선 추천하지 않음
- 간단한 코드를 테스트할 때는 Jupyter Notebook 좋음
- IDE는 VSCode 사용할 예정
- python 설치 시 PATH 설정에 체크하지 않았다면, 환경변수에서 PATH 지정해줄 것

</br>

### Compiler vs. Interpreter

Compiler
- executable 만들 때 리소스를 다 넣고, virtual machine에서 한줄 한줄 실행
- static binding

Interpreter
- 수행하는 순간, 읽는 순간 리소스 (라이브러리) 가져옴, 코드를 한줄 한줄 실행
- dynamic binding
- 라이브러리들을 어디서 가져올까? 인터넷. standard package를 제외한 것들 다운로드

</br>

### Python IDLE

- 대화형 모드: 명령어를 하나씩 입력하고 실행결과 확인
- 스크립트 모드: 일련의 명령어를 모아서 하나의 프로그램으로 작성, 한번에 실행 (확장자 .py)

</br>

### Python Library 설치 확인

- pip 명령어 upgrade

</br>

window or macOS

```
python -m pip install --upgrade pip
```

linux
```
pip install --upgrade pip
```

</br>

### 변수

- 변수는 값을 저장하는 메모리 공간에 대한 Tag
- 값을 저장하는 상자 또는 그릇으로 생각할 수 있음
- 변수는 값이 할당되는 순간 생성되고, 타입이 정해짐
- 변수의 타입은 값을 넣는 순간마다 변경 가능
- 타입을 작성할 필요가 없음

```python
score = 20  # 왼쪽엔 변수이름, 오른쪽엔 값, '=' 는 할당연산자
```

</br>

### 변수 이름 짓기

- 의미있는 이름 사용
- 소문자 대문자 구별
- 변수의 이름은 영문자, 숫자, '_' 로 이루어질 수 있음
- 숫자 시작, 공백, 예약어 불가능
- '-' 불가능한 이유 : 빼기 기호가 같아서
- '_name' 의 형식은 잘 사용되지 않지만, 사용될 경우 특별한 의미(경우)일 것임

</br>

### 변수의 자료형

![image](https://user-images.githubusercontent.com/40768187/178204512-0a5e1c4b-af38-4860-b80f-b03410fbb37c.png)

**mutable 자료형: 데이터 내부의 값을 변경할 수 있는 형태의 자료형 (나머지는 immutable 자료형)**

```type()``` 으로 변수의 자료형 확인 가능

</br>

**종류**

1. 정수형(int)
2. 실수형(float)
    - 사칙연산 수행 가능: +, -, *,/
    - 지수 계산 **, 나머지 %, 나눈 후 소수점 버리기 //
3. 불리언형: true, false
4. 문자열: " " or ' '

</br>

### 자료형 변환

- int() 함수
    - str -> int
    - float -> int
    - 실수 형태의 문자열은 정수로 변환 불가 error!
        ```python
        a = int(5.6) # 5
        b = int('54') # 54

        c = int('15.7') # error
        ```

- float() 함수
    - (실수 형태의) str/int -> float
    ```python
    x = float(3)    # 3.0
    y = float('15.7')   # 15.7
    ```

- str() 함수
    - int/float -> str
    ```python
    a = 123
    c= str(a)   # '123'

    b = 1.23
    c = str(b)  # '1.23'
    ```

</br>

### 산술 연산자

- 수식(espression) = 피연산자들과 연산자의 조합
- 연산자(operator): 연산을 나타내는 기호
- 피연산자(operand): 연산의 대상이 되는 값

</br>

#### 결과 값의 자료형

- 피연산자 모두 정수형이 아닐 경우, 결과는 항상 실수
- 정수와 실수를 연산하면 결과는 실수
- 나누기 연산 결과는 항상 실수
- 소수점은 16자리 정도까지만 표현
- 실수는 부동소수점이라는 특수한 방식으로 표현 -> 미세한 오차 발생 가능

</br>

#### 입출력 함수 - input()

</br>

- variable_name = input("프롬프트 문자열")
  - return 할 때까지 한 string으로 쭉 받음

```python
>>> name = input("이름을 입력하세요: ")
이름을 입력하세요: 홍길동

>>> print("만나서 반갑습니다.", name, "씨!")
만나서 반갑습니다. 홍길동 씨!
```

프롬프트 문자열이 출력되고 사용자의 입력이 변수에 문자열 자료형으로 저장

</br>

```python
x = input("첫 번째 정수를 입력하세요: ")
y = input("두 번째 정수를 입력하세요: ")
sum = x + y
print("합은 ", sum)

#결과

첫 번째 정수를 입력하세요: 10
두 번째 정수를 입력하세요: 20
합은 1020

x = int(input("첫 번째 정수를 입력하세요: "))
y = int(input("두 번째 정수를 입력하세요: "))
sum = x + y
print("합은 ", sum)

# 결과

첫 번째 정수를 입력하세요: 10
두 번째 정수를 입력하세요: 20
합은 30
```

숫자 입력 예시 코드 ↑

</br>

### 입출력 함수 - print()
</br>

- 특수기호는 ```\``` 문자를 사용하여 출력 ex) ```\'```
- print() 함수 실행 시 항상 문자열 마지막에 \n 이 출력되어 줄 바꿈 일어남
- 줄바꿈을 없애기 -> ```end``` 인자 설정 (default: \n)
- 콤마로 구분된 문자열 다르게 결합 -> ```sep``` 인자 설정 (default: 공백)

    ```
    >>> print("No new line"), end="####"); print("ok?")
    No new line####ok?

    >>> print('Hello', 'Python', sep='#')
    Hello#Python
    ```

</br>

- print("문자열")
- print(variable_name)
- print("문자열", variable_name)    # 콤마는 띄어쓰기를 함 (가독성을 위한 것인듯?)


    ```python
    >>> print("True Love")
    True Love

    >>> number1 = 25
    >>> number2 = 30
    >>> sum = number1 + number2
    >>> print(sum)
    55

    >>> print("number", 12, 13)
    number 12 13  #빈칸이 추가된 것을 볼 수 있음

    >>> print("a에 저장된 값은", a, "입니다." )
    a에 저장된 값은 10 입니다.
    >>> print("a에 저장된 값은" + str(a) + "입니다.")
    a에 저장된 값은 10 입니다.
    ```

</br>

### 문자열 자료형

- 문자열은 연속된 문자들의 집합을 의미 (sequence of characters)
- 파이썬은 텍스트를 다루는 자료형으로 문자열(string) 제공
- 문자열은 일단 생성하면 그 내용 변경 불가능 -> **immutable**
- 파이썬에서는 문자열 자료형을 UTF-8 (유니코드) 를 사용하여 인코딩
- ```+``` 연산자로 두 문자열 연결 가능 (숫자 + 숫자 | 문자열 + 문자열)

- 문자열 반복 -> ```*``` 사용

    ```python
    message = "Congratulations!"
    print(message * 3)
    ```
    스크립트 전체 실행

    <img width="398" alt="image" src="https://user-images.githubusercontent.com/40768187/178255296-980e7fb0-2e56-4e4d-9a05-6cf763f153ff.png">

    </br>

- ```in``` 연산자로 원하는 부분이 문자열 안에 존재하는지 확인

    ```python
    a = 'Good Morning'
    'Good' in a
    ```
    한줄한줄 실행

    <img width="245" alt="image" src="https://user-images.githubusercontent.com/40768187/178257434-fe437659-2d4c-42d6-9b5d-239be846e12f.png">

</br>

+) 한글 인코딩 - 1. 완성형 (16bit) 2. 조합형 (3bit 씩 - 초성, 중성, 종성)

</br>

### 문자열 메소드 - split()

- str.split('구분자')
  - 인수로 입력된 구분자를 기준으로 원본 문자열을 분리하여 반환
  - default는 공백을 기준으로 분리
  - list 타입으로 반환

    ```python
    msg = "Life is too short"
    w1, w2, w3, w4 = msg.split()
    print(w1)

    newYear = "2021.01.01"
    year, month, day = newYear.split('.')
    year
    month
    ```

    <img width="282" alt="image" src="https://user-images.githubusercontent.com/40768187/178260870-d04d6353-aefe-4a55-8bcd-4b5e0ce66a4a.png">

</br>

- 입력과 문자열 분리를 한 번에 처리

    ```python
    n1, n2 = input("Enter two number: ").split()    # 입력받으면서 문자열 분리

    n1 = int(n1)    # 문자열을 정수로 변환
    n2 = int(n2)
    print(n1, n2)
    ```

    <img width="317" alt="image" src="https://user-images.githubusercontent.com/40768187/178262835-5c601ba8-6049-4666-972d-15bff175d166.png">

    </br>

### 문자열 포맷팅
</br>

- 데이터를 삽입하여 원하는 문자열을 만들 수 있음
- ```%``` 기호 사용
- ```str.format()``` 메소드 사용

    ```python
    >>> print("the number %d" % 7) # 두번째 % 뒤에 공백 없어도 됨
    the number 7
    >>> print("the number {}".format(7))    # 2개의 값 포맷팅 - print("x={} and y={}".format(x, y))
    the number 7
    >>> print('The light was %s' % 'good')
    The light was good
    >>> print("I {1} eat {0} apples.".format('hi', 'there'))    # 인수의 인덱스 나타냄
    I there eat hi apples
    >>> print('My name is {name}. I am {age} years old'.format(name='jin', age=20))
    My name is jin. I am 20 years old.

    >>> father = "Adam"
    >>> son = "Seth"
    >>> print("%s is a father of %s." % (father, son))  # 포맷팅 기호의 개수와 값의 개수가 같아야 함
    Adam is a father of Seth.

    >>> print("I hava %s apples." % 3)  # str(3) 암묵적 변환 | 실수면 str(3.234) 암묵적 변환
    I eat 3 apples.
    >>> print("Error is %d%%." % 98)    # %% -> % 기호를 문자로 삽입
    Error is 98%.
    ```

</br>

### 문자열 포맷팅 - 자릿수 지정
</br>

- 정수
  - %nd : n은 자릿수
  - 숫자가 n자릿수를 초과하면 초과하여 표시

- 실수
  - %n.mf : n은 전체 너비, m은 소수점 이하 자릿수

```python
# 정수
>>> print("average=%10d" % 59832)
average=     59832
>>> print("average=%3d" % 59832)
average=59832

# 실수
>>> print("average=%10.2f" % 57.467657)
average=     57.47

>>> print("average="%10.2f" % 12345678.923)
average=12345678.92

>>> print("average=%10.2f" % 57.4)
average=     57.40
```

</br>

### 문자열 포맷팅 - 포맷 코드 (폭 지정, 정렬 지정)

- {순서:출력형식}.format(var)

```python
>>> temp = 25.232123
>>> humi = 45.32345
>>> print("온도는 {1:.1f}도, 습도는 {0:.0f}% 입니다.".format(humi, temp))
온도는 25.2도, 습도는 45% 입니다.

>>> print("The light was {:10}.".format('good'))
The light was good      .       # 문자는 왼쪽 정렬, 숫자는 오른쪽 정렬 디폴트!

# 서식 정렬

Weight=57.478
>>> "{:<10.2f }".format(weight)     # 왼쪽 정렬   ==  print('Hello Python'.ljust(20))
'57.74     '
>>> "{0:<10 }".format("hi")     # 왼쪽 정렬
'hi        '
>>> "{:>10 }".format("hi")      # 오른쪽 정렬   ==  print('Hello Python'.rjust(20))
'        hi'
>>> "{:^10 }".format("hi")      # 가운데 정렬   ==  print('Hello Python'.center(20))
'    hi    '
```

- ```.zfill()``` : 오른쪽 정렬하고 빈 자리 0으로 채움
- ```.capitalize()``` : 첫 글자만 대문자로
- ```.upper()``` : 문자열 전체를 대문자로

</br>

### 파일 입출력
</br>

```python
fp_r = open("in.txt", 'r')      # read mode
fp_w = open("out.txt", 'w')      # write mode

# 'a' :  기존 파일에 덧붙여서 이어서 쓰기 작업
```
</br>

### file read
</br>

- ```.read()``` : 파일 전체를 하나의 문자열로 읽어 들임 (파일 용량 작을 때 사용)
- ```.readlines()``` : 파일을 줄 단위로 읽어 각 죽을 문자열 형식으로 저장. 문자열을 원소로 하는 리스트 반환
- ```.readline()``` : 한 줄을 문자열 형식으로 읽어 이를 반환. 다음 줄 읽기 위해 해당 함수 계속 반복

```python
for aLine   in  fp_r :      # 변수 aLine은 fp_r에서 한 줄씩 읽어 들인 문자열
        statements          # 읽어 들인 줄(문자열)에 처리할 명령어들
```

</br>

### file write
</br>

- ```fp_w.write(string)```
  - string 문자열 하나를 파일에 씀
  - 줄바꿈 문자가 자동으로 삽입되지 않음
  - 줄바꿈이 필요한 경우, string의 마지막에 줄바꿈 기호를 추가

- ```print(*objects, file = fp_w)```
  - 화면 대신 파일 fp_w에 씀
  - print() 함수는 줄바꿈이 자동
  - 줄바꿈을 하지 않으려면, end 인수값 변경
  - 잘 사용하지 않는 구문. binary 로는 씀. 위 구문이 가끔 작동 안할 때도 사용함

    ```python
    # print(*objects, file = fp_w, end = "")

    print("Year:", 2020, file = fp_w, end = "")
    ```

</br>

### file close
</br>

```fp_r.close()```
 - 파일을 열었다면 반드시 닫을 것
 - 파일이 열려있는 상태에서는 파일을 지우거나 이름 변경이 불가함

```with``` 키워드
  - with 구문 종료 시 파일 자동으로 닫음

```python
with fp_r = open("in.txt", 'r')
    # 프로그램 코드
    fp_r.read(..)
```

</br>

### 파일 입출력 예제
</br>

```python
fp_r = open("in_mul.txt", 'r')
fp_w = open("out_mul.txt", 'w')
print("The square results are", file = fp_w)

for s in fp_r :
    num = list(int(x) for x in s.split())   # 정수 변환
    for i in range(len(num)) :              # 이렇게 쓰지 말라고 하셨음 ex) range(2, 4)
        sq = num[i] * num[i]
        print("%2d " %sq, file = fp_w, end = '')
    fp_w.write("\n")        # 한 줄 처리 후, 줄바꿈
fR.close();
fW.cloase()
```
</br>

```in_mul.txt``` </br>
1 2 5 8</br>
4 8 9 5 7

```out_mul.txt``` </br>
The square results are</br>
1  9  25  64</br>
16  64  81  25  49