# 1์ฃผ์ฐจ 2022 06 29
</br>

## ๐ Deployment

### Deployment?
- Pod์ Replicaset์ ๋ํ ๊ด๋ฆฌ๋ฅผ ์ ๊ณตํ๋ ๋จ์
- ๊ด๋ฆฌ๋ผ๋ ์๋ฏธ๋ Self-healing, Scaling, Rollout๊ณผ ๊ฐ์ ๊ธฐ๋ฅ ํฌํจ (Self-healing -> ์ ๋ฒ์ ๋งํ๋ ๋์ปค kill)
- Pod์ Deployment๋ก ๋ฐฐํฌํจ์ผ๋ก์จ ์ฌ๋ฌ ๊ฐ๋ก ๋ณต์ ๋ Pod, ์ฌ๋ฌ ๋ฒ์ ์ Pod์ ์์ ํ๊ฒ ๊ด๋ฆฌํ  ์ ์์</br>
  = Pod ๋จ์๋ก๋ ๋ค๋ฅธ ์ปดํจํฐ์ ๋ถ์ฐ ์ํค๊ธฐ ๊ฐ๋ฅ

    <img width="396" alt="image" src="https://user-images.githubusercontent.com/40768187/176706324-a0b00b7c-5363-4e4a-be15-d6ed7aa62b72.png">
</br>

### Deployment ์์ฑ
```vi deployment.yaml``` ์ ์ฌ์ฉํ์ฌ Deployment ์์ฑ ํ์ผ ์์ฑ
```yaml
apiVersion: apps/v1 # kubernetes resource ์ API Version
kind: Deployment # kubernetes resource name
metadata: # ๋ฉํ๋ฐ์ดํฐ : name, namespace, labels, annotations ๋ฑ์ ํฌํจ
  name: nginx-deployment
  labels:
    app: nginx
spec: # ๋ฉ์ธ ํํธ : resource ์ desired state ๋ฅผ ๋ช์
  replicas: 3 # ๋์ผํ template ์ pod ์ 3 ๊ฐ ๋ณต์ ๋ณธ์ผ๋ก ์์ฑํฉ๋๋ค.
  selector:
    matchLabels:
      app: nginx
  template: # Pod ์ template ์ ์๋ฏธํฉ๋๋ค.
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx # container ์ ์ด๋ฆ
        image: nginx:1.14.2 # container ์ image
        ports:
        - containerPort: 80 # container ์ ๋ด๋ถ Port
```
์์ฑํ ํ์ผ ์คํ
```
kubectl apply -f deployment.yaml
```

### Deployment ์กฐํ
์์ฑํ Deployment์ ์ํ ํ์ธ
```
kubectl get deployment
# ๋ค์๊ณผ ๊ฐ์ ๋ฉ์์ง๊ฐ ์ถ๋ ฅ๋ฉ๋๋ค.
# NAME               READY   UP-TO-DATE   AVAILABLE   AGE
# nginx-deployment   0/3     3            0           10s

kubectl get deployment,pod # pod์ ์ํ๋ ๋ณผ ์ ์์
```
์๊ฐ์ด ์ง๋๋ฉด ```READY 3/3``` ์ผ๋ก ๋ฐ๋ ๊ฒ์ ๋ณผ ์ ์์

```
kubectl describe pod <pod-name>

# pod์ ์ ๋ณด๋ฅผ ์์ธํ ์กฐํํ๋ฉด 'Controlled By'๋ก๋ถํฐ Deployment์ ์ํด ์์ฑ๋๊ณ  ๊ด๋ฆฌ๋๋ ๊ฒ์ ํ์ธํ  ์ ์์
```

### Deployment Auto-healing
pod ํ๋ ์ญ์ 
```
kubectl delete pod <pod-name>

kubectl get pod # pod๊ฐ ์ญ์ ๋๊ณ  ์๋ก ํ๋ ์์ฑ๋ ๊ฒ์ ํ์ธ ํ  ์ ์์ (์ญ์ ํ pod์๋ ์ด๋ฆ์ด ๋ค๋ฆ)
```

### Deployment Scaling
replica ๊ฐ์ ๋๋ฆฌ๊ธฐ
```
kubectl scale deployment/nginx-deployment --replicas=5

kubectl get deployment

kubectl get pod
```

replica ๊ฐ์ ์ค์ด๊ธฐ
```
kubectl scale deployment/nginx-deployment --replicas=1

kubectl get deployment

kubectl get pod
```

### Deployment ์ญ์ 
deployment ์ญ์ 
```
kubectl delete deployment <deployment-name>

kubectl get deployment

kubectl get pod
```
Deployment์ control์ ๋ฐ๋ pod๋ ๋ชจ๋ ์ญ์ ๋ ๊ฒ์ ํ์ธ

+) ```-f``` ์ต์์ผ๋ก YAML ํ์ผ์ ์ฌ์ฉํด ์ญ์  ๊ฐ๋ฅ
```
kubectl delete -f <YAML-ํ์ผ-๊ฒฝ๋ก>
```
</br>

