# 2주차 2022 07 05
</br>

## 📌 Azure IaaS

### Azure Virtual Network

- Azure 데이터센터에 가상의 네트워크 만들어 네트워크 기반 통신
- Azure 리소스 간 안전한 통신 가능
- 온프레미스 인프라 리소스와 안전한 통신 ex) VPN, Express Route 등 이용
- Azure 지역에 종속되며 생성에 제한 없음
- 다른 계정의 가상 네트워크와는 기본적으로 차단되는 독립적 네트워크

#### 사전 지식

<img width="1203" alt="image" src="https://user-images.githubusercontent.com/40768187/177472246-61abe52b-1cdc-4e25-92e4-267c9df39ab4.png">

<img width="1131" alt="image" src="https://user-images.githubusercontent.com/40768187/177472390-da8ed30f-f549-46a8-8066-499fe17ed020.png">

IP 주소의 영역을 여러 네트워크 영역으로 나누기 위해 ip 를 묶는 방식
- 여러 개의 사설망을 구축하기 위해 망을 나누는방법
  
<img width="1205" alt="image" src="https://user-images.githubusercontent.com/40768187/177480306-76262b1a-6765-4719-8d2c-c5b4a1961bea.png">

</br>

### Private Network

<img width="1208" alt="image" src="https://user-images.githubusercontent.com/40768187/177472837-b3275857-35c7-4fdb-a065-eb819cbc170e.png">

참고 사이트: [CIDR.xyz](https://cidr.xyz/)

- 하나의 Public IP 를 여러 기기가 공유할 수 있는 방법
- 하나의 망에는 private IP 를 부여받은 기기들과 gateway 로 구성
  - 각 기기는 인터넷과 통신시 Gateway 를 통해 통신
- Private IP 는 지정된 대역의 아이피만 사용 가능

    <img width="1113" alt="image" src="https://user-images.githubusercontent.com/40768187/177472668-29738ea6-3947-4a63-a46a-33ed3fbedfca.png">

- 첫번째/마지막 IP는 예약되어 있어 사용 불가능
  - 첫번째 IP는 네트워크 자체를 가르키는 IP
  - 마지막 IP는 Broadcast IP
  - 10.1.0.0/24 의 경우 0~3, 255 는 예약되어 있음

### Subnet

<img width="1250" alt="image" src="https://user-images.githubusercontent.com/40768187/177480897-d80ff356-056f-4dd2-9fcd-1f5e28594854.png">

- 실제 Azure VM 이 배치되는 네트워크 단위
- Virtual Network 에 종속
- 가상 네트워크와 서브넷은 크기 조절 가능
- 네트워크를 정의할 수 있는 최소 단위로써 네트워크 정책 반영시 필요
- 가상 네트워크를 위해 서브넷은 존재해야함

#### 장점
- 네트워크 성능과 속도 향상
- 네트워크 정체를 줄임
- 네트워크 보안 향상
- 불필요하게 네트워크가 비대해지지 않음
- 관리 용이


#### 실습
Public IP 만들기

1. 리소스 그룹에 들어가 ```공용 IP 주소```  또는 ```Public IP``` 검색 후 ```+ 만들기``` 선택
2. 이름 작성, 리소스 그룹 선택, 위치 선택 후 나머지는 기본으로 두고 만들기

    <img width="1660" alt="image" src="https://user-images.githubusercontent.com/40768187/177550026-b9f1f9dc-0f61-4a80-a507-620ae3f3c17e.png">


가상 네트워크 만들기

1. 리소스 그룹에 들어가 ```가상 네트워크``` 또는 ```Virtual network``` 검색 후 ```+ 만들기``` 선택
2. 리소스 그룹 선택 후 주소 공간 ```172.16.0.0/16```, 서브넷 ```172.16.1.0/24``` 으로 하고 나머지는 기본
3. 생성 완료

    <img width="1465" alt="image" src="https://user-images.githubusercontent.com/40768187/177561254-cf3c484f-c369-4c52-846e-cbb8f05e8f25.png">

</br>

### Azure Virtual Machine

- IaaS 의 대표적인 리소스
- Azure 에서는 인프라 단위까지 관리해주고, OS 위의 부분은 사용자 관리


### 위치 및 가격 책정

위치
- 각 지역마다 하드웨어 및 서비스 기능 다름
- 가상 머신을 사용자에게 최대한 가깝게 배치
- 규정 준수 및 법적 의무를 보장하도록 가상 머신 배치

가격 책정
- 컴퓨팅 비용
- 스토리지 비용

### 가상 컴퓨터 크기

<img width="912" alt="image" src="https://user-images.githubusercontent.com/40768187/177549327-de9f170a-ab14-40f0-a27a-6c0506782259.png">

+) B 시리즈 - 웹 서버, 소규모 데이터베이스 및 개발 및 테스트 환경과 같이 cpu의 전체성능이 지속적으로 필요하지 않은 작업에 적합

