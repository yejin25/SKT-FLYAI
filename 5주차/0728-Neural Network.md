# 5주차 2022 07 28
</br>

## 📌 인공 신경망 (Neural Network)

### 퍼셉트론 (Perceptron)

</br>

<img width="1005" alt="image" src="https://user-images.githubusercontent.com/40768187/183297379-9f32beca-d2c7-4270-844d-df27f2b45c2d.png">

</br>

- Frank Rosenblatt 가 1957년에 제안한 초기 형태의 인공 신경망
- 다수의 입력으로부터 하나의 결과를 내보내는 알고리즘
- 두 종류의 클래스를 직선으로 분류하는 선형 분류기 (Linear classifier)

</br>

## XOR 문제 - 첫번째 AI Winter

</br>

<img width="271" alt="image" src="https://user-images.githubusercontent.com/40768187/183299453-dc981fd8-502c-4ed7-81c4-13ae9c68f23f.png">

</br>

다른 논리연산과 다르게 선 1개로 분류되지 않음 (퍼셉트론은 선 1개로 나타남)

</br>

### XOR 문제 해결 (MLP)

</br>

<img width="400" alt="image" src="https://user-images.githubusercontent.com/40768187/183300722-a88772a6-842d-4106-8e7c-beea39acb712.png">

</br>

<img width="600" alt="image" src="https://user-images.githubusercontent.com/40768187/183301097-8cdefb28-e233-47cc-8f67-e00a0dd87ad0.png">

</br>

|       |  x1   |  x2   | NAND  |  OR   | y(AND) |
| :---: | :---: | :---: | :---: | :---: | :----: |
|  P1   |   0   |   0   |   1   |   0   |   0    |
|  P3   |   1   |   0   |   1   |   1   |   1    |
|  P4   |   0   |   1   |   1   |   1   |   1    |
|  P2   |   1   |   1   |   0   |   1   |   0    |

</br>

### 정리

```Perceptron's'``` by Marvin Minsky

- We need to use MLP, multilayer perceptrons
- No one on earth had found a viable way to train MLPs good enough to learn such simple functions => 각각의 W,b 를 학습시킬 수 없음
- **Perceptron은 비선형 문제를 풀수 없다.**
- AI winter의 시작

</br>

### 오차 역전파 (Backpropagation)

</br>

<img width="700" alt="image" src="https://user-images.githubusercontent.com/40768187/183301668-dae37197-e7f2-45ca-b2d8-98f02e7c6d6e.png">

</br>

- MLP 를 학습시킬 수 있는 알고리즘
- 오차(손실)을 네트워크의 뒤로 전달하면서, Weight 들을 갱신시키는 과정
- by Paul Werbos, Geoffrey Hinton

</br>

### Graph 표기 - 역전파

</br>

<img width="800" alt="image" src="https://user-images.githubusercontent.com/40768187/183422182-6e1be7b9-ef88-4b83-9146-958d25acac86.png">

</br>

임의의 한 노드에서의 미분값은, 바로 앞 노드에서 넘어오는 미분값에 로컬 미분값을 곱하는 것만으로 계산할 수 있음

</br>

<img width="668" alt="image" src="https://user-images.githubusercontent.com/40768187/183422555-12a41033-dacc-4f1f-98ae-3cdd91fe213f.png">

</br>

- $∂z\over∂x$ & $∂z\over∂y$ 는 local gradients

- $∂L\over∂z$ is the loss rom the **previous layer** which has to be backpropagated to other layers

</br>

### 순전파 (Forward Propagation)

</br>

