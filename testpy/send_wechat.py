#-*-coding:utf8-*-
import itchat
import datetime, os, platform,time


def timerfun(sched_time) :
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now > sched_time and now < sched_time + datetime.timedelta(seconds=1) :  # 因为时间秒之后的小数部分不一定相等，要标记一个范围判断
            send_move()
            time.sleep(1)    # 每次判断间隔1s，避免多次触发事件
            flag = 1
        else :
            #print('schedual time is {0}'.format(sched_time))
            #print('now is {0}'.format(now))
            if flag == 1 :
                sched_time = sched_time + datetime.timedelta(hours=1)  # 把目标时间增加一个小时，一个小时后触发再次执行
                flag = 0


def send_move():
    # nickname = input('please input your firends\' nickname : ' )
    #   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    # users = itchat.search_friends(name=nickname)
    users = itchat.search_friends(name='我的小姑娘')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    itchat.send("哈哈哈哈",toUserName = userName)
    print('succeed')

if __name__=='__main__':
    itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录
    sched_time = datetime.datetime(2019,03,18,18,05,00)   #设定初次触发事件的事件点
    print('run the timer task at {0}'.format(sched_time))
    timerfun(sched_time)