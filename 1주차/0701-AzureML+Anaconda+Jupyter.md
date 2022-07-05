# 1주차 2022 07 01
</br>

## 📌 Juypter Notebook

Jupyter Notebook: 웹 브라우저에서 파이썬 코드를 작성하고 실행까지 해볼 수 있는 개발도구
</br>

### Anaconda 설치
아나콘다를 설치하면 파이썬과 데이터 분석 패키지의 설치 및 관리 가능

<img width="1310" alt="스크린샷 2022-07-03 오후 11 13 39" src="https://user-images.githubusercontent.com/40768187/177043695-d66a8d25-7105-4948-b6c2-0c6f3d32012c.png">

</br>

### Jupyter notebook 실행

- 강사님이 제공해준 Notebook 파일 다운로드

- Terminal 창에서 ```cd Notebook```으로 해당 파일에 들어간 후  ```jupyter notebook``` 명령어를 사용하여 jupyter notebook 실행
<img width="937" alt="image" src="https://user-images.githubusercontent.com/40768187/177045792-a1e94e77-2cd9-412a-bb93-463f74563b03.png">
새로운 창이 열리면 ```New``` 버튼을 클릭 후 Python 3 를 선택하면 아래와 같은 화면이 나옴
</br>이제 여기에서 Python 코드를 작성하여 실행해볼 수 있음

<img width="1734" alt="image" src="https://user-images.githubusercontent.com/40768187/177045858-7db32a8b-c5d4-4955-a0f2-ca68a6cc7241.png">

</br>

## 📌 데이터 전처리

사전에 문제 없이 실험을 진행하기 위해 데이터를 정리하는 것

1. Scaling
   - Min-Max Normalize
   - Standard Normalize (z-score)

2. Sampling
   - Random Up-Down Sampling
   - SMOTE

3. Dimensionality Reduction
   - PCA

4. Categorical Variable to Numeric Variable
   - Label Encording
   - One-hot Encoding

</br>

```python
import os       # 통째로 파이썬 패키지 가져오기
from os.path import join        # 패키지 중 필요한 부분(객체)만 가져오기
import copy
import warnings
# os 라는 패키지를 다 올리기엔 메모리 부하가 올 수 있음. 파이썬 패키지는 용량이 보통 큼

warnings.filterwarnings('ignore')   # 경고 메세지 무시

import numpy as np
import pandas as pd     # 데이터 전처리 할 때 사용, = Excel 이라고 보면 됨

import sklearn

import matplotlib.pyplot as plt

abalone_path = join('data', 'abalone.txt')      # = data/abalone.txt
# 하드코딩하지 않는 이유 - 윈도우와 리눅스는 경로 표현방식이 다름

column_path = join('data', 'abalone_attributes.txt')

abalone_columns = list()
for l in open(column_path):
    abalone_columns.append(l.strip())
```

전복 데이터셋을 사용하기 위해 불러옴
   - 전복 데이터 셋은 수컷, 암컷, 유아기 3개의 범주로 이루어진 범주형 변수와 길이, 직경, 높이 무게 등 수치형 변수로 이루어져 있음

</br>

데이터를 불러온 후 입력으로 사용할 변수들과 레이블로 사용할 성별 변수로 나눔

```python
data = pd.read_csv(abalone_path, header=None, names=abalone_columns)
label = data['Sex']
```
```data.head()``` 로 5개의 데이터를 확인할 수 있음

<img width="735" alt="image" src="https://user-images.githubusercontent.com/40768187/177045930-9c9f64ef-f10e-45c9-8eda-972a5208a5f9.png">

</br>

```data.shape``` 로 데이터의 모양을 확인할 수 있음 (데이터 개수, 컬럼 개수)

<img width="295" alt="image" src="https://user-images.githubusercontent.com/40768187/177046031-58cf7a13-0fe7-41f5-b66a-771eee5df788.png">

</br>

```del data['Sex']``` 로 Pandas DataFrame 에서 특정 컬럼을 제거</br>
```data.head()``` 로 제거되었는지 확인

<img width="700" alt="image" src="https://user-images.githubusercontent.com/40768187/177046147-7d6bb31f-bedb-4554-8ff2-11bb8265ae76.png">

</br>

```data.describe()``` 로 각 변수별 평균, 표준편차, 최대, 최소, 사분위수 등의 기초 통계량 확인 가능

<img width="841" alt="image" src="https://user-images.githubusercontent.com/40768187/177046411-c01c0aa4-1cf9-453e-b549-5355183293ef.png">

</br>

```data.info()``` 로 각 변수들의 자료형 확인 가능

<img width="478" alt="image" src="https://user-images.githubusercontent.com/40768187/177046440-29511d09-2ffb-45b3-8b9c-047ae5977846.png">

</br>

### 1. Scailing

**스케일링을 왜 할까?**

변수의 크기가 너무 작거나, 너무 큰 경우 해당 변수가 Target에 미치는 영향이 제대로 표현되지 않을 수 있음</br>

- Sklearn 의 대표적인 스케일링 함수
  - Min-Max 스케일링: 특정 변수의 최대, 최소 값으로 조절
  - Standard 스케일링: z-정규화를 이용

#### Min-Max 스케일링
- 값의 범위가 0 ~ 1 사이로 변경됨
- X 에 존재하는 어떤 가장 작은 값 m 에 대해서 m 은 Min(X) 의 값과 같음
- 따라서 스케일링 후 m 은 0 이 되고, X 에 존재하는 어떤 가장 큰 값 M 은 분모의 식과 같아지므로 1 이 됨
- ```data = (data - np.min(data)) / (np.max(data) - np.min(data))```

</br>

1. 모델 불러오기 및 정의