## ๐ Service

### Service?
- ์ฟ ๋ฒ๋คํฐ์ค์ ๋ฐฐํฌํ ์ ํ๋ฆฌ์ผ์ด์(Pod)์ ์ธ๋ถ์์ ์ ๊ทผํ๊ธฐ ์ฝ๊ฒ ์ถ์ํํ ๋ฆฌ์์ค
- Pod๋ IP๋ฅผ ํ ๋น๋ฐ๊ณ  ์์ฑ๋์ง๋ง, ์ธ์ ๋ ์ง ์ฃฝ์๋ค๊ฐ ์ด์๋  ์ ์๊ณ , ์ด ๊ณผ์ ์์ IP๋ ํญ์ ์ฌํ ๋น ๋ฐ๊ธฐ์ ๊ณ ์ ๋ IP๋ก ์ํ๋ Pod์ ์ ๊ทผํ  ์๋ ์์
- ๋ฐ๋ผ์ ํด๋ฌ์คํฐ ์ธ๋ถ ํน์ ๋ด๋ถ์์ Pod์ ์ ๊ทผํ  ๋ Service๋ฅผ ํตํด์ ์ ๊ทผํ๋ ๊ฒ
- Service๋ ๊ณ ์ ๋ IP๋ฅผ ๊ฐ์ง๋ฉฐ, Service๋ ํ๋ ํน์ ์ฌ๋ฌ ๊ฐ์ Pod์ ๋งค์นญ

    <img width="397" alt="image" src="https://user-images.githubusercontent.com/40768187/176707325-9f9a14fb-b36e-46c4-a3d8-2b615298d7f7.png">

</br>

### Service ์์ฑ
deployment ์์ฑํ๊ธฐ, **์์ Deployment ์์ฑ ์ฑํฐ ํ์ธ**
</br>
</br>

์์ฑ๋ Pod์ IP๋ฅผ ํ์ธํ๊ณ  ์ ์ ์๋
```
kubectl get pod -o wide
# Pod ์ IP ๋ฅผ ํ์ธํฉ๋๋ค.

curl -X GET <POD-IP> -vvv
ping <POD-IP>
# ํต์  ๋ถ๊ฐ๋ฅ
```
ํ ๋น๋ ```<POD-IP>```๋ ํด๋ฌ์คํฐ ๋ด๋ถ์์๋ง ์ ๊ทผํ  ์ ์๋ IP. ๋ฐ๋ผ์ ์ธ๋ถ์์๋ Pod์ ์ ์ํ  ์ ์์
</br>
</br>

minikube ๋ด๋ถ๋ก ์ ์ํ๋ฉด ํต์ ๋๋์ง ํ์ธ
```
minikube ssh
# minikube ๋ด๋ถ๋ก ์ ์ํฉ๋๋ค.

curl -X GET <POD-IP> -vvv
ping <POD-IP>
# ํต์  ๊ฐ๋ฅ
```
</br>
</br>
์์์ ์์ฑํ Deployment๋ฅผ ๋งค์นญ์ํจ Service ์์ฑ

```vi service.yaml```์ ์ฌ์ฉํ์ฌ Service ์์ฑ ํ์ผ์ ์์ฑํ๊ณ  ์คํ
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  type: NodePort # Service ์ Type ์ ๋ช์ํ๋ ๋ถ๋ถ์๋๋ค. ์์ธํ ์ค๋ช์ ์ถํ ๋ง์๋๋ฆฌ๊ฒ ์ต๋๋ค.
  ports:
  - port: 80
    protocol: TCP
  selector: # ์๋ label ์ ๊ฐ์ง Pod ์ ๋งคํํ๋ ๋ถ๋ถ์๋๋ค.
    app: nginx 
```
```
vi service.yaml
# ํ์ผ์ ์ด์ด ์์ ๋ด์ฉ์ ๋ณต์ฌ ๋ถ์ฌ๋ฃ๊ธฐ ํฉ๋๋ค.

kubectl apply -f service.yaml

kubectl get service
# PORT 80:<PORT> ์ซ์ ํ์ธ

