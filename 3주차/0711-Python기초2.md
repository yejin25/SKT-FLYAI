# 3μ£Όμ°¨ 2022 07 11
</br>

## π Python κΈ°μ΄2 - λ°μ΄ν° κ΅¬μ‘°μ μ μ΄λ¬Έ

###  μ§ν©ν μλ£ν
</br>

μ¬λ¬ κ°μ λ°μ΄ν°λ₯Ό νλλ‘ λ¬Άμ΄μ μ μ₯ λ° κ΄λ¦¬κ° νμν κ²½μ° -> μ§ν©ν μλ£ν μ κ³΅

- Pythonμ μ§ν©ν μλ£ν
  - list
  - tuple
  - set
  - dict

</br>

### λ¦¬μ€νΈ
</br>

- μ¬λ¬ κ°μ λ°μ΄ν°λ₯Ό μμλλ‘ μ μ₯νκ³  κ΄λ¦¬ν΄μΌ ν  λ μ¬μ©
- μ΄λ€ μλ£νλ μμ κ°μΌλ‘ κ°λ₯
- μμμ μΆκ°, μ­μ  λ³κ²½ κ°λ₯
- λ¬Έμμ΄μ²λΌ μΈλ±μ±κ³Ό μ¬λΌμ΄μ± κ°λ₯
- νμ
  - λ¦¬μ€νΈλͺ = [μμ1, μμ2, μμ3, ...]

</br>

#### λ¦¬μ€νΈ μμ± - lsit(), []

```python
lst = [1, 2, "a"]       # λ¦¬μ€νΈ μμκ°μ μ§μ  μ§μ 
lst = list("abc")       # list ν¨μμ μΈμλ‘ λμ΄ν κ°μ μ·¨νμ¬ λ¦¬μ€νΈ μμκ°μΌλ‘ λ³κ²½
                        # ["a", "b", "c"]
                        # μΈμλ‘λ μμλ₯Ό κ°λ iterableν λ°μ΄ν° 1κ°λ§ μ¬ μ μμ

list1 = list(2, 3, 4)   # error - κ°μ΄ νλκ° μλ(3κ°), iterable νμ§λ μμ

list1 = list(2)         # error - νλμ κ°μ΄μ§λ§ iterable νμ§ μμ

list1 = list([2, 3, 4]) # μ΄μ κ°μ΄ μμ±ν΄μΌ ν¨
```

</br>

- λ¬Έμμ΄μ ```split()``` λ©μλλ₯Ό μ¬μ©ν λ¦¬μ€νΈ μμ±
  - dates = "2020/04/30".split("/") -> dates = ["2020", "04", "30"]
- ```spilt()``` λ©μλλ λ¬Έμμ΄μ μ¬λ¬ κ°μ λ¬Έμμ΄λ‘ λΆλ¦¬νμ¬ μ μ²΄λ₯Ό **λ¦¬μ€νΈ ννλ‘ λ°ν**

</br>

#### λ¦¬μ€νΈ νμ© μμ
</br>

```python
items = input("Enter items: ").split()
iLen = len(items)
sum = 0
for n in range(0, iLen):
    sum += int(items[n])        # items λ¦¬μ€νΈ κ° μμ΄νλ€μ μ μλ‘ λ³ν
print("{}κ° μμ ν©κ³: {}, νκ· : {}".format(iLen, sum, avg))
```

<img width="374" alt="image" src="https://user-images.githubusercontent.com/40768187/178311139-679dd540-43c7-4eae-b7ec-be9425c48ecc.png">

</br>

### μΈλ±μ±κ³Ό μ¬λΌμ΄μ±
</br>

#### λ¬Έμμ΄ μΈλ±μ±κ³Ό μ¬λΌμ΄μ±
</br>

μΈλ±μ€ λ²μ
- len(s) : μλ ₯κ° sμ κΈΈμ΄(μμ μ μ²΄ κ°μ)λ₯Ό λ°ν
- μμ μΈλ±μ€ : 0 ~ len(λ¬Έμμ΄) - 1
- μμ μΈλ±μ€ : -len(λ¬Έμμ΄) ~ -1
- μΈλ±μ€ λ²νΈλ ```[ ]``` μμ κΈ°λ‘νμ¬ ν΄λΉ λ¬Έμ μ°Έμ‘°