```python
from sklearn.preprocessing import MinMaxScaler
# SKlearn 에서 Min-Max Scaler 는 preprocessing 패키지에 위치함

mMscaler = MinMaxScaler()
```

2. 데이터에서 특징 찾기 (Min, Max 값)

```python
mMscaler.fit(data)
```

3. 데이터 변환

```python
mMscaled_data = mMscaler.fit_transform(data)    # 데이터 끼워맞춰서 변환

mMscaled_data.min()     # 0.0

mMscaled_data.max()     # 1.0
```

4. 결과

```python
data.head()
```

```python
mMscaled_data = pd.DataFrame(mMscaled_data, columns = data.columns)
mMscaled_data.head()
```

<img width="736" alt="image" src="https://user-images.githubusercontent.com/40768187/177047080-0d1932ca-c3f7-4616-ba90-cad8803055ba.png">

</br>

### 2. Sampling

**샘플링을 왜 할까?**
클래스 불균형 문제 때문.
</br>
클래스 불균형 문제?
분류를 목적으로 하는 데이터 셋에 클래스 라벨의 비율이 균형을 맞추지 않고, 한쪽으로 치우친 경우

- 샘플링 종류
  - Oversampling: 적은 클래스의 데이터 수를 증가시킴 (더 많이 사용)
  - Undersampling: 많은 클래스의 데이터 수를 감소시킴

#### Random Over, Under Sampling

가장 쉽게 샘플링 하는 방법은 랜덤으로 데이터를 선택하여, 복제하거나 제거하는 방식.
</br>
위 방식은 다음과 같은 문제점이 존재
- 복제하는 경우, 선택된 데이터의 위치에 똑같이 점을 찍기 때문에 데이터 과적합이 될 수 있음
- 제거하는 경우, 데이터셋이 가지고 있는 정보의 손실이 생길 수 있음

1. 모델 불러오기 및 정의

```python
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

ros = RandomOverSampler()
rus = RandomUnderSampler()
```

오류 발생 시 아래와 같은 명령어 작성
```python
!pip install imblearn
# shell 실행하는 명령어?
# ! 이후에 나오는 내용들을 커맨드창에서 입력하는것과 같이 처리 해달라는 뜻
```

2. 데이터에서 특징 찾기 (데이터 비율), 데이터 샘플링

```python
# 데이터에서 특징을 학습함과 동시에 데이터 샘플링
# Over 샘플링
oversampled_data, oversampled_label = ros.fit_resample(data, label)
oversampled_data = pd.DataFrame(oversampled_data, columns=data.columns)
    # DataFrame -> 표 형태로 되어있는 데이터로 만듬 (pandas)

# Under 샘플링
undersampled_data, undersampled_label = rus.fit_resample(data, label)
undersampled_data = pd.DataFrame(undersampled_data, columns=data.columns)
```

3. 결과

```python
print('원본 데이터의 클래스 비율 \n{}'.format(pd.get_dummies(label).sum()))
print('\nRandom Over 샘플링 결과 \n{}'.format(pd.get_dummies(oversampled_label).sum()))
print('\nRandom Under 샘플링 결과 \n{}'.format(pd.get_dummies(undersampled_label).sum()))
```

<img width="1087" alt="image" src="https://user-images.githubusercontent.com/40768187/177157512-af0c7147-cb1f-4162-beb5-0805609b5f52.png">

비율이 비슷하게 맞춰진 것을 볼 수 있음

</br>

### 3. SMOTE (Synthetic Minority Oversampling Technique)

**SMOTE 를 왜 할까?**

위에서 진행했던 Over, Under 샘플링은 데이터의 중복으로 인한 과적합 문제와 데이터 손실의 문제가 있었음</br>
이런 문제를 최대한 피하면서 데이터를 생성하는 알고리즘이 SMOTE

**SMOTE ?**

수가 적은 클래스의 점을 하나 선택해 k 개의 가까운 데이터 샘플을 찾고,  그 사이에 새로운 점을 생성하는 알고리즘


![KakaoTalk_Photo_2022-07-04-22-07-48](https://user-images.githubusercontent.com/40768187/177161220-368f1938-e2f4-4917-9041-84b0c2165923.png)

</br>

0. 시각화를 통해 생성한 데이터 확인

```python
from sklearn.datasets import make_classification
data, label = make_classification(n_samples=1000, n_features=2, n_informative=2,    # feature 2개 => x, y 축
                           n_redundant=0, n_repeated=0, n_classes=3,   # 3가지로 분류
                           n_clusters_per_class=1,
                           weights=[0.05, 0.15, 0.8],   # 0.05 : 0.15 : 0.8 의 가중치 값으로 데이터 생성
                           class_sep=0.8, random_state=2019)
# make_classification : 실험할 때 필요한 데이터를 강제로 만들어 주는 것. 입맞에 맞는 분류형 샘플 데이터 만들어줌
```

```python
fig = plt.Figure(figsize=(12,6))
plt.scatter(data[:, 0], data[:, 1], c=label, linewidth=1, edgecolor='black')
plt.show()
```

<img width="795" alt="image" src="https://user-images.githubusercontent.com/40768187/177162297-f4ebf533-c74c-4bdb-8e77-9d5bd64b081a.png">

+) SMOTE 는 imblearn 라이브러리의 over_sampling 패키지에 존재

1. 모델 불러오기 및 정의

```python
# 분포에서 떨어져 있는 친구와 그 근처에 선을긋고 선 위에 데이터 채우기

from imblearn.over_sampling import SMOTE
## k_neighbors 파라미터로 가까운 데이터 샘플의 수를 결정할 수 있습니다.
smote = SMOTE(k_neighbors=5)    # 이웃 5개를 보고 데이터 채우기
```

2. 데이터 특징 찾기 (데이터 비율), 데이터 샘플링

```python
smoted_data, smoted_label = smote.fit_resample(data, label)
```