curl -X GET $(minikube ip):<PORT>
# ์ด๋ ๊ฒ ์๋น์ค๋ฅผ ํตํด์ ํด๋ฌ์คํฐ ์ธ๋ถ์์๋ ์ ์์ ์ผ๋ก pod ์ ์ ์ํ  ์ ์๋ ๊ฒ์ ํ์ธํฉ๋๋ค.
```
<img width="376" alt="image" src="https://user-images.githubusercontent.com/40768187/176714794-81a16c2f-a6b9-48b0-912d-a0fb92fb889a.png">

</br>
Pod์ ์ ์ํ๋ ๊ตฌ์กฐ์ ๋ํด ์ข ๋ ์ดํดํ๊ธฐ ์ํด ์ด๋ฏธ์ง๋ฅผ ์ฒจ๋ถํ๋ค.
</br>(ํด๋น ์ค์ต์์๋ NodePort์ ํฌํธ๋ฒํธ๊ฐ 31370 ์ด์๋ค.)

</br>

```
์ถ์ฒ: https://blog.naver.com/PostView.naver?blogId=love_tolty&logNo=222499841070&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
```

#### Service์ Type?
- NodePort๋ผ๋ type์ ์ฌ์ฉํ๊ธฐ ๋๋ฌธ์, minikube๋ผ๋ kubernetes cluster ๋ด๋ถ์ ๋ฐฐํฌ๋ ์๋น์ค์ ํด๋ฌ์คํฐ ์ธ๋ถ์์ ์ ๊ทผํ  ์ ์์์
- ์ ๊ทผํ๋ IP๋ pod๊ฐ ๋ ์๋ ๋ธ๋์ IP๋ฅผ ์ฌ์ฉํ๊ณ , Port๋ ํ ๋น๋ฐ์ Port๋ฅผ ์ฌ์ฉ
- NodePort๋ Pod๊ฐ ์ด๋ค Node์ ์ค์ผ์ค๋ง๋  ์ง ๋ชจ๋ฅด๋ ์ํฉ์์, Pod์ด ํ ๋น๋ ํ ํด๋น Node์ IP๋ฅผ ์์์ผ ํ๋ค๋ ๋จ์  ์กด์ฌ
- ์ค๋ฌด์์๋ Kubernetes cluster์ MetalLB์ ๊ฐ์ LB ์ญํ ์ ํ๋ ๋ชจ๋์ ์ค์นํ ํ, LoadBalancer type์ผ๋ก ์๋น์ค๋ฅผ exposeํ๋ ๋ฐฉ์ ์ฌ์ฉ
  
  +) NodePort๋ฅผ ํตํด ๋ค์ด์จ ํธ๋ํฝ์ ๊ฒฝ์ฐ ํด๋ฌ์คํธ ๋ด๋ถ์์ 2๊ฐ์ ๋ณต์  Pod๋ฅผ ๋์์ผ๋ก L-B ๋์ด ์ฒ๋ฆฌ๋จ
    ```
    ์ฐธ๊ณ : https://blog.naver.com/PostView.naver?blogId=love_tolty&logNo=222499841070&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
    ```
</br>

## ๐ DVC

### DVC?
- git์ 100MB ํ๊ณ. ๋ฐ์ดํฐ์์ ์ฌ๋ฆด ์ ์์. ๊ทธ๋์ DVC ์ฌ์ฉ!
- ํ์ผ์ DVC๋ฅผ ํตํด ์คํ ๋ฆฌ์ง์ ์ฌ๋ฆฌ๊ณ , git์ผ๋ก๋ ๋ฒ์  ๊ด๋ฆฌ (ํ์ผ์ ์ถ์ ํ  ์ ์๋ ์ ๋ณด ์ ์ฅ)

### DVC ์ค์น
python ์ค์น
- python 3.8 ์ด์์ ํ๊ฒฝ ์ค๋น
  ```
  sudo apt-get install python3.8
    sudo apt-get update
    sudo apt-get upgrade

    ls -al /usr/bin/python

    ls /usr/bin/ | grep python

    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3
    update-alternatives --config python
  ```

์ค์น ํ์ธ
```
python -V # Python 3.9.6
```

+) ์ถ๊ฐ ์ค์  (์ํด๋ ๋จ)
python3์ ๋ณ์นญ์ python์ผ๋ก ๋ฐ๊ฟ
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3

update-alternatives --config python
```
์ด์  ```python``` ์ด๋ผ๊ณ ๋ง ์ณ๋ python ์คํ

git ์ค์น
```
sudo apt install git

git --version
# git version 2.25.1

git --help
# ์ ์ ์ค์น๋์๋์ง ํ์ธ
```

DVC ์ค์น
- dvc 2.6.4 ๋ฒ์  ๋ค์ด
- ```dvc[all]```์์ ```[all]```์ dvc์ remote storage๋ก, s3, gs, azure, oss, ssh ๋ชจ๋ ์ฌ์ฉํ  ์ ์๋๋ก ๊ด๋ จ ํจํค์ง ์ค์น
```
pip install dvc[all]==2.6.4 # python์ ์ธ๋ถ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๋ค์ด๋ก๋ ๋ช๋ น์ด

dvc --version
# 2.6.4

dvc --help
# ์ ์ ์ค์น๋์๋์ง ํ์ธ
```
pip ๋ช๋ น์ด๋ฅผ ์ฐพ์ ์ ์๋ค๊ณ  ์ค๋ฅ ๋ฐ์์, ```sudo apt install python3-pip``` ๋ก ์ค์น๋ฅผ ํด์ฃผ๋ฉด ๋จ

</br>

### DVC ์ ์ฅ์ ์ธํ
์ Directory ์์ฑ ํ ์ด๋
```
mkdir dvc-tutorial

cd dvc-tutorial
```

