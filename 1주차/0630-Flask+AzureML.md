# 1์ฃผ์ฐจ 2022 06 30
</br>

## ๐ Flask Serving

### Flask ์์ ์ฌ์ฉํ  ๋ชจ๋ธ ํ์ต ๋ฐ ์ ์ฅ
- iris data ๋ฅผ ์ฌ์ฉํ ๊ฐ๋จํ classification model์ ํ์ตํ ๋ค, ๋ชจ๋ธ์ pickle ํ์ผ๋ก ์ ์ฅํ๊ณ , flask๋ฅผ ์ฌ์ฉํด ํด๋น ํ์ผ์ load ํ์ฌ predict ํ๋ server ๊ตฌํ

1) Sample code
   - ์์ค ์ฝ๋

        ```python
        import os       # ์ด์์ฒด๊ณ ๋ด๋น ex) ํ์ผ ์์ฑ
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
        # test_size: ํ์คํธ์ ์ฌ์ฉํ  ๋ฐ์ดํฐ ๋น์จ (๋ฐ์ดํฐ์ 30์ ํ์คํธ, 70์ ํ์ตํ๋ ๋ฐ์ ์ฌ์ฉ)
        # RANDOM_SEED: ํ์ตํ๊ธฐ ์ ์ ์๊ธฐ

        # STEP 3) train model
        model = RandomForestClassifier(n_estimators=300, random_state=RANDOM_SEED)
        model.fit(X_train, y_train)     # ํ์ต์ํค๊ธฐ
        # X = feature - ํน์ฑ, ์๋ ฅ ๋ณ์
        # y = label - ๋ผ๋ฒจ, ์์ธกํ๋ ํญ๋ชฉ

        # STEP 4) evaluate model
        print(f"Accuracy :  {accuracy_score(y_test, model.predict(X_test))}")
        print(classification_report(y_test, model.predict(X_test)))

        # STEP 5) save model to ./build/model.pkl
        os.makedirs("./build", exist_ok=True)
        pickle.dump(model, open('./build/model.pkl', 'wb'))     # wb = write binary
        ```
</br>

2) ๋ชจ๋ธ ํ์ต ๋ฐ ์ ์ฅ
   - ์์ python code๋ฅผ ๋ณต์ฌํ ํ ์คํ

        ```
        cd flask-tutorial

        # ํ์ด์ฌ ๋ฒ์ ์ ํ์ธํฉ๋๋ค.
        python -V

        # requirements ๋ฅผ ์ค์นํฉ๋๋ค.
        pip install scikit-learn==1.0

        # ์์ ์ฝ๋๋ฅผ ๋ณต์ฌ ํ ๋ถ์ฌ๋ฃ์ต๋๋ค.
        vi train.py

        # ์์ ์ฝ๋๋ฅผ ์คํ์ํต๋๋ค.
        python train.py
        ```
    
    - ์คํ ํ ๋ค์๊ณผ ๊ฐ์ ๋ฉ์ธ์ง ์ถ๋ ฅ

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
    
    - ```build``` ๋๋ ํ ๋ฆฌ ๋ด๋ถ์ ```model.pkl``` ํ์ผ์ด ์์ฑ๋์ด ์์

        ```
        cd build

        ls
        # model.pkl ํ์ผ ์กด์ฌ
        ```
</br>