3. 결과

```python
print('원본 데이터의 클래스 비율 \n{}'.format(pd.get_dummies(label).sum()))
print('\nSMOTE 결과 \n{}'.format(pd.get_dummies(smoted_label).sum()))
```

```python
fig = plt.Figure(figsize=(12,6))
plt.scatter(smoted_data[:, 0], smoted_data[:, 1], c=smoted_label, linewidth=1, edgecolor='black')
plt.show()
```

<img width="923" alt="스크린샷 2022-07-04 오후 10 33 20" src="https://user-images.githubusercontent.com/40768187/177165734-49363d24-84c8-4599-8383-37a02f0a2434.png">

이전 것(0번 챕터) 과 비교해 보면 3개로 분류 되어 있는 것을 볼 수 있음
</br> 이전의 2가지 샘플링 방법보다 데이터의 분포를 유지하면서 새로운 위치에 데이터 생성 가능

</br>

### 4. Dimensionality Reduction

**차원 축소를 왜 할까?**

- **차원의 저주?**

    저차원에서는 일어나지 않는 현상들이 고차원에서 데이터를 분석하거나 다룰 때 생겨나는 현상

고차원으로 증가할 수록 공간의 크기 증가, 이에 따라 데이터는 해당 공간에 한정적으로 위치되면서 빈 공간이 많아짐

이러한 이유로 데이터의 차원이 너무 큰 경우, 필요 없는 변수를 제거하고, 과적합을 방지하기 위해 데이터의 차원을 축소함</br>
또는, 사람이 인식할 수 있는 차원은 3차원이 최대이므로 데이터의 시각화를 위해 축소하기도 함

- 차원 축소 기법 종류
  - 주 성분 분석 (Principal Component Analysis, PCA)
    
    여러 차원으로 이루어진 데이터를 가장 잘 표현하는 축으로 Projection 해서 차원을 축소</br>
    데이터를 잘 표현하는 축 = 데이터의 분산을 잘 표현하는 축</br>

    ex) 적군을 기관총으로 쏠 때 정면보다는 양쪽 끝에서 쏘는 것이 잘 맞음</br>

    <img width="218" alt="image" src="https://user-images.githubusercontent.com/40768187/177169409-5fabc60b-c593-4912-9e55-9406a3f4b637.png">

    기본적으로 주성분(PC) 은 데이터 셋을 특이값 분해를 통해 추출된 고유 벡터</br>
    각 고유 벡터들은 서로 직교성을 띄기 때문에 데이터를 주성분으로 Projection 시켰을 때 서로 독립적으로 데이터를 잘 표현할 수 있음

    PCA 단점으로는 떨어뜨린 주성분이 어떤 컬럼인지 설명할 수 없음

  - 주 성분 분석의 단계
    1. 각 컬럼들의 값의 범위를 평균과 표준편차를 사용해 정규화 (스케일링)
    2. 데이터의 공분산 계산
    3. 공분산 행렬에 대해 특이값 분해를 하여 주성분 (고유 벡터) 와 고유 값을 얻어냄
    4. 주성분과 대응되는 고유값은 주성분이 데이터의 분산을 표현하는 정도의 척도로 사용됨</br>
        따라서 고유값의 크기와 비율을 보고 몇개의 주성분을 선택할 것인지 또는 원하는 차원의 개수만큼 주성분 선택
    5. 선택한 주성분으로 모든 데이터를 Projection 시켜 데이터 차원 축소

</br>

**Projection? (사영)**

벡터 b 를 벡터 a 에 사영한다는 것은 벡터 a 에 대해 수직인 방향으로 벡터 b 를 떨어뜨리는 것을 의미</br>
간단히 말해, 벡터 b 의 그림자를 벡터 a 에 떨어뜨린 것

<img width="209" alt="image" src="https://user-images.githubusercontent.com/40768187/177171448-cb773253-e473-4288-9463-59f74641cc15.png"> <img width="473" alt="image" src="https://user-images.githubusercontent.com/40768187/177172674-8d3ef0e7-a441-4a08-9efa-bf9d9d239b72.png">

v 의 u 로 위로의 사영

**PCA의 기본 원리는 데이터의 분산을 가장 잘 표현하는 벡터를 찾아 해당 벡터에 데이터들을 사영 시키는 것**

0. 데이터 살펴보기

```python
from sklearn.datasets import load_digits
digits = load_digits()      # MNIST? 손글씨 데이터 ==> 바이블적인 데이터 (load_digits())
```

```python
print(digits.DESCR)
```

<img width="795" alt="image" src="https://user-images.githubusercontent.com/40768187/177174639-0ab58d5c-7521-4490-96fc-ce9759c65dec.png">

</br>

```python
data = digits.data
label = digits.target   # 답 (예측한 답)
```

```python
data.shape  # (전체 데이터수, 컬럼 수)
```

숫자 이미지가 64 차원 벡터로 표현되어 있으므로 이미지를 확인하기 위해서는 (8,8) 행렬로 변환해줘야 함

```python
plt.imshow(data[0].reshape((8,8)))      # 8 x 8 로 잘라주기
print('Label : {}'.format(label[0]))
```

<img width="411" alt="image" src="https://user-images.githubusercontent.com/40768187/177174728-e77c6417-f9aa-4141-a55c-95f4b80de553.png"> <img width="341" alt="스크린샷 2022-07-04 오후 11 26 25" src="https://user-images.githubusercontent.com/40768187/177174511-55542a2e-ebf8-4a02-9c94-57bc0b188737.png">

0번째 데이터는 이미지 상으로 0으로 보이고, 라벨도 0인 것을 확인함</br>
PCA를 통해 64 차원 데이터를 2차원 데이터로 축소 시킬 예정
- 여기에서 digits 데이터의 각 픽셀(변수)의 스케일은 0 ~ 16 으로 같으므로 추가적인 정규화 진행X

