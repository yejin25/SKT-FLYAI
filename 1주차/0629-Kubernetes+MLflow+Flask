# 1주차 2022 06 29
</br>

## 📌 Deployment

### Deployment?
- Pod와 Replicaset에 대한 관리를 제공하는 단위
- 관리라는 의미는 Self-healing, Scaling, Rollout과 같은 기능 포함 (Self-healing -> 저번에 말했던 도커 kill)
- Pod을 Deployment로 배포함으로써 여러 개로 복제된 Pod, 여러 버전의 Pod을 안전하게 관리할 수 있음</br>
  = Pod 단위로는 다른 컴퓨터에 분산 시키기 가능

    <img width="396" alt="image" src="https://user-images.githubusercontent.com/40768187/176706324-a0b00b7c-5363-4e4a-be15-d6ed7aa62b72.png">
</br>

### Deployment 생성
```vi deployment.yaml``` 을 사용하여 Deployment 생성 파일 작성
```yaml
apiVersion: apps/v1 # kubernetes resource 의 API Version
kind: Deployment # kubernetes resource name
metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함
  name: nginx-deployment
  labels:
    app: nginx
spec: # 메인 파트 : resource 의 desired state 를 명시
  replicas: 3 # 동일한 template 의 pod 을 3 개 복제본으로 생성합니다.
  selector:
    matchLabels:
      app: nginx
  template: # Pod 의 template 을 의미합니다.
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx # container 의 이름
        image: nginx:1.14.2 # container 의 image
        ports:
        - containerPort: 80 # container 의 내부 Port
```
작성한 파일 실행
```
kubectl apply -f deployment.yaml
```

### Deployment 조회
생성한 Deployment의 상태 확인
```
kubectl get deployment
# 다음과 같은 메시지가 출력됩니다.
# NAME               READY   UP-TO-DATE   AVAILABLE   AGE
# nginx-deployment   0/3     3            0           10s

kubectl get deployment,pod # pod의 상태도 볼 수 있음
```
시간이 지나면 ```READY 3/3``` 으로 바뀐 것을 볼 수 있음

```
kubectl describe pod <pod-name>

# pod의 정보를 자세히 조회하면 'Controlled By'로부터 Deployment에 의해 생성되고 관리되는 것을 확인할 수 있음
```

### Deployment Auto-healing
pod 하나 삭제
```
kubectl delete pod <pod-name>

kubectl get pod # pod가 삭제되고 새로 하나 생성된 것을 확인 할 수 있음 (삭제한 pod와는 이름이 다름)
```

### Deployment Scaling
replica 개수 늘리기
```
kubectl scale deployment/nginx-deployment --replicas=5

kubectl get deployment

kubectl get pod
```

replica 개수 줄이기
```
kubectl scale deployment/nginx-deployment --replicas=1

kubectl get deployment

kubectl get pod
```

### Deployment 삭제
deployment 삭제
```
kubectl delete deployment <deployment-name>

kubectl get deployment

kubectl get pod
```
Deployment의 control을 받던 pod도 모두 삭제된 것을 확인

+) ```-f``` 옵션으로 YAML 파일을 사용해 삭제 가능
```
kubectl delete -f <YAML-파일-경로>
```
</br>

## 📌 Service

### Service?
- 쿠버네티스에 배포한 애플리케이션(Pod)을 외부에서 접근하기 쉽게 추상화한 리소스
- Pod는 IP를 할당받고 생성되지만, 언제든지 죽었다가 살아날 수 있고, 이 과정에서 IP는 항상 재할당 받기에 고정된 IP로 원하는 Pod에 접근할 수는 없음
- 따라서 클러스터 외부 혹은 내부에서 Pod에 접근할 때 Service를 통해서 접근하는 것
- Service는 고정된 IP를 가지며, Service는 하나 혹은 여러 개의 Pod와 매칭

    <img width="397" alt="image" src="https://user-images.githubusercontent.com/40768187/176707325-9f9a14fb-b36e-46c4-a3d8-2b615298d7f7.png">

</br>

### Service 생성
deployment 생성하기, **위에 Deployment 생성 챕터 확인**
</br>
</br>

