# 2주차 2022 07 04
</br>

## 📌 Cloud

### 클라우드컴퓨팅 이점

- 고가용성s
- 확장성: 리소스 확장을 위해 구매 필요
- 탄력성: 상황에 따라 리소스 사용
- 민첩성
- 내결함성
- 재해복구
- 글로벌 서비스
- 보안성
- 예산 운용성
- 기술 요구사항

### 규모의 경제

IT 인프라 운영 시 작은 규모로 운영하는 것보다 더 큰 규모로 운영할 때 더 저렴하고 효율적으로 운영 가능

### CapEX vs. OpEx

- 자본 지출 (Capital Expenditure, CapEx)
  - 물리적 인프라 구매하여 사용
  - 서버 구매 후 서비스 운용
  - 높은 초기 비용, 투자의 가치는 시간이 지남에 따라 줄어듬 (소모품)

- 운영 지출 (Operational Expenditure, OpEx)
  - 필요에 따라 서비스나 제품을 구독
  - 서비스에 필요한 제품 즉시 구매
  - 선결제 비용 없음, 사용량에 따라 지불

### 소비기반 모델 (종량제)

-  선결제 비용 없음
-  고가의 인프라를 구매하고 관리할 필요 없음
-  필요에 따라 리소스를 추가 지불하고 사용가능 
-  더 이상 필요하지 않은 리소스에 대한 사용 중지 가능
-  사용한 만큼 결제

### 클라우드 서비스 모델

- 공용 클라우드: 특정되지 않은 사용자에게 리소스와 서비스를 제공
- 사설 클라우드: 클라우드 리소스를 조직에서 소유하고 관리/운영
- 하이브리드 클라우드
  - 공용 클라우드 + 사설 클라우드
  - 무거움이 단점
  - private 만 평상시 사용
  - 특정 시간에만 (트래픽 늘어날 때) public 연결하여 사용 ex) VPN, 전용선

### 클라우드 서비스 유형

<img width="885" alt="image" src="https://user-images.githubusercontent.com/40768187/177332376-b74f37d1-1541-4282-954b-2ae89d4deac0.png">

- IaaS
  - 물리 보안에 대한 모든 책임 = 클라우드 제공자
  - 셀프 서비스 포털을 통해 프로비저닝과 관리할 수 있는 컴퓨터 제공
    - 프로비저닝?</br>
        사용자의 요구에 맞게 시스템 자원을 할당, 배치, 배포해 두었다가 필요 시 시스템을 즉시 사용할 수 잇는 상태로 미리 준비해두는 것

- PaaS
  - 소프트웨어 응용프로그램을 구축, 테스트 배포하기 위한 환경 제공
  - 사용자는 운영 체제, 플랫폼 관리 및 업데이트를 신경 쓰지 안고 제품에 좀 더 집중 가능

- SaaS
  - 클라우드 제공자가 응용프로그램을 제공, 관리
  - 사용자는 구독 모델로 사용하는 응용프로그램에 대한 비용 지불
  - ex) Netflix

</br>

## 📌 Azure

~~중국, 독일은 허용된 사람만 서비스 이용 가능~~

 <img width="185" alt="image" src="https://user-images.githubusercontent.com/40768187/177336152-b4cc9507-3f70-4009-a80d-f4a97ed792cc.png">

### 지역 (Region)

- 최상의 성능과 보안을 제공하기 위해 고속 네트워크를 통해 연결된 데이터 센터의 집합
- region 간 간격 규정 -> 30 km ?
- 전 세계적으로 66개 지역, 140개 국가에서 사용 가능

### 지역 쌍

<img width="451" alt="image" src="https://user-images.githubusercontent.com/40768187/177336955-20dfa059-c155-453d-a21c-afce7b97332b.png">

ex) Korea Central, South korea

### Azure 의 가용성

<img width="590" alt="image" src="https://user-images.githubusercontent.com/40768187/177339195-d002a1cc-b8f2-4882-b9d5-ac777f71e3f8.png">

### Azure 데이터 센터

- 독립적인 전원, 냉각 장치, 네트워크 갖춘 별도 시설

### 가용성 세트

<img width="424" alt="image" src="https://user-images.githubusercontent.com/40768187/177340220-4916b709-669d-4661-90ae-895289c6c625.png">

- Fault Domain
  - 장애 도메인으로 전원, 네트워크, 상면, 항온항습기가 격리된 곳에 가상 컴퓨터를 Microsoft 배포
  
- Update Domain
  - 업데이트 도메인은 동시에 재부팅 할 수 있는 가상 머신의 기본 물리적 하드웨어 그룹을 나타내며 물리적 재부팅이 발생하는 경우 하나의 업데이트 도메인만 재부팅