![IMG_0988ED6BD122-1](https://user-images.githubusercontent.com/40768187/183423720-48c98e68-a47a-4610-8969-e0cfa9a1fdf0.jpeg)

</br>

### 역전파 (Backpropagation)

</br>

<img width="853" alt="image" src="https://user-images.githubusercontent.com/40768187/183423887-f67e99ca-1c96-4eca-b599-584a67c9d912.png">

</br>

- Gradient 계산

    $\frac{∂E_{total}}{∂x} = \frac{∂E_{total}}{∂o_1}\times\frac{∂o_1}{∂z_3}\times\frac{∂z_3}{∂w_5}=0.02592286$

</br>

- 가중치 업데이트, 학습율 = 0.5

    $w5 = w5 - \alpha\frac{∂E_{total}}{∂w_5} = 0.45 - 0.5 \times 0.02592286 = 0.43703857$

</br>

![IMG_C92EFCEA8EB8-1](https://user-images.githubusercontent.com/40768187/183430997-81bcaca5-4278-410d-b83c-a092d1956ab5.jpeg)

</br>

### 기울기 소실 (Gradient Vanishing)

깊은 신경망 (Deep Neural Network) 의 경우, 입력층으로 갈수록 역전파 과정에서 미분값이 사라지면서 학습이 안되는 현상

+) $w_1$ 엄청 작은 값 들어옴, 원인 - 시그모이드

</br>

## 기울기 소실 - 2번째 Ai Winter

</br>

<img width="482" alt="image" src="https://user-images.githubusercontent.com/40768187/183438373-478acc74-a90d-415e-af5d-04acdbd3fbcc.png">

</br>

Sigmoid의 미분값이 거의 0인 것을 볼 수 있음

</br>

### 기울기 소실 원인

역전파 과정에서 Sigmoid 의 미분값의 연속적으로 곱해지면서 기울기가 0으로 사라짐

<img width="904" alt="image" src="https://user-images.githubusercontent.com/40768187/183439943-f588c6d5-c68e-42e1-b268-5dc2ec313401.png">


</br>

### ReLu 함수

<img width="846" alt="image" src="https://user-images.githubusercontent.com/40768187/183440132-2aa3a3e4-454f-44ce-8b62-bf49089c7fb6.png">

</br>

- Sigmoid 의 기울기 소실 문제를 해결하기 위해 새로운 Activation function 사용
- ReLu 는 입력값이 0보다 작으면 0이고, 0보다 크면 입력값 그대로를 내보냄

</br>

## 딥러닝, 학습 관련 기술들

### 활성화 함수 (Activation Function)

<img width="977" alt="스크린샷 2022-08-08 오후 11 43 37" src="https://user-images.githubusercontent.com/40768187/183446297-30a1d4d9-8094-4c22-9fdb-4c762d938a01.png">

</br>

~~ReLU 를 보통 많이 씀~~

</br>

### MPL -> DNN (Deep Neural Network)

</br>

다층 신경망 (MLP) 을 안정적으로 학습시킬 수 있는 알고리즘 = 딥러닝

<img width="677" alt="image" src="https://user-images.githubusercontent.com/40768187/183447824-eb1e59d4-e968-46ad-9894-4de1ce839c13.png">

</br>

### 학습율 (Learning Rate)

<img width="800" alt="image" src="https://user-images.githubusercontent.com/40768187/183448359-3a4d03d1-387b-46ff-86dd-fd0f2a9e95b7.png">

</br>

### Feature Scaling

<img width="883" alt="image" src="https://user-images.githubusercontent.com/40768187/183449737-a9598e81-55da-4843-8ee0-73de4898cb0d.png">

</br>
- 스케일링하지 않은 입력값을 사용하는 경우, 손실함수를 최소화하는 파라미터 w 를 찾기 위해 많이 움직여야 함

</br>

1. Standardization

    <img width="509" alt="image" src="https://user-images.githubusercontent.com/40768187/183452630-ab6063dc-e171-4901-a1fe-7ee3d93e6e9e.png">

    $x_{new} = \frac{x - \mu}{\sigma}$

    </br>

2. Normalization

    $x_{new} = \frac{x-x_{min}}{x_{max}-x_{min}}$

</br>

## Optimizers 의 발달

</br>

<img width="978" alt="image" src="https://user-images.githubusercontent.com/40768187/183453433-10c5df31-f799-4d5e-817d-4a25a0ddf195.png">

</br>

### GD vs. SGD

<img width="420" alt="image" src="https://user-images.githubusercontent.com/40768187/183909896-d5659bc6-a3e6-4714-97f4-5da38823f312.png">

</br>

- GD: 전부 다 읽고나서 최적의 1스텝을 감, 최적이지만 느림
- SGD: 작은 토막마다 일단 1스텝 감, 조금 헤매더라도 인근에 빨리 도착함

</br>

### GD vs. SDG vs. Mini-batch GD

<img width="380" alt="image" src="https://user-images.githubusercontent.com/40768187/183919064-21589d0e-4885-4939-b052-14e48a5d5efc.png">

</br>

- BGD: 전체 데이터 셋에 대한 에러를 구한 뒤 기울기를 한번만 계산하여 모델의 파라미터를 업데이트함, 병렬 처리 유리
- SGD: 추출된 데이터 한 개에 대해서 error gradient 를 계산하고, GD 알고리즘을 적용하는 방법, 스텝에 걸리는 시간이 짧아 수렴속도가 상대적으로 빠름, shooting이 일어나 local optimal 에 빠질 리스크가 적음
- MBGD: 전체 데이터 셋도 아니고, 데이터 셋 중 하나도 아니고, 한번에 20개와 같은 데이터를 고려, 데이터 m 개에 대해서 각 데이터에 대한 기울기 m개를 구한뒤 평균 기울기를 통해 모델 업데이트. 많은 데이터를 요구하지 않고, 계산이 느리지 않음


- MBGD = BGD, SGD의 장점만 빼먹고 싶은 알고리즘
  - BGD 보다 local minimum에 빠질 위험이 적고, SGD 보다 병렬처리가 유리함


    <img width="504" alt="image" src="https://user-images.githubusercontent.com/40768187/183924252-db6c9659-b3f5-47f5-97b9-f2368af93de0.png">

    참고 사이트 : https://light-tree.tistory.com/133

</br>

### Gradient Descent

</br>

$w_{t+1} = w_t - \gamma \nabla \cdot L(w_t)$

</br>

<img width="323" alt="image" src="https://user-images.githubusercontent.com/40768187/184375347-ee45d88a-ebe9-4eb0-9528-f52e22425852.png">

</br>

극소점이나 안장점 근처에서는 $\nabla f(x_n)$ 크기가 작아져 보폭도 작아짐</br>
따라서, 점 $x_n|$ 최소점이 아니라 극소점 또는 안장점에 안착할 수 도 있는 문제점이 있음

</br>

### Momentum

</br>

- 경사하강법의 최적화 알고리즘의 한 종류
- 일종의 관성, 가속도처럼 생각
- 이전에 움직였던 방향(vt)도 어느정도($\rho$) 고려해서 이번에 움직이자! (-$\gamma \cdot vt + 1$)

</br>

$v_{t+1} = \rho v_t + \nabla L(w_t)$

$w_{t+1} = w_t - \gamma\cdot v_{t+1}$

</br>

<img width="333" alt="image" src="https://user-images.githubusercontent.com/40768187/184385626-1a7a66e5-b0eb-4185-9e7c-89f4d82df6f3.png">

</br>

$\gamma$ 는 학습 속도이고 $\rho$ 는 모멘트 효과에 대한 가중치</br>
$v_t$ 는 0으로 초기화되어 있고, 반복이 될 때마다 현재의 그래티언트 ($\nabla L(w_t)$)가 다음번 모멘트 $v_t+1$ 에 누적</br>
다음번 반복에서 $v_t+1$ 가 현재의 모멘트 $v_t$ 로 사용됨

</br>

<img width="256" alt="image" src="https://user-images.githubusercontent.com/40768187/184377403-e9ad492f-3ac6-4109-9ed2-8f17a194a017.png">

</br>

종종 극소점에 빠졌다가 관성의 힘으로 빠져나올 수 있음

</br>

<img width="256" alt="image" src="https://user-images.githubusercontent.com/40768187/184377403-e9ad492f-3ac6-4109-9ed2-8f17a194a017.png">

</br>

협곡에서도 진동방향은 서로 상쇄되고 진행방향은 관성을 받으며 더 효율적으로 움직임

</br>


### Nesterov Momentum

</br>

- Momentum 의 overshooting 문제 해결을 위한 알고리즘
- overshooting : 경사가 가파른 곳을 빠른 속도로 내려오다 관성을 이기지 못하고 최소 지점을 지나쳐 버리는 것
- 현재의 속도 벡터와 현재 속도로 한 걸음 미리 가본 위치($w_t + \rho v_t$)의 그래티언트 벡터를 더해 다음 위치를 정함

</br>

$v_{t+1} = \rho v_t - \nabla L(w_t + \rho v_t)$

</br>

<img width="572" alt="image" src="https://user-images.githubusercontent.com/40768187/184382979-1351fe18-5617-4d43-9421-d2413f64e7e9.png">

</br>

- Momentum은 모멘텀 값과 기울기 값이 더해져 실제 스텝 결정
- Nesterov Momentum은 모멘텀 값이 적용된 지점에서 기울기 값 계산
- Nesterov Momentum은 모멘텀으로 절반 정도 이동한 후 어떤 방식으로 이동할지 다시 계산해서 스텝을 결정하기 때문에 overshooting을 해결할 수 있음

</br>

### Adagrad

</br>

<img width="545" alt="image" src="https://user-images.githubusercontent.com/40768187/184399379-f778ddfc-ea8f-446e-bc11-857561d78d36.png">

</br>

- 기존 방식은 learning rate 가 늘 일괄적으로 적용
- 그래서 learning rate를 좀 더 가변적으로 적용하자는 아이디어
- 많이 변화한 변수는 최적해에 근접했을 거란 가정하에 작은 크기로 이동하고, 반대로 적게 변화한 변수들은 학습률을 크게하여 빠르게 오차 값을 줄이고자함

</br>

### RMSProp

</br>

<img width="534" alt="image" src="https://user-images.githubusercontent.com/40768187/184401332-01a5ae51-74ed-4660-986e-08e18454bb5b.png">

</br>

- Adagrad에서 그대로 누적되던 것들을 조금씩 decay하게 만듦
- Adagrad에서 학습이 진행됨에 따라 변화 폭이 눈에 띄게 줄어들어 결국 움직이지 않게 됨
- 이를 해결하기 위해 $G_t$ 계산식에 지수이동평균을 적용함

</br>

### Adam

`잘 모르겠으면 Adam을 써라`

</br>

<img width="537" alt="image" src="https://user-images.githubusercontent.com/40768187/184405062-992a9a6e-ced1-4c6a-8555-7a9479ede6b7.png">

</br>

- RMSProp + Momentum
- 요즘 거의 디폴트로 사용되고 있는 optimizer
- 기울기 값과 기울기의 제곱값의 지수이동평균 활용하여 step 변화량을 조절

</br>

### Overfitting vs. Underfitting

</br>

<img width="558" alt="image" src="https://user-images.githubusercontent.com/40768187/184405427-825c252d-6ef4-4efe-b6b6-673ba58d340c.png">

</br>

Underfitting - Just right - Overfitting 순

</br>

### Training, Validation, Test Sets

</br>

<img width="899" alt="image" src="https://user-images.githubusercontent.com/40768187/184405910-dbd63df1-3a14-4977-9a0a-c228eb53af97.png">

</br>

인공신경망에서는 교차검증을 많이 사용하지 않음
- 딥러닝 분야의 데이터셋은 충분히 큼
- 교차검증을 수행하기에는 학습시간이 너무 오래 걸림

</br>

### Dropout (과적합 방지)

</br>

<img width="594" alt="image" src="https://user-images.githubusercontent.com/40768187/184654757-35e44b60-d434-44ec-8a72-c1d618c6b23e.png">

</br>

- 모델의 학습시에만 적용
- 모델의 다양성을 만들기 위한 방법으로 이해 (앙상블과 유사)
- 서로 연결된 연결망에서 랜덤하게 노드를 Drop 함
- training data 에서 학습이 덜 될 수 있겠지만 일반화 능력을 키워 Test Data 에 대한 예측률을 높이는 방법

</br>

### Regularization (규제)

</br>

<img width="708" alt="image" src="https://user-images.githubusercontent.com/40768187/184655528-2a38ffec-6cff-41c0-8b2d-5a1fb008a66b.png">

</br>


- Overfitting 을 해결하는 대표적인 방법
- 고차 부분에 높은 Penalty 를 주면, 그 부분의 학습은 커지지 않음

</br>

<img width="472" alt="image" src="https://user-images.githubusercontent.com/40768187/184656377-667e63b1-d4f5-4bec-a6db-c81dd6a24e05.png">

</br>

- Ridge Regression - L2 normalization
- 베타3 과 베타4 가 최소의 error를 가지려면 거의 0의 값을 가져야 하므로 영향력을 감소시킬 수 있음

</br>

## Weight Initialization (가중치 초기화)

</br>

- Weight 와 Bias 를 어떻게 설정하느냐 하는 문제
- 활성화 함수의 출력 데이터를 활성화값이라고 함
- 레어어가 너무 깊으면 양쪽으로 벌어지거나 한쪽으로 치우쳐짐

</br>

<img width="728" alt="image" src="https://user-images.githubusercontent.com/40768187/184658520-e36faabf-bfad-423b-ba07-a4d7597c731f.png">

</br>

- 가중치를 평균이 0, 표준편차가 1인 정규분포로 초기화할 때의 각 층의 활성화 값 분포 (bias 는 전부 0) - Sigmoid 사용
- Sigmoid 는 출력값이 0, 1 에 가까워지면 미분값이 0이 됨
- 데이터가 0과 1에 치우치면 backpropagation 때 gradient가 점점 작아지다가 아예 사라지게 됨 (미분하니깐!) => Gradient Vanishing

</br>

<img width="361" alt="image" src="https://user-images.githubusercontent.com/40768187/184659112-3eed91a8-a712-4800-b97e-7b005e1cf002.png">

</br>

- 가중치를 평균이 0, 표준편차가 0.01 인 정규분포로 초기화할 때의 각 층의 활성화 값 분포
- 활성화 값이 한쪽으로 치우쳐짐
- 뉴런이 거의 같은 값을 가지고 있음 -> 뉴런이 여러 개 둔 의미가 없음
- 표현력을 제한하게 됨

</br>

### Xaiver Glorot 초기화

<img width="385" alt="image" src="https://user-images.githubusercontent.com/40768187/184665046-11fba6c4-4349-4647-adb8-c275b905338a.png">

</br>

- 고정된 표준편차를 사용하지 않고, Layer들의 입력/출력 노드 개수에 따라 동적으로 파라미터 값을 초기화
- 활성화 함수가 tanh, Sigmoid일 때 사용
- 이전 layer의 neuron의 개수가 n이라면 표준편차가 $1 \over \sqrt n$ 인 분포 사용

</br>

<img width="441" alt="image" src="https://user-images.githubusercontent.com/40768187/184664928-6481b814-2f36-484e-9f04-dfef1230bb1e.png">

</br>

- Normal 한 방법, Uniform 한 방법 2개가 존재
- keras 모듈에서는 디폴트로 제공하는 가중치 초기화 방법은 Xaiver Uniform

</br>

### He 초기화

</br>

<img width="342" alt="image" src="https://user-images.githubusercontent.com/40768187/184667566-57c9a191-4f60-4ff3-a971-57c8b7c7c882.png">

</br>

- ReLU 활성함수에 보다 최적화된 파라미터 초기화 방법
- Normal, Uniform 방법 2가지 존재

</br>

<img width="425" alt="image" src="https://user-images.githubusercontent.com/40768187/184667492-af08d19e-8645-42cc-ac34-8f33c7c60116.png">

</br>

- 입력 노드의 개수에만 의존하는 형태
- He Initialization는 앞 layer의 neuron이 n개일 때, 표준편차가 $2 \over \sqrt n$ 인 정규분포를 사용
- ReLU 는 음의 영역이 0 이라서 활성화되는 영역을 더 넓히기 위해 2배의 계수가 필요하다고 해석하면 됨

</br>

### 배치 정규화

</br>

<img width="729" alt="image" src="https://user-images.githubusercontent.com/40768187/184669397-cdd5b0ac-8401-4052-ab09-461d3b66499d.png">

</br>

- 가중치의 초깃값에 상관없이 활성화값을 강제로 분포시킴
- Affine Layer 를 통과한 미니배치 단위 Output을 표준정규분포로 정규화하는 작업
- 학습할 때마다 활성화값, 출력값 정규화
- 일종의 노이즈를 추가하는 방법으로 (bias와 유사) 이는 배치마다 정규화를 함으로써 전체 데이터에 대한 평균의 분산과 값이 달라질 수 있음

</br>

### 데이터 증강 (Data Augmentation)

</br>

<img width="481" alt="image" src="https://user-images.githubusercontent.com/40768187/184669698-e00734f2-5c74-4425-8c8e-6d52eccf55e7.png">

</br>

- 충분한 양의 데이터가 없을 경우, 과적합 생김
- 기존의 데이터를 변형하거나(축소, 확대, 자르기 등) 또는 생성모델을 이용해서 생성함
- 이미지를 변형해서 미리 데이터셋에 추가할 수도 있지만, 학습 과정에서 모델에 입력하기 전에 실시간으로 증강해서 사용

</br>

### Early Stopping

</br>

<img width="502" alt="image" src="https://user-images.githubusercontent.com/40768187/184670395-333058a3-23b9-43cc-8787-65eb3d8abe95.png">

</br>

- 과적합 방지
- 이전 epoch 때와 비교해서 오차가 증가했다면 학습을 중단

    ```python
    from keras.callbacks import EarlyStopping
    early_stopping = EarlyStopping()
    model.fit(X_train, Y_train, epoch = 1000, callbacks = [early_stopping])
    ```

- ```EarlyStopping(monitor = 'val_loss', min_delta = 0, patience = 0, mode = 'auto')```
- ```patience``` : 개선을 위해 몇번의 에포크를 기다릴지 설정

</br>

### Hyperparameter 탐색

</br>

<img width="729" alt="image" src="https://user-images.githubusercontent.com/40768187/184672112-6ff41aef-edba-4eb2-9935-04aad38220db.png">

</br>

- 하이퍼 파라미터는 중요도 차이가 큼
- 따라서 격자보다는 무작위로 선택하는 것이 나음
- 성능이 가장 좋은 조합 주위의 영역을 줌인해서 다시 선택

참고: https://hellominji.tistory.com/31