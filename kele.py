oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f可乐阅读');
活动入口：https://rk1115131229-1322350692.cos.ap-nanjing.myqcloud.com/index.html?upuid=123182
使用方法：
1.入口,WX打开：https://rk1115131229-1322350692.cos.ap-nanjing.myqcloud.com/index.html?upuid=123182
'''#line:7
'''
2.打开活动入口，抓包的任意接口cookie参数
3.青龙环境变量菜单或者配置文件，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
青龙添加环境变量名称 ：klydconfig
方式一：青龙添加环境变量参数 ：
单账户：[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}]
多账户：[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'},{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}]

方式二：配置文件添加
单账户：export klydconfig="[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}]"
多账户：export klydconfig="[
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}
]"
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的cookie参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取

4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
方式一：青龙添加环境变量参数 ：
名称 ：push_config
参数 ：{"printf":0,"threadingf":1,"appToken":"xxxx"}
方式二：配置文件添加
export push_config="{'printf':'0','threadingf':'1','appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
appToken 这个是填wxpusher的appToken,找不到自己百度

5.本地电脑python运行
在本脚本最下方代码if __name__ == '__main__':下填写
例如
loc_push_config={"printf":0,"threadingf":1,"appToken":"xxxx"}
loc_klydconfig=[
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
]
定时运行每半个小时一次
'''#line:55
import requests #line:56
import re #line:57
import random #line:58
import os #line:59
import threading #line:60
import json #line:61
import hashlib #line:62
import time #line:63
from urllib .parse import urlparse ,parse_qs #line:64
checkDict ={'oneischeck':['第一篇文章','过检测'],}#line:67
def getmsg ():#line:68
    O0O0O00OO00OO000O ='v1.1f'#line:69
    O0000O00O00OO0000 =''#line:70
    try :#line:71
        OOOOO0OOOOOO00000 ='http://175.24.153.42:8881/getmsg'#line:72
        O00O0OOO000O00000 ={'type':'zhyd'}#line:73
        O0000O00O00OO0000 =requests .get (OOOOO0OOOOOO00000 ,params =O00O0OOO000O00000 )#line:74
        OOO0OOO0000OO0O0O =O0000O00O00OO0000 .json ()#line:75
        OOOO00O0OO0O0O0O0 =OOO0OOO0000OO0O0O .get ('version')#line:76
        O0000O00OOO000000 =OOO0OOO0000OO0O0O .get ('gdict')#line:77
        O0OOO000OO00000OO =OOO0OOO0000OO0O0O .get ('gmmsg')#line:78
        print ('系统公告:',O0OOO000OO00000OO )#line:79
        print (f'最新版本{OOOO00O0OO0O0O0O0},当前版本{O0O0O00OO00OO000O}')#line:80
        print (f'系统的公众号字典{len(O0000O00OOO000000)}个:{O0000O00OOO000000}')#line:81
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:82
        print ('='*50 )#line:83
    except Exception as OOOO0OO000O0O0000 :#line:84
        print (O0000O00O00OO0000 .text )#line:85
        print (OOOO0OO000O0O0000 )#line:86
        print ('公告服务器异常')#line:87
def push (O0O0O0OOO00O0OO0O ,OO0O000O0OOOOO0OO ,OOO0O00OO00O0000O ,O0OOOOO0O0OOOOO00 ,OO0OOO0000OOOOO00 ,OOOOO000000O0000O ):#line:88
    OO0OO0000O0000000 ='''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>TITLE</title>
