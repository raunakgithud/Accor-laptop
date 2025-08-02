#arr

arr = [2,5,8,4,11]

print(arr[2])

arr_mixed = ['A',2,3,'trash',[1,8,9]]

print(arr_mixed)

print(arr_mixed[3])

print(arr_mixed[4][1])  # nested list

#2-D list example 

arr_2d = [[1,2,3],
          [3,4,5],
          [6,7,8]]

print(arr_2d[0][2])
print(arr_2d[1][0])
print(arr_2d[2])

# accessing data from 2 D array 

status_table = [
    [0,1,0],
    [1,1,1],
    [0,1,1],
    [1,1,0,1],
    [0,0,0,1]
]

print(status_table)

print(status_table[3][2])
print(status_table[0][1])
print(status_table[4])

#iterating elements in a list \\array

Item = []
print(Item)
Item.append([1,8,'A']) # append list inside a list 
print(Item)
Item.append([9,10,'hari'])
print(Item)

print(len(Item))
print(len(Item[0]))

people = [['vishal',28,'male',['reading','listing']],
          ['Nikita',31,'female',['running','playing']]] # 3_D array

print(people[1][3][1])
print(people[0][3][0])

#appending Lists inside list 

list = []
list1 = [2,3,5]
list2 = [8,5,0]
list3 = [9,6,2]
list.append(list1)
print(list)

print(len(list))
list.append(list2)
print(list)
print(len(list))

list.append(list3)
print(list)
print(len(list))

#row lenght of an array 
row_lenth_list = len(list)
print(row_lenth_list)
colomn_lenth_list = len(list[2])
print(colomn_lenth_list)


for row in range(row_lenth_list):
    for colomn in range(colomn_lenth_list):
        print(list[row][colomn])
for row in range(row_lenth_list):
    print(list[row])



bag = ''

for colomn in range(colomn_lenth_list):
    bag += str(list[row][colomn])


print(bag)

# Problem Statement: Write a program that prompts the user to enter 5 numbers (one by one). Append each number to a list and print the final list.


















