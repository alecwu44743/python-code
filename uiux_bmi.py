# import re
from logging import exception
from colorama import init, Fore, Back
import names
import random

# bmi_name = []
bmi_set = []

start_status = -1 # 0:test, 1:std-mode

def isQuit():
    return ((random.randint(1, 100) % 98) == 0)

def YN_Wrong_Gender():
    return ((random.randint(1, 100) % 2) == 0)


def get_random_names():
    toQuit = isQuit()
    
    if toQuit:
        return 'quit'
    else:
        _gender = YN_Wrong_Gender()
        if _gender:
            return names.get_first_name(gender='female')
        else:
            return names.get_first_name(gender='male')


def get_random_number(low, high):
    toQuit = isQuit()
    
    if toQuit:
        return 'quit'
    else:
        giveWrong = YN_Wrong_Gender()
        if giveWrong:
            n = random.uniform(0, 1000)
            cnt = 0
            while n >= low or n <= high:
                if cnt == 4:
                    n = 9
                    break
                n = random.uniform(0, 10000)
                cnt += 1
            return n
        else:
            return random.uniform(low, high+1)


def say_No_or_Yes():
    if YN_Wrong_Gender():
        return 'y'
    else:
        return 'n'


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
        print('     ' + "%-10s %-10s %-10s %-10s %-10s" % ("Name", "Weight", "Height", "BMI", "Status"))
        for data in bmi_set:
            # print('     %s\'s BMI is %.2f, %s - Weight: %.2f, Height: %.2f' % (data["name"], data["bmi"], data["bmi_status"], data["weight"], data["height"]))
            if data["bmi"] < 18.5:
                print('     ' + Fore.YELLOW + "%-10s %-10.2f %-10.2f %-10.2f %-10s" % (data["name"], data["weight"], data["height"], data["bmi"], data["bmi_status"]) + Fore.RESET)
            elif data["bmi"] >= 24:
                print('     ' + Fore.RED + "%-10s %-10.2f %-10.2f %-10.2f %-10s" % (data["name"], data["weight"], data["height"], data["bmi"], data["bmi_status"]) + Fore.RESET)
            else:
                print('     ' + Fore.GREEN + "%-10s %-10.2f %-10.2f %-10.2f %-10s" % (data["name"], data["weight"], data["height"], data["bmi"], data["bmi_status"]) + Fore.RESET)
        print("     " + Fore.BLACK + Back.WHITE + "Total: %d" % len(bmi_set) + Fore.RESET + Back.RESET)
    else:
        print('Oops, no data!')
    print()


def print_categ():
    print("[-] Category:")

    if len(bmi_set) > 0:
        cnt = 0
        
        print(' (Underweight) ')
        for data in bmi_set:
            if(data["bmi"] < 18.5):
                if cnt == 0:
                    print('     ' + "%-10s %-10s %-10s %-10s" % ("Name", "Weight", "Height", "BMI"))
                print('     ' + "%-10s %-10.2f %-10.2f %-10.2f" % (data["name"], data["weight"], data["height"], data["bmi"]))
                cnt += 1
        
        if cnt == 1: 
            print('   ' + Fore.BLACK + Back.WHITE + 'No data' + Fore.RESET + Back.RESET)
        else:
            print('   ' + Fore.BLACK + Back.WHITE + 'Total: %d' % cnt + Fore.RESET + Back.RESET)
        cnt = 0
        
        print('\n (Obese) ')
        for data in bmi_set:
            if(data["bmi"] >= 24):
                if cnt == 0:
                    print('     ' + "%-10s %-10s %-10s %-10s" % ("Name", "Weight", "Height", "BMI"))
                print('     ' + "%-10s %-10.2f %-10.2f %-10.2f" % (data["name"], data["weight"], data["height"], data["bmi"]))
                cnt += 1
        
        if cnt == 1: 
            print('   ' + Fore.BLACK + Back.WHITE + 'No data' + Fore.RESET + Back.RESET)
        else:
            print('   ' + Fore.BLACK + Back.WHITE + 'Total: %d' % cnt + Fore.RESET + Back.RESET)
        
    else:
        print('   ' + Fore.BLACK + Back.WHITE + 'Oops, no data!' + Fore.RESET + Back.RESET)