</br>

1. 모델 불러오기 및 정의

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)   # 2차원
```

2. 데이터에서 특징 찾기 (주 성분 찾기)

```python
pca.fit(data)
```

3. 데이터 변환 (주 성분으로 데이터 사영)

```python
new_data = pca.transform(data)
```

4. 결과

```python
print('원본 데이터의 차원 \n{}'.format(data.shape))
print('\nPCA를 거친 데이터의 차원 \n{}'.format(new_data.shape))
```

```python
plt.scatter(new_data[:,0], new_data[:, 1], c=label, linewidth=1, edgecolor='black')
plt.show()
```

<img width="809" alt="image" src="https://user-images.githubusercontent.com/40768187/177181745-9e848e1a-fc6c-469f-afb2-1e64701ff3e8.png">

</br>

### 5. Catagorical Variable to Numeric Variable

범주형 변수를 수치형 변수로 나타내는 방법

**범주형 변수?**
- 차의 등급을 나타내는 [소형, 중형, 대형] 처럼 표현되는 변수
- 주로 데이터 상에서 문자열로 표현되는 경우가 많고, 문자와 숫자가 매핑되는 형태로 표현되기도 함

**범주형 변수를 수치형 변수로 나타내는 이유가 뭘까?**

그냥 분류일 뿐인데 컴퓨터는 텍스트를 분석을 하면서 시간이 오래걸리게 됨

**종류**
- Label Encoding: n 개의 범주형 데이터를 0~n-1 의 연속적인 수치 데이터로 표현
  - ex) 소형 - 0, 중형 - 1, 대형 - 2
  - Sklearn 의 preprocessing 패키지에 존재
- One-hot Encoding:  n 개의 범주형 데이터를 n 개의 비트 (0,1) 벡터로 표현
  - ex) 소형 - [1,0,0], 중형 - [0,1,0], 대형 - [0,0,1]
  - 서로 다른 범주에 대해서는 벡터 내적을 취했을 때 내적 값 0
  - 이는 서로 다른 범주 데이터는 독립적인 관계라는 것을 뜻함
  - 문장의 차원을 펼쳐놓고 encoding 하는 것
  - ex) 영화 리뷰를 긁어서 encoding 해서 분석
  - Sklearn 의 preprocessing 패키지에 존재

<img width="550" alt="스크린샷 2022-07-05 오전 12 28 01" src="https://user-images.githubusercontent.com/40768187/177184214-fe563f51-dafa-4657-9275-197415fb7e4d.png">

#### 1. Label Encoding

전복 데이터의 target이었던, 성별 변수를 수치형 변수로 변환하기

0. 데이터 살펴보기

```python
data = pd.read_csv(abalone_path, header=None, names=abalone_columns)
label = data['Sex']
del data
```

```python
label.head()
```

<img width="707" alt="image" src="https://user-images.githubusercontent.com/40768187/177184675-f1d15ad8-a7ee-4e8c-9007-fdeeb0e395cf.png">

1. 모델 불러오기 및 정의하기

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
```

2. 데이터에서 특징 찾기 (범주의 수)

```python
le.fit(label)
```

3. 데이터 변환 (범주형 변수를 수치형 변수로)

```python
label_encoded_label = le.transform(label)
```

4. 결과

```python
result = pd.DataFrame(data = np.concatenate([label.values.reshape((-1,1)), 
label_encoded_label.reshape((-1, 1))], axis=1), columns=['label', 'label_encoded'])

result.head(10)
```

```python
le.inverse_transform(label_encoded_label)
```

<img width="1078" alt="image" src="https://user-images.githubusercontent.com/40768187/177185185-60028e3e-2db6-404b-bfac-dbf078143e33.png">

</br>

#### 2. Label Encoding

1. 모델 불러오기 및 정의

```python
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
```

2. 데이터에서 특징 찾기 (범주의 수)

```python
ohe.fit(label.values.reshape((-1, 1)))
```

3. 데이터 변환 (범주형 변수를 수치형 변수로)

```python
one_hot_encoded = ohe.transform(label.values.reshape((-1,1)))
```

4. 결과

```python
columns = np.concatenate([np.array(['label']) , ohe.categories_[0]])

result = pd.DataFrame(data = np.concatenate([label.values.reshape((-1,1)), 
one_hot_encoded.reshape((-1, 3))], axis=1), columns=columns)

result.head(10)
```

<img width="1071" alt="image" src="https://user-images.githubusercontent.com/40768187/177185877-1f7ede62-1082-456a-bff6-895a14faae38.png">

</br>


#### 추가 메모
- 컬럼 개수 = 컬럼 개수 차원
- 데이터 누락은 엄청난 문제를 일으킴 => **노이즈** 라고 함
- 데이터가 충분히 많으면 누락된 데이터가 있는 열을 지워버려도 됨
- 데이터가 부족할 때 살릴려면 영향을 안미치고 채워야함 -> 평균 넣기
- 위 방식은 제대로 된 실험이 될 수 없음. 그래서 MinMaxScaler, PCA 등의 방식을 사용하는 것

</br>

## 📌 Clustering (군집화)

데이터를 막 나눠보다가 잘 나눠졌을 때의 결과의 선 찾기