ํด๋น Directory ๋ฅผ git ์ ์ฅ์๋ก ์ด๊ธฐํ
```
git init
```

ํด๋น Directory๋ฅผ dvc ์ ์ฅ์๋ก ์ด๊ธฐํ
```
dvc init

#์๋ฌ๊ฐ ๋  ๊ฒฝ์ฐ 
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
๋ค์๊ณผ ๊ฐ์ด ๋์ค๋ฉด ์ฑ๊ณต ๐

</br>

### DVC ๊ธฐ๋ณธ ๋ช๋ น์ด - PUSH
1) dvc๋ก ๋ฒ์  trackingํ  data ์์ฑ
   ```
   # data ๋ฅผ ์ ์ฅํ  ์ฉ๋๋ก data ๋ผ๋ ์ด๋ฆ์ ๋๋ ํ ๋ฆฌ๋ฅผ ์์ฑํ๊ณ  ์ด๋ํฉ๋๋ค.
    mkdir data

    cd data

    # ๊ฐ๋ณ๊ฒ ๋ณ๊ฒฝํ  ์ ์๋ ๋ฐ์ดํฐ๋ฅผ ์นดํผํด์ค๊ฑฐ๋, ์๋ก ๋ง๋ญ๋๋ค.
    vi demo.txt

    cat demo.txt
    # Hello AI!
   ```

2) ๋ฐฉ๊ธ ์์ฑํ ๋ฐ์ดํฐ๋ฅผ dvc๋ก traking
   ```
    cd ..

    dvc add data/demo.txt

    # To track the changes with git, run:
    git add data/demo.txt.dvc data/.gitignore
   ```

3) dvc add์ ์ํด ์๋ ์์ฑ๋ ํ์ผ๋ค์ ํ์ธ
   ```
    cd data
    ls
    # demo.txt.dvc ํ์ผ์ด ์๋ ์์ฑ๋ ๊ฒ์ ํ์ธ

    cat demo.txt.dvc
    # demo.txt ํ์ผ์ ๋ฉํ์ ๋ณด๋ฅผ ๊ฐ์ง ํ์ผ์๋๋ค.
    # git ์์๋ demo.txt ํ์ผ์ด ์๋, demo.txt.dvc ํ์ผ๋ง ๊ด๋ฆฌํ๊ฒ ๋ฉ๋๋ค.
   ```

4) git commit
   ```
   git commit -m "Add demo.txt.dvc" # .dvc ํ์ผ์ git push ๋ฅผ ์ํํ์ฌ, git repository์ ์ ์ฅ
   ```

5) data๊ฐ ์ค์ ๋ก ์ ์ฅ๋  remote sotrage ์ธํ
   - ๋ณธ์ธ์ ๊ตฌ๊ธ ๋๋ผ์ด๋ธ์ ์๋ก์ด ํด๋๋ฅผ ํ๋ ์์ฑํด์ฃผ๊ณ , url์ ๋ง์ง๋ง ๋ถ๋ถ์ ๋ณต์ฌ</br></br>
    <img width="596" alt="แแณแแณแแตแซแแฃแบ 2022-07-01 แแฉแแฅแซ 12 55 28" src="https://user-images.githubusercontent.com/40768187/176723351-3f262c76-ecd9-49ff-86bd-d170fd557425.png">
    </br>

        ```
        dvc remote add -d storage gdrive://<GOOGLE_DRIVE_FOLDER_ID>

        # dvc ์ default remote storage ๋ก gdrive://<GOOGLE_DRIVE_FOLDER_ID> ๋ฅผ ์ธํํฉ๋๋ค.
        ```

6) dvc config๋ฅผ git commit
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
    - dvc push ์ํ์ ์ธ์ฆ ๊ณผ์ ์ด ํ์ํจ. ์คํ ํ ์ถ๋ ฅ๋๋ ์ฃผ์๋ก ์ด๋ํ์ฌ ์ธ์ฆ ์ํ
    - ์ธ์ฆ ์๋ฃ ! </br>
        ![Untitled (2)](https://user-images.githubusercontent.com/40768187/176724288-241305f9-3416-432c-b184-c18b4d46c9a4.png)

    - ์ดํ ๊ตฌ๊ธ ๋๋ผ์ด๋ธ๋ก ์ด๋ํด๋ณด๋ฉด ์๋ก์ด ํด๋๊ฐ ์์ฑ๋์ด ์๊ณ , ํด๋น ํด๋ ์์๋ ์๋ก๋ํ ํ์ผ์ด ์๋ ๊ฒ์ ํ์ธ ํ  ์ ์์

</br>

### DVC ๊ธฐ๋ณธ ๋ช๋ น์ด - PULL, CHECKOUT

1) dvc pull
   ```
   cd dvc-tutorial

    # dvc ์บ์๋ฅผ ์ญ์ ํฉ๋๋ค.
    rm -rf .dvc/cache/
    # dvc push ํ๋ ๋ฐ์ดํฐ๋ฅผ ์ญ์ ํฉ๋๋ค.
    rm -rf data/demo.txt

    # dvc pull ๋ก google drive ์ ์๋ก๋ํ๋ ๋ฐ์ดํฐ๋ฅผ ๋ค์ด๋ฐ์ต๋๋ค.
    dvc pull

    # ๋ฐฉ๊ธ ๋ค์ ๋ค์ด๋ฐ์ ๋ฐ์ดํฐ๊ฐ ์ด์  ๋ฐ์ดํฐ์ ๋์ผํ์ง ํ์ธํฉ๋๋ค.
    cat data/demo.txt
   ```

2) dvc checkout
   - data์ ๋ฒ์ ์ ๋ณ๊ฒฝํ๋ ๋ช๋ น์ด
   - ์ค์ต์ ์ํด ์๋ก์ด ๋ฒ์ ์ data๋ฅผ push

        ```
        # ๋ฐ์ดํฐ๋ฅผ ๋ณ๊ฒฝํฉ๋๋ค. (์๋ก์ด ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ์ด๋ฆ์ผ๋ก copy ํด์๋ ์ข์ต๋๋ค.)
        vi data/demo.txt

        # ๋ณ๊ฒฝ๋์๋์ง ํ์ธํฉ๋๋ค.
        cat data/demo.txt

        # dvc add (data/demo.txt.dvc ๋ฅผ ๋ณ๊ฒฝ์์ผ์ฃผ๋ ์ญํ )
        dvc add data/demo.txt

        # git add and commit
        git add data/demo.txt.dvc
        git commit -m "update demo.txt"

        # dvc push (and git push)
        dvc push # ์๋ก์ด ๋ฒ์ ์ data ํ์ผ์ remote storage ์ ์๋ก๋

        (git push) # .dvc ํ์ผ์ git repository ์ ์๋ก๋
        ```
    - ์ด์  ๋ฒ์ ์ data๋ก ๋๋์๊ฐ๊ธฐ
  
        ```
        # git log ๋ฅผ ํ์ธํฉ๋๋ค.
        git log --oneline

        # demo.txt.dvc ํ์ผ์ ์ด์  commit ๋ฒ์ ์ผ๋ก ๋๋๋ฆฝ๋๋ค.
        git checkout <COMMIT_HASH> data/demo.txt.dvc

        # dvc checkout ํฉ๋๋ค. (demo.txt.dvc ์ ๋ด์ฉ์ ๋ณด๊ณ  demo.txt ํ์ผ์ ์ด์  ๋ฒ์ ์ผ๋ก ๋ณ๊ฒฝํฉ๋๋ค.)
        dvc checkout

        # ๋ฐ์ดํฐ๊ฐ ๋ณ๊ฒฝ๋์๋์ง ํ์ธํฉ๋๋ค.
        cat data/demo.txt
        ```

    ์ด์ธ ์ถ๊ฐ์ ์ธ ๊ธฐ๋ฅ์ notion ์์ ํ์ธํ๊ธฐ!

</br>

## ๐ MLflow

### MLflow ์ด์ ์ ์์
 - ๋น์ทํ ์์์ด ๋ฐ๋ณต์ ์ผ๋ก ๋ฐ์
 - Dependency ํจํค์ง๋ค์ด ๋ง๊ณ , ๋ฒ์ ๊ด๋ฆฌ๊ฐ ์ด๋ ค์
 - ์ฌ๋ Dependency ์๊น
 - ํ์คํธ ์ด๋ ค์
 - ์ฌ์์ฐ๋์ง ์๋ ๊ฒฝ์ฐ๊ฐ ๋ง์
 - Model ํ์ต์ฉ ์ฝ๋๋ฅผ ๊ตฌํํ๋ ์ฌ๋๊ณผ Serving์ฉ ์ฝ๋๋ฅผ ๊ตฌํํ๋ ์ฌ๋์ด ๋ถ๋ฆฌ๋์ด ์์

### MLflow?

๋จธ์ ๋ฌ๋ ๋ชจ๋ธ์ ์ถ์ ํ๊ณ , ๋ชจ๋ธ์ ๊ณต์  ๋ฐ ๋ฐฐํฌ๋ฅผ ์ฝ๊ฒ ํ  ์ ์๋๋ก ์ง์ํ๋ ์คํ ์์ค

![Untitled](https://user-images.githubusercontent.com/40768187/176798565-9e9fcdd9-a6b1-47d2-9817-b3b66e13fc24.png)
</br>
+) MLflow ์ธ์๋ Tensorboard, Neptune, Wights & Biases, Comet.ml ๋ฑ์ด ์์

</br>

### MLflow ์ค์น
- Ubuntu 20.04 ์ฌ์ฉ
- python ๊ฐ์ ํ๊ฒฝ
  - conda : mlflow models serve ํ  ๋ ํ์
  - 3.8.5 ์ฌ์ฉ
  - pip3

```
# ์๋ก์ด ๋๋ ํ ๋ฆฌ๋ฅผ ํ๋ ์์ฑํ ๋ค, ์ด๋ํด์ฃผ์ธ์
mkdir mlflow-tutorial
cd mlflow-tutorial