#### Azure Hybrid Benefit (Windows)

- Software Assurance 고객은 Windows Server용 Azure Hybrid Benefit을 통해 Windows 라이선스를 Azure VM 에 이용
- 비용 절감 적용 시 VM 과금에 Windows 라이선스가 빠짐
- Windows 라이선스를 사용하는 모든 3rd party VM 과 모든 지역에 적용 가능
- 2개의 프로세스 또는 16 Core 에는 8 Core 라이선스 2개 또는 16 Core 라이선스 1개로 적용
- Standard Edition 1 회 적용, Datacenter Edition 제한 없음

#### 가상 네트워크 인터페이스

- 가상 컴퓨터가 네트워크에 연결되기 위해 필요한 리소스
- Private IP는 1개 이상 가질 수 있고, Public IP와 1:1 NAT 연결을 할 수 있음
- VM 크기에 따라 연결할 수 있는 vNIC 개수가 다름
- Public IP는 과금 대상

#### 가상 머신 스토리지

- 각 Azure VM에는 두 개 이상의 디스크가 포함되어 있음
  - OS 디스크
  - 임시 디스크 (내용 손실 가능)
  - 데이터 디스크 (선택 사항)

- OS 및 데이터 디스크는 Azure Storage 계정에 있음
  - Azure 기반 스토리지 서비스
  - 표준 HDD, SSD | 프리미엄 SSD | 울트라 SSD

- Azure VM을 만들 때 선택할 수 있는 디스크
  - 관리 디스크 (권장)
  - 비관리 디스크

+) 추가 메모 </br>

저장 디스크 속도 - CPU 성능 올리기</br>
네트워크 속도 - 랜카드 더 꽂아서 대역폭 증가 시키기 (랜카드를 더 꽂으려면 CPU 성능 올려야함)

가상 머신은 언제든지 리부팅될 수 있어서 데이터가 저장되지 않고 날라감. 저장은 디비에!

**state-less architecture**: 디비로 보내는건 속도가 좀 걸리니, Queue 에 담고 디비에 전송해서 저장



#### 가상 컴퓨터 리소스 종속 지도

<img width="920" alt="image" src="https://user-images.githubusercontent.com/40768187/177554183-21ed321d-8bbf-40cf-9d56-02c994ffd2cf.png">

NSG (네트워크 보안 그룹), 그림이 NIC 왼쪽에 위치해야 함

#### 가상 머신 확장

<img width="221" alt="image" src="https://user-images.githubusercontent.com/40768187/177554587-82f671ce-0890-4c9f-b81f-5c7ff18dcf88.png">

확장은 배포 후 VM 구성 및 자동화 작업을 제공하는 소규모 애플리케이션</br>
대부분 제품을 설치하는 옵션임, 최초 가상 컴퓨터 생성 시 실행해야 할 스크립트 지정 가능

</br>

Wordpress 설치해보기

1. ```Ubuntu Sever 18.04 LTS``` 검색후 가상 머신 생성, 가용성 집합은 새로 생성

    <img width="1672" alt="image" src="https://user-images.githubusercontent.com/40768187/177556778-2f3182d2-8f77-43bb-b07c-a9bfcf6cf500.png">