- 종류
  - k-means Clustering
    - 각 클러스터에 할당된 데이터 포인트들의 평균 좌표를 이용해 중심점을 반복적으로 업데이트하며 클러스터 형성
    - 점과 점 사의 거리 측정 방식
      - Manhattan Distance: 각 축에 대해 수직으로만 이동하여 계산하는 거리 측정방식
      - Euclidean Distance: 점과 점 사이의 가장 짧은 거리를 계산하는 거리 측정방식
  
  - Hierarchical Clustering
    - 거리(Distance) 또는 유사도(Similarity)를 기반으로 클러스터를 형성
    - k-means Clustering 과 다르게 클러스터의 수를 설정해 줄 필요 없음
    - 클러스터 형태를 시각적으로 표현해주는 덴드로그램을 통해 적절한 클러스터 수 선택 가능
    - Bottom-Up 방식의 ```Agglomerative Method```와 Top-Down 방식의 ```Divisive Method```로 나뉨
    - 가장 가까운 클러스터를 찾는 방식
      - Single Linkage: 두 클러스터 내의 가장 가까운 점 사이의 거리
      - Complete Linkage: 두 클러스터 내의 가장 먼 점 사이의 거리
      - Average Linkage: 두 클러스터 내의 모든 점 사이의 평균 거리

- 평가
  - Silhouette: 한 클러스터 안의 데이터들이 다른 클러스터와 비교해 얼마나 비슷한가를 나타냄
    - 클러스터 간 거리 -> 높을 수록 좋은 것

### 1. k-means Clustering

- 코드
  
  ```python
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    data = pca.fit_transform(data)

    data.shape

    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=3)

    kmeans.fit(data)

    cluster = kmeans.predict(data)

    plt.scatter(data[:, 0], data[:, 1], c=cluster, linewidth=1, edgecolor='black')
    plt.show()
  ```

- 결과
  
<img width="407" alt="image" src="https://user-images.githubusercontent.com/40768187/177189580-e3667151-756c-4e14-9972-a883d256e341.png">


### 2. k-means Clustering

#### Single Linkage

- 코드

    ```python
    from sklearn.cluster import AgglomerativeClustering
    single_clustering = AgglomerativeClustering(n_clusters=3, linkage='single')

    single_clustering.fit(data)

    single_cluster = single_clustering.labels_
    ```

- 결과
  
  산점도

  ```python
    plt.scatter(data[:,0], data[:,1], c=single_cluster)
    plt.title('Sklearn Single Linkage Hierarchical Clustering')
    plt.show()
  ```

    <img width="385" alt="image" src="https://user-images.githubusercontent.com/40768187/177190870-5b3fdf82-a97c-4044-87ba-c82c7a0e63b6.png">

  덴드로그램

  ```python
  from scipy.cluster.hierarchy import dendrogram
    plt.figure(figsize=(10,10))

    # Hierarchical Clustering의 자식 노드
    children = single_clustering.children_

    # 각 자식 노드간의 거리 정보를 가지고 있지 않기 때문에, 균일하게 그리도록 합니다.
    distance = np.arange(children.shape[0])

    # 각 클러스터 단계를 포함한 노드의 수 계산
    no_of_observations = np.arange(2, children.shape[0]+2)

    # 덴드로그램을 그리기위한 연결 매트릭스를 생성합니다.
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # 덴드로그램을 그립니다.
    dendrogram(linkage_matrix, p = len(data), labels = single_cluster, 
            show_contracted=True, no_labels = True, )
    plt.show()
  ```

    <img width="595" alt="image" src="https://user-images.githubusercontent.com/40768187/177190903-d1ba1911-b53b-4e17-856c-568c7ced844a.png">


#### Complete Linkage

- 코드

    ```python
    complete_clustering = AgglomerativeClustering(n_clusters=3, linkage='complete')

    complete_clustering.fit(data)

    complete_cluster = complete_clustering.labels_
    ```

- 결과
  
  산점도

  ```python
    plt.scatter(data[:,0], data[:,1], c=complete_cluster)
    plt.title('Sklearn Complete Linkage Hierarchical Clustering')
    plt.show()
  ```

  <img width="384" alt="스크린샷 2022-07-05 오전 1 30 16" src="https://user-images.githubusercontent.com/40768187/177192668-3287680a-ce9d-46ca-b0b1-22227a79aeea.png">

  덴드로그램

  ```python
  from scipy.cluster.hierarchy import dendrogram
    plt.figure(figsize=(10,10))

    # Hierarchical Clustering의 자식 노드
    children = complete_clustering.children_

    # 각 자식 노드간의 거리 정보를 가지고 있지 않기 때문에, 균일하게 그리도록 합니다.
    distance = np.arange(children.shape[0])

    # 각 클러스터 단계를 포함한 노드의 수 계산
    no_of_observations = np.arange(2, children.shape[0]+2)

    # 덴드로그램을 그리기위한 연결 매트릭스를 생성합니다.
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # 덴드로그램을 그립니다.
    dendrogram(linkage_matrix, p = len(data), labels = complete_cluster, 
            show_contracted=True, no_labels = True, )
    plt.show()
  ```

    <img width="597" alt="image" src="https://user-images.githubusercontent.com/40768187/177192773-53f95933-5d13-4091-b5a8-15764c930f28.png">

#### Average Linkage

- 코드

    ```python
    average_clustering = AgglomerativeClustering(n_clusters=3, linkage='average')

    average_clustering.fit(data)

    average_cluster = average_clustering.labels_
    ```

- 결과
  
  산점도

  ```python
    plt.scatter(data[:,0], data[:,1], c=average_cluster)
    plt.title('Sklearn Average Linkage Hierarchical Clustering')
    plt.show()
  ```

  <img width="386" alt="image" src="https://user-images.githubusercontent.com/40768187/177193093-dd7779ad-4737-49f4-bf25-760c7d1cc633.png">

  덴드로그램

  ```python
    from scipy.cluster.hierarchy import dendrogram
    plt.figure(figsize=(10,10))

    # Hierarchical Clustering의 자식 노드
    children = average_clustering.children_

    # 각 자식 노드간의 거리 정보를 가지고 있지 않기 때문에, 균일하게 그리도록 합니다.
    distance = np.arange(children.shape[0])

    # 각 클러스터 단계를 포함한 노드의 수 계산
    no_of_observations = np.arange(2, children.shape[0]+2)

    # 덴드로그램을 그리기위한 연결 매트릭스를 생성합니다.
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # 덴드로그램을 그립니다.
    dendrogram(linkage_matrix, p = len(data), labels = average_cluster, 
            show_contracted=True, no_labels = True, )
    plt.show()
  ```

    <img width="595" alt="image" src="https://user-images.githubusercontent.com/40768187/177193114-c250fd8a-9d18-49ac-9104-6fb48c3eaf23.png">