3) Flask server ๊ตฌํ
   - 1 ์์ ํ์ต ํ ์ ์ฅํ๋ ๋ชจ๋ธ(pickle ํ์ผ)์ load ํ์ฌ, POST/predict API๋ฅผ ์ ๊ณตํ๋ Flask Server ๋ฅผ ๊ตฌํ
   - Sample code

        ```python
        import pickle

        import numpy as np     
        # ์ซ์๋ฅผ ๋ค๋ฃจ๊ธฐ ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ (๋ฐฐ์ด(ndarray)์ ์ฌ์น์ฐ์ฐ ๊ฐ๋ฅ)
        # ex) A -> 0, 1, 2, 3, 4, 5 |  A * 5 -> ๋ฐฐ์ด์ ํ๋ ๋ง๋ค๊ณ  ๊ณ์ฐ๋ ๊ฐ ๋ฃ์. (0, 5, 10, 15, 20)
        
        from flask import Flask, jsonify, request

        # ์ง๋ ์๊ฐ์ ํ์ตํ ๋ชจ๋ธ ํ์ผ์ ๋ถ๋ฌ์ต๋๋ค.
        model = pickle.load(open('./build/model.pkl', 'rb'))    # rb = read binary

        # Flask Server ๋ฅผ ๊ตฌํํฉ๋๋ค.
        app = Flask(__name__)


        # POST /predict ๋ผ๋ API ๋ฅผ ๊ตฌํํฉ๋๋ค.
        @app.route('/predict', methods=['POST'])
        def make_predict():
            # API Request Body ๋ฅผ python dictionary object ๋ก ๋ณํํฉ๋๋ค.
            # xml์ ์ ๋ณด๊ฐ ์ด๋ค๊ฑด์ง ์ ํํ ์ ์ ์์ง๋ง, ์ฉ๋์ด ๋๋ฌด ํผ. ๊ทธ๋์ ์ต๊ทผ์ json ์ ๋ง์ด ์
            request_body = request.get_json(force=True)

            # request body ๋ฅผ model ์ ํ์์ ๋ง๊ฒ ๋ณํํฉ๋๋ค.
            X_test = [request_body['sepal_length'], request_body['sepal_width'],
                    request_body['petal_length'], request_body['petal_width']]
            X_test = np.array(X_test)
            X_test = X_test.reshape(1, -1)      # ex) 1, 2, 3, 4, 5, 6, 7, 8 -> 1, 2, 3, 4 | 5, 6, 7, 8

            # model ์ predict ํจ์๋ฅผ ํธ์ถํ์ฌ, prediction ๊ฐ์ ๊ตฌํฉ๋๋ค.
            y_test = model.predict(X_test)

            # prediction ๊ฐ์ json ํํฉ๋๋ค.
            response_body = jsonify(result=y_test.tolist())

            # predict ๊ฒฐ๊ณผ๋ฅผ ๋ด์ API Response Body ๋ฅผ return ํฉ๋๋ค.
            return response_body


        if __name__ == '__main__':          # ์์ฑ์, ์คํํ  ๋๋ง๋ค ๋์ค๋ ์ฝ๋
            app.run(port=5000, debug=True)
        ```
    
    - ์์ ํ์ด์ฌ ์ฝ๋ ์์ฑ ํ ์คํ

        ```
        # ํ์ด์ฌ ๋ฒ์ ์ ํ์ธํฉ๋๋ค.
        python -V

        # requirements ๋ฅผ ์ค์นํฉ๋๋ค.
        pip install scikit-learn==1.0

        # ์์ ์ฝ๋๋ฅผ ๋ณต์ฌ ํ ๋ถ์ฌ๋ฃ์ต๋๋ค.
        vi flask_server.py
        ```
</br>

4) API ํ์คํธ
   - ์์์ ๊ตฌํํ Flask server๋ฅผ run</br>
    ```python flask_server.py```

   - ๋ค์๊ณผ ๊ฐ์ ๋ฉ์ธ์ง ์ถ๋ ฅ์ ์ ์ ๋์
        ```
        FLASK_APP = flask_server.py
        FLASK_ENV = development
        FLASK_DEBUG = 0
        In folder /fast-campus-demo/flask-tutorial
        /.pyenv/versions/flask-tutorial/bin/python -m flask run
        * Serving Flask app 'flask_server.py' (lazy loading)        # Serving? ML Model์ ์๋น์คํ ํ๋ ๊ฒ
        * Environment: development
        * Debug mode: off
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        ```
        ```http://127.0.0.1:5000/``` ๊ฐ flask sever์ ์ฃผ์ ์๋ฏธ
        </br> +) ๋ณธ์ธ์ Azure ์์ ์งํํ๊ธฐ ๋๋ฌธ์ ```http://public IP:5000``` ๊ฐ ๋ง์ (์ ์์ ํด๋ณด์ง ๋ชปํ์)
    
    - ํด๋น Flask server ์ ```POST /predict API```๋ฅผ ์์ฒญํ์ฌ, ์ด๋ค ๊ฒฐ๊ณผ๊ฐ ๋ฐํ๋๋์ง ํ์ธ
        ```
        curl -X POST -H "Content-Type:application/json" --data '{"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 5.1, "petal_width": 1.8}' http://localhost:5000/predict

        # {"result":[2]}
        # 0, 1, 2  ์ค์ ํ๋์ type ์ผ๋ก classification ํ๊ฒ ๋ฉ๋๋ค.
        ```
</br>

## ๐ Azure ML

<img width="871" alt="image" src="https://user-images.githubusercontent.com/40768187/177002455-50f8192f-ea5a-45ac-92a8-4f9bd04f472f.png">

</br>

<img width="903" alt="image" src="https://user-images.githubusercontent.com/40768187/177002573-f758f21e-260a-416c-be79-d44d4591a7b4.png">
</br>
</br>

### Azure ML ์์ฑ

1. ๋ฆฌ์์ค ๊ทธ๋ฃน ์์ฑ
2. ์์ฑ๋ ๋ฆฌ์์ค ๊ทธ๋ฃน ์ ํ > ```+ ๋ง๋ค๊ธฐ```
   
   <img width="1656" alt="แแณแแณแแตแซแแฃแบ 2022-07-02 แแฉแแฎ 10 27 13" src="https://user-images.githubusercontent.com/40768187/177002871-340579a3-c610-4a29-a0a8-e0290bdfd8f6.png">