2. 디스크 탭은 기본으로, 네트워크는 아래와 같이 설정

    <img width="985" alt="image" src="https://user-images.githubusercontent.com/40768187/177557210-9cf49752-084a-4747-ba53-bf87d685afea.png">

3. 고급 설정에서 ```설치할 확장 선택``` 클릭 후 ```Custom Script For Linux``` 추가 로드하고 확인

    <img width="1357" alt="image" src="https://user-images.githubusercontent.com/40768187/177557376-392a57ae-f0d0-4780-b1e3-7ca93eeeca4c.png">

4. 로컬에 있는 첨부할 스크립트 파일을 스토리지에 컨테이너 생성 후 업로드

    <img width="1669" alt="image" src="https://user-images.githubusercontent.com/40768187/177557551-369d3b80-307c-4085-98f9-9613bc91c6d5.png">

    <img width="1672" alt="image" src="https://user-images.githubusercontent.com/40768187/177557775-1ed8e7f4-a176-47ff-a87a-29e9aea0168e.png">

5. 태그는 기본으로 두고, 유효성 검사 후 가상 머신 만들기

6. 생성한 가상머신의 Public IP 로 접속하여 확인

    <img width="1673" alt="image" src="https://user-images.githubusercontent.com/40768187/177559090-a5871146-051a-4c10-86a4-33917f0e5017.png">

</br>

#### 가상 머신 접속 방법

1. SSH
2. RDP
3. BastionHost: 최근에 생긴 개념, 포탈에서 가상머신 접속


#### Azure Storage Account

- 비정형 및 반정형 데이터를 저장하는 저장소
- 뛰어난 내구성과 가용성을 제공
- 제한 없는 저장소 용량
- 손쉬운 액세스
- 높은 성능

종류
-  Blob (Object storage)
-  Files (File share)
-  Table (Key-value store)
-  Queue (Simple queue)

#### Azure Storage 서비스

Azure Containers(Blobs)
- HTTP 또는 HTTPS 를 통해 어디서나 액세스 가능
- 텍스트 또는 이진 파일과 같은 대량의 비구조적 데이터 저장 가능

Azure Files
- SMD 3.0 을 통해 어디서나 액세스 가능
- 항상 사용 가능한 네트워크 파일 공유 호스트

Azure Queues
- HTTP 또는 HTTPS 를 통해 어디서나 액세스 가능/비동기 통신용 큐 기반 메커니즘 제공
- 큐에 최대 64KB 크기의 메시지 저장 가능

Azure Tables
- HTTP 또는 HTTPS를 통해 어디서나 액세스 가능
- NoSQL 테이블 저장 가능

#### Storage Account 유형

<img width="880" alt="image" src="https://user-images.githubusercontent.com/40768187/177784272-e94c1407-4717-480a-86ba-d4080b318193.png">

#### 복제 전략
<img width="872" alt="image" src="https://user-images.githubusercontent.com/40768187/177784473-42235ea6-74e4-434d-9a1f-7696b7a7ec6d.png">

#### 스토리지 액세스

모든 개체에는 계정 이름과 스토리지 유형에 따른 고유한 URL 주소가 존재

<img width="872" alt="image" src="https://user-images.githubusercontent.com/40768187/177786084-a0140618-ea23-48bf-b885-4dcfcaf6cc42.png">

#### Blob Storage

Blob Storage 의 일반적인 용도
-  브라우저에 이미지나 문서 직접 제공
-  설치 등의 분산 액세스용으로 파일 저장
-  비디오 및 오디오 스트리밍
-  백업 및 복원, 재해 복구, 보관을 위한 데이터 저장
-  온-프레미스 또는 Azure 호스팅 서비스에서 분석할 수 있도록 데이터 저장

Blob Service 에 포함된 세 가지 리소스 유형
- 스토리지 계정
- 스토리지 계정의 컨테이너
- 컨테이너의 Blob

