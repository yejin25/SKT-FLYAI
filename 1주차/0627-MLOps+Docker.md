# 1์ฃผ์ฐจ 2022 06 27
</br>

## ๐ Deep Learning โ ML โ AI

### ML?
```
A computer program is said to learn from experience E with respect
to task T and performance measure P, if itโs performance at
tasks in T, as measured by P, improves with experience E.

-Tom Mitchell
```

- ML ์ ํ
  
  - Supervised Learning (์ ๋ต์ ์๊ณ  ์์ธก)
  - Unsupervised Learning (์ ๋ต์ ๋ชจ๋ฅด๊ณ  ์์ธก)
  - Reinforcement Learning

![The-main-types-of-machine-learning-Main-approaches-include-classification-and](https://user-images.githubusercontent.com/40768187/175952246-bd77df04-2fa3-44ef-b5c3-ddba7235d0a7.png)

์ถ์ฒ: https://www.researchgate.net/figure/The-main-types-of-machine-learning-Main-approaches-include-classification-and_fig1_354960266

___
</br>

## ๐ MLOps
~~์ ํํ๋ ํ์ด ์๋ ์ถ์ถ์ ๊ตญ์๋ ์ฌ๊ธฐ์  ์ด ํด ์ฐ๊ณ  ์ ๊ธฐ์  ์ด ํด ์ฐ๊ณ ~~

= ๋จธ์ ๋ฌ๋ ์์ง๋์ด๋ง + ๋ฐ์ดํฐ ์์ง๋์ด๋ง + ์ธํ๋ผ + Ops

<img width="2100" alt="image" src="https://user-images.githubusercontent.com/40768187/175956667-dc5c8751-620c-4760-ac57-a217993ef865.png">

</br>
</br>

```
๋จธ์ ๋ฌ๋ ๋ชจ๋ธ ๊ฐ๋ฐ๊ณผ ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ ์ด์์์ ์ฌ์ฉ๋๋ ๋ฌธ์ , ๋ฐ๋ณต์ ์ต์ํํ๊ณ  ๋น์ฆ๋์ค ๊ฐ์น๋ฅผ ์ฐฝ์ถํ๋ ๊ฒ์ด
๋ชฉํ ๋ชจ๋ธ๋ง์ ์ง์คํ  ์ ์๋๋ก ๊ด๋ จ๋ ์ธํ๋ผ๋ฅผ ๋ง๋ค๊ณ , ์๋์ผ๋ก ์ด์๋๋๋ก ๋ง๋๋ ์ผ
```

ex) API ํํ๋ก ์๋ฒ ๋ง๋ค๊ธฐ, ์คํ ํ๋ผ๋ฏธํฐ์ ๊ฒฐ๊ณผ ์ ์ฅํ๊ธฐ, ๋ชจ๋ธ ๊ฒฐ๊ณผ ์๋ํํ๊ธฐ, ๋ฐ์ดํฐ Validation

</br>

### MLOps ๊ตฌ์ฑ์์
<img width="1495" alt="image" src="https://user-images.githubusercontent.com/40768187/175957106-39500b5f-0df8-4100-902c-566700206005.png">

๊ฐ ์์๋ค์ ํ์ดํ ๋ผ์ธ์ผ๋ก ์ฐ๊ฒฐ๋์ด ์์

**~~ML ์ฝ๋ ๋ถ๋ถ์ ์ ๋ง ์ ์ฒด ์ค์์ ์์ ๋ถ๋ถ ์ค ํ๋์ผ ๋ฟ~~**
___
</br>

## Research ML VS Production ML
|           | Research ML                                      | Production ML                               |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| ๋ฐ์ดํฐ    | ๊ณ ์ (static)                                     | ๊ณ์ ๋ณํจ(Dynamic-Shifting)                 |
| ์ค์ ์์ | ๋ชจ๋ธ ์ฑ๋ฅ(Accuracy, RMSE)                        | ๋ชจ๋ธ ์ฑ๋ฅ, ๋น ๋ฅธ Inference ์๋, ํด์ ๊ฐ๋ฅํจ |
| ๋์  ๊ณผ์  | ๋ ์ข์ ์ฑ๋ฅ์ ๋ด๋ ๋ชจ๋ธ, ์๋ก์ด ๊ตฌ์กฐ์ ๋ชจ๋ธ     | ์์ ์ ์ธ ์ด์, ์ ์ฒด ์์คํ ๊ตฌ์กฐ             |
| ํ์ต      | ๋ฐ์ดํฐ๊ฐ ๊ณ ์ ์ด๋ผ ๋ชจ๋ธ๊ตฌ์กฐ, ํ๋ผ๋ฏธํฐ ๊ธฐ๋ฐ ์ฌํ์ต | ์๊ฐ์ ํ๋ฆ์ ๋ฐ๋ผ ๋ฐ์ดํฐ๊ฐ ๋ณ๊ฒฝ๋์ด ์ฌํ์ต |
| ๋ชฉ์       | ๋ผ๋ฌธ ์ถํ                                        | ์๋น์ค์์ ๋ฌธ์  ํด๊ฒฐ                        |
| ํํ      | Offline                                          | Online                                      |

~~์ฐ๊ตฌ์ฉ์ ์ฑ๋ฅ ์ข์ ๋ชจ๋ธ๋ง๋ค๋ฉด ๋~~

___
</br>

## ๐ Docker

### Docker? VM?
<img width="737" alt="image" src="https://user-images.githubusercontent.com/40768187/175973620-fb132183-c819-4189-abc4-41947494c6d1.png">

