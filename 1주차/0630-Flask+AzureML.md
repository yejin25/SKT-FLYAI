# 1주차 2022 06 30
</br>

## 📌 Flask Serving

### Flask 에서 사용할 모델 학습 및 저장
- iris data 를 사용한 간단한 classification model을 학습한 뒤, 모델을 pickle 파일로 저장하고, flask를 사용해 해당 파일을 load 하여 predict 하는 server 구현

1) Sample code
   - 소스 코드

        ```python
        import os       # 운영체계 담당 ex) 파일 생성
        import pickle

        from sklearn.datasets import load_iris
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score, classification_report
        from sklearn.model_selection import train_test_split

        RANDOM_SEED = 1234

        # STEP 1) data load
        data = load_iris()

        # STEP 2) data split
        X = data['data']
        y = data['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_SEED)
        # test_size: 테스트에 사용할 데이터 비율 (데이터의 30을 테스트, 70을 학습하는 데에 사용)
        # RANDOM_SEED: 학습하기 전에 섞기

        # STEP 3) train model
        model = RandomForestClassifier(n_estimators=300, random_state=RANDOM_SEED)
        model.fit(X_train, y_train)     # 학습시키기
        # X = feature - 특성, 입력 변수
        # y = label - 라벨, 예측하는 항목

        # STEP 4) evaluate model
        print(f"Accuracy :  {accuracy_score(y_test, model.predict(X_test))}")
        print(classification_report(y_test, model.predict(X_test)))

        # STEP 5) save model to ./build/model.pkl
        os.makedirs("./build", exist_ok=True)
        pickle.dump(model, open('./build/model.pkl', 'wb'))     # wb = write binary
        ```
</br>

2) 모델 학습 및 저장
   - 위의 python code를 복사한 후 실행

        ```
        cd flask-tutorial

        # 파이썬 버전을 확인합니다.
        python -V

        # requirements 를 설치합니다.
        pip install scikit-learn==1.0

        # 위의 코드를 복사 후 붙여넣습니다.
        vi train.py

        # 위의 코드를 실행시킵니다.
        python train.py
        ```
    
    - 실행 후 다음과 같은 메세지 출력

        ```
        Accuracy :  0.9555555555555556
                    precision    recall  f1-score   support

                0       1.00      1.00      1.00        16
                1       0.94      0.94      0.94        17
                2       0.92      0.92      0.92        12

        accuracy                            0.96        45
        macro avg       0.95      0.95      0.95        45
        weighted avg    0.96      0.96      0.96        45
        ```
    
    - ```build``` 디렉토리 내부에 ```model.pkl``` 파일이 생성되어 있음

        ```
        cd build

        ls
        # model.pkl 파일 존재
        ```
</br>

3) Flask server 구현
   - 1 에서 학습 후 저장했던 모델(pickle 파일)을 load 하여, POST/predict API를 제공하는 Flask Server 를 구현
   - Sample code

        ```python
        import pickle

        import numpy as np     
        # 숫자를 다루기 위한 라이브러리 (배열(ndarray)에 사칙연산 가능)
        # ex) A -> 0, 1, 2, 3, 4, 5 |  A * 5 -> 배열을 하나 만들고 계산된 값 넣음. (0, 5, 10, 15, 20)
        
        from flask import Flask, jsonify, request

        # 지난 시간에 학습한 모델 파일을 불러옵니다.
        model = pickle.load(open('./build/model.pkl', 'rb'))    # rb = read binary

        # Flask Server 를 구현합니다.
        app = Flask(__name__)


        # POST /predict 라는 API 를 구현합니다.
        @app.route('/predict', methods=['POST'])
        def make_predict():
            # API Request Body 를 python dictionary object 로 변환합니다.
            # xml은 정보가 어떤건지 정확히 알 수 있지만, 용량이 너무 큼. 그래서 최근엔 json 을 많이 씀
            request_body = request.get_json(force=True)

            # request body 를 model 의 형식에 맞게 변환합니다.
            X_test = [request_body['sepal_length'], request_body['sepal_width'],
                    request_body['petal_length'], request_body['petal_width']]
            X_test = np.array(X_test)
            X_test = X_test.reshape(1, -1)      # ex) 1, 2, 3, 4, 5, 6, 7, 8 -> 1, 2, 3, 4 | 5, 6, 7, 8

            # model 의 predict 함수를 호출하여, prediction 값을 구합니다.
            y_test = model.predict(X_test)

            # prediction 값을 json 화합니다.
            response_body = jsonify(result=y_test.tolist())

            # predict 결과를 담아 API Response Body 를 return 합니다.
            return response_body


        if __name__ == '__main__':          # 생성자, 실행할 때마다 나오는 코드
            app.run(port=5000, debug=True)
        ```
    
    - 위의 파이썬 코드 작성 후 실행

        ```
        # 파이썬 버전을 확인합니다.
        python -V

        # requirements 를 설치합니다.
        pip install scikit-learn==1.0

        # 위의 코드를 복사 후 붙여넣습니다.
        vi flask_server.py
        ```
