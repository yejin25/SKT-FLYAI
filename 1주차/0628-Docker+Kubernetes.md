# 1์ฃผ์ฐจ 2022 06 28
</br>

## ๐ Docker ๊ธฐ๋ณธ ๋ช๋ น์ด

### 1) Docker pull
- doker image repository ๋ถํฐ Docker image ๋ฅผ ๊ฐ์ ธ์ด
    ```
    docker pull <image name>
    ```
    +) ์ฐธ๊ณ : privateํ repository ์์ image๋ฅผ ๊ฐ์ ธ์ค๋ ๊ฒฝ์ฐ -> docker login์ ํตํด ํน์  repository ๋ฐ๋ผ๋ณด๋๋ก ํ๊ณ , pull ์ํ

### 2) Docker images
- ๋ก์ปฌ์ ์กด์ฌํ๋ image ๋ฆฌ์คํธ ์ถ๋ ฅ
  ```
  docker images
  ```

### 3) Docker ps
- ํ์ฌ ์คํ ์ค์ธ ์ปจํ์ด๋ ๋ฆฌ์คํธ ์ถ๋ ฅ
  ```
  docker ps
  docker ps -a
  ```

### 4) Docker run
- ๋์ปค ์ปจํ์ด๋ ์คํ (์์ ์ค ํ๋)
  ```
  docker run -it --name <name> <image name> /bin/bash
  ```
  ```-it``` ํ์ค ์๋ ฅ(stdin) ํ์ฑํ, TTY ๋ชจ๋ ์ฌ์ฉ - bash ์ฌ์ฉ ์ ํ์ -> ์์ด๋ CLI ๋๊ตฌ๋ก ์ฌ์ฉํ  ๋ ์ ์ฉ </br>
  ```/bin/bash``` ์ปจํ์ด๋๋ฅผ ์คํ์ํด๊ณผ ๋์์ ์คํํ  ๋ช๋ น์ด, bash ํฐ๋ฏธ๋์ ์ฌ์ฉํ๋ ๊ฒ์ ์๋ฏธ

  +) run ํ์ ๋ ์ด๋ฏธ์ง๊ฐ local์ ์๋ค๋ฉด ์ธ๋ถ registry์์ ๋ค์ด๋ก๋
  
  ~~๋๊ตฐ๊ฐ๊ฐ ์ด๋ฏธ ์ด๋ฏธ์ง๋ฅผ ๋ง๋ค์ด ๋์์ ๊ฒ์ด๋ค. ์ด๋ฏธ์ง ๋ง๋ ๋ค๊ณ  ์ฝ์งํ์ง ๋ง์~~

  **์ปจํ์ด๋ ์คํ ํ exit๋ก ์์์ ์ข๋ฃํ์ ๋**
  - ์ด๋ฏธ์ง๋ฅผ ์คํํ ํ์ ์์์ ํตํ ๋ณ๊ฒฝ์ฌํญ์ ์ปจํ์ด๋์ ๋ด์ฉ์ด ๋ณ๊ฒฝ๋๋ ๊ฒ์ด์ง, ์ด๋ฏธ์ง๋ ๋ณ๊ฒฝ๋์ง ์์
  - ๋ฐ๋ผ์ ์ปจํ์ด๋ ์ข๋ฃ์ ๋ณ๊ฒฝ์ฌํญ์ ๋ชจ๋ ใ2~
  - ctrl + p (or q) ๋ฅผ ํตํด ์ปจํ์ด๋๋ฅผ ์ข๋ฃ์ํค์ง ์๊ณ  ๋น ์ ธ๋์ฌ ์ ์์

### 5) Docker exec
- ์ปจํ์ด๋ ๋ด๋ถ์์ ๋ช๋ น์ ๋ด๋ฆฌ๊ฑฐ๋, ๋ด๋ถ๋ก ์ ์ํ๋ ๋ช๋ น์ด
  ```
  docker run -it -d --name <name> <image name>
  docker ps
  ```
  ```-d``` ์ปจํ์ด๋๋ฅผ ๋ฐฑ๊ทธ๋ผ์ด๋์์ ์คํํ๋ ๋ช๋ น์ด
  ```
  docker exec -it <name> /bin/bash
  ```