3.  ```Azure Machine Learning``` ๊ฒ์ ํ ์ ํ > ```๋ง๋ค๊ธฐ``` ์ ํ > ```์ด๋ฆ```, ```์ง์ญ``` ์ ํ ํ ๋ง๋ค๊ธฐ (๋๋จธ์ง๋ ๊ธฐ๋ณธ ์ค์ )
   
    <img width="1655" alt="image" src="https://user-images.githubusercontent.com/40768187/177003007-8c9d29b8-ead2-4c7c-b6e3-2cf793ddc465.png">

4. ๋ฆฌ์์ค ์์ฑ ์๋ฃ ํ ```Studio ์์ํ๊ธฐ``` ํด๋ฆญ ํ ์ ์
   
   <img width="1660" alt="image" src="https://user-images.githubusercontent.com/40768187/177003093-e27553fc-6e72-4921-ac2e-831fa94ab348.png">

</br>

### Azure ML Desinger ์ฌ์ฉํด๋ณด๊ธฐ

1. Designer ์์ํ๊ธฐ

    <img width="1656" alt="แแณแแณแแตแซแแฃแบ 2022-07-02 แแฉแแฎ 10 36 24" src="https://user-images.githubusercontent.com/40768187/177003813-6861fc77-6f24-4757-a88d-df35ef651da9.png">

