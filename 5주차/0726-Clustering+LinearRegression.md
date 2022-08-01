# 4주차 2022 07 19
</br>

## 📌 Clustering

### 군집화

- 레이블이 없는 데이터 안에서 패턴과 구조를 발견하는 **비지도 학습**
- 군집화의 목표는 서로 유사한 데이터들을 같은 그룹으로 묶어주는 것
- 몇 개의 그룹으로 묶을지, 유사도는 어떻게 정의할 것인지 정해야 함

</br>

### K-Means Clustering

- k 는 몇 개의 그룹으로 묶을지 결정
- k 개의 임의의 중심점 배치 (각 중심점 사이의 거리가 최대한 멀어지도록)
- 각 데이터들을 가장 가까운 중심점으로 할당
- 해당 군집의 중심으로 이동
- 더 이상 중심점의 이동이 없을 때까지 반복

</br>


<img width="300" alt="image" src="https://user-images.githubusercontent.com/40768187/181924303-b454bf07-4c2f-480d-bcfc-df8d2e58c28f.png">  <img width="300" alt="image" src="https://user-images.githubusercontent.com/40768187/181924437-49015c65-42a0-4e8e-9ed6-46d3df6447a9.png">

</br>

<img width="300" alt="image" src="https://user-images.githubusercontent.com/40768187/181924522-9843c057-92f1-4991-a891-4e5a43dec519.png"> <img width="360" alt="image" src="https://user-images.githubusercontent.com/40768187/181925414-613d78e0-37bb-4421-8f19-15ae2fa83d00.png">

</br>

### SSE (Sum of Squared Error)

<img width="540" alt="image" src="https://user-images.githubusercontent.com/40768187/181934336-8ad98ee2-461c-44b6-b757-6309da7e63b5.png">

- 적당한 k 를 선택하는 방법
- 관측치와 중심들 사이의 거리
- 군집들이 얼만큼 뭉쳐져 있는지를 나타내는 지표

</br>

## 📌 차원 축소 (Dimensionality Reduction)

### 차원

- 공간에서 데이터의 위치를 나타내기 위해 필요한 축(Axis)의 수
- feature 의 수

</br>

### 차원의 저주 (Curse of Dimensionality)

- 차원이 증가하면 정보의 밀도 감소 (필요한 데이터의 수가 지수 함수적 증가)
- 정보의 감소로 과적합 문제 발생하기 쉬움

<img width="1279" alt="image" src="https://user-images.githubusercontent.com/40768187/182143587-9bd69346-5f21-49e1-8010-8be16b124cb7.png">

</br>

### 해결법

- 샘플의 밀도가 충분히 높아질 때까지 훈련 셋의 크기 키우기
  - 차원이 증가하면 필요한 데이터의 수가 지수 함수적 증가하기 때문에 불가능한 경우 많음

- 차원 축소
  - 특징 선택 (Feature Selection, 변수 선택)
  - 특징 추출 (Feature Extraction) : 원본 데이터의 특징을 조합해서 새로운 특징 만들기
    - PCA, LDA etc.

</br>

### 투영 (Projection)

- 차원 축소 알고리즘의 주요한 접근법의 하나

<img width="600" alt="image" src="https://user-images.githubusercontent.com/40768187/182144549-db880429-9253-47dd-83c6-e3a0089cb56b.png">

</br>

### 주성분 분석 (PCA : Principal Component Analysis)

- 가장 인기있는 차원 축소 알고리즘
- 분산이 최대로 되는 축(주성분)을 선택하고, 축에 대해 투영함
- 첫번째 축에 직교하고 남은 분산을 최대한 보존하는 두번째 축 찾음

    <img width="473" alt="스크린샷 2022-08-01 오후 9 14 26" src="https://user-images.githubusercontent.com/40768187/182145556-5277b0e6-e60b-4e63-8672-8cbc1a7e784f.png">

</br>

## 📌 선형 회귀 (Linear Regression)

### 선형 회귀

