# ๋ฒ์ธ 1
</br>

## ๐ MLflow ๋ฅผ ์ฌ์ฉํ ์๋น Example

- MLflow๋ฅผ ์ฌ์ฉํ์ฌ ๊ฐ๋จํ๊ฒ ์๋น๋ ๊ฐ๋ฅ
  - https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html

    ```
    mlflow models serve -m $(pwd)/mlruns/0/<run-id>/artifacts/model -p <port>

    mlflow models serve -m $(pwd)/mlruns/0/63d1a9cde7f84190a5634648467be195/artifacts/model -p 1234
    ```

    ์ํ๋ ๋ชจ๋ธ์ run id ๋ฅผ ํ์ธํ๊ณ , port๋ฅผ ์ง์ ํ์ฌ ```mlflow models serve``` ๋ช๋ น ์ํ
    - ๋ชจ๋ธ ์๋น์ ์ฝ๊ฒ ๋งํ๋ฉด 127.0.0.1:1234 ์์ REST API ํํ๋ก .predict() ํจ์๋ฅผ ์ฌ์ฉํ  ์ ์๋ ๊ฒ์ ์๋ฏธ

- ํด๋น ์๋ฒ์ API ๋ฅผ ๋ณด๋ด์, ```predict()```์ ๊ฒฐ๊ณผ ํ์ธ
- API ๋ฅผ ๋ณด๋ด๊ธฐ ์ํด์๋, request body ์ ํฌํจ๋  data ์ ํ์์ ์๊ณ  ์์ด์ผ ํจ
  - diabets data ์ column ๊ณผ sample data ํ์ธ
    - https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html

  - sample data ํ์ธ
    ```python
    data = load_diabetes()
    print(data.feature_names)

    df = pd.DataFrame(data.data)
    print(df.head())

    print(data.target[0])
    ```

    ```
    ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'] 
              0         1         2         3         4         5         6\
    0  0.038076  0.050680  0.061696  0.021872 -0.044223 -0.034821 -0.043401
    1 -0.001882 -0.044642 -0.051474 -0.026328 -0.008449 -0.019163  0.074412
    2  0.085299  0.050680  0.044451 -0.005671 -0.045599 -0.034194 -0.032356
    3 -0.089063 -0.044642 -0.011595 -0.036656  0.012191  0.024991 -0.036038
    4  0.005383 -0.044642 -0.036385  0.021872  0.003935  0.015596  0.008142
              7         8         9 
    0 -0.002592  0.019908 -0.017646 
    1 -0.039493 -0.068330 -0.092204 
    2 -0.002592  0.002864 -0.025930 
    3  0.034309  0.022692 -0.009362 
    4 -0.002592 -0.031991 -0.046641

    151.0
    ```
</br>

- 127.0.0.1:1234 ์๋ฒ์์ ์ ๊ณตํ๋ ```POST /invocations```  API ์์ฒญ ์ํ
  
  ```
    curl -X POST -H "Content-Type:application/json" --data '{"columns":["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"],"data":[[0.038076, 0.050680,  0.061696,  0.021872, -0.044223, -0.034821, -0.043401, -0.002592,  0.019908, -0.017646]]}' http://127.0.0.1:1234/invocations
  ```

  prediction value ๊ฐ API์ response ๋ก ๋ฐํ๋๋ ๊ฒ์ ํ์ธ ๊ฐ๋ฅ

- ์ ํด์ง Data size ์ ๋ค๋ฅด๊ฒ ```POST /invocations``` API ์์ฒญ ์ํ (10๊ฐ ์ปฌ๋ผ์ธ๋ฐ 11๊ฐ ์ปฌ๋ผ ์๋ ฅ)

    ```
    curl -X POST -H "Content-Type:application/json" --data '{"columns":["Age", "Sex", "Body mass index", "Average blood pressure", "S1", "S2", "S3", "S4", "S5", "S6", "S7"],"data":[[0.038076, 0.050680,  0.061696,  0.021872, -0.044223, -0.034821, -0.043401, -0.002592,  0.019908, -0.017646]]}' http://127.0.0.1:1234/invocations
    ```

    Data size ๊ฐ predict ํ๊ธฐ์๋ ์๋ง๋ค๋ ์๋ฌ๊ฐ ๋ฐํ๋จ