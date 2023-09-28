Questions = [ ['Which language was used to create youtube ?', 'Python', 'Php', 'Javascript', 'Matlab', 1],
             
['Who is the founder of google ?', 'Larry page', 'Sundar pichai', 'Sandeep Verma','Bill Gates', 1],

['Who made the whole universe ?', 'Jesus Christ', 'Allah', 'Bramha Ji', 'Sandeep Verma', 3],

['Who fucked your mommy ?', 'Daddy', 'You', 'God', 'Sandeep', 4],

['Which language was used to create youtube ?', 'Python', 'Php', 'Javascript', 'Matlab', 1],
             
['Who is the founder of google ?', 'Larry page', 'Sundar pichai', 'Sandeep Verma','Bill Gates', 1],

['Who make the whole universe ?', 'Jesus Christ', 'Allah', 'Bramha Ji', 'Sandeep Verma', 4],

['Who fucked your mommy ?', 'Daddy', 'You', 'Sandeep Verma', 'Sandeep', 3] ]

levels = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000, 2048000, 4096000]

money = 0

for i in range(0,len(Questions)):
    question = Questions[i]
    print(f'Question for Rs. {levels[i]}')
    print()
    print(question[0])
    print(f'1. {question[1]}        2. {question[2]}')
    print(f'3. {question[3]}        4. {question[4]}')
    print()
    reply = int(input("Enter your answer (1-4)"))
    if reply==question[-1]:
        print(f"Correct answer, You won Rs. {levels[i]}")
        print()
        if i==4:
            money=10000
        elif i==9:
            money=320000
        elif i==14:
            money=10000000
    else:
        print("Wrong answer!")
        print()
        break

print(f"Your take home money is {money}")