<style type=text/css>
   body {
   	background-image: linear-gradient(120deg, #fdfbfb 0%, #a5d0e5 100%);
    background-size: 300%;
    animation: bgAnimation 6s linear infinite;
}
@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
</style>
</head>
<body>
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
<p><a href="http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl=LINK">点击阅读检测文章</a></p><br>
</body>
</html>
    '''#line:113
    O0OO00OO000000O00 =OO0OO0000O0000000 .replace ('TITTLE',O0O0O0OOO00O0OO0O ).replace ('LINK',OO0O000O0OOOOO0OO ).replace ('TEXT',OOO0O00OO00O0000O ).replace ('TYPE',O0OOOOO0O0OOOOO00 ).replace ('KEY',OOOOO000000O0000O )#line:115
    OO0OOO0OO0O0O00O0 ={"appToken":appToken ,"content":O0OO00OO000000O00 ,"summary":O0O0O0OOO00O0OO0O ,"contentType":2 ,"uids":[OO0OOO0000OOOOO00 ]}#line:122
    OOOOO00O00000O000 ='http://wxpusher.zjiecode.com/api/send/message'#line:123
    try :#line:124
        O0O0O0OO000OO0O00 =requests .post (url =OOOOO00O00000O000 ,json =OO0OOO0OO0O0O00O0 ).text #line:125
        print (O0O0O0OO000OO0O00 )#line:126
        return True #line:127
    except :#line:128
        print ('推送失败！')#line:129
        return False #line:130
def getinfo (O0000O000000OOO0O ):#line:131
    try :#line:132
        OO000OOO00OO00OOO =requests .get (O0000O000000OOO0O )#line:133
        OO0OOOOO0O0OO0O0O =re .sub ('\s','',OO000OOO00OO00OOO .text )#line:135
        OO0O0OO0OO0OOOO0O =re .findall ('varbiz="(.*?)"\|\|',OO0OOOOO0O0OO0O0O )#line:136
        if OO0O0OO0OO0OOOO0O !=[]:#line:137
            OO0O0OO0OO0OOOO0O =OO0O0OO0OO0OOOO0O [0 ]#line:138
        if OO0O0OO0OO0OOOO0O ==''or OO0O0OO0OO0OOOO0O ==[]:#line:139
            if '__biz'in O0000O000000OOO0O :#line:140
                OO0O0OO0OO0OOOO0O =re .findall ('__biz=(.*?)&',O0000O000000OOO0O )#line:141
                if OO0O0OO0OO0OOOO0O !=[]:#line:142
                    OO0O0OO0OO0OOOO0O =OO0O0OO0OO0OOOO0O [0 ]#line:143
        O0OO0000OO0000O0O =re .findall ('varnickname=htmlDecode\("(.*?)"\);',OO0OOOOO0O0OO0O0O )#line:144
        if O0OO0000OO0000O0O !=[]:#line:145
            O0OO0000OO0000O0O =O0OO0000OO0000O0O [0 ]#line:146
        O0O0OO0000O0000OO =re .findall ('varuser_name="(.*?)";',OO0OOOOO0O0OO0O0O )#line:147
        if O0O0OO0000O0000OO !=[]:#line:148
            O0O0OO0000O0000OO =O0O0OO0000O0000OO [0 ]#line:149
        OO0OOOO00O0O0OO00 =re .findall ("varmsg_title='(.*?)'\.html\(",OO0OOOOO0O0OO0O0O )#line:150
        if OO0OOOO00O0O0OO00 !=[]:#line:151
            OO0OOOO00O0O0OO00 =OO0OOOO00O0O0OO00 [0 ]#line:152
        OO0OOO00000OOO00O =f'公众号唯一标识：{OO0O0OO0OO0OOOO0O}|文章:{OO0OOOO00O0O0OO00}|作者:{O0OO0000OO0000O0O}|账号:{O0O0OO0000O0000OO}'#line:153
        print (OO0OOO00000OOO00O )#line:154
        return O0OO0000OO0000O0O ,O0O0OO0000O0000OO ,OO0OOOO00O0O0OO00 ,OO0OOO00000OOO00O ,OO0O0OO0OO0OOOO0O #line:155
    except Exception as O0000O00O000OOOOO :#line:156
        print (O0000O00O000OOOOO )#line:157
        print ('异常')#line:158
        return False #line:159
class WXYD :#line:160
    def __init__ (O0O0O00O000OO0O00 ,O00O0O0OO0OO00000 ):#line:161
        O0O0O00O000OO0O00 .name =O00O0O0OO0OO00000 ['name']#line:162
        O0O0O00O000OO0O00 .key =O00O0O0OO0OO00000 ['key']#line:163
        O0O0O00O000OO0O00 .uids =O00O0O0OO0OO00000 ['uids']#line:164
        O0O0O00O000OO0O00 .headers ={'Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Linux; Android 13; 22011211C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20230805 MMWEBID/2575 MicroMessenger/8.0.42.2460(0x28002A92) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64','Referer':'http://ab1115072245.c0722451115.ww1112001.cn/new?upuid=','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Cookie':O00O0O0OO0OO00000 ['cookie'],}#line:172
    def printjson (OO0O0O0OO0O0OO0OO ,OOO0O0000OO000OO0 ):#line:173
        if printf ==0 :#line:174
            return #line:175
        print (OO0O0O0OO0O0OO0OO .name ,OOO0O0000OO000OO0 )#line:176
    def setstatus (O00OO00OO000OO000 ):#line:177
        try :#line:178
            OOO00O00OOO000O0O ='http://175.24.153.42:8882/setstatus'#line:179
            O0OOO00000OOO0OO0 ={'key':O00OO00OO000OO000 .key ,'type':'zhyd','val':'1','ven':oo0o }#line:180
            O0OO0O0OO0OOOO000 =requests .get (OOO00O00OOO000O0O ,params =O0OOO00000OOO0OO0 ,timeout =10 )#line:181
            print (O00OO00OO000OO000 .name ,O0OO0O0OO0OOOO000 .text )#line:182
            if '无效'in O0OO0O0OO0OOOO000 .text :#line:183
                exit (0 )#line:184
        except Exception as OO0O0O00OO0O000OO :#line:185
            print (O00OO00OO000OO000 .name ,'设置状态异常')#line:186
            print (O00OO00OO000OO000 .name ,OO0O0O00OO0O000OO )#line:187
    def getstatus (OO000OO0OO0O000OO ):#line:189
        try :#line:190
            OOOO00O0O0O0OOO00 ='http://175.24.153.42:8882/getstatus'#line:191
            O0O0O00OO0OO00000 ={'key':OO000OO0OO0O000OO .key ,'type':'zhyd'}#line:192
            O000OOOOO0OO0000O =requests .get (OOOO00O0O0O0OOO00 ,params =O0O0O00OO0OO00000 ,timeout =3 )#line:193
            return O000OOOOO0OO0000O .text #line:194
        except Exception as OO000OO00O000OOO0 :#line:195
            print (OO000OO0OO0O000OO .name ,'查询状态异常',OO000OO00O000OOO0 )#line:196
            return False #line:197
    def tuijian (OO00OOO0OO0OO0O0O ):#line:198
        O0O00000O0O0OOO0O ='http://ab1115131510.c1315101115.ww1112001.cn/tuijian'#line:199
        O0O00OO0O0OOO0O00 =requests .get (O0O00000O0O0OOO0O ,headers =OO00OOO0OO0OO0O0O .headers )#line:200
        try :#line:201
            O0OOO0OOO0OOO0O0O =O0O00OO0O0OOO0O00 .json ()#line:202
            if O0OOO0OOO0OOO0O0O .get ('code')==0 :#line:203
                OO00OOOOOOOO0OO00 =O0OOO0OOO0OOO0O0O ['data']['user']['username']#line:204
                O0O0OOOO00OO00000 =float (O0OOO0OOO0OOO0O0O ['data']['user']['score'])/100 #line:205
                print (f'{OO00OOOOOOOO0OO00}:当前剩余{O0O0OOOO00OO00000}元')#line:206
                return True #line:207
            else :#line:208
                print (O0OOO0OOO0OOO0O0O )#line:209
                print ('账号异常0,ck可能失效')#line:210
                return False #line:211
        except Exception as O0000OOO000OOO0OO :#line:212
            print (O0000OOO000OOO0OO )#line:213
            print ('账号异常1，ck可能失效')#line:214
            return False #line:215
    def get_read_url (OO000OO00O0O0O0O0 ):#line:216
        O0OO0OOOO0O00OO0O =f'http://ab1115072245.c0722451115.ww1112001.cn/new/get_read_url'#line:217
        O0OO00O00O000OO00 =requests .get (O0OO0OOOO0O00OO0O ,headers =OO000OO00O0O0O0O0 .headers )#line:218
        O000O0OOOOOOOO0OO =O0OO00O00O000OO00 .json ()#line:219
        OOOOO00OOOO0OOO00 =O000O0OOOOOOOO0OO .get ('jump')#line:221
        OO00O0O000OOO000O =parse_qs (urlparse (OOOOO00OOOO0OOO00 ).query )#line:222
        OO0000O00OOO00O0O =urlparse (OOOOO00OOOO0OOO00 ).netloc #line:223
        OO0O0000O0OO00OO0 =OO00O0O000OOO000O .get ('iu')[0 ]#line:224
        OOOO0OOOO000000O0 ={'Host':OO0000O00OOO00O0O ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; 22011211C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20230805 MMWEBID/2575 MicroMessenger/8.0.42.2460(0x28002A92) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':OOOOO00OOOO0OOO00 ,'Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:234
        O0OO00O00O000OO00 =requests .get (OOOOO00OOOO0OOO00 ,headers =OOOO0OOOO000000O0 )#line:235
        OOOO0OOOO000000O0 .update ({'Cookie':f'PHPSESSID={O0OO00O00O000OO00.cookies.get("PHPSESSID")}'})#line:236
        return OO0O0000O0OO00OO0 ,OO0000O00OOO00O0O ,OOOO0OOOO000000O0 #line:237
    def do_read (OOO0O00O0OO0000OO ):#line:239
        OO0OOOO00000OOOO0 =OOO0O00O0OO0000OO .get_read_url ()#line:240
        OOO0O00O0OO0000OO .jkey =''#line:241
        OO000OOO0000000OO =0 #line:242
        while True :#line:243
            OOO0O00O0OO0000OO .tuijian ()#line:244
            OO00OOO000000OOO0 =f'?for=&zs=&pageshow&r={round(random.uniform(0, 1), 17)}&iu={OO0OOOO00000OOOO0[0]}{OOO0O00O0OO0000OO.jkey}'#line:245
            OOO000O0O0000OO00 =f'http://{OO0OOOO00000OOOO0[1]}/tuijian/do_read{OO00OOO000000OOO0}'#line:246
            print (OOO000O0O0000OO00 )#line:247
            OOOO0O0OOOOOO0O00 =requests .get (OOO000O0O0000OO00 ,headers =OO0OOOO00000OOOO0 [2 ])#line:248
            print ('-'*50 )#line:250
            OO00O0O0000O00OOO =OOOO0O0OOOOOO0O00 .json ()#line:251
            if OO00O0O0000O00OOO .get ('msg'):#line:252
                print ('弹出msg',OO00O0O0000O00OOO .get ('msg'))#line:253
            O000000OOO0O00000 =OO00O0O0000O00OOO .get ('url')#line:254
            if O000000OOO0O00000 =='close':#line:255
                print (f'阅读结果：{OO00O0O0000O00OOO.get("success_msg","开始阅读或者异常")}')#line:256
                return True #line:257
            if 'weixin'in O000000OOO0O00000 :#line:258
                print (f'上一篇阅读结果：{OO00O0O0000O00OOO.get("success_msg","开始阅读或者异常")}')#line:259
                OO000O00OO0OO0O00 =OO00O0O0000O00OOO .get ('jkey')#line:260
                OOO0O00O0OO0000OO .jkey =f'&jkey={OO000O00OO0OO0O00}'#line:261
                OO00OOOO0OOO0OO0O =getinfo (O000000OOO0O00000 )#line:262
                if OO000OOO0000000OO ==0 :#line:263
                    O00O0O0OO000O00O0 =list (OO00OOOO0OOO0OO0O )#line:264
                    O00O0O0OO000O00O0 [4 ]='oneischeck'#line:265
                    if OOO0O00O0OO0000OO .testCheck (O00O0O0OO000O00O0 ,O000000OOO0O00000 )==False :#line:266
                        return False #line:267
                    OO000OOO0000000OO =1 #line:268
                if OOO0O00O0OO0000OO .testCheck (OO00OOOO0OOO0OO0O ,O000000OOO0O00000 )==False :#line:269
                    return False #line:270
                print ('开始本次阅读')#line:271
                OO0OO00OOOOOO000O =random .randint (6 ,9 )#line:272
                print (f'本次模拟读{OO0OO00OOOOOO000O}秒')#line:273
                time .sleep (OO0OO00OOOOOO000O )#line:274
            else :#line:275
                print ('未知结果')#line:276
                print (OO00O0O0000O00OOO )#line:277
                break #line:278
    def testCheck (OO000000O00OO000O ,OOO0000O00O000OO0 ,O0OOOOO0O0OOO0O0O ):#line:279
        if OOO0000O00O000OO0 [4 ]==[]:#line:280
            print (OO000000O00OO000O .name ,'这个链接没有获取到微信号id',O0OOOOO0O0OOO0O0O )#line:281
            return True #line:282
        if checkDict .get (OOO0000O00O000OO0 [4 ])!=None :#line:283
            OO000000O00OO000O .setstatus ()#line:284
            for O00OO0OO0OOOOO0O0 in range (60 ):#line:285
                if O00OO0OO0OOOOO0O0 %30 ==0 :#line:286
                    push (f'可乐阅读过检测:{OO000000O00OO000O.name}',O0OOOOO0O0OOO0O0O ,OOO0000O00O000OO0 [3 ],'zhyd',OO000000O00OO000O .uids ,OO000000O00OO000O .key )#line:287
                OOO0O0O000OO00O00 =OO000000O00OO000O .getstatus ()#line:288
                if OOO0O0O000OO00O00 =='0':#line:289
                    print (OO000000O00OO000O .name ,'过检测文章已经阅读')#line:290
                    return True #line:291
                elif OOO0O0O000OO00O00 =='1':#line:292
                    print (OO000000O00OO000O .name ,f'正在等待过检测文章阅读结果{O00OO0OO0OOOOO0O0}秒。。。')#line:293
                    time .sleep (1 )#line:294
                else :#line:295
                    print (OO000000O00OO000O .name ,OOO0O0O000OO00O00 )#line:296
                    print (OO000000O00OO000O .name ,'服务器异常')#line:297
                    return False #line:298
            print (OO000000O00OO000O .name ,'过检测超时中止脚本防止黑号')#line:299
            return False #line:300
        else :#line:301
            return True #line:302
    def withdrawal (O00000OO000O0O000 ):#line:303
        O00O0OOOOO00OO00O ='http://ab1115072245.c0722451115.ww1112001.cn/withdrawal'#line:304
        O0OOO0OO0OOOOOO00 =requests .get (O00O0OOOOO00OO00O ,headers =O00000OO000O0O000 .headers )#line:305
        OO0OO00OO00O00000 =O0OOO0OO0OOOOOO00 .json ()#line:306
        time .sleep (3 )#line:307
        if OO0OO00OO00O00000 .get ('code')==0 :#line:308
            O00O0O0O000000O0O =int (float (OO0OO00OO00O00000 ['data']['user']['score']))#line:309
            if O00O0O0O000000O0O >=2000 :#line:310
                O00O0O0O000000O0O =2000 #line:311
            O0OOO000OO00OO00O =O00000OO000O0O000 .headers .copy ()#line:312
            O0OOO000OO00OO00O .update ({'Content-Type':'application/x-www-form-urlencoded'})#line:313
            O00O0OOOOO00OO00O ='http://ab1116084433.c0844331116.ww1112004.cn/withdrawal/doWithdraw'#line:314
            OOO0000O0OOO0O000 =f'amount={O00O0O0O000000O0O}&type=wx'#line:315
            O0OOO0OO0OOOOOO00 =requests .post (O00O0OOOOO00OO00O ,headers =O0OOO000OO00OO00O ,data =OOO0000O0OOO0O000 )#line:316
            print ('提现结果',O0OOO0OO0OOOOOO00 .text )#line:317
        else :#line:318
            print (OO0OO00OO00O00000 )#line:319
    def run (OO0OO0OO0000O00O0 ):#line:320
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='e00d9b235da07e11c89608f0fc8c8e36':OO0OO0OO0000O00O0 .setstatus ()#line:321
        if OO0OO0OO0000O00O0 .tuijian ():#line:322
            OO0OO0OO0000O00O0 .do_read ()#line:323
            time .sleep (2 )#line:324
            OO0OO0OO0000O00O0 .withdrawal ()#line:325
def getEnv (O0000OOOO0O00000O ):#line:326
    OOOOO000O0OO0O0O0 =os .getenv (O0000OOOO0O00000O )#line:327
    if OOOOO000O0OO0O0O0 ==None :#line:328
        print (f'{O0000OOOO0O00000O}没有获取到，使用本地参数')#line:329
        return False #line:330
    try :#line:331
        OOOOO000O0OO0O0O0 =json .loads (OOOOO000O0OO0O0O0 .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:332
        return OOOOO000O0OO0O0O0 #line:333
    except Exception as O0O0OO00O0OOOOO00 :#line:334
        print ('错误:',O0O0OO00O0OOOOO00 )#line:335
        print ('你填写的变量是:',OOOOO000O0OO0O0O0 )#line:336
        print ('请检查变量参数是否填写正确')#line:337
        print (f'{O0000OOOO0O00000O}使用本地参数')#line:338
if __name__ =='__main__':#line:339
    loc_push_config = {"printf": 1, "threadingf": 0, "appToken": "AT_9KCxxxxxxu6JC"}
    loc_klydconfig = [
        {'name':'备注名','cookie':'PHPSESSID=hxxxxpud; udtauth3=c2b68xxxx','key':'xxxx','uids':'xxxxx'},
        #{'name': '备注名', 'cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
        #{'name': '备注名', 'cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
    ]
    #--------------------------------------------------------
    push_config = getEnv('push_config')
    if push_config == False: push_config = loc_push_config
    print(push_config)
    klydconfig = getEnv('klydconfig')
    if klydconfig==False:klydconfig=loc_klydconfig
    print(klydconfig)
    printf = push_config['printf']  # 打印调试日志0不打印，1打印，若运行异常请打开调试
    appToken = push_config['appToken']  # 这个是填wxpusher的appToken
    threadingf = push_config['threadingf']
    getmsg()
    if threadingf == 1:
        tl=[]
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            time.sleep(0.5)
        for t in tl:
            t.join()
    elif threadingf == 0:
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            api.run()
            print(f'{cg["name"]}执行完毕')
            time.sleep(3)
    else:
        print('请确定推送变量中threadingf参数是否正确')
    print('全部账号执行完成')
    time.sleep(15)
