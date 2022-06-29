# 1주차 2022 06 28
</br>

## 📌 Docker 기본 명령어

### 1) Docker pull
- doker image repository 부터 Docker image 를 가져옴
    ```
    docker pull <image name>
    ```
    +) 참고: private한 repository 에서 image를 가져오는 경우 -> docker login을 통해 특정 repository 바라보도록 하고, pull 수행

### 2) Docker images
- 로컬에 존재하는 image 리스트 출력
  ```
  docker images
  ```

### 3) Docker ps
- 현재 실행 중인 컨테이너 리스트 출력
  ```
  docker ps
  docker ps -a
  ```

### 4) Docker run
- 도커 컨테이너 실행 (예시 중 하나)
  ```
  docker run -it --name <name> <image name> /bin/bash
  ```
  ```-it``` 표준 입력(stdin) 활성화, TTY 모드 사용 - bash 사용 시 필수 -> 쉘이나 CLI 도구로 사용할 때 유용 </br>
  ```/bin/bash``` 컨테이너를 실행시킴과 동시에 실행할 명령어, bash 터미널을 사용하는 것을 의미

  +) run 했을 때 이미지가 local에 없다면 외부 registry에서 다운로드
  
  ~~누군가가 이미 이미지를 만들어 놓았을 것이다. 이미지 만든다고 삽질하지 말자~~

  **컨테이너 실행 후 exit로 작업을 종료했을 때**
  - 이미지를 실행한 후의 작업을 통한 변경사항은 컨테이너의 내용이 변경되는 것이지, 이미지는 변경되지 않음
  - 따라서 컨테이너 종료시 변경사항은 모두 ㅂ2~
  - ctrl + p (or q) 를 통해 컨테이너를 종료시키지 않고 빠져나올 수 있음

### 5) Docker exec
- 컨테이너 내부에서 명령을 내리거나, 내부로 접속하는 명령어
  ```
  docker run -it -d --name <name> <image name>
  docker ps
  ```
  ```-d``` 컨테이너를 백그라운드에서 실행하는 명령어
  ```
  docker exec -it <name> /bin/bash
  ```

### 6) Docker logs
- 컨테이너의 log 확인
  ```
  docker run --name <name> -d <image name = busybox> sh -c "while true; do $(echo date); sleep 1; done"
  ```

  ```<name>``` 이라는 busybox 이미지를 백그라운드에서 컨테이너로 실행하여 1초에 한 번씩 현재 시간 출력

  ```
  docker logs <name>
  docker logs <name> -f
  ```
  ```-f``` : 계속해서 log 출력

### 7) Docker stop
- 실행 중인 도커 컨테이너 중단
  ```
  docker stop <name>
  ```
  +) 정지가 되도 컨테이너는 메모리에 남아있

### 8) Docker rm
- 도커 컨테이너 삭제
  ```
  docker rm <name>
  ```

### 9) Docker rmi
- 도커 이미지 삭제
  ```
  docker rmi <image name>
  ```
  삭제하려는 이미지로 컨테이너를 생성했다면, 해당 컨테이너를 먼저 삭제해야함

+) run = 그냥 플레이 느낌, exec = 내가 멀리서 플레이시키는 느낌 </br>
최근엔 apache 잘 안씀. 이젠 컨테이너 내의 작은 웹서버가 인기있음. ex) nginx (경량 웹서버)

## 📌 Dockerfile , 도커 말아봤니?
사용자가 도커 이미지를 쉽게 만들 수 있도록 제공하는 템플릿

### 1) Dockerfile 만들기
- Dockerfile 이라는 이름으로 빈 file 생성
  ~~~
  # home 디렉토리 이동
  cd $HOME

  mkdir docker-practice

  cd docker-practice

  touch Dockerfile

  ls
  ~~~

### 2) Dockerfile 내용 작성하기
- vi/vim 등의 편집기로 Dockerfile 내용 작성 -> ```vi Dockerfile```
  ~~~java
  FROM ubuntu:18.04  # base image 명시 ex) FROM <image></image>[:<tag>] [AS <name>]

  RUN apt-get update # 명시한 커맨드를 컨테이너에서 실행

  CMD ["echo", "Hello Docker"]  # 명시한 커맨드를 컨테이너가 시작될 때, 실행할 것을 명시하는 명령어
  ~~~
  +) CMD 명령어의 3가지 형태
  ~~~java
   CMD <command> <param1> <param2>
   CMD ["executable", "parma1", "param2"]
   CMD ["parma1", "param2"] # ENTRYPOINT 와 함께 사용될 때
  ~~~

- 그외 명령어
  ~~~java
  COPY a.txt /some-directory/b.txt # a.txt 파일을 뒤에 작성한 경로에 복사

  WORKDIR /home/demo # 이후 작성될 명령어를 수행할 디렉토리 명시

  ENV locale-gen ko_KR.UTF-8 # 컨테이너 내부에서 지속적으로 사용될 환경 변수 설정

  EXPOSE 8080/<protocol> # 컨테이너와 연결할 포트/프로토콜 지정 (default 프로토콜: TCP)


  FROM ubuntu
  ENTRYPOINT ["/bin/echo", "Hello"] # docker run 실행 시 실행되는 명령어
  CMD ["world"]

  # Hello world
  # docker run -it --rm <image name> ME
  # Hello ME
  ~~~