생성된 Pod의 IP를 확인하고 접속 시도
```
kubectl get pod -o wide
# Pod 의 IP 를 확인합니다.

curl -X GET <POD-IP> -vvv
ping <POD-IP>
# 통신 불가능
```
할당된 ```<POD-IP>```는 클러스터 내부에서만 접근할 수 있는 IP. 따라서 외부에서는 Pod에 접속할 수 없음
</br>
</br>

minikube 내부로 접속하면 통신되는지 확인
```
minikube ssh
# minikube 내부로 접속합니다.

curl -X GET <POD-IP> -vvv
ping <POD-IP>
# 통신 가능
```
</br>
</br>
위에서 생성한 Deployment를 매칭시킨 Service 생성

```vi service.yaml```을 사용하여 Service 생성 파일을 작성하고 실행
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  type: NodePort # Service 의 Type 을 명시하는 부분입니다. 자세한 설명은 추후 말씀드리겠습니다.
  ports:
  - port: 80
    protocol: TCP
  selector: # 아래 label 을 가진 Pod 을 매핑하는 부분입니다.
    app: nginx 
```
```
vi service.yaml
# 파일을 열어 위의 내용을 복사 붙여넣기 합니다.

kubectl apply -f service.yaml

kubectl get service
# PORT 80:<PORT> 숫자 확인

curl -X GET $(minikube ip):<PORT>
# 이렇게 서비스를 통해서 클러스터 외부에서도 정상적으로 pod 에 접속할 수 있는 것을 확인합니다.
```
<img width="376" alt="image" src="https://user-images.githubusercontent.com/40768187/176714794-81a16c2f-a6b9-48b0-912d-a0fb92fb889a.png">
</br>
Pod에 접속하는 구조에 대해 좀 더 이해하기 위해 이미지를 첨부했다.

</br>

```
해당 실습에서는 NodePort의 포트번호가 31370 이었다.

출처: https://blog.naver.com/PostView.naver?blogId=love_tolty&logNo=222499841070&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
```

#### Service의 Type?
- NodePort라는 type을 사용하기 때문에, minikube라는 kubernetes cluster 내부에 배포된 서비스에 클러스터 외부에서 접근할 수 있었음
- 접근하는 IP는 pod가 떠있는 노드의 IP를 사용하고, Port는 할당받은 Port를 사용
- NodePort는 Pod가 어떤 Node에 스케줄링될 지 모르는 상황에서, Pod이 할당된 후 해당 Node의 IP를 알아야 한다는 단점 존재
- 실무에서는 Kubernetes cluster에 MetalLB와 같은 LB 역할을 하는 모듈을 설치한 후, LoadBalancer type으로 서비스를 expose하는 방식 사용
  
  +) NodePort를 통해 들어온 트래픽의 경우 클러스트 내부에서 2개의 복제 Pod를 대상으로 L-B 되어 처리됨
    ```
    참고: https://blog.naver.com/PostView.naver?blogId=love_tolty&logNo=222499841070&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
    ```
</br>

## 📌 DVC

### DVC?
- git은 100MB 한계. 데이터셋을 올릴 수 없음. 그래서 DVC 사용!
- 파일은 DVC를 통해 스토리지에 올리고, git으로는 버전 관리 (파일을 추적할 수 있는 정보 저장)

### DVC 설치
python 설치
- python 3.8 이상의 환경 준비
  ```
  sudo apt-get install python3.8
    sudo apt-get update
    sudo apt-get upgrade

    ls -al /usr/bin/python

    ls /usr/bin/ | grep python

    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3
    update-alternatives --config python
  ```

설치 확인
```
python -V # Python 3.9.6
```

+) 추가 설정 (안해도 됨)
python3의 별칭을 python으로 바꿈
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3

update-alternatives --config python
```
이제 ```python``` 이라고만 쳐도 python 실행

git 설치
```
sudo apt install git

git --version
# git version 2.25.1

git --help
# 정상 설치되었는지 확인
```

