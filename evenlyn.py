# BMIv7
import string
import random


print("""-----Please choose the mode-----
\033[5;30;47mMode 1\033[0;37;40m  Input Mode
\033[5;30;47mMode 2\033[0;37;40m  Random Data Mode
--------------------------------
""")
mode = int(input("Please input the mode:"))

bmi_set = {}

def is_float(n):
  try:
    float(n)
    return True
  except ValueError:
    return False

def break_or_not(n):
  if(not is_float(n)):
    if(n.upper() == "Q"):
      return True

def Caculate():
      bmi = round(w/(h**2), 1)
      bmi_set[n] = bmi

def Ouput():
      normal, over_w, under_w = {},{},{}

      for k,v in bmi_set.items():
      #print ('The BMI of {} is {}'.format(k, v))
        if (v >= 24):
            over_w[k] = v
        elif (v <= 18.5):
            under_w[k] = v
        else:
          normal[k] = v

      if (not over_w and not under_w):
        print ('Every one is good!!')

      if (over_w):
        print ('Overweight people, please Exercise ⚽️⚽️!')
        print ('Total: {}'.format(len(over_w)))
        for k,v in over_w.items():
          print ('The BMI of {} is {} '.format(k,v))
        print ()  

      if (under_w):     
        print ('Under weight people, please Eat more 🍖🍖!')
        print ('Total: {}'.format(len(under_w)))
        for k,v in under_w.items():
          print ('The BMI of {} is {} '.format(k,v))

if(mode == 1):
        print ("Please input name, weight and height, press Q/q to quit")
        while True:
          n = str(input('Please input the name:'))
          if (len(n) == 1 and break_or_not(n[0])):
            break

          while True:     
              try:
                w = input('Please input the weight(kg):')
                if(w.upper() == "Q"): break 
                w = float(w)
              except ValueError:
                print ('Input should be a value, please re-input ')
                continue
              if(w < 10 or w >500):
                  print("Weight error! Please input weight between 10kg to 500kg.")
                  continue
              break
          if(break_or_not(w)): break

          while True:
              try:    
                h = input('Please input the height(m):')
                if(h.upper() == "Q"): break
                h = float(h)
              except ValueError:
                print ('Input should be a value, please re-input ')
                continue
              if(h < 1 or h > 2.2):
                  print("Height error! Please input height between 1m to 2.2m.")
                  continue
              break
          
          if(break_or_not(h)): break
          
          if(is_float(h) and is_float(w)):
            Caculate()
          
        Ouput()

elif(mode == 2):
        data_num = int(input("Please input the number of datas: "))
        str_len = 5
        for x in range(data_num):
          n = (''.join(random.choice(string.ascii_letters) for _ in range(str_len)))
          w = random.randint(10,500)
          h = round(random.uniform(1.0,2.2),1)
          Caculate()
        Ouput()
