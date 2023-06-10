# Ввод списка из целых элементов
A = []
n = int(input("Введите размер списка: "))
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    A.append(element)

# 1. Вычисление произведения элементов списка с четными номерами
product = 1
for i in range(1, n, 2):
    product *= A[i]

print("Произведение элементов с четными номерами:", product)

# 2. Вычисление суммы элементов списка, расположенных между первым и последним нулевыми элементами
sum_between_zeros = 0
first_zero_index = -1
last_zero_index = -1

for i in range(n):
    if A[i] == 0:
        if first_zero_index == -1:
            first_zero_index = i
        else:
            last_zero_index = i

if first_zero_index != -1 and last_zero_index != -1:
    sum_between_zeros = sum(A[first_zero_index + 1:last_zero_index])

print("Сумма элементов между первым и последним нулевыми элементами:", sum_between_zeros)

# Преобразование списка: положительные элементы в начало, отрицательные - в конец
positive_elements = [x for x in A if x >= 0]
negative_elements = [x for x in A if x < 0]

transformed_list = positive_elements + negative_elements

print("Преобразованный список:")
print(transformed_list)