DVC 설치
- dvc 2.6.4 버전 다운
- ```dvc[all]```에서 ```[all]```은 dvc의 remote storage로, s3, gs, azure, oss, ssh 모두 사용할 수 있도록 관련 패키지 설치
```
pip install dvc[all]==2.6.4 # python의 외부라이브러리 다운로드 명령어

dvc --version
# 2.6.4

dvc --help
# 정상 설치되었는지 확인
```
pip 명령어를 찾을 수 없다고 오류 발생시, ```sudo apt install python3-pip``` 로 설치를 해주면 됨

</br>

### DVC 저장소 세팅
새 Directory 생성 후 이동
```
mkdir dvc-tutorial

cd dvc-tutorial
```

해당 Directory 를 git 저장소로 초기화
```
git init
```

해당 Directory를 dvc 저장소로 초기화
```
dvc init

#에러가 날 경우 
sudo python -m pip install --upgrade --force pip

sudo wget \
       https://dvc.org/deb/dvc.list \
       -O /etc/apt/sources.list.d/dvc.list
wget -qO - https://dvc.org/deb/iterative.asc | sudo apt-key add -
sudo apt update
sudo apt install dvc
```

![Untitled (1)](https://user-images.githubusercontent.com/40768187/176720853-91a2f00e-8857-476f-ab2b-c63760561eeb.png)
</br>
다음과 같이 나오면 성공 🎉

</br>

### DVC 기본 명령어 - PUSH
1) dvc로 버전 tracking할 data 생성
   ```
   # data 를 저장할 용도로 data 라는 이름의 디렉토리를 생성하고 이동합니다.
    mkdir data

    cd data

    # 가볍게 변경할 수 있는 데이터를 카피해오거나, 새로 만듭니다.
    vi demo.txt

    cat demo.txt
    # Hello AI!
   ```

2) 방금 생성한 데이터를 dvc로 traking
   ```
    cd ..

    dvc add data/demo.txt

    # To track the changes with git, run:
    git add data/demo.txt.dvc data/.gitignore
   ```

3) dvc add에 의해 자동 생성된 파일들을 확인
   ```
    cd data
    ls
    # demo.txt.dvc 파일이 자동 생성된 것을 확인

    cat demo.txt.dvc
    # demo.txt 파일의 메타정보를 가진 파일입니다.
    # git 에서는 demo.txt 파일이 아닌, demo.txt.dvc 파일만 관리하게 됩니다.
   ```

4) git commit
   ```
   git commit -m "Add demo.txt.dvc" # .dvc 파일은 git push 를 수행하여, git repository에 저장
   ```

5) data가 실제로 저장될 remote sotrage 세팅
   - 본인의 구글 드라이브에 새로운 폴더를 하나 생성해주고, url의 마지막 부분을 복사</br>
    <img width="596" alt="스크린샷 2022-07-01 오전 12 55 28" src="https://user-images.githubusercontent.com/40768187/176723351-3f262c76-ecd9-49ff-86bd-d170fd557425.png">
    </br>

        ```
        dvc remote add -d storage gdrive://<GOOGLE_DRIVE_FOLDER_ID>

        # dvc 의 default remote storage 로 gdrive://<GOOGLE_DRIVE_FOLDER_ID> 를 세팅합니다.
        ```

6) dvc config를 git commit
   ```
   git add .dvc/config

   git commit -m "add remote storage"
   ```

7) dvc push
    ```
    dvc push

    #Go to the following link in your browser:
    #
    #    https://accounts.google.com/o/oauth2/.........
    #
    # Enter verification code:
    ```
    - dvc push 수행은 인증 과정이 필요함. 실행 후 출력되는 주소로 이동하여 인증 수행
    - 인증 완료 ! </br>
        ![Untitled (2)](https://user-images.githubusercontent.com/40768187/176724288-241305f9-3416-432c-b184-c18b4d46c9a4.png)

    - 이후 구글 드라이브로 이동해보면 새로운 폴더가 생성되어 있고, 해당 폴더 안에는 업로드한 파일이 있는 것을 확인 할 수 있음

</br>

### DVC 기본 명령어 - PULL, CHECKOUT

1) dvc pull
   ```
   cd dvc-tutorial

    # dvc 캐시를 삭제합니다.
    rm -rf .dvc/cache/
    # dvc push 했던 데이터를 삭제합니다.
    rm -rf data/demo.txt

    # dvc pull 로 google drive 에 업로드했던 데이터를 다운받습니다.
    dvc pull

    # 방금 다시 다운받은 데이터가 이전 데이터와 동일한지 확인합니다.
    cat data/demo.txt
   ```