Blob Storage 생성

<img width="1653" alt="image" src="https://user-images.githubusercontent.com/40768187/177792824-c925e68f-635e-41da-8244-cd86d2b53735.png">

</br>

1. 리소스 그룹에서 ```Storage account``` 검색 후 만들기

2. 전세계에서 유일한 이름으로 스토리지 이름 작성 후, 지역 선택. 나머지는 기본으로 두고 만들기

    <img width="942" alt="image" src="https://user-images.githubusercontent.com/40768187/177793066-536b5962-f248-46d4-948b-1290c8d2d388.png">

3. 생성된 스토리지 선택 후 이름 작성 후 컨테이너 생성

   <img width="1347" alt="image" src="https://user-images.githubusercontent.com/40768187/177804547-01fed240-fcb1-40c2-b5ff-3f6a088e461c.png">

#### Blob 컨테이너

- Private: Storage Account 의 인증을 통해 Container와 Blob에 접근
- Blob: 익명의 사용자에게 Blob에 읽기 권한 부여
- Container: 익명의 사용자에게 Container와 Blob에 읽기 권한 부여

    <img width="817" alt="image" src="https://user-images.githubusercontent.com/40768187/177794130-117a506a-99d1-4689-8ecb-5888ec1d8a6f.png">

    스토리지의 컨테이너 목록에서 선택 후 (또는 컨테이너에 들어가서)  ```Change access level``` 클릭 후 권한 변경 가능

#### Blob 액세스 계층

- 핫: 스토리지 계정의 개체에 자주 액세스하는 경우에 적합
- 쿨: 자주 액세스하지 않으며 30일 이상 저장되는 대량의 데이터를 저장하는데 가장 적합
- 보관: 검색 대기 시간이 몇 시간이어도 되며 180일 이상 보관 계층에 저장할 데이터에 가장 적합

#### 스토리지 계층

- 스토리지 계층을 사용하면 솔루션에 이상적인 비율로 성능과 비용을 조정할 수 있음
  
  <img width="601" alt="image" src="https://user-images.githubusercontent.com/40768187/177801495-1e475316-5de1-4f28-a086-7f5da3bbaaf7.png">

#### Blob 수명 주기 관리

수명 주기 관리 정책을 사용하여 수행할 수 있는 작업
- 성능과 비용 최적화를 위해 Blob을 계층의 하위 스토리지 계층으로 전환
  - 핫 -> 쿨/보관, 쿨 -> 보관
- 수명 주기가 끝날 때 Blob 삭제
- 스토리지 계정 수준에서 하루에 한 번 실행할 규칙 저으이
- 컨테이너 또는 Blob의 하위 집합에 규칙 적용 (접두사를 필터로 사용)

수명 주기 관리 규칙 추가하기

1. 스토리지 계정에서 ```Lifecycle management``` 선택 후 ```Add a rule``` 클릭

    <img width="1661" alt="image" src="https://user-images.githubusercontent.com/40768187/177803515-d85b4f08-18e6-4281-9b48-a069ea89d4fc.png">

1. 규칙 이름 작성 후 나머지는 기본으로 두고 ```Next```

2. 보관 기간을 정하고, 어떻게 처리할 것인지 선택

    <img width="781" alt="image" src="https://user-images.githubusercontent.com/40768187/177805710-c5bd1791-8738-4ea3-9605-0cb8fd77a31d.png">

#### 스토리지 가격 책정

- 스토리지 비용
- 데이터 액세스 비용
- 트랜잭션 비용
- 지역 복제 데이터 전송 비용
- 아웃바운드 데이터 전송 비용
- 스토리지 계층 변경

#### 스토리지 계정 키

- Azure 에서는 각 스토리지 계정용으로 2개 (기본 키/ 보조 키)를 생성
- 키 중 하나가 계정에 대한 모든 액세스 제공
- 키는 정기적으로/손상된 경우 다시 생성해야 함

#### 스토리지 엔드포인트 보호

