import random

def generate_fortunate_number():
    return random.randint(0,100)

def generate_fortunate_number_discription(f_number):
    a=str()
    if(f_number<10):
        a="幸运值有点低哦，坐和放宽。"
    elif(f_number>=10 and f_number<30):
        a="宜：在群里说“啊这”。"
    elif(f_number>=30 and f_number<50):
        a="宜：抄写《道德与法治》提纲。"
    elif(f_number>=50 and f_number<70):
        a="宜：看看群并拍拍群主。"
    elif(f_number>=70 and f_number<90):
        a="欧吃矛！！！"
    elif(f_number>=90 and f_number<100):
        a="运气已经达到了人类无法触及的高度……也许这就是大佬吧，吸吸吸。"
    else:
        a="(｡·ˇ‸ˇ·｡)哼！都怪你 (`ȏ´) 运气这么好也不哄哄人家(〃′o`)人家超想哭的，捶你胸口，大坏蛋！！！(￣^￣)ゞ咩QAQ捶你胸口你好讨厌！(=ﾟωﾟ)ﾉ要抱抱嘤嘤嘤哼，人家拿小拳拳捶你胸口！！！(｡· ^·̀｡)大坏蛋，打死你(つд⊂)"
    return a


if __name__=="__main__":
    fn=generate_fortunate_number()
    fnd=generate_fortunate_number_discription(fn)
    print("今天的幸运数字是："+str(fn)+"！"+fnd)
