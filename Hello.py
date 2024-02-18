m = 0
a = 0
b = 0
print_frequency ="|frequency (f)"
class_print = "|classes  "
frequency = []
n = 0
print_upperlimits = []
greatest_frequency_len = 0
greatest_class_len = 0
class_lowerlimits = []
class_upperlimits = []
print_listfrequency = []
class_lowerlimit = int(input("enter class lower limit of the first class-> "))
class_upperlimit = int(input("enter class upper limit of the first class-> "))
class_lowerlimits.append(class_lowerlimit)
class_upperlimits.append(class_upperlimit)
class_size = class_upperlimit - class_lowerlimit
if class_size <= 0:
    print("incorrect class size")
if class_size > 0:
    number_of_classes = int(input("how many classes are present in the data?-"))
    while number_of_classes > n + 1:
        class_lowerlimits.append(class_upperlimits[n])
        class_upperlimits.append(class_lowerlimits[n + 1] + class_size)
        n = n + 1
    for i in class_upperlimits:
        print_upperlimits.append(str(i))
    for c in class_lowerlimits:
        print_value = len(f"{c} - {class_upperlimits[m]}")
        if len(class_print) > print_value:
            greatest_class_len = len(class_print)
        elif greatest_frequency_len < len(f"{class_lowerlimits[-1]} - {class_upperlimits[-1]}"):
            greatest_class_len = len(f"{class_lowerlimits[-1]} - {class_upperlimits[-1]}")
        elif greatest_class_len < print_value:
            greatest_class_len = print_value
            m = m + 1
        else:
            m = m + 1
    for i in print_upperlimits:
        print_value = len(f"{class_lowerlimits[a]} - {i}")
        if greatest_class_len > print_value:
            while greatest_class_len > print_value:
                print_upperlimits[a] = print_upperlimits[a] + " "
                print_value = print_value + 1
            a = a + 1
        else:
            greatest_class_len = greatest_class_len
            a = a + 1
    while greatest_class_len >= len(class_print):
        class_print = class_print + " "
    for x in class_upperlimits:
        frequency_add = int(input("type the frequency according to the classes: "))
        frequency.append(frequency_add)
    for i in frequency:
        print_listfrequency.append(str(i))
    for x in print_listfrequency:
        print_f_value = len(f"|  {x} |")
        if greatest_frequency_len < print_f_value:
            greatest_frequency_len = print_f_value
        else:
            greatest_frequency_len = greatest_frequency_len 
    if greatest_frequency_len < len(f"{print_frequency}|"):
      greatest_frequency_len = len(f"{print_frequency}|")
    print(f"{greatest_frequency_len}")     
    for y in print_listfrequency:
        print_F_value = len(f"|  {y} |")
        if greatest_frequency_len > print_F_value:
            while greatest_frequency_len > print_F_value:
                print_listfrequency[b] = print_listfrequency[b] + " "
                print_F_value = print_F_value + 1
            b = b + 1
        else:
            b = b + 1

    while greatest_frequency_len > len(f"{print_frequency}|"):
        print_frequency = print_frequency + " "   
    print(f"{class_print}{print_frequency}|")
    n = 0
    for x in class_lowerlimits:
        print(f"|{x} - {print_upperlimits[n]}|  {print_listfrequency[n]} |")
        n = n + 1
    while True:
        mean_median_mode = input("what do you want to find mean(x) median(y) mode(z):").lower()
        if mean_median_mode == "x":
          postion = 0
          sigma_fixi = 0
          sigma_f = 0
          fixi= []
          print_fixi = []
          m = 0
          xi = []
          print_xi = []
          str_xi = "| xi "
          greatest_fixi_len = 0
          greatest_xi_len = 0
          for y in class_upperlimits:
            xi_add = (class_upperlimits[m] + class_lowerlimits[m])/2
            xi.append(xi_add)
            fixi_add = frequency[m] * xi[m]
            fixi.append(fixi_add)
            m = m + 1
          print(f"{class_print}{print_frequency}{str_xi}")
          m = 0
          for x in print_upperlimits:
              print(f"|{class_lowerlimits[m]} - {x}|  {print_listfrequency[m]} | {xi[m]} |")
              m = m + 1
          print("classes _|frequency (f)|_  xi _|_fixi_|\n\n\n")
          m = 0
          for x in print_upperlimits:
              print(f"{class_lowerlimits[m]} - {x}|  {print_listfrequency[m]} | {xi[m]} | {fixi[m]} |")
              m = m + 1
          for i  in frequency:
              sigma_f = sigma_f + i  
          for j in fixi:
              sigma_fixi = sigma_fixi + j
          mean = sigma_fixi / sigma_f 
          print(f'''
              ∑fi = {sigma_f}
              ∑fixi = {sigma_fixi}
              mean = {sigma_fixi}/{sigma_f} = {mean}
              ''')
        frequency_cf = 0
        if mean_median_mode == "y":
          n = 0
          C_F = []
          print_cf = []
          greatest_cf_len = 0
          print_strcf = " CF "
          postion = 0
          for x in frequency:
              frequency_cf = frequency_cf + x
              C_F.append(frequency_cf)
          for i in C_F:
            print_cf.append(str(i))
          greatest_cf_len = len(f" {print_cf[-1]} ")
          if greatest_cf_len < len(f"|{print_strcf}|"):
            greatest_cf_len = len(f"|{print_strcf}|")
          if len(print_strcf) < greatest_cf_len:
            while len(print_strcf) < greatest_cf_len+1:
              print_strcf = print_strcf + " "
          for i in print_cf:
            cf_print_value = len(f"|{i}|")
            if greatest_cf_len > cf_print_value:
              while greatest_cf_len > cf_print_value:
                print_cf[n] = print_cf[n] + " "
                cf_print_value = cf_print_value + 1
              n = n + 1
            else:
              n = n + 1
          n_by_2 = C_F[-1] / 2
          for x in C_F:
              if n_by_2 <= x:
                  postion = C_F.index(x) 
                  break
              else:
                  n_by_2 = n_by_2
          median_lowerclass = class_lowerlimits[postion]
          median_frequency = frequency[postion]
          C_F_calc = C_F[postion - 1]
          print(f"{class_print}{print_frequency}|{print_strcf}|")
          n = 0
          for x in print_upperlimits:
              print(f"|{class_lowerlimits[n]} - {x}|  {print_listfrequency[n]} |  {print_cf[n]} |")
              n = n + 1
          print(f''' 

  median class = {median_lowerclass} - {class_upperlimits[postion]}

  frequency = {median_frequency}

  C.F = {C_F_calc}

  class height = {class_size}

  lower limit = {median_lowerclass}

  n = {C_F[-1]}

  n/2 = {n_by_2}
  |
  |
  V
  \n
  ''')
          step_1 = (n_by_2 - C_F_calc)/median_frequency
          step_2 = step_1 * class_size
          median = step_2 + median_lowerclass
          print(f"Hence median = {median}")
        f1 = 0
        if mean_median_mode == "z":
          n = 0
          frequency_mode = [0]
          for y in frequency:
              frequency_mode.append(y)
          frequency_mode.append(0)
          for x in frequency:
            if x > f1:
              f1 = x
            else:
              f1 = f1
          position_f1 = frequency.index(f1)
          f0 = frequency_mode[position_f1]
          f2 = frequency_mode[position_f1 + 2]
          modal_lower_class = class_lowerlimits[position_f1]
          step_1_mode = f1 - f0
          step_2_mode = 2*f1 - f0 - f2
          step_3_mode= step_1_mode / step_2_mode
          step_4_mode = step_3_mode * class_size
          mode = modal_lower_class + step_4_mode
          print(f"{class_print}{print_frequency}|")
          for i in print_upperlimits:
            print(f"{class_lowerlimits[n]} - {i}|  {print_listfrequency[n]} |")
            n = n + 1
          print(f'''     
      modal class = {modal_lower_class} - {class_upperlimits[position_f1]}    
      f0 = {f0}         
      f1 = {f1}
      f2 = {f2}
      lower limit of modal class = {modal_lower_class}    
      class size (h) = {class_size}

    Hence mode = {mode}
            ''')
        if mean_median_mode == "q":
          break