#### 가장 좋은 클러스터를 형성하는 클러스터 수

k-means 클러스터링과 Average Linkage를 사용한 Hierarchical 클러스터링에서 가장 높은 점수의 클러스터 수는 무엇인지 알아볼 예정

Silhouette 스코어링은 Sklearn의 metrics 패키지에 존재

1. k-means
   
   ```python
   from sklearn.metrics import silhouette_score

   best_n = 1
    best_score = -1

    for n_cluster in range(2, 11):
        kmeans = KMeans(n_clusters=n_cluster)
        kmeans.fit(data)
        cluster = kmeans.predict(data)
        score = silhouette_score(data, cluster)
        
        print('클러스터의 수 : {}, 실루엣 점수 : {:.2f}'.format(n_cluster, score))
        if score > best_score :
            best_n = n_cluster
            best_score = score
            
    print('가장 높은 실루엣 점수를 가진 클러스터 수 : {}, 실루엣 점수 : {:.2f}'.format(best_n, best_score))
   ```

    클러스터의 수 : 2, 실루엣 점수 : 0.49</br>
    클러스터의 수 : 3, 실루엣 점수 : 0.57</br>
    클러스터의 수 : 4, 실루엣 점수 : 0.49</br>
    클러스터의 수 : 5, 실루엣 점수 : 0.45</br>
    클러스터의 수 : 6, 실루엣 점수 : 0.42</br>
    클러스터의 수 : 7, 실루엣 점수 : 0.38</br>
    클러스터의 수 : 8, 실루엣 점수 : 0.38</br>
    클러스터의 수 : 9, 실루엣 점수 : 0.38</br>
    클러스터의 수 : 10, 실루엣 점수 : 0.38</br>
    가장 높은 실루엣 점수를 가진 클러스터 수 : 3, 실루엣 점수 : 0.57

2. Average Linkage Hierarchical Clustering
   
   ```python
    from sklearn.metrics import silhouette_score

    best_n = 1
    best_score = -1

    for n_cluster in range(2, 11):
        average_clustering = AgglomerativeClustering(n_clusters= n_cluster, linkage='average')
        average_clustering.fit(data)
        cluster = average_clustering.labels_
        score = silhouette_score(data, cluster)
        
        print('클러스터의 수 : {}, 실루엣 점수 : {:.2f}'.format(n_cluster, score))
        if score > best_score :
            best_n = n_cluster
            best_score = score
            
    print('가장 높은 실루엣 점수를 가진 클러스터 수 : {}, 실루엣 점수 : {:.2f}'.format(best_n, best_score))
   ```

클러스터의 수 : 2, 실루엣 점수 : 0.49</br>
클러스터의 수 : 3, 실루엣 점수 : 0.56</br>
클러스터의 수 : 4, 실루엣 점수 : 0.48</br>
클러스터의 수 : 5, 실루엣 점수 : 0.42</br>
클러스터의 수 : 6, 실루엣 점수 : 0.37</br>
클러스터의 수 : 7, 실루엣 점수 : 0.34</br>
클러스터의 수 : 8, 실루엣 점수 : 0.34</br>
클러스터의 수 : 9, 실루엣 점수 : 0.37</br>
클러스터의 수 : 10, 실루엣 점수 : 0.33</br>
가장 높은 실루엣 점수를 가진 클러스터 수 : 3, 실루엣 점수 : 0.56

## 📌 Regression (회귀)

- Linear Regression: 종속 변수와 한 개 이상의 독립 변수와의 선형 상관 관계를 모델링하는 회귀 분석 기법
  - Simple Linear Regression: x (독립 변수) 가 1개인 단순 회귀 분석

    <img width="365" alt="image" src="https://user-images.githubusercontent.com/40768187/177226899-0b7ac3e3-b7de-46b0-a206-115caddbf29c.png">

  - Multiple Linear Regression: x (독립 변수) 가 2개 이상인 다중 회귀 분석

    <img width="366" alt="image" src="https://user-images.githubusercontent.com/40768187/177226953-3a411678-2a96-4f50-b232-58505988f935.png">

- Machine Learning Algorithm Based Regression
  - Decision Tree Regression: 데이터 불순도(impurity, Entropy)를 최소화 하는 방향으로 트리를 분기하여 모델 생성

    <img width="372" alt="image" src="https://user-images.githubusercontent.com/40768187/177227412-7807b3f9-5713-49a9-bb9f-081eebe53e11.png">

  - Support Vector Machine Regressor: 결정 경계와 가장 가까운 데이터 샘플의 거리(Margin) 을 최대화 하는 방식

    <img width="366" alt="image" src="https://user-images.githubusercontent.com/40768187/177227474-ff2f7dfa-3254-4e10-935b-c70cd66d734e.png">

  - Random Forest Regression
  - MLP Regression: 딥러닝의 기본 모델인 뉴럴 네트워크를 기반으로 한 회귀 모델, MLP => 입력층-은닉층-출력층

    <img width="364" alt="image" src="https://user-images.githubusercontent.com/40768187/177227534-9559bc5c-f556-459e-a137-2998b81acff9.png">

  