### 가용성 영역

-  Azure 내에 고유한 물리적 위치 지정
-  고가용성 디자인은 사용자가 직접 수행
-  가상머신, 관리디스크 등을 특정 영역에 종속

    <img width="406" alt="image" src="https://user-images.githubusercontent.com/40768187/177341417-2c4d13a4-c1f2-4cb4-8556-0b1ce738e702.png">

### Azure Resource Manager

<img width="881" alt="image" src="https://user-images.githubusercontent.com/40768187/177341960-bde11dcd-ecdd-4f8c-add6-4f66ecd06122.png">

### 용어 정리

- 리소스: 가상 머신, 데이터베이스, 가상 네트워크 등 단일 리소스를 나타내는 단위
- 리소스 그룹: 리소스를 묶을 수 있는 단위
- 리소스 공급자: 원하는 리소스를 제공하는 서비스    ex) 가상머신의 경우 공급자는 Microsoft.Compute
- 리소스 제공자: 리소스를 제공하는 주체 ex) Microsoft, Cisco, Fotinet

### 실습 진행

1. 계정 만들기 -  Azure for student 구독 계정으로 시작
2. 리소스 그룹 만들기
3. 리소스 만들기 - 공용 IP 주소 생성

    ```+만들기``` 클릭후 Public IP address 검색 후 생성

    <img width="253" alt="image" src="https://user-images.githubusercontent.com/40768187/177342865-cd7e182d-c1bc-4bfb-8f36-950e565a797f.png">

4. 포털 사용법
5. Azure PowerShell

    <img width="1669" alt="image" src="https://user-images.githubusercontent.com/40768187/177343875-16ca23fc-e71f-4e43-aa26-bc8911f99cb8.png">

    </br>

    ```python
    az --help

    az account list

    az group create --location westus --name MyRG
     
    az vm create -n myVM -g MyRG --location koreacentral --image UbuntuLTS --generate-ssh-keys
    ```

    <img width="1677" alt="image" src="https://user-images.githubusercontent.com/40768187/177345792-7ba36adb-ebfb-48ae-963e-505b7db051c5.png">

    </br>

    <img width="1501" alt="image" src="https://user-images.githubusercontent.com/40768187/177346078-cd589824-e2a1-4823-9de2-943e543b9b4e.png">

    ```MyRG``` 라는 리소스 그룹이 생성된 것을 확인할 수 있음

    <img width="1350" alt="image" src="https://user-images.githubusercontent.com/40768187/177346207-0efd32e5-04c8-459b-adcf-3162b51d33a5.png">

     ```MyRG``` 라는 리소스 그룹에 들어가보면, VM 이 생성된 것을 확인할 수 있음

</br>

#### 리소스와 리소스 그룹 관리

<img width="555" alt="image" src="https://user-images.githubusercontent.com/40768187/177349656-4de3968c-fa27-4f9b-8521-5912dc7a04d6.png">

### 리소스와 태그

- 논리적으로 분류 체계를 구성하는 방법
- 리소스를 보다 정교하게 필터링하고 사용량 보고서 생성 가능
- 태그 이름/값의 쌍은 최대 50개 까지 부여 가능
- 특수문자 포함X

### 리소스 이동

<img width="486" alt="image" src="https://user-images.githubusercontent.com/40768187/177351583-d9d2324f-25f4-4eef-af81-0fda40cb92f3.png">

- 구독 간 이동은 양쪽 구독이 동일한 Azure Active Directory 에 연결된 경우만 가능
- 리소스 이동 작업 중에는 원본 그룹과 대상 그룹은 모드 잠금
- 리소스와 종속성이 있는 리소스가 있으면 함께 이동
- 다른 구독으로 이동하려는 경우 종속성 있는 리소스가 각기 다른 리소스 그룹에 흩어져 있을 경우 먼저 하나의 리소스 그룹으로 모은 후 이동 가능
- Azure Active Directory, ExpressRoute 는 이동 하지 못함

### Azure Active Directory?

<img width="500" alt="image" src="https://user-images.githubusercontent.com/40768187/177350751-ac0b4600-1ff3-41d1-9942-7039e370136e.png"> <img width="292" alt="image" src="https://user-images.githubusercontent.com/40768187/177350666-92f37612-a0cc-43cd-b46f-ec753528b276.png">

사용자의 로그인과 클라우드 서비스 권한 부여 등을 담당, 사용자 계정 통합 관리 서비스

<img width="425" alt="image" src="https://user-images.githubusercontent.com/40768187/177350898-e4d729af-e4ea-4fb1-9453-c22b3f451d97.png"> <img width="463" alt="image" src="https://user-images.githubusercontent.com/40768187/177350847-107bc07d-0ddd-42ac-9960-e1614cfea174.png">