### 6) Docker logs
- ์ปจํ์ด๋์ log ํ์ธ
  ```
  docker run --name <name> -d <image name = busybox> sh -c "while true; do $(echo date); sleep 1; done"
  ```

  ```<name>``` ์ด๋ผ๋ busybox ์ด๋ฏธ์ง๋ฅผ ๋ฐฑ๊ทธ๋ผ์ด๋์์ ์ปจํ์ด๋๋ก ์คํํ์ฌ 1์ด์ ํ ๋ฒ์ฉ ํ์ฌ ์๊ฐ ์ถ๋ ฅ

  ```
  docker logs <name>
  docker logs <name> -f
  ```
  ```-f``` : ๊ณ์ํด์ log ์ถ๋ ฅ

### 7) Docker stop
- ์คํ ์ค์ธ ๋์ปค ์ปจํ์ด๋ ์ค๋จ
  ```
  docker stop <name>
  ```
  +) ์ ์ง๊ฐ ๋๋ ์ปจํ์ด๋๋ ๋ฉ๋ชจ๋ฆฌ์ ๋จ์์

### 8) Docker rm
- ๋์ปค ์ปจํ์ด๋ ์ญ์ 
  ```
  docker rm <name>
  ```

### 9) Docker rmi
- ๋์ปค ์ด๋ฏธ์ง ์ญ์ 
  ```
  docker rmi <image name>
  ```
  ์ญ์ ํ๋ ค๋ ์ด๋ฏธ์ง๋ก ์ปจํ์ด๋๋ฅผ ์์ฑํ๋ค๋ฉด, ํด๋น ์ปจํ์ด๋๋ฅผ ๋จผ์  ์ญ์ ํด์ผํจ

+) run = ๊ทธ๋ฅ ํ๋ ์ด ๋๋, exec = ๋ด๊ฐ ๋ฉ๋ฆฌ์ ํ๋ ์ด์ํค๋ ๋๋ </br>
์ต๊ทผ์ apache ์ ์์. ์ด์   ์ปจํ์ด๋ ๋ด์ ์์ ์น์๋ฒ๊ฐ ์ธ๊ธฐ์์. ex) nginx (๊ฒฝ๋ ์น์๋ฒ)

## ๐ Dockerfile , ๋์ปค ๋ง์๋ดค๋?
์ฌ์ฉ์๊ฐ ๋์ปค ์ด๋ฏธ์ง๋ฅผ ์ฝ๊ฒ ๋ง๋ค ์ ์๋๋ก ์ ๊ณตํ๋ ํํ๋ฆฟ

### 1) Dockerfile ๋ง๋ค๊ธฐ
- Dockerfile ์ด๋ผ๋ ์ด๋ฆ์ผ๋ก ๋น file ์์ฑ
  ~~~
  # home ๋๋ ํ ๋ฆฌ ์ด๋
  cd $HOME

  mkdir docker-practice

  cd docker-practice

  touch Dockerfile

  ls
  ~~~

### 2) Dockerfile ๋ด์ฉ ์์ฑํ๊ธฐ
- vi/vim ๋ฑ์ ํธ์ง๊ธฐ๋ก Dockerfile ๋ด์ฉ ์์ฑ -> ```vi Dockerfile```
  ~~~java
  FROM ubuntu:18.04  # base image ๋ช์ ex) FROM <image></image>[:<tag>] [AS <name>]

  RUN apt-get update # ๋ช์ํ ์ปค๋งจ๋๋ฅผ ์ปจํ์ด๋์์ ์คํ

  CMD ["echo", "Hello Docker"]  # ๋ช์ํ ์ปค๋งจ๋๋ฅผ ์ปจํ์ด๋๊ฐ ์์๋  ๋, ์คํํ  ๊ฒ์ ๋ช์ํ๋ ๋ช๋ น์ด
  ~~~
  +) CMD ๋ช๋ น์ด์ 3๊ฐ์ง ํํ
  ~~~java
   CMD <command> <param1> <param2>
   CMD ["executable", "parma1", "param2"]
   CMD ["parma1", "param2"] # ENTRYPOINT ์ ํจ๊ป ์ฌ์ฉ๋  ๋
  ~~~

