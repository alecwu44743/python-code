#輸入：
#(+)先輸入語系(C.中文 E.English)
#(+)再輸入
#姓、名、性別、出生年
#First Name, Last Name, Gender, Birth Year

#處理：
#(+)依語系區分欄位名稱
#(+)依語系顯示姓名 (注意中英文姓名慣例)
#(+)依性別顯示稱呼 (先生/小姐, Mr./Ms.)
#(+)設定變數 this_year 為今年(2021)及計算年齡
#(+)判斷是否成年(>=18歲)

#輸出：
#(+)稱呼、姓名
#(+)成年(Adult) / 未成年 (Kid)


while True:
    language_family = input("C.中文 E.English: ")
    if language_family == 'C': #c
        first_name = input("姓: ")
        last_name = input("名: ")
        gender = input("性別 (F.女 M.男): ")
        birth_Year = input("出生年: ")
        print(first_name + last_name + " ", end="")
        if gender == 'M':
            print("先生")
        else:
            print("小姐")

        if 2021 - int(birth_Year) >= 18 : print("成年")
        else : print("未成年")
    else: #e
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        gender = input("Gender (F.Female M.Male): ")
        birth_Year = input("Birth Year: ")
        if gender == 'M':
            print("Mr. ", end="")
        else: 
            print("Ms. ", end="")
        print(first_name + " " + last_name)
        if 2021 - int(birth_Year) >= 18 : print("Adult")
        else : print("Kid")
    print("------------------------------")



# language_family = input('What is your language_family?')
# first_name = input('First Name?')
# last_name = input('Last Name?')
# gender = input('Gender?')
# birth_Year = input('Birth Year?')

# if language_family =='C':
#     print('1.Your name is',last_name +' ' +first_name )
# else: print('1.Your name is',last_name +' ' +first_name )
# if birth_Year