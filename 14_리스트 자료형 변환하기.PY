# int나 float 자료형으로 이뤄진 item들을 str로 변환할 때

# int=>str
sample_li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li_str = list(map(str, sample_li))
print(sample_li)
print(li_str)

# str=>int
li_int = list(map(int, li_str))
print(li_int)

# str=>float
li_float = list(map(float, li_str))
print(li_float)