# conda ๊ฐ์ํ๊ฒฝ ์ธํ
# python ๋ฒ์  ํ์ธ
python -V

pip install mlflow==1.20.2

mlflow --version
# mlflow, version 1.20.2
```
์ค์ต ์ค ์ค์น ์ค๋ฅ ๋ฐ์ -> protobuf ๋ฒ์ ์ 3.20.0 ์ผ๋ก ๋ฒ์ ์
```
pip uninstall mlflow    # 1

python-updates  # 3

pip intstall protobuf==3.20.0   # 4

pip install mlflow==1.20.2      # 2
```
์ค์ต์์  ์ฃผ์๊ณผ ๊ฐ์ ์์๋ก ๋ช๋ น์ด๋ฅผ ์คํํ์. ๊ทธ๋๋ ์ ์์ ์ผ๋ก ์ค์น ์๋ฃ๋๊ธด ํ์.

</br>

### MLflow tracking server ๋์๋ณด๊ธฐ
```
mlflow ui --help
# mlflow tracking server ๋ฅผ ๋์๋๋ค.
# UI (dashboard) ์ default url ์ http://localhost:5000 ์๋๋ค.
# 5000 ํฌํธ๊ฐ ์ด๋ ค์๋์ง ํ์ธํด์ฃผ์ธ์.
# production ์ฉ์ผ๋ก๋ mlflow ui ๋์  mlflow server ๋ฅผ ์ฌ์ฉํ๋ผ๋ ์๋ด๊ฐ ์ถ๋ ฅ๋ฉ๋๋ค.