### 3) Docker build from Dockerfile
  ```
  docker build -t my-image:v1.0.0 .
  ```
  - ```.``` 현재 경로(에 있는 Dockerfile)
  - my-image 라는 이름과 v1.0.0 이라는 태그로 이미지를 빌드
  
  ```
  docker images | grep my-image
  ```
  - 이미지 빌드 되었는지 확인

```
docker run my-image:v1.0.0 # Hello Docker 출력
```
- docker 컨테이너 실행하여 출력 확인

## 📌 Docker Image 저장소

### 1) Docker Registry
도커 레지스트리를 직접 띄워보고, 빌드했던 이미지를 도커 레지스트리에 push 해보기
- registry? 하드에서 실행되는 중 (컨테이너 안에서), 도커 이미지를 보내면 해당 이미지 관리 (그냥 원격 저장소 같은 거)

- docker registry 띄우기
  ```
  docker run -d -p 5000:5000 --name registry registry

  docker ps
  
  # registry 라는 이름이로 이미지 생성 확인, localhost:5000 으로 registry와 통신 가능
  ```

  +) 참고: ip는 하나지만, 포트는 여러개
  ~~~
  <portNumber>:<protNumber>
  # 앞의 포트번호는 도커를 설치한 호스트의 번호를 뒤의 컨테이너 포트번호에 연결한다는 뜻
  ~~~

- my-image를 방금 생성한 registry를 바라보도록 tag하기
  ```
  docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0

  docker images | grep my-image
  # localhost:5000/my-image:v1.0.0 로 생성된 것을 확인할 수 있음
  ```
- my-image를 registry 에 push
  ```
  docker push localhost:5000/my-image:v1.0.0
  ```

- 정상적으로 push 되었는지 확인
  ```
  # localhost:5000 이라는 registry에 저장된 이미지 리스트 출력
  curl -X  GET http://localhost:5000/v2/_catalog 
  
  # 출력: {"repositories":["my-image]}

  # my-image 라는 이미지 네임에 어떤 태그가 저장되어있는지 리스트 출력
  curl -X GET http://localhost:5000/v2/my-image/tags/list
  
  # 출력: {"name":"my-image","tag":["v1.0.0"]}
  ```

### 2) Docker Hub
- Docker login
  ```
  docker login
  ```

- Docker Hub를 바라보도록 tag 생성
  ~~~
  docker tag my-image:v1.0.0 <username>/my-image:v1.0.0
  ~~~

- Docker image push to Docker Hub
  ~~~
  docker push <username>/my-image:v1.0.0
  ~~~

- Docker hub 의 본인 계정에서 업로드한 이미지 확인
  - https://hub.docker.com/repositories

___
</br>

## 📌 Kubernetes

**Kubernetes?** Container Orchestration Tool</br>
~~도커야 혹시 자니? 대답 없으면 Kill~~

<img width="857" alt="image" src="https://user-images.githubusercontent.com/40768187/176466220-a92a4359-ade3-4e07-b2b0-c4e5f9c5a7dc.png">
</br>

- Worker Node = 서버
-  Pod = 쿠베네티스에서 생성, 관리할 수 있는 배포 가능한 가장 작은 컴퓨팅 단위

+)쿠버네티스도 도커 기반

## 📌 minikube 사용해보기
- minikube 참고: https://minikube.sigs.k8s.io/docs/start/
- kubectl 참고: https://kubernetes.io/ko/docs/tasks/tools/install-kubectl-linux/
</br>

- 최소 사양
  - CPU: 2 이상 (6 이상 추천, 프로세서 4개로 함)
  - Memory: 2 GB 이상 (12GB 이상 추천)
  - Disk: 20 GB 이상 (100GB 이상 추천)

### 1) minikube install
- amd 기반의 CPU 기준
  ```
  curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64

  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  ```

- 정상 다운로드 확인
  ```
  minikube --help
  
  minikube version
  ```

### 2) Kubectl install
- kubectl? kubernetes cluster(server)에 요청을 간편히 보내기 위해 사용되는 client 툴
  ```
  curl -LO https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl
  ```
- kubectl 바이너리를 사용할 수 있도록 권한과 위치 변경
  ```
  sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
  ```
- 설치 확인
  ```
  kubectl --help # kubernetes server를 생성하지 않아서 에러 메세지 일부 출력됨
  ```

