from random import randint
from time import sleep

questions = {1: "夜间在没有路灯，照明条件不良情况下行驶",
             2: "同方向近距离跟车行驶",
             3: "超车",
             4: "与对方会车距对方来车将近150米",
             5: "夜间在窄路窄桥与非机动车会车",
             6: "夜间通过没有交通信号灯路口",
             7: "夜间在有路灯照明良好的条件下行驶",
             8: "通过有信号灯路口",
             9: "路边临时停车"}
answers = {"夜间在没有路灯，照明条件不良情况下行驶": "远光灯",
           "同方向近距离跟车行驶": "近光灯",
           "超车": "远近光交替",
           "与对方会车距对方来车将近150米": "近光灯",
           "夜间在窄路窄桥与非机动车会车": "近光灯",
           "夜间通过没有交通信号灯路口": "远近光交替",
           "夜间在有路灯照明良好的条件下行驶": "近光灯",
           "通过有信号灯路口": "近光灯",
           "路边临时停车": "开示廓灯，关闭远近光灯"}

for i in range(5):
    question_sel = []
    for j in range(5):
        question_num = randint(1, 9)
        while question_num in question_sel:
            question_num = randint(1, 9)
        question_sel.append(question_num)
    question_sel.sort()
    print("\n ******* 第 【", i + 1, "】 次模拟考试 ｜｜｜ 夜间驾驶模拟考试开始，请在听到考试指令做出相应动作.  *******\n\n")
    sleep(3)
    print("~~~~~~~ 打开前照灯 ~~~~~~~ \n\n")
    sleep(3)
    for question_light in range(5):
        question = questions[question_sel[question_light]]
        answer = answers[question]
        print("####### 问题：", question, ' #######\n')
        sleep(3)
        print("======= 答案：", answer, ' =======\n\n')
        sleep(1)
    print("¥¥¥¥¥¥¥ 原地灯光模拟结束，请关闭所有灯光 ¥¥¥¥¥¥¥\n\n")
    sleep(5)
    print("(^_^) 注意：关闭灯光，并打左转向灯了吗 (^_^)\n")
    print("一定要注意：打转向后一定要 3  3  3 3  3  3 秒动方向盘哟  \n")
    print("切记切记切记：一定要3 3 3 3 3秒后关闭转向灯呀  \n\n")
    sleep(2)