- ๊ทธ์ธ ๋ช๋ น์ด
  ~~~java
  COPY a.txt /some-directory/b.txt # a.txt ํ์ผ์ ๋ค์ ์์ฑํ ๊ฒฝ๋ก์ ๋ณต์ฌ

  WORKDIR /home/demo # ์ดํ ์์ฑ๋  ๋ช๋ น์ด๋ฅผ ์ํํ  ๋๋ ํ ๋ฆฌ ๋ช์

  ENV locale-gen ko_KR.UTF-8 # ์ปจํ์ด๋ ๋ด๋ถ์์ ์ง์์ ์ผ๋ก ์ฌ์ฉ๋  ํ๊ฒฝ ๋ณ์ ์ค์ 

  EXPOSE 8080/<protocol> # ์ปจํ์ด๋์ ์ฐ๊ฒฐํ  ํฌํธ/ํ๋กํ ์ฝ ์ง์  (default ํ๋กํ ์ฝ: TCP)


  FROM ubuntu
  ENTRYPOINT ["/bin/echo", "Hello"] # docker run ์คํ ์ ์คํ๋๋ ๋ช๋ น์ด
  CMD ["world"]

  # Hello world
  # docker run -it --rm <image name> ME
  # Hello ME
  ~~~

### 3) Docker build from Dockerfile
  ```
  docker build -t my-image:v1.0.0 .
  ```
  - ```.``` ํ์ฌ ๊ฒฝ๋ก(์ ์๋ Dockerfile)
  - my-image ๋ผ๋ ์ด๋ฆ๊ณผ v1.0.0 ์ด๋ผ๋ ํ๊ทธ๋ก ์ด๋ฏธ์ง๋ฅผ ๋น๋
  
  ```
  docker images | grep my-image
  ```
  - ์ด๋ฏธ์ง ๋น๋ ๋์๋์ง ํ์ธ

```
docker run my-image:v1.0.0 # Hello Docker ์ถ๋ ฅ
```
- docker ์ปจํ์ด๋ ์คํํ์ฌ ์ถ๋ ฅ ํ์ธ

## ๐ Docker Image ์ ์ฅ์

### 1) Docker Registry
๋์ปค ๋ ์ง์คํธ๋ฆฌ๋ฅผ ์ง์  ๋์๋ณด๊ณ , ๋น๋ํ๋ ์ด๋ฏธ์ง๋ฅผ ๋์ปค ๋ ์ง์คํธ๋ฆฌ์ push ํด๋ณด๊ธฐ
- registry? ํ๋์์ ์คํ๋๋ ์ค (์ปจํ์ด๋ ์์์), ๋์ปค ์ด๋ฏธ์ง๋ฅผ ๋ณด๋ด๋ฉด ํด๋น ์ด๋ฏธ์ง ๊ด๋ฆฌ (๊ทธ๋ฅ ์๊ฒฉ ์ ์ฅ์ ๊ฐ์ ๊ฑฐ)

- docker registry ๋์ฐ๊ธฐ
  ```
  docker run -d -p 5000:5000 --name registry registry

  docker ps
  
  # registry ๋ผ๋ ์ด๋ฆ์ด๋ก ์ด๋ฏธ์ง ์์ฑ ํ์ธ, localhost:5000 ์ผ๋ก registry์ ํต์  ๊ฐ๋ฅ
  ```

  +) ์ฐธ๊ณ : ip๋ ํ๋์ง๋ง, ํฌํธ๋ ์ฌ๋ฌ๊ฐ
  ~~~
  <portNumber>:<protNumber>
  # ์์ ํฌํธ๋ฒํธ๋ ๋์ปค๋ฅผ ์ค์นํ ํธ์คํธ์ ๋ฒํธ๋ฅผ ๋ค์ ์ปจํ์ด๋ ํฌํธ๋ฒํธ์ ์ฐ๊ฒฐํ๋ค๋ ๋ป
  ~~~

- my-image๋ฅผ ๋ฐฉ๊ธ ์์ฑํ registry๋ฅผ ๋ฐ๋ผ๋ณด๋๋ก tagํ๊ธฐ
  ```
  docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0

  docker images | grep my-image
  # localhost:5000/my-image:v1.0.0 ๋ก ์์ฑ๋ ๊ฒ์ ํ์ธํ  ์ ์์
  ```
- my-image๋ฅผ registry ์ push
  ```
  docker push localhost:5000/my-image:v1.0.0
  ```

