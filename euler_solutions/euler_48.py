
series = []
for i in range(1,1001):
    series.append(i**i)


sum_series = sum(series)
print(sum_series)

lst_series = list(str(sum_series))
print(lst_series[-10:])

str_series = ''.join([str(x) for x in lst_series[-10:]])
print(str_series)