- 평가
  - R 제곱: 학습한 회귀 모델이 얼마나 데이터를 잘 표현하는지에 대한 정도를 나타내는 통계적인 척도 (0 < R 제곱 < 1)
  - Adjusted R 제곱: 변수의 수가 증가하는 경우, R 제곱 값은 모델 성능에 관계없이 값이 유지되거나 증가하게 됨. 이러한 문제를 해결하기 위해 나온 평가 척도 (Sklearn 지원X)


## 📌 Classification (분류)

머신러닝과 통계학에서의 분류는 새로 관측된 데이터가 어떤 범주 집합에 속하는지를 식별하는 것을 말함

훈련 데이터를 이용해 모델을 학습하면, 모델은 결정 경계 (Decision boundary) 라는 데이터를 분류하는 선 만들어냄

- 종류
  - Logistic Regression: 선형 회귀 모델에서 변형된 모델

    <img width="536" alt="image" src="https://user-images.githubusercontent.com/40768187/177308865-fdde732e-748c-4bbc-9e06-7895704de2ef.png">

  - SVM: 주어진 데이터를 바탕으로 하여 두 카테고리 사이의 간격을 최대화하는 데이터 포인트를찾아내고, 그 서포트 벡터에 수직인 경계를 통해 데이터 분류하는 알고리즘

    <img width="543" alt="image" src="https://user-images.githubusercontent.com/40768187/177308595-ad7ff8bf-cd9f-4de6-8d71-635814c565be.png">

    <img width="361" alt="image" src="https://user-images.githubusercontent.com/40768187/177308762-17e21677-9579-4d7d-ad99-feea3a6358c3.png">

  - Decision Tree: 입력 변수를 특정한 기준으로 잘라(분기) 트리 형태의 구조로 분류하는 모델, 데이터의 불순도를 최소화할 수 있는 방향으로 트리 분기
    - 불순도? 정보 이론에서 말하는 얻을 수 있는 정보량이 많은 정도
  - Random Forest: 작은 트리들을 여러개만들어 합치는 모델

- 평가
  - Accuracy: 모든 데이터에 대해 클래스 라벨을 얼마나 잘 맞췄는지 계산
  - Confution Matrix: 모델의 목적에 맞게 분류 모델 평가
    - Precision, Sensitivity, Specificity, False Alarm
  - ROC Curve, AUC: 민감도와 특이도가 서로 어떤 관계를 가지며 변하는지 2차원 평면 상에 표현한 것
    - Curve: 그려지는 곡선
    - AUC: ROC Curve의 면, 1에 가까울 수록 좋은 모델

</br>

### 추가 메모

<img width="783" alt="image" src="https://user-images.githubusercontent.com/40768187/177309368-7bebfb8c-f017-4bdb-905f-e9bcb2191547.png">

</br>

- 지도 학습: 문제, 답 둘 다 주고, 비슷한 거 나오면 맞춤 ex) Classification
- 비지도 학습: 특정한 학습 없이 감이 생기는 것. 데이터를 보고 알아서 분류 ex) Clustering

</br>

## 📌 Azure ML 파이프라인

### Azure ML Notebooks 사용하기
</br>

https://github.com/yejin25/SKT-FLYAI/blob/master/1%EC%A3%BC%EC%B0%A8/0630-Flask%2BAzureML.md

위 링크에서 Azure ML 을 만들고, Designer, Automated ML 을 사용한 적이 있음

이번엔 Notebooks 에서 Python 코드를 작성할 예정

</br>

1. Notebooks 시작하기

    <img width="1605" alt="image" src="https://user-images.githubusercontent.com/40768187/177312854-2107273b-7f95-494f-a141-a466f1b436cc.png">


2.  ```+ Create``` > ```Create new file``` 선택 후 파일 생성

    <img width="1614" alt="image" src="https://user-images.githubusercontent.com/40768187/177313067-43b1eb4d-b9c1-4308-bea0-96e6648f9c30.png">

3. Compute instance 선택
    
    <img width="1168" alt="image" src="https://user-images.githubusercontent.com/40768187/177315355-0fb3a65f-27b3-4ba0-a5c0-0aa46894e589.png">

    생성된 인스턴스가 없다면 생성하러 ㄱㄱ 이미 해봤으니깐 잘할듯

4. Python 코드 작성
    
    <img width="1168" alt="image" src="https://user-images.githubusercontent.com/40768187/177315504-892d1aec-cfc0-478f-b3c0-9ffce51de50c.png">

    코드는 실행 버튼 말고도 ```shift``` + ```Enter``` 를 눌러주면 실행됨

