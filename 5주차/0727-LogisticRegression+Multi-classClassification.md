# 5주차 2022 07 27
</br>

## 📌 로지스틱 회귀 (Logistic Regression)

### 선형 회귀

- 선형회귀는 계수들을 찾는 것
- 베타 계수가 영향을 많이 끼침
- feature 간에는 독립적이어야하고, feature와 target 은 관계가 있어야 함
- optimazation, 경사하강법 중요
- 모든 모델 경사하강법으로 학습시키고 있음

</br>

### 로지스틱 회귀?

- 회귀 알고리즘이지만 **분류**에 사용
- 회귀를 사용하여 데이터가 어떤 범주에 속할 확률을 0에서 1 사이의 값으로 예측함
- 선형 회귀처럼 입력 특성치의 가중치 합을 계산함
- 가중치의 합을 바로 출력하지 않고, 결과값의 로지스틱(Logistic)을 출력함
- 이진 분류
  - 시험 합격 여부 : Pass or Fail
  - 스팸 필터: Spam or Ham
  - SNS 피드 노출: Show or Hide

</br>

### 선형 회귀 - 종속 변수가 범주형일 경우

- 종속 변수의 범위가 -∞ ~ ∞ 범위를 가지고 연속형이 됨
- 선형 회귀 모델로 문제 해결 불가
- 선형이 아닌 S 곡선


    <img width="605" alt="image" src="https://user-images.githubusercontent.com/40768187/183255282-ee7d4d6c-887e-42fc-8dc7-884b8266449b.png">

</br>

### 시그모이드 함수 (Sigmoid Function)

해당 함수에 MSE - 경사하강법을 쓰기에는 local minimum 이 많아 최저값을 찾기 어려움

```로지스틱 함수``` 라고도 부름

</br>

<img width="500" alt="스크린샷 2022-08-07 오전 12 24 25" src="https://user-images.githubusercontent.com/40768187/183255384-6379fe9e-381d-4df7-bf49-1c05d734b19c.png">

</br>

### Sigmoid 함수 살펴보기
</br>

<img width="500" alt="스크린샷 2022-08-07 오전 12 27 17" src="https://user-images.githubusercontent.com/40768187/183255504-2e2d547a-3233-479b-a779-0b9ec4dc9a1c.png">

https://angeloyeo.github.io/2020/09/23/logistic_regression.html

</br>

### 손실 함수로 MSE 사용하지 않는 이유

</br>

<img width="280" alt="image" src="https://user-images.githubusercontent.com/40768187/183255902-9e85a8a0-6f86-4ec0-bba7-1fbf75d9bc60.png">

</br>

- 시그모이드 함수는 비선형 함수로, 기울기가 0이 되는 곳이 2곳
- 따라서 극솟값이 여러개 나오게 됨

+) 기울기가 굉장히 작은 완만한 지점에 왔을 때, 경사 하강법이 잘 진행되지 않아 학습이 굉장히 느려질 수 있는 경우도 발생

</br>

### 손실 함수의 역할

- 정답과 예측값의 차이에 비례해서 값을 반환하는 역할
- 정답과 가까우면 작은 값을 정답과 멀면 큰 값을 반환하면 됨
- 학습이란 비용함수를 최소로 만드는 파라미터 찾음

</br>

### (Binary) Cross Entropy

</br>

<img width="582" alt="image" src="https://user-images.githubusercontent.com/40768187/183256568-1c23bf71-8da6-4d15-b799-38d78f31bfdd.png">

</br>

- Cross Entropy: 두 확률분포 사이의 오차를 측정
- 로그 곡선
- 앞에서 배운 경사 하강법 (MSE)으로 잘 풀어지지않아 다른 손실함수 사용한 것

</br>

- 샘플 한 개의 오차 (비용)

    <img width="299" alt="image" src="https://user-images.githubusercontent.com/40768187/183256691-7b3ab96e-d506-4d95-a058-6efddcf2d5fd.png">

- 손실 함수

    <img width="371" alt="image" src="https://user-images.githubusercontent.com/40768187/183256949-b32eef76-6aad-4a48-ac50-4270b108dc2e.png">

</br>

### 경사 하강법

</br>

<img width="580" alt="image" src="https://user-images.githubusercontent.com/40768187/183256998-4a38139f-d7b1-4e7e-8af9-b692027dac46.png">

</br>

## 📌 다중 분류 (Multi-class Classification)


### 이진 분류기 (로지스틱 회귀) 여러개

</br>

<img width="717" alt="image" src="https://user-images.githubusercontent.com/40768187/183257362-ffa52834-6441-4746-8abd-67f622c710d5.png">

</br>

- 이진 분류기에선 확률로 해석하고자 했는데, 다중 분류에선 확률이 높은 것을 선택하기엔 세 선의 총 확률이 1.3이 됨
- 따라서 시그모이드 함수를 사용하지 않고, softmax 를 사용

</br>

### Softmax 사용

</br>

<img width="625" alt="image" src="https://user-images.githubusercontent.com/40768187/183257516-baa7f9d2-625a-4361-bf59-54ea7e0af543.png">

</br>

다중 클래스 분류일 경우, Sigmoid 대신, Softmax 함수를 사용

</br>

### Categorical Cross Entropy

</br>

<img width="689" alt="image" src="https://user-images.githubusercontent.com/40768187/183293736-02d44f71-8f0f-4ef6-85ee-c7c7f481c107.png">

</br>

### 다중 클래스 분류에서의 경사 하강법

</br>

<img width="568" alt="image" src="https://user-images.githubusercontent.com/40768187/183293834-66e2f127-33fa-488a-afd9-cbbda4827747.png">

</br>

## 📌 정리

</br>

|           | 활성화 함수 |         손실 함수         |   최적화 방법    |
| :-------: | :---------: | :-----------------------: | :--------------: |
| 선형회귀  |      -      |    Mean Squared Error     | Gradient Descent |
| 2진 분류  |   Sigmoid   |   Binary Cross Entropy    | Gradient Descent |
| 다중 분류 |   Softmax   | Categorical Cross Entropy | Gradient Descent |

</br>

- 활성화 함수는 말단에서 사용하는거고 나머지는 변경되지 않음
- 활성화 함수는 중간 과정에서 다른 것이 사용될 수도 있음