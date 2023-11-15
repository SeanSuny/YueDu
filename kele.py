oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f可乐阅读');
频道地址：https://t.me/ymxzpd

活动入口：https://rk1111205522-1322351385.cos.ap-nanjing.myqcloud.com/index.html?upuid=123182
使用方法：
1.入口,WX打开：https://rk1111205522-1322351385.cos.ap-nanjing.myqcloud.com/index.html?upuid=123182
2.打开活动入口，抓包的任意接口cookie参数
3.青龙环境变量菜单或者配置文件，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
青龙添加环境变量名称 ：klydconfig
方式一：青龙添加环境变量参数 ：
单账户：[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}]
多账户：[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}]

方式二：配置文件添加
单账户：export klydconfig="[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}]"
多账户：export klydconfig="[
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
]"
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的cookie参数

4.本地电脑python运行
在本脚本最下方代码if __name__ == '__main__':下填写
例如
loc_klydconfig=[
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
]
定时运行每半个小时一次
'''#line:35
import requests #line:36
import re #line:37
import random #line:38
import os #line:39
import threading #line:40
import json #line:41
import time #line:42
from urllib .parse import urlparse ,parse_qs #line:43
def getinfo (O0OOO0OOO00OO00O0 ):#line:44
    try :#line:45
        O0000O0OOOOOOOOO0 =requests .get (O0OOO0OOO00OO00O0 )#line:46
        O00O0O0O0000OO0OO =re .sub ('\s','',O0000O0OOOOOOOOO0 .text )#line:48
        O0O0O0OOOO0O0O00O =re .findall ('varbiz="(.*?)"\|\|',O00O0O0O0000OO0OO )#line:49
        if O0O0O0OOOO0O0O00O !=[]:#line:50
            O0O0O0OOOO0O0O00O =O0O0O0OOOO0O0O00O [0 ]#line:51
        if O0O0O0OOOO0O0O00O ==''or O0O0O0OOOO0O0O00O ==[]:#line:52
            if '__biz'in O0OOO0OOO00OO00O0 :#line:53
                O0O0O0OOOO0O0O00O =re .findall ('__biz=(.*?)&',O0OOO0OOO00OO00O0 )#line:54
                if O0O0O0OOOO0O0O00O !=[]:#line:55
                    O0O0O0OOOO0O0O00O =O0O0O0OOOO0O0O00O [0 ]#line:56
        OOOO0O0O0O0OO0OO0 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O00O0O0O0000OO0OO )#line:57
        if OOOO0O0O0O0OO0OO0 !=[]:#line:58
            OOOO0O0O0O0OO0OO0 =OOOO0O0O0O0OO0OO0 [0 ]#line:59
        OO00OO0000O0000O0 =re .findall ('varuser_name="(.*?)";',O00O0O0O0000OO0OO )#line:60
        if OO00OO0000O0000O0 !=[]:#line:61
            OO00OO0000O0000O0 =OO00OO0000O0000O0 [0 ]#line:62
        OO0O00OO0O0O0O000 =re .findall ("varmsg_title='(.*?)'\.html\(",O00O0O0O0000OO0OO )#line:63
        if OO0O00OO0O0O0O000 !=[]:#line:64
            OO0O00OO0O0O0O000 =OO0O00OO0O0O0O000 [0 ]#line:65
        O00O0OOO000O0OOO0 =f'公众号唯一标识：{O0O0O0OOOO0O0O00O}|文章:{OO0O00OO0O0O0O000}|作者:{OOOO0O0O0O0OO0OO0}|账号:{OO00OO0000O0000O0}'#line:66
        print (O00O0OOO000O0OOO0 )#line:67
        return OOOO0O0O0O0OO0OO0 ,OO00OO0000O0000O0 ,OO0O00OO0O0O0O000 ,O00O0OOO000O0OOO0 ,O0O0O0OOOO0O0O00O #line:68
    except Exception as O0O0OO0OOO0000OO0 :#line:69
        print (O0O0OO0OOO0000OO0 )#line:70
        print ('异常')#line:71
        return False #line:72
class WXYD :#line:73
    def __init__ (O0OOO00O00OO000OO ,OO00OOOO0OO0OOOO0 ):#line:74
        O0OOO00O00OO000OO .headers ={'Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309080f) XWEB/8461 Flue','Referer':'http://ab1115072245.c0722451115.ww1112001.cn/new?upuid=','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Cookie':OO00OOOO0OO0OOOO0 ['cookie'],}#line:82
    def get_read_url (OOOO0O00OO00O00OO ):#line:84
        OO0000OO0O0O00O00 =f'http://ab1115072245.c0722451115.ww1112001.cn/new/get_read_url'#line:85
        OO00O0O0OOOO00OOO =requests .get (OO0000OO0O0O00O00 ,headers =OOOO0O00OO00O00OO .headers )#line:86
        OO00O000OOO0OO0OO =OO00O0O0OOOO00OOO .json ()#line:87
        print ('get_read_url',OO00O0O0OOOO00OOO .text )#line:88
        O0OO00OOO000O0OOO =OO00O000OOO0OO0OO .get ('jump')#line:89
        OOO0OOO0O0000O00O =parse_qs (urlparse (O0OO00OOO000O0OOO ).query )#line:90
        OO000O00O00000O0O =urlparse (O0OO00OOO000O0OOO ).netloc #line:91
        O0OO0O00O0OOOOOO0 =OOO0OOO0O0000O00O .get ('iu')[0 ]#line:92
        O0000O0O0OOOO00OO ={'Host':OO000O00O00000O0O ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309080f) XWEB/8461 Flue','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':O0OO00OOO000O0OOO ,'Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:102
        return O0OO0O00O0OOOOOO0 ,OO000O00O00000O0O ,O0000O0O0OOOO00OO #line:103
    def do_read (OO00OOOO0000OOO0O ):#line:105
        O00O0O0O0OO0O0OO0 =OO00OOOO0000OOO0O .get_read_url ()#line:106
        OO00OOOO0000OOO0O .params ={'for':'','zs':'','pageshow':'','r':str (round (random .uniform (0 ,1 ),17 )),'iu':O00O0O0O0OO0O0OO0 [0 ]}#line:107
        while True :#line:108
            OO0O00O00000O0OOO =requests .get (f'http://{O00O0O0O0OO0O0OO0[1]}/tuijian/do_read',headers =O00O0O0O0OO0O0OO0 [2 ],params =OO00OOOO0000OOO0O .params )#line:109
            print ('-'*50 )#line:111
            OO0O000OO00OOOOO0 =OO0O00O00000O0OOO .json ()#line:112
            if OO0O000OO00OOOOO0 .get ('msg'):#line:113
                print ('弹出msg',OO0O000OO00OOOOO0 .get ('msg'))#line:114
            OOO0OO00OOOOOOO00 =OO0O000OO00OOOOO0 .get ('url')#line:115
            if OOO0OO00OOOOOOO00 =='close':#line:116
                print ('可能是完成阅读了')#line:117
                return True #line:118
            if '阅读成功'in OO0O00O00000O0OOO .text :#line:119
                print (f'上一篇阅读结果：{OO0O000OO00OOOOO0["success_msg"]}')#line:120
                OO0OOO0OO00OOOO00 =OO0O000OO00OOOOO0 .get ('jkey')#line:121
                OO00OOOO0000OOO0O .params .update ({'jkey':OO0OOO0OO00OOOO00 })#line:122
                O0OO00O0O00O0OOO0 =getinfo (OOO0OO00OOOOOOO00 )#line:123
                print ('开始本次阅读')#line:124
                O00OO00000OO0OO00 =random .randint (6 ,9 )#line:125
                print (f'本次模拟读{O00OO00000OO0OO00}秒')#line:126
                time .sleep (O00OO00000OO0OO00 )#line:127
            else :#line:128
                print ('未知结果')#line:129
                break #line:130
    def withdrawal (OOOOOO0O00O00O00O ):#line:131
        OOO0OO0OO00O00000 ='http://ab1115072245.c0722451115.ww1112001.cn/withdrawal'#line:132
        OOO00O000OOO0OOO0 =requests .get (OOO0OO0OO00O00000 ,headers =OOOOOO0O00O00O00O .headers )#line:133
        OO00OOOOO00OOOO00 =OOO00O000OOO0OOO0 .json ()#line:134
        if OO00OOOOO00OOOO00 .get ('code')==0 :#line:136
            O000OOO000OOOO0OO =OO00OOOOO00OOOO00 ['data']['user']['username']#line:137
            O0O0OO0O0OO00OO0O =OO00OOOOO00OOOO00 ['data']['user']['score']#line:138
            print (f'{O000OOO000OOOO0OO}:{O0O0OO0O0OO00OO0O}')#line:139
    def run (OOO000OOO0O00O00O ):#line:140
        OOO000OOO0O00O00O .do_read ()#line:141
        time .sleep (2 )#line:142
        OOO000OOO0O00O00O .withdrawal ()#line:143
def getEnv (O0OOOOO0O00OO0O00 ):#line:144
    OOOOOO0OO0OOOOOO0 =os .getenv (O0OOOOO0O00OO0O00 )#line:145
    if OOOOOO0OO0OOOOOO0 ==None :#line:146
        print (f'{O0OOOOO0O00OO0O00}没有获取到，使用本地参数')#line:147
        return False #line:148
    try :#line:149
        OOOOOO0OO0OOOOOO0 =json .loads (OOOOOO0OO0OOOOOO0 .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:150
        return OOOOOO0OO0OOOOOO0 #line:151
    except Exception as O0OOO000OO0000O0O :#line:152
        print ('错误:',O0OOO000OO0000O0O )#line:153
        print ('你填写的变量是:',OOOOOO0OO0OOOOOO0 )#line:154
        print ('请检查变量参数是否填写正确')#line:155
        print (f'{O0OOOOO0O00OO0O00}使用本地参数')#line:156
if __name__ =='__main__':#line:157
    loc_klydconfig =[{'name':'备注名','cookie':'PHPSESSID=xxxx; udtauth3=xxxxxx'},]#line:162
    klydconfig =getEnv ('klydconfig')#line:164
    if klydconfig ==False :klydconfig =loc_klydconfig #line:165
    print (klydconfig )#line:166
    tl =[]#line:167
    for cg in klydconfig :#line:168
        print ('*'*50 )#line:169
        print (f'开始执行{cg["name"]}')#line:170
        api =WXYD (cg )#line:171
        t =threading .Thread (target =api .run ,args =())#line:172
        tl .append (t )#line:173
        t .start ()#line:174
        time .sleep (0.5 )#line:175
    for t in tl :#line:176
        t .join ()#line:177
    print ('全部账号执行完成')#line:178
    time .sleep (15 )#line:179