<img width="1264" alt="image" src="https://user-images.githubusercontent.com/40768187/177807416-c075060d-f95f-4ed3-bfef-b221314aea24.png">

- 방화벽과 가상 네트워크 설정을 사용하면 특정 가상 네트워크 서브넷에서 스토리지 계정 액세스 제한 가능
- 가상 네트워크와 해당 서브넷은 스토리지 계정과 같은 Azure 지역 또는 지역 쌍에 있어야 함

#### URI 및 SAS 매개 변수

<img width="871" alt="image" src="https://user-images.githubusercontent.com/40768187/177813540-074f6581-59f1-490d-bcb1-a8f911ca9a5d.png">

- SAS는 하나 이상의 스토리지 리소스를 가리키는 서명된 URI
- 스토리지 리소스 URI 및 SAS 토근으로 구성
- 리소스 URI, 스토리지 서비스 버전, 서비스, 리소스 유형, 시작 시간, 만료 시간, 리소스, 권한, IP 범위, 프로토콜, 서명에 대한 매개변수 포함


#### 파일 공유 관리

- 파일 공유 할당량
- Windows - 포트 445가 열려 있는지 확인
- Linux - 드라이브 탑재
- MacOS - 드라이브 탑재
- 보안 전송 필요 - SMB 3.0 암호화

파일 공유 해보기

1. File share 추가

    <img width="1648" alt="image" src="https://user-images.githubusercontent.com/40768187/177808180-1c5396a6-bbc0-422f-beb9-4733ddd90268.png">

2. 생성한 File share 선택 후 ```Connect``` 선택

    <img width="1638" alt="image" src="https://user-images.githubusercontent.com/40768187/177808627-f9e77d7b-5419-428e-8017-cc72adfb5334.png">

    window 면 아래 스크립트를 powershell 에서 실행하면 접속할 수 있음
    
    ~~실습장에선 포트 445 를 막아둔 상태여서 접속하지 못햇음~~

    이번엔 MacOS 에서 접속해 볼 예정! 포트 열려있는데 안되네..? 아쉽..

<img width="372" alt="image" src="https://user-images.githubusercontent.com/40768187/177811129-979e1906-d412-4042-a3c8-28e738220358.png">

#### 파일 공유 스냅샷

- 특정 시점의 공유 상태를 캡처하는 증분 스냅샷
- 데이터의 읽기 전용 복사본
- 파일 공유 수준의 스냅샷으로서 파일 수준에서 복원

#### 스토리지 탐색기

- Storage Account를 좀 더 쉽게 조작할 수 있는 Application
- Storage Account 와 Cosmos DB, Data Lake Gen1 지원
- 인증 방법은 AAD와 Storage Account Key, SAS 로 가능
- Local에서 Storage Account를 사용할 수 있도록 애뮬레이터 지원

</br>

1. 구독 선택 후 Azure 계정으로 로그인

<img width="1042" alt="image" src="https://user-images.githubusercontent.com/40768187/177815730-136b7fe3-90ab-4468-990e-fcac5653b02a.png">

2. 인증 완료

<img width="1734" alt="image" src="https://user-images.githubusercontent.com/40768187/177815153-5f5b40d9-b92b-4734-b680-db1a3bdc6435.png">

3. 접속 후 왼쪽 탭의 가장 위쪽 탭을 선택하면 스토리지 확인 가능

<img width="1112" alt="image" src="https://user-images.githubusercontent.com/40768187/177815603-d4621897-83fb-430b-8783-ea46db4dcb32.png">

</br>

## 📌 Databases

### Azure Database

- Azure의 관리형 데이터베이스 서비스
- Azure Database 유형
  - Azure SQL Database - SQL Server
  - Azure SQL Managed Instance - SQL Server (vNet 필요)
  - Azure Database for MySQL
  - Azure Database for MariaDB
  - Azure Database for PostgreSQL
  - 파트너사에서 제공하는 관리형 데이터베이스 (ClearDB 등)
