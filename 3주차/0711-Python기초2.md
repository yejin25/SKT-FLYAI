# 3주차 2022 07 11
</br>

## 📌 Python 기초2 - 데이터 구조와 제어문

###  집합형 자료형
</br>

여러 개의 데이터를 하나로 묶어서 저장 및 관리가 필요한 경우 -> 집합형 자료형 제공

- Python의 집합형 자료형
  - list
  - tuple
  - set
  - dict

</br>

### 리스트
</br>

- 여러 개의 데이터를 순서대로 저장하고 관리해야 할 때 사용
- 어떤 자료형도 요소 값으로 가능
- 요소의 추가, 삭제 변경 가능
- 문자열처럼 인덱싱과 슬라이싱 가능
- 형식
  - 리스트명 = [요소1, 요소2, 요소3, ...]

</br>

#### 리스트 생성 - lsit(), []

```python
lst = [1, 2, "a"]       # 리스트 요소값을 직접 지정
lst = list("abc")       # list 함수의 인수로 나열형 값을 취하여 리스트 요소값으로 변경
                        # ["a", "b", "c"]
                        # 인수로는 원소를 갖는 iterable한 데이터 1개만 올 수 있음

list1 = list(2, 3, 4)   # error - 값이 하나가 아님(3개), iterable 하지도 않음

list1 = list(2)         # error - 하나의 값이지만 iterable 하지 않음

list1 = list([2, 3, 4]) # 이와 같이 작성해야 함
```

</br>

- 문자열의 ```split()``` 메소드를 사용한 리스트 생성
  - dates = "2020/04/30".split("/") -> dates = ["2020", "04", "30"]
- ```spilt()``` 메소드는 문자열을 여러 개의 문자열로 분리하여 전체를 **리스트 형태로 반환**

</br>

#### 리스트 활용 예시
</br>

```python
items = input("Enter items: ").split()
iLen = len(items)
sum = 0
for n in range(0, iLen):
    sum += int(items[n])        # items 리스트 각 아이템들을 정수로 변환
print("{}개 수의 합계: {}, 평균: {}".format(iLen, sum, avg))
```

<img width="374" alt="image" src="https://user-images.githubusercontent.com/40768187/178311139-679dd540-43c7-4eae-b7ec-be9425c48ecc.png">

</br>

### 인덱싱과 슬라이싱
</br>

#### 문자열 인덱싱과 슬라이싱
</br>

인덱스 범위
- len(s) : 입력값 s의 길이(요소 전체 개수)를 반환
- 양수 인덱스 : 0 ~ len(문자열) - 1
- 음수 인덱스 : -len(문자열) ~ -1
- 인덱스 번호는 ```[ ]``` 안에 기록하여 해당 문자 참조