</br>

4) API 테스트
   - 위에서 구현한 Flask server를 run</br>
    ```python flask_server.py```

   - 다음과 같은 메세지 출력시 정상 동작
        ```
        FLASK_APP = flask_server.py
        FLASK_ENV = development
        FLASK_DEBUG = 0
        In folder /fast-campus-demo/flask-tutorial
        /.pyenv/versions/flask-tutorial/bin/python -m flask run
        * Serving Flask app 'flask_server.py' (lazy loading)        # Serving? ML Model을 서비스화 하는 것
        * Environment: development
        * Debug mode: off
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        ```
        ```http://127.0.0.1:5000/``` 가 flask sever의 주소 의미
        </br> +) 본인은 Azure 에서 진행했기 때문에 ```http://public IP:5000``` 가 맞음 (접속은 해보지 못했음)
    
    - 해당 Flask server 에 ```POST /predict API```를 요청하여, 어떤 결과가 반환되는지 확인
        ```
        curl -X POST -H "Content-Type:application/json" --data '{"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 5.1, "petal_width": 1.8}' http://localhost:5000/predict

        # {"result":[2]}
        # 0, 1, 2  중의 하나의 type 으로 classification 하게 됩니다.
        ```
</br>

## 📌 Azure ML

<img width="871" alt="image" src="https://user-images.githubusercontent.com/40768187/177002455-50f8192f-ea5a-45ac-92a8-4f9bd04f472f.png">

</br>

<img width="903" alt="image" src="https://user-images.githubusercontent.com/40768187/177002573-f758f21e-260a-416c-be79-d44d4591a7b4.png">
</br>
</br>

### Azure ML 생성

1. 리소스 그룹 생성
2. 생성된 리소스 그룹 선택 > ```+ 만들기```
   
   <img width="1656" alt="스크린샷 2022-07-02 오후 10 27 13" src="https://user-images.githubusercontent.com/40768187/177002871-340579a3-c610-4a29-a0a8-e0290bdfd8f6.png">

3.  ```Azure Machine Learning``` 검색 후 선택 > ```만들기``` 선택 > ```이름```, ```지역``` 선택 후 만들기 (나머지는 기본 설정)
   
    <img width="1655" alt="image" src="https://user-images.githubusercontent.com/40768187/177003007-8c9d29b8-ead2-4c7c-b6e3-2cf793ddc465.png">

4. 리소스 생성 완료 후 ```Studio 시작하기``` 클릭 후 접속
   
   <img width="1660" alt="image" src="https://user-images.githubusercontent.com/40768187/177003093-e27553fc-6e72-4921-ac2e-831fa94ab348.png">

</br>

### Azure ML Desinger 사용해보기

1. Designer 시작하기

    <img width="1656" alt="스크린샷 2022-07-02 오후 10 36 24" src="https://user-images.githubusercontent.com/40768187/177003813-6861fc77-6f24-4757-a88d-df35ef651da9.png">