def input_data():
    testCounter = 0
    
    while True:
        if testCounter == 30 and start_status == 0:
            break
        
        _name = ""
        print("[>] Enter your name (enter \"quit\" to quit): ", end='')
        if start_status == 0:
            _name = get_random_names()
            print(_name)
        elif start_status == 1:
            _name = input()
            
            
        if _name.upper() == 'QUIT':
            break
        
        _exit = 0
        
        w = 0
        h = 0


        while True:
            try:
                w = 0
                print('[>] Please input the weight[kg] (press \"q\" to quit): ', end='')
                if start_status == 0:
                    w = get_random_number(10, 500)
                    print(w)
                elif start_status == 1:
                    w = input()
                    
                if type(w) == str:
                    if w.upper() == 'Q' or w.upper() == 'QUIT':
                        _exit = 1
                        break
                if float(w) > 500 or float(w) < 10:
                    raise
                else:
                    break
                
                # pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
                # result = pattern.match(w)
            except:
                print ('\033[93m' + '    Weight should be a number and in the range (10kg to 500kg), please re-input ' + '\033[0m')
        if _exit == 1: break


        while True:
            try:
                print('[>] Please input the height[cm] (press \"q\" to quit): ', end='')
                if start_status == 0:
                    h = get_random_number(100, 220)
                    print(h)
                elif start_status == 1:
                    h = input()
                
                if type(h) == str:
                    if h.upper() == 'Q' or h.upper() == 'QUIT':
                        _exit = 1
                        break
                    elif h.find('.') != -1:
                        print('\033[93m' + ' [!] Do you mean %.2f cm? (y/n): ' % (float(h)*100) + '\033[0m', end='')
                        if start_status == 0:
                            res = say_No_or_Yes() 
                        elif start_status == 1:
                            while True:
                                try:
                                    res = input()
                                    if res.upper() == 'Y' or res.upper() == 'YES' or res.upper() == 'N' or res.upper() == 'NO':
                                        break
                                except:
                                    continue        
                        
                            if res.upper() == 'Y' or res.upper() == 'YES':
                                h = float(h)*100
                                if h > 220 or h < 100:
                                    raise
                    elif float(h) <= 220 or float(h) >= 100:
                            break
                if float(h)>220 or float(h)<100:
                    raise
                else:
                    break
            except:
                print ('\033[93m' + '    Height should be a number and in the range (100cm to 220cm), please re-input ' + '\033[0m')
        if _exit == 1: break
        
        
        # bmi_name.append(name)
        # h = float(h) / 100
        # bmi = float(w)/(h*h)
        bmi_set.append({
            "name": _name,
            "weight": float(w),
            "height": float(h),
            "bmi": float(w)/((float(h)/100)**2),
            "bmi_status": get_BMI_status(float(w)/((float(h)/100)**2))
        })
        testCounter += 1


if __name__ == '__main__':
    while True:
        try:
            start_status = int(input('[info] (0):Test Mode (1):Standard Mode (2):Exit >> '))
            bmi_set.clear()
            if start_status == 0 or start_status == 1:
                input_data()
        
                print()
                print_all()
        
                print()
                print_categ()
                print()
            elif start_status == 2:
                print('\n\nBye! Bye! ;)')
                break
        except:
            continue


# 修正原本程式碼的錯誤，如：算式更正、型別轉換等，
# 並加入輸入'q'或'quit'時，結束程式的功能，無需再多打兩次-999，
# 最後再將輸出做更正，增加bmi狀態、名字、變更排版等。