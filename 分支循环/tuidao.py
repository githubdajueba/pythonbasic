"""
 推导式
"""
#list = ["day1","day2",...]
# list = ["day"+str(i) for i in range(1,8)]
# print(list)

list = ['day_1', 'day_2', 'day_3', 'day_4', 'day5', 'day6', 'day7']
result_list = [i.replace("_","0") for i in list]
print(result_list)