### 3) minikube 시작하기
- minikube를 docker drvier를 기반으로 시작
  ```
  minikube start --driver=docker
  ````
- 설치 완료
  ![Untitled](https://user-images.githubusercontent.com/40768187/176473582-cbcc7632-5882-4350-bde6-9c0ec3c3cb86.png)

- 정상 설치 확인
  ```
  minikube status
  ```
  아래와 같이 출력되어야 함
  ```
  minikube
  type: Control Plane
  host: Running
  kubelet: Running
  apiserver: Running
  kubeconfig: Configured
  ```
- kubectl을 사용하여 minikube 내부의 default pod 정상 생성 확인
  ```
  kubectl get pod -n kube-system
  ```
  아래와 같이 출력되어야 함
  ```
  NAME                               READY   STATUS    RESTARTS   AGE
  coredns-558bd4d5db-bwkjv           1/1     Running   0          3m40s
  etcd-minikube                      1/1     Running   0          3m46s
  kube-apiserver-minikube            1/1     Running   0          3m46s
  kube-controller-manager-minikube   1/1     Running   0          3m53s
  kube-proxy-ppgbx                   1/1     Running   0          3m40s
  kube-scheduler-minikube            1/1     Running   0          3m46s
  storage-provisioner                1/1     Running   1          3m51s
  ```

### 4) minikube 삭제
  ```
  minikube delete
  ```
  아래와 같이 출력되면 삭제 완료
  ```
  🔥  docker 의 "minikube" 를 삭제하는 중 ...
  🔥  Deleting container "minikube" ...
  🔥  /home/kjy/.minikube/machines/minikube 제거 중 ...
  💀  "minikube" 클러스터 관련 정보가 모두 삭제되었습니다
  ```

  ## 📌 Pod
  
  ### 1) Pod?
- 쿠버네티스에서 생성하고 관리할 수 있는 배포가능한 가장 작은 컴퓨팅 단위
- 쿠버네티스는 Pod 단위로 스케줄링, 로드밸런싱, 스케일링 등 관리 작업 수행
  - 애플리케이션을 배포하고 싶다면 최소 Pod로 구성해야함
- 하나의 Pod는 한 개의 Container 혹은 여러 개의 Container로 이루어져 있을 수 있음
- Stateless 하고, 언제든지 삭제될 수 있는 자원

### 2) Pod 생성
  - ```vi pod.yaml``` 로 파일 생성
    ```yaml
    apiVersion: v1 # kubernetes resource 의 API Version
    kind: Pod # kubernetes resource name
    metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함
      name: counter
    spec: # 메인 파트 : resource 의 desired state 를 명시
      containers:
      - name: count # container 의 이름
        image: busybox # container 의 image
        args: [/bin/sh, -c, 'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done'] # 해당 image 의 entrypoint 의 args 로 입력하고 싶은 부분
    ```
- 위의 스펙대로 Pod 생성
  ```
  kubectl apply -f pod.yaml # kubectl apply -f <yaml-file-path>
  ```
  yaml-file-path 에 해당하는 kubernetes resource 생성 또는 변경 가능

  kubernetes resource의 desired state를 기록해놓기 위해 yaml 파일을 항상 저장하고, 버전 관리 하기

  ~~권장하는 방식은 아니지만 ```kubectl run```으로 파일 생성없이 pod 생성 가능함~~

- Pod 상태 확인
  ```
  kubectl get pod # 시간이 지난 후 Running 으로 변한 것 확인 가능
  ```

### 3) Pod 조회
  ```
  kubectl get pod # Current State 출력
  ```
  
  - namespace 란?
    - kubernetes에서 리소스를 격리하는 가상(논리적인) 단위
    - ```kubectl config view --minify | grep namespace:``` 로 current namespace 확인 가능
      - 따로 설정하지 않았다면 default namespace로 설정되어 있을 것
  
  - 특정 namespace 혹은 모든 namespace의 pod 조회
    ```
    kubectl get pod -n kube-system # kube-system namespace의 pod 조회

    kubectl get pod -A # 모든 namespace의 모든 pod 조회
    ```
  - pod 하나 조회
    ```
    kubectl get pod <pod-name> # 더 자세히 조회, kubectl describe pod <pod-name>
    ```
  - 기타 유용한 명령어
    ```
    kubectl get pod -o wide
    # pod 목록을 보다 자세히 출력합니다.

    kubectl get pod <pod-name> -o yaml
    # <pod-name> 을 yaml 형식으로 출력합니다.

    kubectl get pod -w
    # kubectl get pod 의 결과를 계속 보여주며, 변화가 있을 때만 업데이트됩니다.
    ```
  
### 4) Pod 로그
  - pod의 로그 확인
    ```
    kubectl logs <pod-name>

    kubectl logs <pod-name> -f # 로그 계속 보여줌
    ```

  - pod 안에 여러 개의 container 가 있는 경우 로그 확인
    ```
    kubectl logs <pod-name> -c <container-name>

    kubectl logs <pod-name> -c <container-name> -f
    ```

### 5) Pod 내부 접속
- pod 내부 접속
  ```
  kubectl exec -it <pod-name> -- <명령어>

  kubectl exec -it counter /bin/bash
  ```
- pod 안에 여러 개의 container가 있는 경우
  ```
  kubectl exec -it <pod-name> -c <container-name> -- <명령어>
  ```

### 6) Pod 삭제
- pod 삭제
  ```
  kubectl delete pod <pod-name>

  kubectl delete pod counter
  ```
- 리소스 생성시 사용한 yaml 파일 사용하여 삭제
  ```
  kubectl delete -f <YAML-파일-경로>
  ```
  - 이 명령어는 pod가 아니더라도 모든 kubernetes resource 에 적용 가능