2. New pipeline ์์ ```+``` ๋ชจ์ ์ ํ (```Easy-to-user prebuilt components```)
3. ์ํ๋ component ๊ฒ์ ํ ์ค๋ฅธ์ชฝ์ผ๋ก ๋๋๊ทธํด์ ๋๊ณ , component ํด๋ฆญ ํ ์ค์ 

    ![KakaoTalk_Photo_2022-07-04-21-04-42](https://user-images.githubusercontent.com/40768187/177152820-20134c78-7b39-4a3c-bc26-dcfeefd26031.png)

    ![KakaoTalk_Photo_2022-07-04-21-04-47](https://user-images.githubusercontent.com/40768187/177152888-c9d83224-7ab5-4a70-b888-173ba5060884.png)

    Split Rows : ์ด๋จ์๋ก ์ชผ๊ฐ๊ธฐ </br>
    Fraction of rows in the first output dataset : test ๋ฐ์ดํฐ, training ๋ฐ์ดํฐ์ ๋น์จ ์กฐ์ 

    </br>

    ![KakaoTalk_Photo_2022-07-04-21-04-51](https://user-images.githubusercontent.com/40768187/177152962-0943d0e4-04ee-429f-9e7f-7f94aaea2a75.png)

    <img width="1660" alt="image" src="https://user-images.githubusercontent.com/40768187/177154140-a0a706e9-1e84-4038-969a-35127d122a10.png">

4. Settings ์์ compute instance ์ง์ ํด์ฃผ๊ธฐ
   
   ![KakaoTalk_Photo_2022-07-04-21-05-01](https://user-images.githubusercontent.com/40768187/177153400-872cd383-46b0-4382-91bc-a8ae76d8bbd7.png)


5. ๊ฒฐ๊ณผ ๋ณด๊ธฐ
   
    ![KakaoTalk_Photo_2022-07-04-21-05-24](https://user-images.githubusercontent.com/40768187/177153116-15054fff-ea75-4a5a-9239-3853b533f4a8.png)

    Enter Data Manually ์ ๋๊ทธ๋ผ๋ฏธ์ ์ค๋ฅธ์ชฝ ํด๋ฆญ ํ์ ```Preview data``` ์ ํ ํ ๋์ค๋ ํ๋ฉด

    ![image](https://user-images.githubusercontent.com/40768187/177153260-0550da9f-63cc-48d1-994f-bd47f8dc388b.png)

    Scored_dataset ์ ```Preview data```

    <img width="1665" alt="image" src="https://user-images.githubusercontent.com/40768187/177156564-1ca315ae-9fe0-443d-b2ae-5729d027464b.png">

    Evaluation_results ์ ```Preview data```

    <img width="1671" alt="image" src="https://user-images.githubusercontent.com/40768187/177156937-37841a8d-1c69-499c-bc9d-d7aa961ecb67.png">

</br>

### Azure ML Automated ML ์ฌ์ฉํด๋ณด๊ธฐ

- ํ์ดํ๋ ์น๊ฐ ๋ช๋จ ๋ฐ์ดํฐ๋ฅผ ์ด์ฉํ์ฌ ์ด๋ค ๊ฒ์ด ์์ฌ์ ์ํฅ์ ๋ฏธ์ณค๋์ง ์์๋ณผ ์์ ~

1. Automated ML ์์ํ๊ธฐ
   
    <img width="1709" alt="แแณแแณแแตแซแแฃแบ 2022-07-02 แแฉแแฎ 11 52 19" src="https://user-images.githubusercontent.com/40768187/177005613-59e13b99-ebd8-4437-ade6-abadf43d6630.png">

2. ```+ New Automated ML job``` ํด๋ฆญ > **Select data asset**์์ ```+ Create``` ํด๋ฆญ > ```From local files``` ์ ํ

3. ๋ฐ์ดํฐ Name ์์ฑ > ```Browse``` ํด๋ฆญ ํ ๋ฐ์ดํฐ ํ์ผ ์ ํ
   
   <img width="1710" alt="แแณแแณแแตแซแแฃแบ 2022-07-03 แแฉแแฅแซ 12 09 13" src="https://user-images.githubusercontent.com/40768187/177006178-b280f38c-a868-4750-9dd8-07fb6468cf4f.png">

4. **Settings and preview** ์ ๊ธฐ๋ณธ์ผ๋ก ๋๊ณ  ```Next``` ์ ํ
5. ๋ฐ์ดํฐ ์ค ํ์ํ ์ปฌ๋ผ๋ง ํฌํจ์ํค๊ธฐ
   
   <img width="1712" alt="แแณแแณแแตแซแแฃแบ 2022-07-03 แแฉแแฅแซ 12 20 35 1" src="https://user-images.githubusercontent.com/40768187/177006538-40d16fbb-b1af-467b-9834-1fa68ffb9780.png">

   ```Servived```, ```Pclass```, ```Sex```, ```Age``` ๋ง ํฌํจ์์ผฐ์

   </br>


6. ๋ค์ **Select data asset** ์์ ๋ฐฉ๊ธ ๋ง๋  ๋ฐ์ดํฐ ์ด๋ฆ์ ๊ฒ์ํ๊ณ , ์ ํํด์ค ๋ค ```Next```
7. **New experiment name** ์์ฑํด์ฃผ๊ณ , **Target column** ์ ์ ํ, **compute type** -> ```instance``` ์ ํ, ์์ผ๋ฉด instance ์์ฑ
   
   <img width="1653" alt="แแณแแณแแตแซแแฃแบ 2022-07-03 แแฉแแฅแซ 1 05 55" src="https://user-images.githubusercontent.com/40768187/177007963-fa28e011-ff94-4fde-adea-dd6401ffb2a0.png">

   Target column ์ ์์ธกํ๊ณ  ์ถ์ ์ปฌ๋ผ ์ ํ, ```Survived``` ์ ํ

   <img width="1674" alt="แแณแแณแแตแซแแฃแบ 2022-07-03 แแฉแแฅแซ 12 48 32" src="https://user-images.githubusercontent.com/40768187/177007822-f69971bb-dca9-49e6-927e-0387aabf4148.png">

   instance ์์ผ๋ฉด ```create``` ๋๋ฌ์ ์์ฑํ๊ธฐ

   </br>

8. **Classification** ์ ํ๋๊ฑฐ ๊ทธ๋๋ก ๋๊ณ  ```Next``` ํด๋ฆญ, ๊ทธ ์ดํ์ ์ต์๋ ๊ธฐ๋ณธ์ผ๋ก ๋๊ณ  ```Finish``` ํด๋ฆญ

9. Not Started -> Running -> Completed ์์ผ๋ก ์งํ๋๋ ๊ฒ์ ๋ณผ ์ ์์
    
    <img width="903" alt="image" src="https://user-images.githubusercontent.com/40768187/177008694-cecac7c7-df15-406b-8105-56f94bca381b.png">

    <img width="919" alt="image" src="https://user-images.githubusercontent.com/40768187/177009846-595440df-ef36-42af-acbd-3e15e432c3ac.png">

10. ๊ฒฐ๊ณผ ์ดํด๋ณด๊ธฐ

    <img width="1676" alt="แแณแแณแแตแซแแฃแบ 2022-07-03 แแฉแแฅแซ 2 09 05" src="https://user-images.githubusercontent.com/40768187/177009907-dd90f892-87a7-4a83-8283-71e0562b23bc.png">

    ```Experiment``` ์ ํ ์ ๋ค์๊ณผ ๊ฐ์ ํ๋ฉด์ ๋ณผ ์ ์์

    <img width="1672" alt="image" src="https://user-images.githubusercontent.com/40768187/177009985-bd6d205b-56e2-4582-baf4-b42fe2d60f76.png">
    
    ~~๋จธ์ ๋ฌ๋์ ๋ํด ๊ณต๋ถํ์ง ์์ ์ํ๋ผ ํด์๊น์ง๋ ํ๋ฌ~~