- VM ์ Hypervisor๋ผ๋ ์ค๊ฐ SW๋ฅผ ํตํด ๊ฐ์ํ๊ฒฝ์ ๋ง๋ค๊ณ , Guest OS๋ฅผ ํฌํจํจ</br>
- Docker ๋ Guest OS ๋ฅผ ํฌํจํ๊ณ  ์์ง ์์ VM ๋ณด๋ค ๊ฐ๋ฒผ์</br>
์๋น์ค ์ด์ ํ๊ฒฝ์ Host OS์ ๋น์์กด</br>
์๋น์ค ์ด์ ํ๊ฒฝ์ ์ด๋ฏธ์ง๋ก ๋ง๋ค๊ณ  ์ด๋ฅผ ๋ฐฐํฌํ์ฌ ์ด์๋๋ฉด ์ปจํ์ด๋๊ฐ ๋จ.
์ธ์  ์ด๋์๋ ๋์ผํ ํ๊ฒฝ์์ ์คํ
</br>

### Docker ์ค์น

Docker๋ ๊ฐ์๋จธ์  ์์ Ubuntu 20.04LTS ๋ฒ์ ์ ์ฌ๋ ค ์ค์น ์งํํ์์ต๋๋ค.

ํญ์ ์ฒ์์ ํจํค์ง ๋งค๋์  ์๋ฐ์ดํธ, ์๊ทธ๋ ์ด๋ ํ์
```
sudo apt-get -y update && sudo apt-get -y upgrade
```

์ค์น ๋ฐฉ๋ฒ: https://docs.docker.com/engine/install/ubuntu/
</br>
</br>
### Install using the repository
Docker Engine์ ์ค์นํ๊ธฐ ์ ์ Docker repository ์ค์ ์ด ํ์ํจ</br>
๊ทธ๋์ผ Docker๋ฅผ repo๋ก๋ถํฐ ์ค์น ๋ฐ ์๋ฐ์ดํธ๊ฐ ๊ฐ๋ฅํจ

#### Set up the repository
- docker์ prerequisite package ์ค์น
   ```
   sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
   ```

- GPG key ์ถ๊ฐ</br>์ฐธ์กฐ: https://librewiki.net/wiki/์๋ฆฌ์ฆ:์ํธ์_์๋_๋ชฐ๋ผ๋_์ฝ๊ฒ_ํ๋_GPG
  ```
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  ```

- stable ๋ฒ์ ์ repository ๋ฐ๋ผ๋ณด๋๋ก ์ค์ 
  ```
  echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```
  +) arm ๊ธฐ๋ฐ cpu
    ```
    echo \
    "deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

#### Install Docker Engine
- Docker Engine, containerd ์ต์  ๋ฒ์  ์ค์น
  ```
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```
     ๋ฆฌ๋์ค์์ ๋ง์ง๋ง์ -d ๊ฐ ๋ถ์ ๊ฒ์ "demon" (์๋น์ค) ๋ฅผ ๋ปํ๋ค

    +) ํน์  ๋ฒ์  ์ค์น ๋ฐฉ๋ฒ
    ```
    apt-cache madison docker-ce
    ```
    <img width="887" alt="image" src="https://user-images.githubusercontent.com/40768187/175963213-3be84cbf-b38c-456d-8146-909d0d2e9b8d.png">

    ๋ช๋ น์ด ์คํ ํ ์์ ๊ฐ์ด ๋ชฉ๋ก์ด ๋์จ๋ค.</br>์ฌ๊ธฐ์ **5:20.10.16~3-0~ubuntu-jammy** ๊ฐ <VERSION_STRING> ์ด๋ค
    ```
    sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
    ```

#### Verifying Normal Installation
- Docker image ๋ฅผ ์คํ์์ผ ์ค์น ํ์ธ
    ```
    sudo docker run hello-world
    ```

    ![image](https://user-images.githubusercontent.com/40768187/175965494-1d467855-9906-42cd-8ce4-6d3255f00861.png)
    
    ์์ ๊ฐ์ ๋ฌธ์ฅ์ด ๋์ค๋ฉด ์ ์ ์ค์น ๐๐


### Docker ๊ถํ ์ค์ 
docker ๊ด๋ จ ์์์ root ์๊ฒ๋ง ๊ถํ์ด ์์ ๊ทธ๋์ ```sudo```๋ฅผ ๋ช๋ น์ด ์์ ๋ถ์ฌ์ผ ํจ</br>
๊ทผ๋ฐ ```sudo``` ๊ณ์ ๋ถ์ด๊ธฐ ๊ท์ฐฎ์ผ๋ ๊ถํ ๋ค์ ์ค์ 

```
sudo usermod -a -G docker $USER //$USER (<- ์ ์ ์ด๋ฆ)์ docker (๋ณด์กฐ)๊ทธ๋ฃน์ ์ถ๊ฐ, -a ์ต์์ -G ์ต์ํ๊ณ ๋ง ๊ฐ์ด ์ฐ์
sudo service docker restart //docker ์ฌ์คํ
```

์๋ ๋ช๋ น์ด ์์ฑ ํ ๊ถํ์ด ๊ฑฐ๋ถ๋๋ค๋ฉด ์ฌ๋ถํํ๊ณ  ๋ค์ ํ์ธํด๋ณด๊ธฐ</br>
~~๊ธฐ๊ณ๋ ์ญ์ ์ฌ๋ถํ์ด ์  ๋ง~~
```
docker ps   //ํ์ฌ ๊ฐ๋์ค์ธ ์ปจํ์ด๋ ๋ฆฌ์คํธ ์ถ๋ ฅ
```
์ด๋ ๊ฒ ๋์ค๋ฉด ๊ถํ ์ค์  ์๋ฃ ๐๐๐
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