- Azure Database 컴퓨팅 구성
  - DTU (Database Transaction Units) : 기본, 표준, 프리미엄
  - vCore : 범용, 중요 비즈니스용, 하이

### Azure SQL Database 서비스

배포 모델

<img width="617" alt="image" src="https://user-images.githubusercontent.com/40768187/177823589-89173454-977c-4875-97e7-74833871e69a.png">

- 단일 데이터베이스 - DTU / vCore
- Managed Instance  - vCOre
- 탄력적 풀

### Azure SQL Database Managed Instance

<img width="971" alt="image" src="https://user-images.githubusercontent.com/40768187/177824235-cbfc4c98-383d-4472-9fb7-3f0850d61f39.png">

### DTU

<img width="433" alt="image" src="https://user-images.githubusercontent.com/40768187/177825263-d1438139-40e6-4b1c-af36-f751b4af4d57.png">

- CPU, 메모리, I/O (데이터 및 트랜잭션 로그 I/O) 의 혼합된 측정치
- 리소스를 지정하는 것이 아닌 트랜잭션을 기준으로 성능을 측정하여 제공
- Azure 는 DTU 계산기를 제공하고 있으며, 모니터링 수치도 제공

### Azure SQL Database 에서 단일 데이터베이스 크기 조정

- Azure SQL Database의 단일 데이터베이스는 수동 동적 확장성 지원
- 언제든지 가동 중지 시간을 최소화하며 DTU 서비스 계층 또는 vCore 특성 변경 가능

### vCore 모델

- vCore 수와 메모리, 디스크 용량 정할 수 있음
- Gen4 의 경우 Core 당 7GB, Gen5의 경우 Core 당 5.5GB
- 범용 계층은 프리미엄 저장소 (vCore 당 500 IOPS)
- 중요 비즈니스 계층은 로컬SSD (vCore 당 5000 IOPS)
- vCore 수에 따라 Log 저장소의 크기가 달라짐
- 300 초를 초과하는 DTU 가 있다면 vCOre 가 비용 절약

### SQL Database 복구

<img width="969" alt="image" src="https://user-images.githubusercontent.com/40768187/177827540-0b9b88b5-cc4e-48ad-b5c4-53392487a545.png">

### 지역에서 복제

- Azure 지역을 기준으로 SQL Database 복제
- 과금이 높아 다음 사항일 시 사용 추천
  - 중요 업용
  - 24시간 이상의 가동 중지 시간 허용하지 않는 SLA(서비스 수준 약정) 존재
  - 데이터 변경 속도 높고 1시간에 해당하는 데이터 손실 허용할 수 없음
  - 가동 중지가 재무적 책임 유발
  - 활성 지역 복제 사용 시 발생하는 추가 비용이 잠재적인 재무적 책임과 연계된 비즈니스 손실보다 낮음

### 데이터베이스 동기화

- Azure SQL Database를 이용하여 Database 양방향 동기화
- Hub Database 는 Azure SQL Database
- Member Database는 On-prem도 가능
- Sync Database도 Azure SQL Database (Hub와 동일지역)
- On-prem의 경우 Agent 필요
- 허브 우선과 구성원 우선으로 데이터 충돌 해결

### 보안 기능

<img width="409" alt="image" src="https://user-images.githubusercontent.com/40768187/177831718-095941d0-708c-4fb7-b5a3-181b4bdf7005.png">

- 데이터베이스 방화벽으로 IP 차단 가능
- SSL 인증서 기반 통신으로 통신 암호화 가능

### Azure Defender for DB (Advanced Threat Protection)

- SQL 고급 보안 기능에 대한 통합 패키지
- 중요한 데이터의 검색, 분류, 레이블 지정 및 보호
- 잠재적인 디비 취약성을 검색, 추적 및 수정할 수 있는 서비스 간편하게 구성
- 비정상적이며 잠재적으로 유해할 수 있는 데이터베이스 액세스 또는 악용 시도를 나타내는 비정상적인 활동 검색
  - SQL Injection 등 검출 및 e-mail 보고