mlflow server --help
# mlflow server ๋ worker ๋ฅผ ์ฌ๋ฌ ๊ฐ ๋์ธ ์ ์๊ณ , prometheus ๊ฐ metrics ์ ๊ฐ์ ธ๊ฐ ์ ์๋๋ก ์๋ํฌ์ธํธ๋ฅผ ์ ๊ณตํ๋ ๋ฑ์ ์ถ๊ฐ์ ์ธ ๊ธฐ๋ฅ์ด ์กด์ฌํฉ๋๋ค.
```
๋ก์ปฌ์์ ๋์ฐ๊ณ , ์ฌ์ฉ์๊ฐ ํ ๋ช์ด๊ธฐ์ ๋ ๊ฐ๋ฒผ์ด ```mlflow ui```๋ก MLflow tracking server ๋์ธ ์์ 
```
mlflow ui
```
๋ธํธ๋ถ์์ 5000 ๋ฒ ํฌํธ๊ฐ ์ฌ์ฉ ์ค์ด ์๋๋ผ๋ฉด, ๋ค์๊ณผ ๊ฐ์ด ์ถ๋ ฅ๋๊ณ  ```http://127.0.0.1:5000``` ์ผ๋ก ์ ์ํ๋ฉด ๋จ
![Untitled (1)](https://user-images.githubusercontent.com/40768187/176801877-d082f5ca-c2f5-4667-9251-552eb0120f86.png)
</br>

+) ์ค์ต์ Azure์์ ์งํํ๊ธฐ ๋๋ฌธ์ ๋ช๋ น์ด๋ฅผ ์กฐ๊ธ ๋ค๋ฅด๊ฒ ์์ฑํ๊ณ , ๋ณด์ ๊ท์น์ ๋ณ๊ฒฝํด์ฃผ๊ณ , localhost ๊ฐ ์๋ ๊ฐ์๋จธ์ ์ public IP๋ก ์ ์ํด์ผ ํ์
```
mlflow ui -h 0.0.0.0 -p 5000 # publicIP:5000 ์ผ๋ก ์ ์
```
![11](https://user-images.githubusercontent.com/40768187/176802510-d4827c73-64a7-4dc8-a1a8-34843afcac94.png)
</br>
**์ ์ ์๋ฃ !**

![Untitled (2)](https://user-images.githubusercontent.com/40768187/176802221-5191f74d-23b2-489c-b0a6-2c63419585b6.png)

 ๋ค๋ฅธ ํฐ๋ฏธ๋์ ์ด์ด์, ```mlflow-tutorial```๋ก ์ด๋ํด๋ณด๋ฉด, mlruns ๋ผ๋ ๋๋ ํ ๋ฆฌ๊ฐ ์์ฑ๋์ด ์์
 - ```mlflow ui``` ์คํ์ ```--backend-store-uri```, ```--default-artifact-root``` ์ต์์ ์ฃผ์ง ์์ ๊ฒฝ์ฐ, ```mlflow ui```๋ฅผ ์คํํ ๋๋ ํ ๋ฆฌ์ ```mlruns```๋ผ๋ ๋๋ ํ ๋ฆฌ๋ฅผ ์์ฑํ ๋ค ์ด ๊ณณ์ ์คํ ๊ด๋ จ ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๊ฒ ๋จ

    ```
    cd mlflow-tutorial

    ls
    cd mlruns
    cat 0/meta.yaml
    # ๋ฌด์ธ๊ฐ ์ฑ์์ง ๊ฒ์ ํ์ธํ  ์ ์์ต๋๋ค.
    ```

</br>

### MLflow ์ฌ์ฉํด๋ณด๊ธฐ

Example code ๋ค์ด
```
# VM ํน์ linux ์ฌ์ฉ์
wget https://raw.githubusercontent.com/mlflow/mlflow/master/examples/sklearn_elasticnet_diabetes/linux/train_diabetes.py

# Mac ์ฌ์ฉ์
wget https://raw.githubusercontent.com/mlflow/mlflow/master/examples/sklearn_elasticnet_diabetes/osx/train_diabetes.py
```

- mlflow์์ example๋ก ์ ๊ณตํด์ฃผ๋ ๋ค์ํ example ์ค ํ๋์ธ ```train_diabetes.py```
  - scikit-learn ํจํค์ง์์ ์ ๊ณตํ๋ ๋น๋จ๋ณ ์งํ๋ ์์ธก์ฉ ๋ฐ์ดํฐ
  - ElasticNet ๋ชจ๋ธ์ ํ์ตํ์ฌ, predict ํ ๋ค ๊ทธ evaluation metric์ MLflow์ ๊ธฐ๋กํ๋ ์์ 
  - 442 ๋ช์ ๋น๋จ๋ณ ํ์๋ฅผ ๋์์ผ๋ก, ๋์ด, ์ฑ๋ณ, bmi ๋ฑ์ 10๊ฐ์ ๋๋ฆฝ๋ณ์(X)๋ฅผ ๊ฐ์ง๊ณ  1๋ ๋ค ๋น๋จ๋ณ์ ์งํ๋ฅ (y)๋ฅผ ์์ธกํ๋ ๋ฌธ์ 

Example code ์คํ
```
# mlflow ui ๋ฅผ ์ํํ ๋๋ ํ ๋ฆฌ์ ๊ฐ์ ๋๋ ํ ๋ฆฌ๋ก ์ด๋
cd mlflow-tutorial

# example ์ฝ๋๋ฅผ ์คํ ํ mlflow ์ ๊ธฐ๋ก๋๋ ๊ฒ ํ์ธ
python train_diabetes.py
```
์คํ ์ค๋ฅ๊ฐ ๋๋ค๋ฉด ```pip install sklearn```์ผ๋ก ๊ด๋ จ ํจํค์ง ์ค์น ํ ์ฌ์คํ ํด๋ณด๊ธฐ


![Untitled (3)](https://user-images.githubusercontent.com/40768187/176823819-66ea4e21-5ad3-4754-bb3e-089acfc5b3fe.png)
</br>
model ๊ด๋ จ meta ์ ๋ณด์ ๋๋ถ์ด pkl ํ์ผ์ด ์ ์ฅ๋ ๊ฒ์ ํ์ธ

๋ค์ํ parameter๋ก ํ์คํธํ ํ์ mlflow ํ์ธ
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
์์ ๊ฐ์ ํ๋ฉด์ด ๋์ค๊ณ , metrics์ parameter๋ฅผ ํ ๋์ ๋น๊ต ๊ฐ๋ฅ

</br>

### MLflow ๋ฐ์ดํฐ ์ ์ฅ ๋ฐฉ์
```
cd mlruns/0
ls
# ๊ต์ฅํ ๋ง์ ๋๋ ํ ๋ฆฌ๊ฐ ์์ฑ๋์์ต๋๋ค.
# (๊ฐ๊ฐ์ ์ ์ ์๋ ํด๋๋ช์ mlflow ์ run-id ๋ฅผ ์๋ฏธํฉ๋๋ค.)

# ์๋ฌด ๋๋ ํ ๋ฆฌ์๋ ๋ค์ด๊ฐ๋ณด๊ฒ ์ต๋๋ค.
cd <ํน์  ๋๋ ํ ๋ฆฌ>
ls

# artifacs, metrics, params, tag ์ ๊ฐ์ ๋๋ ํ ๋ฆฌ๊ฐ ์๊ณ  ๊ทธ ์์ ์ค์  mlflow run ์ ๋ฉํ ์ ๋ณด๊ฐ ์ ์ฅ๋ ๊ฒ์ ํ์ธํ  ์ ์์ต๋๋ค.
```

</br>

## ๐ Flask

### Flask?
The python micro framework for building web applications
- MSA๋ฅผ ์ํ web app framework
- Django ๋ฑ ๋ค๋ฅธ framework์ ๋นํด ๊ต์ฅํ ๊ฐ๋ณ๊ณ , ํ์ฅ์ฑ, ์ ์ฐ์ฑ์ด ๋ฐ์ด๋จ
- ์ฌ์ฉํ๊ธฐ ์ฝ๊ณ , ๊ฐ๋จํ ๊ธฐ๋ฅ์ ๊ฐ๋ณ๊ฒ ๊ตฌํํ๊ธฐ์ ์ ํฉํ๊ธฐ ๋๋ฌธ์ ๋๋ถ๋ถ ML Model์ ์ฒซ๋ฐฐํฌ๋ก Flask ์ด์ฉ

<br>

### Flask ์ค์น
- python (3.6 ์ด์), pip3 ์ค์น

flask ์ค์น ์งํ
  ```
  # ์๋ก์ด ๋๋ ํ ๋ฆฌ๋ฅผ ํ๋ ์์ฑํ ๋ค, ์ด๋ํด์ฃผ์ธ์
    mkdir flask-tutorial
    cd flask-tutorial

    # python ๋ฒ์  ํ์ธ
    python -V

    # Flask ์ค์น
    pip install -U Flask==2.0.2

    # Flask Version ํ์ธ
    flask --version

    # Python 3.8.9
    # Flask 2.0.2
    # Werkzeug 2.0.2
  ```

<br>

### Hello world! with Flask
- Web Server ๋์ฐ๊ธฐ
- ```app.py``` ํ์ผ ์์ฑ ์๋ ์ฝ๋ ๋ณต๋ถ
  ```
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    if __name__ == "__main__":      # ์์ฑ์, ์คํํ  ๋ ๋์ค๋ ์ฝ๋
        app.run(debug=True, host='0.0.0.0', port=5000)
    # debug ๋ชจ๋๋ก ์คํ, ๋ชจ๋  IP ์์ ์ ๊ทผ ํ์ฉ, 5000 ํฌํธ๋ก ์ฌ์ฉํ๋ ๊ฒ์ ์๋ฏธ
  ```

- ๋์ผํ ํด๋์์ ```python app.py```๋ฅผ ์ํํ์ฌ application server๋ฅผ ๋ก์ปฌ์ ๋์
- ```127.0.0.1:5000```์ผ๋ก ์ ์ํ๋ฉด, ```Hello, World!```๋ผ๋ ๋ฌธ์๊ฐ ๋ธ๋ผ์ฐ์ ์ ๋ณด์ด๋ ๊ฒ์ ํ์ธ ๊ฐ๋ฅ
  
+) ์์ ๋งํ๋ฏ์ด ์ค์ต์ Azure์์ ์งํํ์. ์ด์ ๋ฐ๋ผ MLflow ์ฑํฐ์์ ๋ณด์ ๊ท์น๋ ์ถ๊ฐํด์ฃผ์๊ธฐ ๋๋ฌธ์ ๋ณธ์ธ์ ```publicIP:5000``` ์ผ๋ก ์ ์ํจ

<br>

### Routing
- flask์ ```route()``` ๋ฐ์ฝ๋ ์ดํฐ๋ python ํจ์๋ฅผ web server์ URL์ mapping ์ํฌ ์ ์์
- ```app.py``` ์๋์ ๊ฐ์ด ์์ 
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

```python app.py``` ์ํ ํ ์ด์ ๊ณผ ๊ฐ์ด ๋ธ๋ผ์ฐ์ ์ ์ ์ํด ๋ณด๋ฉด ```Hello, World!``` ๋ฟ๋ง ์๋๋ผ ```Hello, AI!``` ๋ผ๋ ๋ฌธ์๋ ์ถ๋ ฅ๋์ด ์์

+) **HTTP ์๋ต ํ์ธํด๋ณด๊ธฐ**
```
  curl -X GET 127.0.0.1:5000
  curl -X GET 127.0.0.1:5000/helloai
```

<br>

### POST method
- falsk๋ HTTP Method ๋ ์ง์  ๊ฐ๋ฅ
- ์ด๋ฅผ ํ์ฉํ์ฌ API ๊ฐ๋ฐ ๊ฐ๋ฅ
- ```app.py``` ์์ 

```
from flask import Flask
import json

app = Flask(__name__)

@app.route("/predict", methods=["POST", "PUT"])
def inference():
    return json.dumps({'hello': 'world'}), 200 # http status code ๋ฅผ 200 ์ผ๋ก ๋ฐํํ๋ ๊ฒ์ ์๋ฏธํฉ๋๋ค.

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
```
```python app.py``` ์ํ ํ HTTP ์๋ต ํ์ธ
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
- POST, PUT ๋ง ํ์ฉํ์ผ๋ฏ๋ก GET์ ๋ํ ์๋ต์ 405 ์๋ฌ๊ฐ ๋ฐ์

</br>
+) ์ค์ต ๋ชฉ์ ์ ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ์ API ์๋น์ค๋ก ์ ๊ณตํ  ๋, Flask ์ฌ์ฉํ๋ ๋ฐฉ๋ฒ์ ์์ ๋ณด๋ ๊ฒ์