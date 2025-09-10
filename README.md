Exit=False
while not Exit:
    num = int(input('What type of data you want to convert? \n1 : Height\n2 : Weight\n0 :Exit\n>>>> '))
    if num == 1:
        Height = int(input('1 : Inches to CM\n2 : CM to Inches\n>>>> '))
        if Height == 1:
            value = float(input("Enter a number to convert: "))
            print(f'{value} inches = {round(value * 2.54, 2)} CM')
        elif Height == 2:
            value = float(input("Enter a number to convert: "))
            print(f'{value} CM = {round(value * 0.393700787, 2)} inches')
        else:
            print('Invalid option!!')
    elif num == 2:
        Weight = int(input('1 : KG to Pounds\n2 : Pounds to KG\n>>>> '))
        if Weight == 1:
            value = float(input("Enter a number to convert: "))
            print(f'{value} KG = {round(value * 2.20462262, 2)} pounds')
        elif Weight == 2:
            value = float(input("Enter a number to convert: "))
            print(f'{value} pounds = {round(value * 0.45359237, 2)} KG')
        else:
            print('Invalid option!')
    elif num==0:
        Exit=True
    else:
        print('Invalid option!')
# projcts