2. New pipeline 에서 ```+``` 모양 선택 (```Easy-to-user prebuilt components```)
3. 원하는 component 검색 후 오른쪽으로 드래그해서 놓고, component 클릭 후 설정

    ![KakaoTalk_Photo_2022-07-04-21-04-42](https://user-images.githubusercontent.com/40768187/177152820-20134c78-7b39-4a3c-bc26-dcfeefd26031.png)

    ![KakaoTalk_Photo_2022-07-04-21-04-47](https://user-images.githubusercontent.com/40768187/177152888-c9d83224-7ab5-4a70-b888-173ba5060884.png)

    Split Rows : 열단위로 쪼개기 </br>
    Fraction of rows in the first output dataset : test 데이터, training 데이터의 비율 조절

    </br>

    ![KakaoTalk_Photo_2022-07-04-21-04-51](https://user-images.githubusercontent.com/40768187/177152962-0943d0e4-04ee-429f-9e7f-7f94aaea2a75.png)

    <img width="1660" alt="image" src="https://user-images.githubusercontent.com/40768187/177154140-a0a706e9-1e84-4038-969a-35127d122a10.png">

4. Settings 에서 compute instance 지정해주기
   
   ![KakaoTalk_Photo_2022-07-04-21-05-01](https://user-images.githubusercontent.com/40768187/177153400-872cd383-46b0-4382-91bc-a8ae76d8bbd7.png)


5. 결과 보기
   
    ![KakaoTalk_Photo_2022-07-04-21-05-24](https://user-images.githubusercontent.com/40768187/177153116-15054fff-ea75-4a5a-9239-3853b533f4a8.png)

    Enter Data Manually 의 동그라미에 오른쪽 클릭 후에 ```Preview data``` 선택 후 나오는 화면

    ![image](https://user-images.githubusercontent.com/40768187/177153260-0550da9f-63cc-48d1-994f-bd47f8dc388b.png)

    Scored_dataset 의 ```Preview data```

    <img width="1665" alt="image" src="https://user-images.githubusercontent.com/40768187/177156564-1ca315ae-9fe0-443d-b2ae-5729d027464b.png">

    Evaluation_results 의 ```Preview data```

    <img width="1671" alt="image" src="https://user-images.githubusercontent.com/40768187/177156937-37841a8d-1c69-499c-bc9d-d7aa961ecb67.png">

</br>

### Azure ML Automated ML 사용해보기

- 타이타닉 승객 명단 데이터를 이용하여 어떤 것이 생사에 영향을 미쳤는지 알아볼 예정~

1. Automated ML 시작하기
   
    <img width="1709" alt="스크린샷 2022-07-02 오후 11 52 19" src="https://user-images.githubusercontent.com/40768187/177005613-59e13b99-ebd8-4437-ade6-abadf43d6630.png">

2. ```+ New Automated ML job``` 클릭 > **Select data asset**에서 ```+ Create``` 클릭 > ```From local files``` 선택

3. 데이터 Name 작성 > ```Browse``` 클릭 후 데이터 파일 선택
   
   <img width="1710" alt="스크린샷 2022-07-03 오전 12 09 13" src="https://user-images.githubusercontent.com/40768187/177006178-b280f38c-a868-4750-9dd8-07fb6468cf4f.png">

4. **Settings and preview** 은 기본으로 두고 ```Next``` 선택
5. 데이터 중 필요한 컬럼만 포함시키기
   
   <img width="1712" alt="스크린샷 2022-07-03 오전 12 20 35 1" src="https://user-images.githubusercontent.com/40768187/177006538-40d16fbb-b1af-467b-9834-1fa68ffb9780.png">

   ```Servived```, ```Pclass```, ```Sex```, ```Age``` 만 포함시켰음

   </br>


6. 다시 **Select data asset** 에서 방금 만든 데이터 이름을 검색하고, 선택해준 뒤 ```Next```
7. **New experiment name** 작성해주고, **Target column** 을 선택, **compute type** -> ```instance``` 선택, 없으면 instance 생성
   
   <img width="1653" alt="스크린샷 2022-07-03 오전 1 05 55" src="https://user-images.githubusercontent.com/40768187/177007963-fa28e011-ff94-4fde-adea-dd6401ffb2a0.png">

   Target column 은 예측하고 싶은 컬럼 선택, ```Survived``` 선택

   <img width="1674" alt="스크린샷 2022-07-03 오전 12 48 32" src="https://user-images.githubusercontent.com/40768187/177007822-f69971bb-dca9-49e6-927e-0387aabf4148.png">

   instance 없으면 ```create``` 눌러서 생성하기

   </br>

8. **Classification** 선택된거 그대로 두고 ```Next``` 클릭, 그 이후의 옵션도 기본으로 두고 ```Finish``` 클릭

9. Not Started -> Running -> Completed 순으로 진행되는 것을 볼 수 있음
    
    <img width="903" alt="image" src="https://user-images.githubusercontent.com/40768187/177008694-cecac7c7-df15-406b-8105-56f94bca381b.png">

    <img width="919" alt="image" src="https://user-images.githubusercontent.com/40768187/177009846-595440df-ef36-42af-acbd-3e15e432c3ac.png">

10. 결과 살펴보기

    <img width="1676" alt="스크린샷 2022-07-03 오전 2 09 05" src="https://user-images.githubusercontent.com/40768187/177009907-dd90f892-87a7-4a83-8283-71e0562b23bc.png">

    ```Experiment``` 선택 시 다음과 같은 화면을 볼 수 있음

    <img width="1672" alt="image" src="https://user-images.githubusercontent.com/40768187/177009985-bd6d205b-56e2-4582-baf4-b42fe2d60f76.png">
    
    ~~머신러닝에 대해 공부하지 않은 상태라 해석까지는 힘듬~~