- ์ ์์ ์ผ๋ก push ๋์๋์ง ํ์ธ
  ```
  # localhost:5000 ์ด๋ผ๋ registry์ ์ ์ฅ๋ ์ด๋ฏธ์ง ๋ฆฌ์คํธ ์ถ๋ ฅ
  curl -X  GET http://localhost:5000/v2/_catalog 
  
  # ์ถ๋ ฅ: {"repositories":["my-image]}

  # my-image ๋ผ๋ ์ด๋ฏธ์ง ๋ค์์ ์ด๋ค ํ๊ทธ๊ฐ ์ ์ฅ๋์ด์๋์ง ๋ฆฌ์คํธ ์ถ๋ ฅ
  curl -X GET http://localhost:5000/v2/my-image/tags/list
  
  # ์ถ๋ ฅ: {"name":"my-image","tag":["v1.0.0"]}
  ```

### 2) Docker Hub
- Docker login
  ```
  docker login
  ```

- Docker Hub๋ฅผ ๋ฐ๋ผ๋ณด๋๋ก tag ์์ฑ
  ~~~
  docker tag my-image:v1.0.0 <username>/my-image:v1.0.0
  ~~~

- Docker image push to Docker Hub
  ~~~
  docker push <username>/my-image:v1.0.0
  ~~~

- Docker hub ์ ๋ณธ์ธ ๊ณ์ ์์ ์๋ก๋ํ ์ด๋ฏธ์ง ํ์ธ
  - https://hub.docker.com/repositories

___
</br>

## ๐ Kubernetes

**Kubernetes?** Container Orchestration Tool</br>
~~๋์ปค์ผ ํน์ ์๋? ๋๋ต ์์ผ๋ฉด Kill~~

<img width="857" alt="image" src="https://user-images.githubusercontent.com/40768187/176466220-a92a4359-ade3-4e07-b2b0-c4e5f9c5a7dc.png">
</br>

- Worker Node = ์๋ฒ
-  Pod = ์ฟ ๋ฒ ๋คํฐ์ค์์ ์์ฑ, ๊ด๋ฆฌํ  ์ ์๋ ๋ฐฐํฌ ๊ฐ๋ฅํ ๊ฐ์ฅ ์์ ์ปดํจํ ๋จ์

+)์ฟ ๋ฒ๋คํฐ์ค๋ ๋์ปค ๊ธฐ๋ฐ

## ๐ minikube ์ฌ์ฉํด๋ณด๊ธฐ
- minikube ์ฐธ๊ณ : https://minikube.sigs.k8s.io/docs/start/
- kubectl ์ฐธ๊ณ : https://kubernetes.io/ko/docs/tasks/tools/install-kubectl-linux/
</br>

- ์ต์ ์ฌ์
  - CPU: 2 ์ด์ (6 ์ด์ ์ถ์ฒ, ํ๋ก์ธ์ 4๊ฐ๋ก ํจ)
  - Memory: 2 GB ์ด์ (12GB ์ด์ ์ถ์ฒ)
  - Disk: 20 GB ์ด์ (100GB ์ด์ ์ถ์ฒ)

### 1) minikube install
- amd ๊ธฐ๋ฐ์ CPU ๊ธฐ์ค
  ```
  curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64

  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  ```

- ์ ์ ๋ค์ด๋ก๋ ํ์ธ
  ```
  minikube --help
  
  minikube version
  ```

### 2) Kubectl install
- kubectl? kubernetes cluster(server)์ ์์ฒญ์ ๊ฐํธํ ๋ณด๋ด๊ธฐ ์ํด ์ฌ์ฉ๋๋ client ํด
  ```
  curl -LO https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl
  ```
- kubectl ๋ฐ์ด๋๋ฆฌ๋ฅผ ์ฌ์ฉํ  ์ ์๋๋ก ๊ถํ๊ณผ ์์น ๋ณ๊ฒฝ
  ```
  sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
  ```
- ์ค์น ํ์ธ
  ```
  kubectl --help # kubernetes server๋ฅผ ์์ฑํ์ง ์์์ ์๋ฌ ๋ฉ์ธ์ง ์ผ๋ถ ์ถ๋ ฅ๋จ
  ```