### 리소스와 리소스 그룹 보호

- 리소스는 쉽게 제거 가능
- 읽기 전용 잠금과 삭제 잠금 두가지가 제공s

잠금할 리소스 그룹에 들어간 뒤 ```Lock``` > ```+ Add``` > ```Lock name``` 작성, ```Lock type``` 을 선택

<img width="1021" alt="image" src="https://user-images.githubusercontent.com/40768187/177351932-257f9521-9619-40e6-9a06-2986d81837c9.png">

</br>

잠금 설정된 리소스 그룹 삭제 시도 시, 다음과 같은 알림이 오면서 삭제 실패

<img width="522" alt="image" src="https://user-images.githubusercontent.com/40768187/177352052-60bfe2b9-b34f-4135-957f-82025ca2fe8b.png">

### 리소스와 리소스 그룹 삭제하기

- 리소스를 개별적으로 삭제 가능
- 리소스 그룹을 삭제하면 한번에 리소스들을 삭제 가능

</br>

## 📌 인증과 권한

- 인증: User 또는 Service 계정 식별, 액세스 제어 규칙을 만들기 위한 기초
- 권한: 인증된 User 또는 Service 의 액세스 수준 정의, 액세스 할 수 있는 리소스와 함께 수행할 수 있는 작업 정의

### Azure AD (Azure Active Directory)
</br>


<img width="515" alt="image" src="https://user-images.githubusercontent.com/40768187/177441407-6eca48eb-2712-4040-a173-154aafefe3ee.png">

</br>

- 다중 테넌트 클라우드 기반 디렉터리 및 ID 관리
- 클라우드 애플리케이션 및리소스용 Single Sign-On 액세스 기능 제공
- 전역 범위에서 원활하게 앱 개발
- 전체 ID 관리 기능 제공
  - 셀프 서비스 암호 및 그룹 관리
  - 권한 있는 계정 관리
  - 역할기반 액세스 제어
  - 앱 사용량 모니터링
  - 보안 모니터링 
  - 디바이스 등록
  - 경고
  - MFA (Multi-Factor Authentication)

#### 개념

- ID: 인증할 수 있는 개체
- 계정: 연결된 데이터가 있는 ID
- Azure AD 계정: Azure AD 또는 기타 Microsoft 클라우드 서비스를 통해 만든 ID
- Azure AD 테넌트/디렉터리
  - 테넌트는 조직에서 Microsoft 클라우드 서비스 구독에 가입할 때 자동으로 만들어지는 Azure AD의 신뢰할 수 있는 전용 인스턴스
  - Azure AD의 추가 인스턴스를 만들 수 있음
  - Azure AD는 ID 서비스를 제공하는 기본 제품
  - 테넌트라는 용어는 단일 조직을 나타내는 Azure AD의 단일 인스턴스 의미
  - 테넌트와 디렉터리는 종종 서로 교환해서 사용되는 용어
- Azure 구독: Azure Cloud Service 비용 지불하는 데 사용

#### Azure AD 버전

</br>
<img width="905" alt="image" src="https://user-images.githubusercontent.com/40768187/177441571-210633bb-bd3e-4e3d-8cc8-7a3274e5d42a.png">

</br>

보통 Premium P1 정도까지만 사용함

### 기본 디렉터리

- 모든 계정은 기본적으로 기본 디렉터리로 로그인
- 별도로 도메인을 등록하지 않으면 ```onmicrosoft.com``` 이라는 하위 도메인과 Azure 에가입할 때 사용한 메일 별칭 그리고 최상위 도메인으로 조합된 이름 사용함
- ex) yejin@outlook.com -> yejin@yejinoutlook.onmicrosoft.com

### 기본 디렉터리외 추가 티렉터리

- 개발이나 테스트를 위한 Azure AD 필요
- 시스템에 따라 인증을 분리하고자 하는 경우

새로운 테넌트 (디렉터리) 추가해보기

1. ```Azure Active Directory``` 검색 후 들어가서 ```Manage tenants``` 선택

    <img width="1355" alt="image" src="https://user-images.githubusercontent.com/40768187/177523870-da2b3087-6400-4cc9-83a4-41d55aff3cc5.png">

2. tenant Type 은 기본으로 두고, 조직 이름과 도메인명, 지역 선택
   
   <img width="893" alt="image" src="https://user-images.githubusercontent.com/40768187/177524033-45471551-8e45-4e02-8e8c-ed0f19ff2ac1.png">

3. 로봇이 아님을 인증하고 만들기
   
   <img width="1538" alt="image" src="https://user-images.githubusercontent.com/40768187/177524182-23127e10-03c1-4bf5-9e8e-225548143377.png">

