# 1주차 2022 06 27
</br>

## 📌 Deep Learning ⊂ ML ⊂ AI

### ML?
```
A computer program is said to learn from experience E with respect
to task T and performance measure P, if it’s performance at
tasks in T, as measured by P, improves with experience E.

-Tom Mitchell
```

- ML 유형
  
  - Supervised Learning (정답을 알고 예측)
  - Unsupervised Learning (정답을 모르고 예측)
  - Reinforcement Learning

![The-main-types-of-machine-learning-Main-approaches-include-classification-and](https://user-images.githubusercontent.com/40768187/175952246-bd77df04-2fa3-44ef-b5c3-ddba7235d0a7.png)
출처: https://www.researchgate.net/figure/The-main-types-of-machine-learning-Main-approaches-include-classification-and_fig1_354960266

___
</br>

## 📌 MLOps
~~정형화된 틀이 없는 춘추전국시대 여기선 이 툴 쓰고 저기선 이 툴 쓰고~~

= 머신러닝 엔지니어링 + 데이터 엔지니어링 + 인프라 + Ops

<img width="2100" alt="image" src="https://user-images.githubusercontent.com/40768187/175956667-dc5c8751-620c-4760-ac57-a217993ef865.png">

</br>
</br>

```
머신러닝 모델 개발과 머신러닝 모델 운영에서 사용되는 문제, 반복을 최소화하고 비즈니스 가치를 창출하는 것이
목표 모델링에 집중할 수 있도록 관련된 인프라를 만들고, 자동으로 운영되도록 만드는 일
```

ex) API 형태로 서버 만들기, 실험 파라미터와 결과 저장하기, 모델 결과 자동화하기, 데이터 Validation

</br>

### MLOps 구성요소
<img width="1495" alt="image" src="https://user-images.githubusercontent.com/40768187/175957106-39500b5f-0df8-4100-902c-566700206005.png">

각 요소들은 파이프 라인으로 연결되어 있음

**~~ML 코드 부분은 정말 전체 중에서 작은 부분 중 하나일 뿐~~**
___
</br>

## Research ML VS Production ML
|           | Research ML                                      | Production ML                               |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| 데이터    | 고정(static)                                     | 계속 변함(Dynamic-Shifting)                 |
| 중요 요소 | 모델 성능(Accuracy, RMSE)                        | 모델 성능, 빠른 Inference 속도, 해석 가능함 |
| 도전 과제 | 더 좋은 성능을 내는 모델, 새로운 구조의 모델     | 안정적인 운영, 전체 시스템 구조             |
| 학습      | 데이터가 고정이라 모델구조, 파라미터 기반 재학습 | 시간의 흐름에 따라 데이터가 변경되어 재학습 |
| 목적      | 논문 출판                                        | 서비스에서 문제 해결                        |
| 표현      | Offline                                          | Online                                      |

~~연구용은 성능 좋은 모델만들면 끝~~

___
</br>

## 📌 Docker

Docker는 가상머신 위에 Ubuntu 20.04LTS 버전을 올려 설치 진행하였습니다.

항상 처음엔 패키지 매니저 업데이트, 업그레이드 필수
```
sudo apt-get -y update && sudo apt-get -y upgrade
```

설치 방법: https://docs.docker.com/engine/install/ubuntu/
</br>
</br>
### Install using the repository
Docker Engine을 설치하기 전에 Docker repository 설정이 필요함</br>
그래야 Docker를 repo로부터 설치 및 업데이트가 가능함

#### Set up the repository
- docker의 prerequisite package 설치
   ```
   sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
   ```

- GPG key 추가</br>참조: https://librewiki.net/wiki/시리즈:암호의_암도_몰라도_쉽게_하는_GPG
  ```
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  ```

- stable 버전의 repository 바라보도록 설정
  ```
  echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```
  +) arm 기반 cpu
    ```
    echo \
    "deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

#### Install Docker Engine
- Docker Engine, containerd 최신 버전 설치
  ```
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```
     리눅스에서 마지막에 -d 가 붙은 것은 "demon" (서비스) 를 뜻한다

    +) 특정 버전 설치 방법
    ```
    apt-cache madison docker-ce
    ```
    <img width="887" alt="image" src="https://user-images.githubusercontent.com/40768187/175963213-3be84cbf-b38c-456d-8146-909d0d2e9b8d.png">

    명령어 실행 후 위와 같이 목록이 나온다.</br>여기서 **5:20.10.16~3-0~ubuntu-jammy** 가 <VERSION_STRING> 이다
    ```
    sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
    ```

#### Verifying Normal Installation
- Docker image 를 실행시켜 설치 확인
    ```
    sudo docker run hello-world
    ```

    ![image](https://user-images.githubusercontent.com/40768187/175965494-1d467855-9906-42cd-8ce4-6d3255f00861.png)
    위와 같은 문장이 나오면 정상 설치 🎉🎉


### Docker 권한 설정
docker 관련 작업은 root 에게만 권한이 있음 그래서 ```sudo```를 명령어 앞에 붙여야 함</br>
근데 ```sudo``` 계속 붙이기 귀찮으니 권한 다시 설정

```
sudo usermod -a -G docker $USER //$USER (<- 유저이름)을 docker (보조)그룹에 추가, -a 옵션은 -G 옵션하고만 같이 쓰임
sudo service docker restart //docker 재실행
```

아래 명령어 작성 후 권한이 거부된다면 재부팅하고 다시 확인해보기</br>
~~기계는 역시 재부팅이 제 맛~~
```
docker ps   //현재 가동중인 컨테이너 리스트 출력
```
이렇게 나오면 권한 설정 완료 🎉🎉🎉
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
