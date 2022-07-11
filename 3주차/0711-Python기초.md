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
