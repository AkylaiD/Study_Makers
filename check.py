# # Task 1
# a = {'John':{'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature': 91}, 'Kelly':{'history': 84, 'math': 85, 'literature': 87}}
# b = {k1: k2 for k1, v1 in a.items() for k2, v2 in v1.items() if max(v1.values()) == v2}
# print(b)

# # # Task 2
# cash = int(input('Сумма, которая есть у вас в бумажнике: '))
# if cash < 0:
#     raise Exception ('Сумма не может быть отрицательной')
# else:
#     print(cash)


# # Task 3
# import functools
# list_ = [1, 2, 3, 4]
# list_ = functools.reduce(lambda x, y: x + y, list_)
# print(list_)

# print(sum(list_))

# # total_sum = 0
# # for i in list_:
# #     total_sum += i
# # print(total_sum)

# # Task 4
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_ = list(filter(lambda i: i % 2  == 0, list_))
# print(list_)

# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append(i)
# print(new_list)