<img width="247" alt="image" src="https://user-images.githubusercontent.com/40768187/182153873-795dc727-7e86-4c53-b647-cf9323795839.png">

- 독립변수와 종속변수를 선형적인 관계로 가정하고, 데이터를 가장 잘 나타내는 선형식 찾기
- 종속 변수 Y를 독립변수 X들의 선형 결합으로 표현한 모델 (선형 회귀 모델)

</br>

### 단순 선형 회귀

<img width="121" alt="image" src="https://user-images.githubusercontent.com/40768187/182165769-73ad2200-57b6-477d-ba98-f5930b57830f.png">

- 독립 변수가 1개인 선형 회귀
- 가설 ^y 중에서 데이터를 가장 잘 설명하는 직선 하나를 찾아야 하는 문제

</br>

### 오차(손실) 계산

- 데이터를 가장 잘 나타내는 직선이란, 가설과 실제값(정답)과의 차이가 최소가 됨

    <img width="500" alt="image" src="https://user-images.githubusercontent.com/40768187/182166685-9284c989-2585-49f3-80f7-c2a50901769b.png">

</br>

### 잔차 제곱합 (RSS : Residual Sum of Squared)

<img width="435" alt="image" src="https://user-images.githubusercontent.com/40768187/182173645-e29a2354-817f-4061-a141-671e947864d6.png">

- 오차를 제곱해서 다 더한 것
- ```^y``` : 예측값 (y = predict())

</br>

### 평균 제곱 오차 (Mean Squared Error)

<img width="481" alt="image" src="https://user-images.githubusercontent.com/40768187/182174898-08814343-b539-4d0d-82f6-69c9121cb4d3.png">

- 잔차 제곱합에 1/n 을 해준 것
- 가장 작은 값이 가장 좋은 직선

</br>

### 비용 함수 (Cost Function)

- 손실 함수 (Loss Function)이라고도 함
- 정답과 예측의 차이(Loss)를 계산하는 함수
- **회귀 알고리즘은 손실함수가 최소가 되는 파라미터를 찾는 문제**
- RSS, MSE, MAE(Mean Absolute Square), RMSE(Root Mean Squared Square)

<img width="373" alt="image" src="https://user-images.githubusercontent.com/40768187/182177033-16d8284c-4b20-4595-bb9a-1e51fd27c779.png"> <img width="323" alt="image" src="https://user-images.githubusercontent.com/40768187/182177102-516a9936-effe-4e34-aca0-cf61b2ecddc8.png">

</br>

### 손실함수를 최소로 하는 파라미터를 찾는 방법

- 최소 제곱법 (Ordinary Least Squares, OLS) : 해석학적 방법
- 경사하강법 (Gradient Descent) : 점진적 학습

</br>

### 최소 제곱법

<img width="351" alt="image" src="https://user-images.githubusercontent.com/40768187/182177507-3cecdbaa-ab8f-4cc7-a0e7-59ac824162c0.png">

- 최소가 되는 β0, β1 결정


    <img width="410" alt="image" src="https://user-images.githubusercontent.com/40768187/182179192-f7905982-c468-4577-965c-d84596064a60.png"> <img width="410" alt="image" src="https://user-images.githubusercontent.com/40768187/182179341-da257482-3332-40b9-be54-78ae9ae2c335.png">

</br>

### 경사 하강법

- 여러 종류의 문제에서 최적의 해법을 찾을 수 있는 최적화 알고리즘
- 비용함수(Cost Function)를 최소화하기 위해 반복해서 파라미터 조정
- 경사: 기울기, 하강: 내려감 - 기울기를 따라서 반복해서 내려가는 알고리즘

    <img width="709" alt="image" src="https://user-images.githubusercontent.com/40768187/182180888-eb26d2e2-468a-4527-b04a-88617671025b.png">
    <img width="390" alt="image" src="https://user-images.githubusercontent.com/40768187/182180948-f28800ee-b013-46cb-9380-3fdd2b0c036b.png">