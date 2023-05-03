from random import randint

garden_size = int(input("Введите количество кустов: "))
berry_size = int(input("Введите максимальную урожайность с куста: "))
garden_list = dict()

for i in range(0, garden_size):
    garden_list[i] = randint(0, berry_size)
    
    
result_max = 0    #костыль для смыкания окружности
result_max1 = garden_list[len(garden_list)-2] + garden_list[len(garden_list)-1] + garden_list[0]
result_max2 = garden_list[len(garden_list)-1] + garden_list[0] + garden_list[1]
key_max = 0
if result_max1 >= result_max2:
    result_max = result_max1
    key_max = [len(garden_list)-2, len(garden_list)-1, 0]
else :
    result_max = result_max2
    key_max = [len(garden_list)-1, 0, 1]
    
    
for i in range(2, len(garden_list)):
    if result_max < garden_list[i-2] + garden_list[i-1] + garden_list[i]:
        result_max = garden_list[i-2] + garden_list[i-1] + garden_list[i]
        key_max = [i-2, i-1, i]

print(garden_list)
print("С кустов: ", key_max)
print("Максимальное количество ягод за один заход: ", result_max)