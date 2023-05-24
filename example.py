data = {"Input1": 'check', "Input2": 'check2', "Input3:": 'check3'}
check = 1

while check != len(data):
    check += 1
    for i in range(len(data)):
        if data[f'Input{i}'][:-1] == data[f'Input{i+1}'][:-1]:
            print(f"It is much{data}")