2) dvc checkout
   - data의 버전을 변경하는 명령어
   - 실습을 위해 새로운 버전의 data를 push
        ```
        # 데이터를 변경합니다. (새로운 데이터를 같은 이름으로 copy 해와도 좋습니다.)
        vi data/demo.txt

        # 변경되었는지 확인합니다.
        cat data/demo.txt

        # dvc add (data/demo.txt.dvc 를 변경시켜주는 역할)
        dvc add data/demo.txt

        # git add and commit
        git add data/demo.txt.dvc
        git commit -m "update demo.txt"

        # dvc push (and git push)
        dvc push # 새로운 버전의 data 파일을 remote storage 에 업로드

        (git push) # .dvc 파일을 git repository 에 업로드
        ```
    - 이전 버전의 data로 되돌아가기
        ```
        # git log 를 확인합니다.
        git log --oneline

        # demo.txt.dvc 파일을 이전 commit 버전으로 되돌립니다.
        git checkout <COMMIT_HASH> data/demo.txt.dvc

        # dvc checkout 합니다. (demo.txt.dvc 의 내용을 보고 demo.txt 파일을 이전 버전으로 변경합니다.)
        dvc checkout

        # 데이터가 변경되었는지 확인합니다.
        cat data/demo.txt
        ```

    이외 추가적인 기능은 notion 에서 확인하기!

</br>

## 📌 MLflow

MLflow 이전의 작업
 - 비슷한 작업이 반복적으로 발생
 - Dependency 패키지들이 많고, 버전관리가 어려움
 - 사람 Dependency 생김
 - 테스트 어려움
 - 재생산되지 않는 경우가 많음
 - Model 학습용 코드를 구현하는 사람과 Serving용 코드를 구현하는 사람이 분리되어 있음

### MLflow?

머신러닝 모델을 추적하고, 모델을 공유 및 배포를 쉽게 할 수 있도록 지원하는 오픈 소스

![Untitled](https://user-images.githubusercontent.com/40768187/176798565-9e9fcdd9-a6b1-47d2-9817-b3b66e13fc24.png)
</br>
+) MLflow 외에도 Tensorboard, Neptune, Wights & Biases, Comet.ml 등이 있음

</br>

### MLflow 설치
- Ubuntu 20.04 사용
- python 가상 환경
  - conda : mlflow models serve 할 때 필요
  - 3.8.5 사용
  - pip3

```
# 새로운 디렉토리를 하나 생성한 뒤, 이동해주세요
mkdir mlflow-tutorial
cd mlflow-tutorial

# conda 가상환경 세팅
# python 버전 확인
python -V

pip install mlflow==1.20.2

mlflow --version
# mlflow, version 1.20.2
```
실습 중 설치 오류 발생 -> protobuf 버전을 3.20.0 으로 버전업
```
pip uninstall mlflow    # 1

python-updates  # 3

pip intstall protobuf==3.20.0   # 4

pip install mlflow==1.20.2      # 2
```
실습에선 주석과 같은 순서로 명령어를 실행했음. 그래도 정상적으로 설치 완료되긴 했음.

</br>