### 3) minikube ์์ํ๊ธฐ
- minikube๋ฅผ docker drvier๋ฅผ ๊ธฐ๋ฐ์ผ๋ก ์์
  ```
  minikube start --driver=docker
  ````
- ์ค์น ์๋ฃ
  ![Untitled](https://user-images.githubusercontent.com/40768187/176473582-cbcc7632-5882-4350-bde6-9c0ec3c3cb86.png)

- ์ ์ ์ค์น ํ์ธ
  ```
  minikube status
  ```
  ์๋์ ๊ฐ์ด ์ถ๋ ฅ๋์ด์ผ ํจ
  ```
  minikube
  type: Control Plane
  host: Running
  kubelet: Running
  apiserver: Running
  kubeconfig: Configured
  ```
- kubectl์ ์ฌ์ฉํ์ฌ minikube ๋ด๋ถ์ default pod ์ ์ ์์ฑ ํ์ธ
  ```
  kubectl get pod -n kube-system
  ```
  ์๋์ ๊ฐ์ด ์ถ๋ ฅ๋์ด์ผ ํจ
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

### 4) minikube ์ญ์ 
  ```
  minikube delete
  ```
  ์๋์ ๊ฐ์ด ์ถ๋ ฅ๋๋ฉด ์ญ์  ์๋ฃ
  ```
  ๐ฅ  docker ์ "minikube" ๋ฅผ ์ญ์ ํ๋ ์ค ...
  ๐ฅ  Deleting container "minikube" ...
  ๐ฅ  /home/kjy/.minikube/machines/minikube ์ ๊ฑฐ ์ค ...
  ๐  "minikube" ํด๋ฌ์คํฐ ๊ด๋ จ ์ ๋ณด๊ฐ ๋ชจ๋ ์ญ์ ๋์์ต๋๋ค
  ```

  ## ๐ Pod
  
  ### 1) Pod?
- ์ฟ ๋ฒ๋คํฐ์ค์์ ์์ฑํ๊ณ  ๊ด๋ฆฌํ  ์ ์๋ ๋ฐฐํฌ๊ฐ๋ฅํ ๊ฐ์ฅ ์์ ์ปดํจํ ๋จ์
- ์ฟ ๋ฒ๋คํฐ์ค๋ Pod ๋จ์๋ก ์ค์ผ์ค๋ง, ๋ก๋๋ฐธ๋ฐ์ฑ, ์ค์ผ์ผ๋ง ๋ฑ ๊ด๋ฆฌ ์์ ์ํ
  - ์ ํ๋ฆฌ์ผ์ด์์ ๋ฐฐํฌํ๊ณ  ์ถ๋ค๋ฉด ์ต์ Pod๋ก ๊ตฌ์ฑํด์ผํจ
- ํ๋์ Pod๋ ํ ๊ฐ์ Container ํน์ ์ฌ๋ฌ ๊ฐ์ Container๋ก ์ด๋ฃจ์ด์ ธ ์์ ์ ์์
- Stateless ํ๊ณ , ์ธ์ ๋ ์ง ์ญ์ ๋  ์ ์๋ ์์

### 2) Pod ์์ฑ
  - ```vi pod.yaml``` ๋ก ํ์ผ ์์ฑ
    ```yaml
    apiVersion: v1 # kubernetes resource ์ API Version
    kind: Pod # kubernetes resource name
    metadata: # ๋ฉํ๋ฐ์ดํฐ : name, namespace, labels, annotations ๋ฑ์ ํฌํจ
      name: counter
    spec: # ๋ฉ์ธ ํํธ : resource ์ desired state ๋ฅผ ๋ช์
      containers:
      - name: count # container ์ ์ด๋ฆ
        image: busybox # container ์ image
        args: [/bin/sh, -c, 'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done'] # ํด๋น image ์ entrypoint ์ args ๋ก ์๋ ฅํ๊ณ  ์ถ์ ๋ถ๋ถ
    ```
- ์์ ์คํ๋๋ก Pod ์์ฑ
  ```
  kubectl apply -f pod.yaml # kubectl apply -f <yaml-file-path>
  ```
  yaml-file-path ์ ํด๋นํ๋ kubernetes resource ์์ฑ ๋๋ ๋ณ๊ฒฝ ๊ฐ๋ฅ

  kubernetes resource์ desired state๋ฅผ ๊ธฐ๋กํด๋๊ธฐ ์ํด yaml ํ์ผ์ ํญ์ ์ ์ฅํ๊ณ , ๋ฒ์  ๊ด๋ฆฌ ํ๊ธฐ

  ~~๊ถ์ฅํ๋ ๋ฐฉ์์ ์๋์ง๋ง ```kubectl run```์ผ๋ก ํ์ผ ์์ฑ์์ด pod ์์ฑ ๊ฐ๋ฅํจ~~

- Pod ์ํ ํ์ธ
  ```
  kubectl get pod # ์๊ฐ์ด ์ง๋ ํ Running ์ผ๋ก ๋ณํ ๊ฒ ํ์ธ ๊ฐ๋ฅ
  ```

### 3) Pod ์กฐํ
  ```
  kubectl get pod # Current State ์ถ๋ ฅ
  ```
  
  - namespace ๋?
    - kubernetes์์ ๋ฆฌ์์ค๋ฅผ ๊ฒฉ๋ฆฌํ๋ ๊ฐ์(๋ผ๋ฆฌ์ ์ธ) ๋จ์
    - ```kubectl config view --minify | grep namespace:``` ๋ก current namespace ํ์ธ ๊ฐ๋ฅ
      - ๋ฐ๋ก ์ค์ ํ์ง ์์๋ค๋ฉด default namespace๋ก ์ค์ ๋์ด ์์ ๊ฒ
  
  - ํน์  namespace ํน์ ๋ชจ๋  namespace์ pod ์กฐํ
    ```
    kubectl get pod -n kube-system # kube-system namespace์ pod ์กฐํ

    kubectl get pod -A # ๋ชจ๋  namespace์ ๋ชจ๋  pod ์กฐํ
    ```
  - pod ํ๋ ์กฐํ
    ```
    kubectl get pod <pod-name> # ๋ ์์ธํ ์กฐํ, kubectl describe pod <pod-name>
    ```
  - ๊ธฐํ ์ ์ฉํ ๋ช๋ น์ด
    ```
    kubectl get pod -o wide
    # pod ๋ชฉ๋ก์ ๋ณด๋ค ์์ธํ ์ถ๋ ฅํฉ๋๋ค.

    kubectl get pod <pod-name> -o yaml
    # <pod-name> ์ yaml ํ์์ผ๋ก ์ถ๋ ฅํฉ๋๋ค.

    kubectl get pod -w
    # kubectl get pod ์ ๊ฒฐ๊ณผ๋ฅผ ๊ณ์ ๋ณด์ฌ์ฃผ๋ฉฐ, ๋ณํ๊ฐ ์์ ๋๋ง ์๋ฐ์ดํธ๋ฉ๋๋ค.
    ```
  
### 4) Pod ๋ก๊ทธ
  - pod์ ๋ก๊ทธ ํ์ธ
    ```
    kubectl logs <pod-name>

    kubectl logs <pod-name> -f # ๋ก๊ทธ ๊ณ์ ๋ณด์ฌ์ค
    ```

  - pod ์์ ์ฌ๋ฌ ๊ฐ์ container ๊ฐ ์๋ ๊ฒฝ์ฐ ๋ก๊ทธ ํ์ธ
    ```
    kubectl logs <pod-name> -c <container-name>

    kubectl logs <pod-name> -c <container-name> -f
    ```

### 5) Pod ๋ด๋ถ ์ ์
- pod ๋ด๋ถ ์ ์
  ```
  kubectl exec -it <pod-name> -- <๋ช๋ น์ด>

  kubectl exec -it counter /bin/bash
  ```
- pod ์์ ์ฌ๋ฌ ๊ฐ์ container๊ฐ ์๋ ๊ฒฝ์ฐ
  ```
  kubectl exec -it <pod-name> -c <container-name> -- <๋ช๋ น์ด>
  ```

### 6) Pod ์ญ์ 
- pod ์ญ์ 
  ```
  kubectl delete pod <pod-name>

  kubectl delete pod counter
  ```
- ๋ฆฌ์์ค ์์ฑ์ ์ฌ์ฉํ yaml ํ์ผ ์ฌ์ฉํ์ฌ ์ญ์ 
  ```
  kubectl delete -f <YAML-ํ์ผ-๊ฒฝ๋ก>
  ```
  - ์ด ๋ช๋ น์ด๋ pod๊ฐ ์๋๋๋ผ๋ ๋ชจ๋  kubernetes resource ์ ์ ์ฉ ๊ฐ๋ฅ