4. 생성 완료

    <img width="1303" alt="image" src="https://user-images.githubusercontent.com/40768187/177525430-db59ada4-ad1f-4387-baf7-3ab6f972c17c.png">

    테넌트를 생성한 계정이 전역 관리자가 된 것을 확인 할 수 있음
    </br> 테넌트 전환은 ```테넌트 관리``` > 전환할 테넌트 선택 > ```전환``` 선택

### 구독

</br>

<img width="400" alt="image" src="https://user-images.githubusercontent.com/40768187/177449136-996054a7-6548-46f9-9094-35e3a3316f83.png"><img width="400" alt="image" src="https://user-images.githubusercontent.com/40768187/177447243-184b7966-a845-4293-bf3e-cc73848309d3.png">

Azure 구독은 Azure 계정에 대한 액세스를 인증하고 이러한 액세스에 필요한 권한 부여

- 청구 경계: 각구독에 해당하는 개별 청구 보고서와 청구서 생성
- 액세스 제어 경계: 사용자가 특정 구독으로 프로비전할 수 있는 리소스 액세스를 관리/제어

+) 구독은 옮기기도 가능

<img width="400" alt="스크린샷 2022-07-06 오후 6 40 13" src="https://user-images.githubusercontent.com/40768187/177521164-ad34832e-e997-4307-9709-4e4f42eb0f3d.png">


### 사용자 계정

<img width="852" alt="image" src="https://user-images.githubusercontent.com/40768187/177526663-e51e0dcd-6270-402c-8013-45af78121403.png">

- 모든 사용자는 계정을 소유해야 함
- 직접 생성 또는 Azure AD 계정을 게스트로 초대 가능
- Windows AD 와 통합 가능
- 클라우드 ID: 클라우드 상에서만 존재하는 아이디로 테넌트에 추가
- 게스트 사용자: 외부의 다른 클라우드 공급자에게 제공된 경우로 구글이나 페이스북 그리고 마소에서 제공한 아이디
- 하이브리드 ID: Windows Server 의 ADDS (Active Directory Domain Service) 와 Azure AD를 동기화 시켜 생성한 사용자 계정

</br>

사용자 계정 추가하기

- ```+ 새 사용자``` 선택 후 다음과 같은 화면에서 각 항목을 작성해주면 만들 수 있음</br>
- 사용자 초대도 해당 사용자의 메일 주소를 작성하면 가능함

    <img width="1052" alt="스크린샷 2022-07-06 오후 7 09 18" src="https://user-images.githubusercontent.com/40768187/177527221-cc3531c5-cdec-4b1f-90d7-4f217cb68f2e.png">

</br>

### 그룹 관리

<img width="854" alt="image" src="https://user-images.githubusercontent.com/40768187/177527483-fc5e8f08-5dfb-4edb-9d3f-27bbf445ebae.png">

- 사용자 계정을 그룹으로 묶어 관리 가능
- Microsoft 365 그룹과 보안 그룹으로 나뉨
- 구성원 유형은 할당됨, 동적 사용자, 동적 디바이스로 구분

### Azure AD 권한 관리

<img width="804" alt="image" src="https://user-images.githubusercontent.com/40768187/177528392-52054692-d996-47f8-a779-c45dd32e0158.png">

- 기여자, 소유자, 독자(판독기) 를 가장 많이 사용
- Azure AD를 관리할 수 있는 권한
- 사용자 계정에게 Azure AD 를 조작할 수 있는 권한 부여
- 이 권한으로 Azure 리소스를 조작은 불가능
- 계정 생성, 비밀번호 초기화 등을 구성 가능

### Azure 권한 구성

<img width="817" alt="image" src="https://user-images.githubusercontent.com/40768187/177453168-b0cc0b4b-96ef-4055-b699-8e955ef66066.png">

### 역할 기반 액세서 제어 (RBAC)

- Role Based Access Control
- 액세스 할 수 있는 영역과 Azure 리소스, 리소스 그룹 단위로 액세스 제어 가능
- 사전에 정의 된 RBAC 의 역할 제공
- 소유자: 모든 권한을 가지고 있으며 다른 사용자 계정에 액세스 권한 할당 가능
- 기여자: 할당된 사용 권한 내에서 완전히 관리 가능하지만 다른 사용자 계정에 엑세스 권한 할당X
- 독자: 모든 Azure 리소스를 확인할 수 있는 권한만 존재

+) 추가 메모</br>

DDos Protection
-  디도스 공격으로부터 보호, 정상적인 접근을 위장한 디도스도 존재
-  7계층 HTTP, 4계층 tcp로 접속할 수 있음
-  WAF DDos 라는 장비로 보호
-  Standard 는 디도스 공격 보고서를 사람이 작성하여 보고해줌