- 월별 노드당 $15
- 처음 60일 무료 평가 기간

### Azure Database for MySQL

- MySQL 5.6.39, 5.7.21 지원
- 로그는 최대 7일간 보존, 7.5GB 초과시 여유공간이 생길 때까지 오래된 파일 삭제
- Slow query는 기본적으로 비활성화, slow_query_log를 ON으로 설정해야 함
- HA, 확장, 축소시 새로운 인스턴스를 생성 (Downtime)
- 응용프로그램의 재시도 연결 필수
- DTU 계층 없음

#### Azure Database for MySQL servers 생성해보기

1. 리소스 그룹에 들어가서 ```+ 만들기``` > ```Azure Database for MySQL servers```  검색 후 생성

    <img width="1064" alt="image" src="https://user-images.githubusercontent.com/40768187/177834459-196fd888-cd2a-47fc-9121-91e3d0238463.png">

2. 이름, 지역 설정 후 MySQL 버전을 ```8.0``` 으로 선택, Admin 이름과 비밀번호 설정

    <img width="1106" alt="image" src="https://user-images.githubusercontent.com/40768187/177834723-b3eaf691-0088-4a3a-96ae-e594ee13b280.png">

3. 모든 네트워크에서 접근할 수 있도록 체크, 허용된 IP 만 접근할 수 있도록 할 수도 있음

    <img width="1092" alt="image" src="https://user-images.githubusercontent.com/40768187/177834853-c07ccdd8-b9fd-4b02-9acd-c47be8ffb98e.png">

4. 생성 완료
   
    <img width="1664" alt="image" src="https://user-images.githubusercontent.com/40768187/177834936-dc38acda-0313-40a9-9d02-64140671f8fe.png">

#### MySQL Workbench 로 위에서 생성한 디비 접속해보기

1. MySQL Workbench 설치 후 ```MySQL Connections + ``` 선택
   
    ![image](https://user-images.githubusercontent.com/40768187/177890209-29df42e1-3d77-4274-8eba-f5010d3d1f4c.png)

2. ```Connection name``` 지정 후 ```Hostname``` Azure Database for MySQL 대시보드의 서버이름 복붙, ```username``` 과 ```비밀번호(Store in Valut)``` 작성후 테스트 연결 시도 

    ![image](https://user-images.githubusercontent.com/40768187/177890275-d67d564c-f79e-4590-a367-3afdfc739ebf.png)

    ![화면 캡처 2022-07-08 085632](https://user-images.githubusercontent.com/40768187/177890356-55e09f96-ce86-42c4-b4b3-50c40e9941d3.png)

3. 생성한 Connection 선택 후 (비밀번호 저장이 안되어 있다면 입력) 접속

    ![화면 캡처 2022-07-08 085730](https://user-images.githubusercontent.com/40768187/177890420-e06ca3d1-9164-4981-9fef-d159f1f9e91b.png)

4. 접속하면 다음과 같은 화면을 볼 수 있음. 해당 화면에서 쿼리 작성후 번개 버튼을 누르면 쿼리 실행 가능

    ![image](https://user-images.githubusercontent.com/40768187/177891024-43969218-d33a-4e28-9e0a-a4c5bfdac0bd.png)

    MySQL 튜토리얼 사이트에서 샘플 SQL 파일을 가져와 쿼리 실행 해봄</br>
    해당 사이트에서 단어 찾기로 ```Download MySQL Sample Database``` 검색하면 됨

MySQL 튜토리얼 : https://www.mysqltutorial.org/

### Azure Database for PostgreSQL

- PostgreSQL 9.5.11, 9.6.7, 10.3 지원
- 로그는 최대 7일간 보존, 1시간 또는 100MB 마다 순환
- 쿼리 로깅 및 오류 로그 설정 가능
- HA, 확장, 축소시 새로운 인스턴스를 생성 (Downtime)
- 응용프로그램의 재시도 연결 필수
- DTU 계층 없음