5. 샘플 코드 설명

    작업공간 생성

   ```python
    from azureml.core import Workspace
    ws = Workspace.from_config()
    print('Workspace name:' + ws.name)
   ```

   실험공간 생성

   ```python
    from azureml.core import Experiment
    experiment = Experiment(workspace=ws, name='diabetes-experiment')
   ```

   데이터 준비

   ```python
    from azureml.opendatasets import Diabetes
    from sklearn.model_selection import train_test_split

    x_df = Diabetes.get_tabular_dataset().to_pandas_dataframe().dropna()
    y_df = x_df.pop("Y")

    X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2, random_state=66)

    print(X_train)
   ```

   모델 훈련하면서 로그 남기고 모델 파일 업로드

   ```python
    from sklearn.linear_model import Ridge
    from sklearn.metrics import mean_squared_error
    from sklearn.externals import joblib
    import math

    alphas = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

    for alpha in alphas:
        run = experiment.start_logging()
        run.log('alpha_value', alpha)

        model = Ridge(alpha=alpha)
        model.fit(X=X_train,y=y_train)

        y_pred=model.predict(X=X_test)
        
        rmse = mean_squared_error(y_true=y_test, y_pred=y_pred)
        run.log('rmse', rmse)

        model_name = 'model_alpha_' + str(alpha) + '.pkl'
        filename = 'outputs/' + model_name

        joblib.dump(value=model, filename=filename)
        run.upload_file(name=model_name, path_or_stream=filename)
        run.complete()

        print(f'{alpha} exp completed')     # f: alpha 값을 치환해주는 거?
   ```

    아래와 같이 로그를 남기면서 훈련시키는 것을 볼 수 있음

   <img width="1165" alt="image" src="https://user-images.githubusercontent.com/40768187/177316965-851e355f-de7f-4a60-af40-95aad575501e.png">

   </br>

    파일 목록을 새로고침해주면 outputs 폴더를 생겼고, 모델 파일들이 업로드 되어 있는 것을 확인할 수 있음

   <img width="638" alt="image" src="https://user-images.githubusercontent.com/40768187/177317462-52407ffe-07fe-40a2-b2be-dc31df6d21a3.png">

   </br>

    Studio 에서 실험 결과 확인 및 모델 다운로드

    ```python
    experiment
    ```
    
    <img width="1135" alt="image" src="https://user-images.githubusercontent.com/40768187/177317797-522e899f-3cf0-47fc-ab5a-fc6fc4fb9bde.png">

    Report Page 확인해보기

    <img width="1599" alt="image" src="https://user-images.githubusercontent.com/40768187/177317876-c6989b8d-4664-4126-a48d-973850e4d1c4.png">

    </br>

    Best model 탐색 후 다운로드

   ```python
    minimum_rmse_runid = None
    minimum_rmse = None

    for run in experiment.get_runs():
        run_metrics = run.get_metrics()
        run_details = run.get_details()
        # each logged metric becomes a key in this returned dict
        run_rmse = run_metrics["rmse"]
        run_id = run_details["runId"]
        
        if minimum_rmse is None:
            minimum_rmse = run_rmse
            minimum_rmse_runid = run_id
        else:
            if run_rmse < minimum_rmse:
                minimum_rmse = run_rmse
                minimum_rmse_runid = run_id

    print("Best run_id: " + minimum_rmse_runid)
    print("Best run_id rmse: " + str(minimum_rmse))
   ```

   ```python
   from azureml.core import Run
    best_run = Run(experiment=experiment, run_id=minimum_rmse_runid)
    print(best_run.get_file_names())
   ```

   ```python
   best_run.download_file(name=str(best_run.get_file_names()[0]))
   ```


    <img width="1031" alt="image" src="https://user-images.githubusercontent.com/40768187/177318578-362dbb48-d0f0-402c-8373-bb4dbf502bdd.png">

    ```model_alpha_0.1.pkl``` 이라는 베스트 모델 파일이 다운로드 된 것을 확인할 수 있음

    </br>

    DataStore 에 Input/Output 데이터셋 등록

   ```python
    import numpy as np
    from azureml.core import Dataset

    np.savetxt('features.csv', X_train, delimiter=',')
    np.savetxt('labels.csv', y_train, delimiter=',')

    datastore = ws.get_default_datastore()
    datastore.upload_files(files=['./features.csv', './labels.csv'],
                        target_path='diabetes-experiment/',
                        overwrite=True)

    input_dataset = Dataset.Tabular.from_delimited_files(path=[(datastore, 'diabetes-experiment/features.csv')])
    output_dataset = Dataset.Tabular.from_delimited_files(path=[(datastore, 'diabetes-experiment/labels.csv')])
   ```
    datastore.upload_files함수는 deprecated 되었다고 함</br>
    FileDatasetFactory.upload_directory 대신 쓰라고 했지만, 파이썬을 몰라서 일단 패스

    <img width="1397" alt="image" src="https://user-images.githubusercontent.com/40768187/177324035-720b87c0-c6de-4a06-9234-ff8eb356b79a.png">
    파일 목록에 csv 파일 추가된 것을 확인할 수 있음

    </br>

    Best model 등록

   ```python
    import sklearn

    from azureml.core import Model
    from azureml.core.resource_configuration import ResourceConfiguration


    model = Model.register(workspace=ws,
                        model_name='diabetes-experiment-model',
                        model_path=f"./{str(best_run.get_file_names()[0])}", 
                        model_framework=Model.Framework.SCIKITLEARN,  
                        model_framework_version=sklearn.__version__,  
                        sample_input_dataset=input_dataset,
                        sample_output_dataset=output_dataset,
                        resource_configuration=ResourceConfiguration(cpu=1, memory_in_gb=0.5),
                        description='Ridge regression model to predict diabetes progression.',
                        tags={'area': 'diabetes', 'type': 'regression'})

    print('Name:', model.name)
    print('Version:', model.version)
   ```

   <img width="1613" alt="image" src="https://user-images.githubusercontent.com/40768187/177325262-51a79420-9005-43d6-a126-9540013f0002.png">

    모델 배포

   ```python
    service_name = 'diabetes-service'

    service = Model.deploy(ws, service_name, [model], overwrite=True)
    service.wait_for_deployment(show_output=True)
   ```

   배포 서비스 테스트

   - 노트북

        ```python
        import json

        input_payload = json.dumps({
            'data': X_train[0:2].values.tolist(),
            'method': 'predict'
        })

        output = service.run(input_payload)

        print(output)
        ```

        <img width="578" alt="image" src="https://user-images.githubusercontent.com/40768187/177325087-95e6d205-2330-493d-8c11-05c60993c6b5.png">
        
    - [Models]-[Endpoints]-[서비스명]-[Test]

        <img width="742" alt="image" src="https://user-images.githubusercontent.com/40768187/177325569-16183b44-452b-466b-8dfa-939b02e15b3b.png">

    서비스 삭제

    ```python
    service.delete()
    ```