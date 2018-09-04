# skref 1 taka við n frá notanda
# skref 2 búa til lista með fyrstu 3 tölunum
# skref 3 leggja saman síðustu 3 tölur og bæta við listann
# skref 4 endurtaka skref 3 þar til það eru komnar n tölur í listann
# skref 5 prenta út rétt magn af tölum

n = int(input("Enter the length of the sequence: "))

sequence = list((1, 2, 3))

while len(sequence) < n:
    temp_num = sequence[-1] + sequence[-2] + sequence[-3]
    sequence.append(temp_num)

if n == 1:
    print("1")
elif n == 2:
    print("1")
    print("2")
else:
    print(*sequence, sep = "\n")
