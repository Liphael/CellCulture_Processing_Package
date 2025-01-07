print(
    "Simple Feed Calculator"
    )
print(
    "Welcome :)"
    )
print(
    "------------------------------------------------------------------------------------------------"
    )
#Title
statusquit = "q"
i=1
while i > 0:
    print(
        "Please input the cultrue mass before sampling:(g)(ml)"
        )
    mass_0 = float(input())
    print(
        "------------------------------------------------------------------------------------------------"
        )
#获取取样前培养质量
    print(
        "Please input the sampling amount:(g)(ml)"
        )
    mass_1 = float(input())
    print(
        "------------------------------------------------------------------------------------------------"
        )
#获取取样量
    mass_2 = mass_0 - mass_1

#计算补料前培养质量
    print(
        "########################Pre_Data:         NO.%s"%(i)
        )
    print(
        "The cultrue mass before sampling is:           %.2F"%(mass_0)+"(g)(ml)"
        )
    print(
        "The sampling amount is:                        %.2F"%(mass_1)+"(g)(ml)"
        )
    print(
        "Please input the cultrue mass before feeding:  %.2F"%(mass_2)+"(g)(ml)"
        )
    print(
        "------------------------------------------------------------------------------------------------"
        )
#数据统计1
    print(
        "#####Warning!#####If feed squence is not used, please input 0!"
        )
    print(
        "Please input the percentage of Feed_(01):(%)"
        )
    por_1 = float(input())
    print(
        "------------------------------------------------------------------------------------------------"
        )
#获取补料_(01)百分比
    print(
        "Please input the percentage of Feed_(02):(%)"
        )
    por_2 = float(input())
    print(
        "------------------------------------------------------------------------------------------------"
        )
#获取补料_(02)百分比
    print(
        "Please input the concentration of Feed_(Glucose):(g/L)"
        )
    c_glucose = float(input())
    if c_glucose > 0:
        glucose_jugde = "The concentration of Feed_(Glucose):  %.5F"%(c_glucose)
        print(
            "------------------------------------------------------------------------------------------------"
            )
    else:
        c_glucose = 6
        glucose_jugde = "The concentration of Feed_(Glucose) is greater than or equal Target C"
        print(
            "------------------------------------------------------------------------------------------------"
            )
#获取补料_(葡萄糖)百分比
    print(
        "########################Proportion_Data:  NO.%s"%(i)
        )
    print(
        "The percentage of Feed_(01):          %.2F"%(por_1)+"(%)"
        )
    print(
        "The percentage of Feed_(02):          %.2F"%(por_2)+"(%)"
        )
    print(
        glucose_jugde + "(g/L), Target C of Gluc is 6(g/L)"
        )
    print(
        "------------------------------------------------------------------------------------------------"
        )
#数据统计2
    mass_a = mass_2 * por_1 * 0.01
    mass_b = mass_2 * por_2 * 0.01
    mass_glucose = (6 - c_glucose) * mass_2 /300
    mass_d = mass_2 + mass_a + mass_b + mass_glucose
    print(
        "########################Results:          NO.%s"%(i)
        )
    print(
        "Cultrue mass before feeding:          %.1f"%(mass_2)+"(g)(ml)"
        )
    print(
        "Feed_(01) needed:                     %.1f"%(mass_a)+"(g)(ml)"
        )
    print(
        "Feed_(02) needed:                     %.1f"%(mass_b)+"(g)(ml)"
        )
    print(
        "Feed_(glucose) needed:                %.1f"%(mass_glucose)+"(g)(ml)"
        )
    print(
        "Expected cultrue mass after feeding:  %.1f"%(mass_d)+"(g)(ml)"
        )
    print(
        "------------------------------------------------------------------------------------------------"
        )
#结果输出
    print(
        "Input q to exit, or any other continue..."
        )
    checkpoint = input("")
    if (checkpoint == statusquit):
        exit()
    else: i = i + 1
#循环确认