### MLflow tracking server 띄워보기
```
mlflow ui --help
# mlflow tracking server 를 띄웁니다.
# UI (dashboard) 의 default url 은 http://localhost:5000 입니다.
# 5000 포트가 열려있는지 확인해주세요.
# production 용으로는 mlflow ui 대신 mlflow server 를 사용하라는 안내가 출력됩니다.

mlflow server --help
# mlflow server 는 worker 를 여러 개 띄울 수 있고, prometheus 가 metrics 을 가져갈 수 있도록 엔드포인트를 제공하는 등의 추가적인 기능이 존재합니다.
```
로컬에서 띄우고, 사용자가 한 명이기에 더 가벼운 ```mlflow ui```로 MLflow tracking server 띄울 예정
```
mlflow ui
```
노트북에서 5000 번 포트가 사용 중이 아니라면, 다음과 같이 출력되고 ```http://127.0.0.1:5000``` 으로 접속하면 됨
![Untitled (1)](https://user-images.githubusercontent.com/40768187/176801877-d082f5ca-c2f5-4667-9251-552eb0120f86.png)
</br>

+) 실습을 Azure에서 진행했기 때문에 명령어를 조금 다르게 작성하고, 보안 규칙을 변경해주고, localhost 가 아닌 가상머신의 public IP로 접속해야 했음
```
mlflow ui -h 0.0.0.0 -p 5000 # publicIP:5000 으로 접속
```
![11](https://user-images.githubusercontent.com/40768187/176802510-d4827c73-64a7-4dc8-a1a8-34843afcac94.png)
</br>
접속 완료 !

![Untitled (2)](https://user-images.githubusercontent.com/40768187/176802221-5191f74d-23b2-489c-b0a6-2c63419585b6.png)

 다른 터미널을 열어서, ```mlflow-tutorial```로 이동해보면, mlruns 라는 디렉토리가 생성되어 있음
 - ```mlflow ui``` 실행시 ```--backend-store-uri```, ```--default-artifact-root``` 옵션을 주지 않은 경우, ```mlflow ui```를 실행한 디렉토리에 ```mlruns```라는 디렉토리를 생성한 뒤 이 곳에 실험 관련 데이터를 저장하게 됨

    ```
    cd mlflow-tutorial

    ls
    cd mlruns
    cat 0/meta.yaml
    # 무언가 채워진 것을 확인할 수 있습니다.
    ```

</br>

### MLflow 사용해보기

Example code 다운
```
# VM 혹은 linux 사용자
wget https://raw.githubusercontent.com/mlflow/mlflow/master/examples/sklearn_elasticnet_diabetes/linux/train_diabetes.py

# Mac 사용자
wget https://raw.githubusercontent.com/mlflow/mlflow/master/examples/sklearn_elasticnet_diabetes/osx/train_diabetes.py
```

- mlflow에서 example로 제공해주는 다양한 example 중 하나인 ```train_diabetes.py```
  - scikit-learn 패키지에서 제공하는 당뇨병 진행도 예측용 데이터
  - ElasticNet 모델을 학습하여, predict 한 뒤 그 evaluation metric을 MLflow에 기록하는 예제
  - 442 명의 당뇨병 환자를 대상으로, 나이, 성별, bmi 등의 10개의 독립변수(X)를 가지고 1년 뒤 당뇨병의 진행률(y)를 예측하는 문제

Example code 실행
```
# mlflow ui 를 수행한 디렉토리와 같은 디렉토리로 이동
cd mlflow-tutorial

# example 코드를 실행 후 mlflow 에 기록되는 것 확인
python train_diabetes.py
```
실행 오류가 난다면 ```pip install sklearn```으로 관련 패키지 설치 후 재실행 해보기


![Untitled (3)](https://user-images.githubusercontent.com/40768187/176823819-66ea4e21-5ad3-4754-bb3e-089acfc5b3fe.png)
</br>
model 관련 meta 정보와 더불어 pkl 파일이 저장된 것을 확인

다양한 parameter로 테스트한 후에 mlflow 확인
```
python train_diabetes.py  0.01 0.01
python train_diabetes.py  0.01 0.75
python train_diabetes.py  0.01 1.0
python train_diabetes.py  0.05 1.0
python train_diabetes.py  0.05 0.01
python train_diabetes.py  0.5 0.8
python train_diabetes.py  0.8 1.0
```

![Untitled (4)](https://user-images.githubusercontent.com/40768187/176824017-d23fe0b5-7440-4985-b5c9-c421f3612d35.png)
</br>
위와 같은 화면이 나오고, metrics와 parameter를 한 눈에 비교 가능

</br>

### MLflow 데이터 저장 방식
```
cd mlruns/0
ls
# 굉장히 많은 디렉토리가 생성되었습니다.
# (각각의 알 수 없는 폴더명은 mlflow 의 run-id 를 의미합니다.)

# 아무 디렉토리에나 들어가보겠습니다.
cd <특정 디렉토리>
ls

# artifacs, metrics, params, tag 와 같은 디렉토리가 있고 그 안에 실제 mlflow run 의 메타 정보가 저장된 것을 확인할 수 있습니다.
```

</br>

## 📌 Flask

### Flask?
The python micro framework for building web applications
- MSA를 위한 web app framework
- Django 등 다른 framework에 비해 굉장히 가볍고, 확장성, 유연성이 뛰어남
- 사용하기 쉽고, 간단한 기능을 가볍게 구현하기에 적합하기 때문에 대부분 ML Model의 첫배포로 Flask 이용

<br>

### Flask 설치
- python (3.6 이상), pip3 설치

flask 설치 진행
  ```
  # 새로운 디렉토리를 하나 생성한 뒤, 이동해주세요
    mkdir flask-tutorial
    cd flask-tutorial

    # python 버전 확인
    python -V

    # Flask 설치
    pip install -U Flask==2.0.2

    # Flask Version 확인
    flask --version

    # Python 3.8.9
    # Flask 2.0.2
    # Werkzeug 2.0.2
  ```

<br>

### Hello world! with Flask
- Web Server 띄우기
- ```app.py``` 파일 생성 아래 코드 복붙
  ```
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    if __name__ == "__main__":      # 생성자, 실행할 때 나오는 코드
        app.run(debug=True, host='0.0.0.0', port=5000)
    # debug 모드로 실행, 모든 IP 에서 접근 허용, 5000 포트로 사용하는 것을 의미
  ```

- 동일한 폴더에서 ```python app.py```를 수행하여 application server를 로컬에 띄움
- ```127.0.0.1:5000```으로 접속하면, ```Hello, World!```라는 문자가 브라우저에 보이는 것을 확인 가능
  
+) 앞서 말했듯이 실습을 Azure에서 진행했음. 이에 따라 MLflow 챕터에서 보안 규칙도 추가해주었기 때문에 본인은 ```publicIP:5000``` 으로 접속함

<br>

### Routing
- flask의 ```route()``` 데코레이터는 python 함수를 web server의 URL에 mapping 시킬 수 있음
- ```app.py``` 아래와 같이 수정
  ```
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/helloai")
    def hello_AI():
        return "<p>Hello, AI!</p>"

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=5000)
  ```

```python app.py``` 수행 후 이전과 같이 브라우저에 접속해 보면 ```Hello, World!``` 뿐만 아니라 ```Hello, AI!``` 라는 문자도 출력되어 있음

+) **HTTP 응답 확인해보기**
```
  curl -X GET 127.0.0.1:5000
  curl -X GET 127.0.0.1:5000/helloai
```

<br>

### POST method
- falsk는 HTTP Method 도 지정 가능
- 이를 활용하여 API 개발 가능
- ```app.py``` 수정

```
from flask import Flask
import json

app = Flask(__name__)

@app.route("/predict", methods=["POST", "PUT"])
def inference():
    return json.dumps({'hello': 'world'}), 200 # http status code 를 200 으로 반환하는 것을 의미합니다.

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
```
```python app.py``` 수행 후 HTTP 응답 확인
```
curl -X POST http://127.0.0.1:5000/predict
# {"hello": "world"}

curl -X PUT http://127.0.0.1:5000/predict
# {"hello": "world"}

curl -X GET http://127.0.0.1:5000/predict
# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
# <title>405 Method Not Allowed</title>
# <h1>Method Not Allowed</h1>
# <p>The method is not allowed for the requested URL.</p>
```
- POST, PUT 만 허용했으므로 GET에 대한 응답은 405 에러가 발생

</br>
+) 실습 목적은 머신러닝 모델을 API 서비스로 제공할 때, Flask 사용하는 방법을 알아 보는 것임