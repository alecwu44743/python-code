# import re

# bmi_name = []
bmi_set = []

exit = 0

def get_BMI_status(b):
    if(b < 18.5):
        return "Underweight"
    elif(b >= 18.5 and b < 24):
        return "Normal"
    elif(b >= 24 and b < 27):
        return "Overweight"
    elif(b >= 27 and b < 30):
        return "Obese"
    elif(b >= 30 and b < 35):
        return "Severely Obese"
    elif(b >= 35):
        return "Very Severely Obese"


def print_all():
    print("[-] All data:")
    if len(bmi_set) > 0:
        for data in bmi_set:
            print('     %s\'s BMI is %.2f, %s - Weight: %.2f, Height: %.2f' % (data["name"], data["bmi"], data["bmi_status"], data["weight"], data["height"]))
    else:
        print('Oops, no data!')
        
        
def print_categ():
    print("[-] Category:")
    empty = 1
    if len(bmi_set) > 0:
        
        print(' (Underweight) ')
        for data in bmi_set:
            if(data["bmi"] < 18.5):
                print('   The BMI of the %s is %.2f' % (data["name"], data["bmi"]), end='')
                empty = 0
        
        if empty == 1: 
            print('   No data')
        empty = 1
        
        print('\n (Obese) ')
        for data in bmi_set:
            if(data["bmi"] >= 24):
                print('   The BMI of the %s is %.2f' % (data["name"], data["bmi"]), end='')
                empty = 0
        
        if empty == 1:
            print('   No data')
        
    else:
        print('Oops, no data!')

def input_data():
    while True:
        name = input("[>] Enter your name (enter \"quit\" to quit): ")
        if name.upper() == 'QUIT':
            break
        
        # while True:
        #     try:
        #         w = float(input('Please input the weight[kg] (press \"q\" to quit): '))
        #         break
        #     except ValueError:
        #         print ('Input should be a value, please re-input ')
        #         continue

        # while True:
        #     w = input('Please input the weight[kg] (press \"q\" to quit): ')
        #     if w.upper() == 'Q' or w.upper() == 'QUIT':
        #         break
        #     if (int(w)>500 or int(w)<10):
        #         print ('Weight should be in the range (10, 500), please re-input ')
        #         continue
        #     else:
        #         break
        
        w = 0
        h = 0
        exit = 0
        
        
        while True:
            try:
                w = input('[>] Please input the weight[kg] (press \"q\" to quit): ')
                if w.upper() == 'Q' or w.upper() == 'QUIT':
                    exit = 1
                    break
                # pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
                # result = pattern.match(w)
                if (float(w)>500 or float(w)<10):
                    raise
                break
            except:
                print ('    Weight should be a number and in the range (10kg to 500kg), please re-input ')
        if exit == 1: break
        
        
        while True:
            try:
                h = input('[>] Please input the height[cm] (press \"q\" to quit): ')
                if h.upper() == 'Q' or h.upper() == 'QUIT':
                    exit = 1
                    break
                if h.find('.') != -1:
                    res = input('[>] Do you mean %s cm? (y/n)' % (float(h)*100))
                    if res.upper() == 'Y' or res.upper() == 'YES':
                        h = float(h)*100
                        if h > 220 or h < 100:
                            raise
                        else:
                            break
                    else:
                        continue
                if float(h)>220 or float(h)<100:
                    raise
                break
            except:
                print ('    Height should be a number and in the range (100cm to 222cm), please re-input ')
        if exit == 1: break
        
        
        # bmi_name.append(name)
        # h = float(h) / 100
        # bmi = float(w)/(h*h)
        bmi_set.append({
            "name": name,
            "weight": float(w),
            "height": float(h),
            "bmi": float(w)/((float(h)/100)**2),
            "bmi_status": get_BMI_status(float(w)/((float(h)/100)**2))
        })


if __name__ == '__main__':
    input_data()
    
    print()
    print_all()
    
    print()
    print_categ()


# 修正原本程式碼的錯誤，如：算式更正、型別轉換等，
# 並加入輸入'q'或'quit'時，結束程式的功能，無需再多打兩次-999，
# 最後再將輸出做更正，增加bmi狀態、名字、變更排版等。