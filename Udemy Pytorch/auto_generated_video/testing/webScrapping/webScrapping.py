import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# class Questions:
#     def __init__(self, question, o1, o2, o3, o4, c_option):
#         self.question = question
#         self.o1 = o1
#         self.o2 = o2
#         self.o3 = o3
#         self.o4 = o4
#         self.c_option = c_option


question = []
o1 = []
o2 = []
o3 = []
o4 = []
c_option = []

ff = [

    ["computer-gk", 52],
    ["political-gk", 42],
    ["economics-gk", 1],
    ["history-gk", 1],
    ["sports-gk", 1],
    ["geography-gk", 1],
    ["teaching-aptitude-in-hindi", 1],
    ["ctet-gk-in-hindi", 1],
    ["bed-entrance-gk-in-hindi", 1],
    ["bank-gk", 1],
    ["ssc-gk-in-hindi", 1],
    ["rail-gk", 1],
    ["upsc-gk-in-hindi", 1],
    ["indian-army-gk-in-hindi", 1],
    ["hindi-grammar-gk", 1],
    ["hindi-grammar-mcq", 1],
    ["reasoning-in-hindi", 1],
    ["bihar-gk-in-hindi", 1],
    ["rajasthan-gk-in-hindi", 1],
    ["jharkhand-gk-in-hindi", 1],
    ["mp-gk-in-hindi", 1],
    ["up-gk-in-hindi", 1],
    ["chhattisgarh-gk-in-hindi", 1],
    ["haryana-gk-in-hindi", 1],
    ["himachal-pradesh-gk-in-hindi", 1],
    ["electronics-gk-in-hindi", 1],
    ["agriculture-gk", 1],
    ["current-affairs-2018-in-hindi", 1],
    ["current-affairs-2019-in-hindi", 1],
    ["math-gk", 1],
    ["states-capitals-gk", 1],
    ["kbc-gk-in-hindi", 1],
    ["bollywood-gk", 1],
    ["ramayan-gk", 1],
    ["author-name", 1],
    ["computer-in-hindi", 1], ]
for path in ff:
    run = True
    m = 1
    while run:
        try:
            r = requests.get("https://gk-hindi.in/" + path[0] + "?page=" + str(m), params={'address': "kolkata"})
            soup = BeautifulSoup(r.content, 'html.parser')
            # print(soup)
            para = soup.find_all("div", class_="question")
            # print(para)
            if len(para) == 0:
                print('completed------' + str(path[0]) + 'with index' + str(m))
                run = False
                break
            for p in para:
                soup2 = BeautifulSoup(str(p), 'html.parser')
                q = soup2.find("b")
                # print(q.string)
                o = soup2.find("ul")
                op = []
                for option in o.stripped_strings:
                    op.append(option)
                    # print(option)
                c_o = soup2.find("button")
                # print(c_o.attrs['data-answer'])
                question.append(q.string)
                o1.append(op[0])
                o2.append(op[1])
                o3.append(op[2])
                o4.append(op[3])
                c_option.append(c_o.attrs['data-answer'])

        except Exception as e:
            print(e)
        print("---------------------------------part " + str(m) + " of " + path[0] + "----------completed")
        m += 1


    dicto = {"question": question, "o1": o1, "o2": o2, "o3": o3, "o4": o4, "c_option": c_option}
    df = pd.DataFrame(dicto)
    df.to_csv('gk_questions/' + path[0] + '.csv')
    time.sleep(2)
    question = []
    o1 = []
    o2 = []
    o3 = []
    o4 = []
    c_option = []

