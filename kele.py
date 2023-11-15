oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f可乐阅读');
活动入口：https://rk1115131229-1322350692.cos.ap-nanjing.myqcloud.com/index.html?upuid=123182
使用方法：
1.入口,WX打开：https://rk1115131229-1322350692.cos.ap-nanjing.myqcloud.com/index.html?upuid=123182
'''

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
'''#line:52
import requests #line:53
import re #line:54
import random #line:55
import os #line:56
import threading #line:57
import json #line:58
import time #line:59
from urllib .parse import urlparse ,parse_qs #line:60
checkDict ={'oneischeck':['第一篇文章','过检测'],}#line:63
def getmsg ():#line:64
    O000O00O0O0OOO0OO ='v1.0f'#line:65
    OO00000OO0O0OO0OO =''#line:66
    try :#line:67
        O0O0O0O0O0OO0OOO0 ='http://175.24.153.42:8881/getmsg'#line:68
        OO00OOO00OO00O00O ={'type':'zhyd'}#line:69
        OO00000OO0O0OO0OO =requests .get (O0O0O0O0O0OO0OOO0 ,params =OO00OOO00OO00O00O )#line:70
        OOO0OO0OO0O0OO0OO =OO00000OO0O0OO0OO .json ()#line:71
        O0O0OOO0OOOO0O000 =OOO0OO0OO0O0OO0OO .get ('version')#line:72
        O000O0O0000OO0OO0 =OOO0OO0OO0O0OO0OO .get ('gdict')#line:73
        O0OOOO000000O000O =OOO0OO0OO0O0OO0OO .get ('gmmsg')#line:74
        print ('系统公告:',O0OOOO000000O000O )#line:75
        print (f'最新版本{O0O0OOO0OOOO0O000},当前版本{O000O00O0O0OOO0OO}')#line:76
        print (f'系统的公众号字典{len(O000O0O0000OO0OO0)}个:{O000O0O0000OO0OO0}')#line:77
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:78
        print ('='*50 )#line:79
    except Exception as OO0O00O00OO0OO00O :#line:80
        print (OO00000OO0O0OO0OO .text )#line:81
        print (OO0O00O00OO0OO00O )#line:82
        print ('公告服务器异常')#line:83
def push (OO00OOOOOO0O00O0O ,OO000000O000OO000 ,O0OOO0O0O0OOOOO0O ,OOOOOOOO00OO0O0OO ,OO0000OOO0OOOOO00 ,O0O000O0O0OO0O000 ):#line:84
    OO0O000OO00000000 ='''<!DOCTYPE html>
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
    '''#line:109
    OO0O0000000OOOO00 =OO0O000OO00000000 .replace ('TITTLE',OO00OOOOOO0O00O0O ).replace ('LINK',OO000000O000OO000 ).replace ('TEXT',O0OOO0O0O0OOOOO0O ).replace ('TYPE',OOOOOOOO00OO0O0OO ).replace ('KEY',O0O000O0O0OO0O000 )#line:111
    O00O0OOO0O00O0O00 ={"appToken":appToken ,"content":OO0O0000000OOOO00 ,"summary":OO00OOOOOO0O00O0O ,"contentType":2 ,"uids":[OO0000OOO0OOOOO00 ]}#line:118
    OO0OO00O00O000O00 ='http://wxpusher.zjiecode.com/api/send/message'#line:119
    try :#line:120
        O000OOO00O0OOOOO0 =requests .post (url =OO0OO00O00O000O00 ,json =O00O0OOO0O00O0O00 ).text #line:121
        print (O000OOO00O0OOOOO0 )#line:122
        return True #line:123
    except :#line:124
        print ('推送失败！')#line:125
        return False #line:126
def getinfo (OO00000OO00O0OO00 ):#line:127
    try :#line:128
        OOO000000OOOOOO00 =requests .get (OO00000OO00O0OO00 )#line:129
        OOO0O0OO0O0000OO0 =re .sub ('\s','',OOO000000OOOOOO00 .text )#line:131
        O0OO0OO00000OO000 =re .findall ('varbiz="(.*?)"\|\|',OOO0O0OO0O0000OO0 )#line:132
        if O0OO0OO00000OO000 !=[]:#line:133
            O0OO0OO00000OO000 =O0OO0OO00000OO000 [0 ]#line:134
        if O0OO0OO00000OO000 ==''or O0OO0OO00000OO000 ==[]:#line:135
            if '__biz'in OO00000OO00O0OO00 :#line:136
                O0OO0OO00000OO000 =re .findall ('__biz=(.*?)&',OO00000OO00O0OO00 )#line:137
                if O0OO0OO00000OO000 !=[]:#line:138
                    O0OO0OO00000OO000 =O0OO0OO00000OO000 [0 ]#line:139
        OOO0OO00000O0OO0O =re .findall ('varnickname=htmlDecode\("(.*?)"\);',OOO0O0OO0O0000OO0 )#line:140
        if OOO0OO00000O0OO0O !=[]:#line:141
            OOO0OO00000O0OO0O =OOO0OO00000O0OO0O [0 ]#line:142
        O0OO00O00O000OOO0 =re .findall ('varuser_name="(.*?)";',OOO0O0OO0O0000OO0 )#line:143
        if O0OO00O00O000OOO0 !=[]:#line:144
            O0OO00O00O000OOO0 =O0OO00O00O000OOO0 [0 ]#line:145
        O00O000OO00O000O0 =re .findall ("varmsg_title='(.*?)'\.html\(",OOO0O0OO0O0000OO0 )#line:146
        if O00O000OO00O000O0 !=[]:#line:147
            O00O000OO00O000O0 =O00O000OO00O000O0 [0 ]#line:148
        OO000O000OO000000 =f'公众号唯一标识：{O0OO0OO00000OO000}|文章:{O00O000OO00O000O0}|作者:{OOO0OO00000O0OO0O}|账号:{O0OO00O00O000OOO0}'#line:149
        print (OO000O000OO000000 )#line:150
        return OOO0OO00000O0OO0O ,O0OO00O00O000OOO0 ,O00O000OO00O000O0 ,OO000O000OO000000 ,O0OO0OO00000OO000 #line:151
    except Exception as O0OOO000000000O0O :#line:152
        print (O0OOO000000000O0O )#line:153
        print ('异常')#line:154
        return False #line:155
class WXYD :#line:156
    def __init__ (OOOO00OOO0O0OO0OO ,OO0O0O000OOO0000O ):#line:157
        OOOO00OOO0O0OO0OO .name =OO0O0O000OOO0000O ['name']#line:158
        OOOO00OOO0O0OO0OO .key =OO0O0O000OOO0000O ['key']#line:159
        OOOO00OOO0O0OO0OO .uids =OO0O0O000OOO0000O ['uids']#line:160
        OOOO00OOO0O0OO0OO .headers ={'Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Linux; Android 13; 22011211C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20230805 MMWEBID/2575 MicroMessenger/8.0.42.2460(0x28002A92) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64','Referer':'http://ab1115072245.c0722451115.ww1112001.cn/new?upuid=','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Cookie':OO0O0O000OOO0000O ['cookie'],}#line:168
    def printjson (OO000O0O000O0O0O0 ,OO0O0O00OO0O0O00O ):#line:169
        if printf ==0 :#line:170
            return #line:171
        print (OO000O0O000O0O0O0 .name ,OO0O0O00OO0O0O00O )#line:172
    def setstatus (O000OOOOO00OO0OOO ):#line:173
        try :#line:174
            OO0O0OOOOOO00O00O ='http://175.24.153.42:8882/setstatus'#line:175
            O0O0OOO00OOOO000O ={'key':O000OOOOO00OO0OOO .key ,'type':'zhyd','val':'1','ven':oo0o }#line:176
            O0O00O00O0OO00OO0 =requests .get (OO0O0OOOOOO00O00O ,params =O0O0OOO00OOOO000O ,timeout =10 )#line:177
            print (O000OOOOO00OO0OOO .name ,O0O00O00O0OO00OO0 .text )#line:178
            if '无效'in O0O00O00O0OO00OO0 .text :#line:179
                exit (0 )#line:180
        except Exception as OO00OO0OO0O0OOO0O :#line:181
            print (O000OOOOO00OO0OOO .name ,'设置状态异常')#line:182
            print (O000OOOOO00OO0OOO .name ,OO00OO0OO0O0OOO0O )#line:183
    def getstatus (O000O00O0O00O0O00 ):#line:185
        try :#line:186
            O0000O0000OOO0000 ='http://175.24.153.42:8882/getstatus'#line:187
            O00OO0OO0OO0O0O0O ={'key':O000O00O0O00O0O00 .key ,'type':'zhyd'}#line:188
            OOO0O0O000O00OO0O =requests .get (O0000O0000OOO0000 ,params =O00OO0OO0OO0O0O0O ,timeout =3 )#line:189
            return OOO0O0O000O00OO0O .text #line:190
        except Exception as OOOO00000OO0O00OO :#line:191
            print (O000O00O0O00O0O00 .name ,'查询状态异常',OOOO00000OO0O00OO )#line:192
            return False #line:193
    def tuijian (OOO0OO000O0OOOOOO ):#line:194
        OO0O000OOO00OO0O0 ='http://ab1115131510.c1315101115.ww1112001.cn/tuijian'#line:195
        O0O0O0000O0OO0000 =requests .get (OO0O000OOO00OO0O0 ,headers =OOO0OO000O0OOOOOO .headers )#line:196
        try :#line:197
            OOOO0OO00O0O0OOOO =O0O0O0000O0OO0000 .json ()#line:198
            if OOOO0OO00O0O0OOOO .get ('code')==0 :#line:199
                O0O0000O000000OOO =OOOO0OO00O0O0OOOO ['data']['user']['username']#line:200
                O000OOO0OO00000OO =float (OOOO0OO00O0O0OOOO ['data']['user']['score'])/100 #line:201
                print (f'{O0O0000O000000OOO}:当前剩余{O000OOO0OO00000OO}元')#line:202
            else :#line:203
                print (OOOO0OO00O0O0OOOO )#line:204
                print ('账号异常0')#line:205
                exit (0 )#line:206
        except Exception as O0OOO0O0OO0OO00O0 :#line:207
            print (O0OOO0O0OO0OO00O0 )#line:208
            print ('账号异常1')#line:209
            exit (0 )#line:210
    def get_read_url (OO00O0O00O000OOO0 ):#line:211
        OO00O0OO0OOOO0OO0 =f'http://ab1115072245.c0722451115.ww1112001.cn/new/get_read_url'#line:212
        OOOOO0OOOOO0OOOOO =requests .get (OO00O0OO0OOOO0OO0 ,headers =OO00O0O00O000OOO0 .headers )#line:213
        OO0O0OOOOO0O0O00O =OOOOO0OOOOO0OOOOO .json ()#line:214
        OOOOOOOOOO0OOO00O =OO0O0OOOOO0O0O00O .get ('jump')#line:216
        O0O0OO000O00OOOOO =parse_qs (urlparse (OOOOOOOOOO0OOO00O ).query )#line:217
        OO0000O0OOO000000 =urlparse (OOOOOOOOOO0OOO00O ).netloc #line:218
        OOOOOOO0OOO0000OO =O0O0OO000O00OOOOO .get ('iu')[0 ]#line:219
        O0O00O00OO00OO000 ={'Host':OO0000O0OOO000000 ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; 22011211C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20230805 MMWEBID/2575 MicroMessenger/8.0.42.2460(0x28002A92) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':OOOOOOOOOO0OOO00O ,'Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:229
        OOOOO0OOOOO0OOOOO =requests .get (OOOOOOOOOO0OOO00O ,headers =O0O00O00OO00OO000 )#line:230
        O0O00O00OO00OO000 .update ({'Cookie':f'PHPSESSID={OOOOO0OOOOO0OOOOO.cookies.get("PHPSESSID")}'})#line:231
        return OOOOOOO0OOO0000OO ,OO0000O0OOO000000 ,O0O00O00OO00OO000 #line:232
    def do_read (O0O0000O0O0O000O0 ):#line:234
        OOO0OO0O0000OOOO0 =O0O0000O0O0O000O0 .get_read_url ()#line:235
        O0O0000O0O0O000O0 .jkey =''#line:236
        O0OO00O0OOO0OOOO0 =0 #line:237
        while True :#line:238
            O0O0000O0O0O000O0 .tuijian ()#line:239
            OO0O00O00O0000OOO =f'?for=&zs=&pageshow&r={round(random.uniform(0, 1), 17)}&iu={OOO0OO0O0000OOOO0[0]}{O0O0000O0O0O000O0.jkey}'#line:240
            O000O0OOOOO0O0O00 =f'http://{OOO0OO0O0000OOOO0[1]}/tuijian/do_read{OO0O00O00O0000OOO}'#line:241
            print (O000O0OOOOO0O0O00 )#line:242
            O00O00000000O0O0O =requests .get (O000O0OOOOO0O0O00 ,headers =OOO0OO0O0000OOOO0 [2 ])#line:243
            print ('-'*50 )#line:245
            O0OO0OOOOOO00O000 =O00O00000000O0O0O .json ()#line:246
            if O0OO0OOOOOO00O000 .get ('msg'):#line:247
                print ('弹出msg',O0OO0OOOOOO00O000 .get ('msg'))#line:248
            OO00OO0000OOO0000 =O0OO0OOOOOO00O000 .get ('url')#line:249
            if OO00OO0000OOO0000 =='close':#line:250
                print (f'阅读结果：{O0OO0OOOOOO00O000.get("success_msg","开始阅读或者异常")}')#line:251
                return True #line:252
            if 'weixin'in OO00OO0000OOO0000 :#line:253
                print (f'上一篇阅读结果：{O0OO0OOOOOO00O000.get("success_msg","开始阅读或者异常")}')#line:254
                OO0O0O00O00OO000O =O0OO0OOOOOO00O000 .get ('jkey')#line:255
                O0O0000O0O0O000O0 .jkey =f'&jkey={OO0O0O00O00OO000O}'#line:256
                OO000OOOO0O0O0OOO =getinfo (OO00OO0000OOO0000 )#line:257
                if O0OO00O0OOO0OOOO0 ==0 :#line:258
                    O000OO0O0OOOOOO00 =list (OO000OOOO0O0O0OOO )#line:259
                    O000OO0O0OOOOOO00 [4 ]='oneischeck'#line:260
                    if O0O0000O0O0O000O0 .testCheck (O000OO0O0OOOOOO00 ,OO00OO0000OOO0000 )==False :#line:261
                        return False #line:262
                    O0OO00O0OOO0OOOO0 =1 #line:264
                if O0O0000O0O0O000O0 .testCheck (OO000OOOO0O0O0OOO ,OO00OO0000OOO0000 )==False :#line:265
                    return False #line:266
                print ('开始本次阅读')#line:267
                OO0OOOOOOOO0OO0OO =random .randint (6 ,9 )#line:268
                print (f'本次模拟读{OO0OOOOOOOO0OO0OO}秒')#line:269
                time .sleep (OO0OOOOOOOO0OO0OO )#line:270
            else :#line:271
                print ('未知结果')#line:272
                print (O0OO0OOOOOO00O000 )#line:273
                break #line:274
    def testCheck (OO000O0O0O00OOO0O ,OOO000O00O00O0O0O ,O0OO00OOOO00O0000 ):#line:275
        if OOO000O00O00O0O0O [4 ]==[]:#line:276
            print (OO000O0O0O00OOO0O .name ,'这个链接没有获取到微信号id',O0OO00OOOO00O0000 )#line:277
            return True #line:278
        if checkDict .get (OOO000O00O00O0O0O [4 ])!=None :#line:279
            OO000O0O0O00OOO0O .setstatus ()#line:280
            for OO000O0O0O0OO0OO0 in range (60 ):#line:281
                if OO000O0O0O0OO0OO0 %30 ==0 :#line:282
                    push (f'可乐阅读过检测:{OO000O0O0O00OOO0O.name}',O0OO00OOOO00O0000 ,OOO000O00O00O0O0O [3 ],'zhyd',OO000O0O0O00OOO0O .uids ,OO000O0O0O00OOO0O .key )#line:283
                O0000000OOOO0OO00 =OO000O0O0O00OOO0O .getstatus ()#line:284
                if O0000000OOOO0OO00 =='0':#line:285
                    print (OO000O0O0O00OOO0O .name ,'过检测文章已经阅读')#line:286
                    return True #line:287
                elif O0000000OOOO0OO00 =='1':#line:288
                    print (OO000O0O0O00OOO0O .name ,f'正在等待过检测文章阅读结果{OO000O0O0O0OO0OO0}秒。。。')#line:289
                    time .sleep (1 )#line:290
                else :#line:291
                    print (OO000O0O0O00OOO0O .name ,O0000000OOOO0OO00 )#line:292
                    print (OO000O0O0O00OOO0O .name ,'服务器异常')#line:293
                    return False #line:294
            print (OO000O0O0O00OOO0O .name ,'过检测超时中止脚本防止黑号')#line:295
            return False #line:296
        else :#line:297
            return True #line:298
    def withdrawal (OO0000O0000OO00OO ):#line:299
        O00OOOO0O0OO000OO ='http://ab1115072245.c0722451115.ww1112001.cn/withdrawal'#line:300
        OOOOO0OO0O0O0O0O0 =requests .get (O00OOOO0O0OO000OO ,headers =OO0000O0000OO00OO .headers )#line:301
        O000O0OOOO00OOOOO =OOOOO0OO0O0O0O0O0 .json ()#line:302
        if O000O0OOOO00OOOOO .get ('code')==0 :#line:303
            O0O00OOOOOOO00OOO =O000O0OOOO00OOOOO ['data']['user']['username']#line:304
            O0OOOO0O0O000O00O =O000O0OOOO00OOOOO ['data']['user']['score']#line:305
            print (f'{O0O00OOOOOOO00OOO}:{O0OOOO0O0O000O00O}')#line:306
        else :#line:307
            print (O000O0OOOO00OOOOO )#line:308
    def run (OOOOO0OOOO0000000 ):#line:309
        OOOOO0OOOO0000000 .do_read ()#line:310
        time .sleep (2 )#line:311
        OOOOO0OOOO0000000 .withdrawal ()#line:312
def getEnv (O00OOOO000OO0OOOO ):#line:313
    O0000OO0O00O00OOO =os .getenv (O00OOOO000OO0OOOO )#line:314
    if O0000OO0O00O00OOO ==None :#line:315
        print (f'{O00OOOO000OO0OOOO}没有获取到，使用本地参数')#line:316
        return False #line:317
    try :#line:318
        O0000OO0O00O00OOO =json .loads (O0000OO0O00O00OOO .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:319
        return O0000OO0O00O00OOO #line:320
    except Exception as OO0000OOOO0O000OO :#line:321
        print ('错误:',OO0000OOOO0O000OO )#line:322
        print ('你填写的变量是:',O0000OO0O00O00OOO )#line:323
        print ('请检查变量参数是否填写正确')#line:324
        print (f'{O00OOOO000OO0OOOO}使用本地参数')#line:325
if __name__ =='__main__':#line:326
    loc_push_config = {"printf": 1, "threadingf": 0, "appToken": "AT_9KCYwpxyu6JC"}
    loc_klydconfig = [
        {'name':'备注名','cookie':'PHPSESSID=mm4o08oh0; udtauth3=8b31JfOt6FYSJqY','key':'xxxx','uids':'xxxxx'},
        #{'name': '备注名', 'cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
        #{'name': '备注名', 'cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
    ]
    push_config =getEnv ('push_config')#line:334
    if push_config ==False :push_config =loc_push_config #line:335
    print (push_config )#line:336
    klydconfig =getEnv ('klydconfig')#line:337
    if klydconfig ==False :klydconfig =loc_klydconfig #line:338
    print (klydconfig )#line:339
    printf =push_config ['printf']#line:340
    appToken =push_config ['appToken']#line:341
    threadingf =push_config ['threadingf']#line:342
    getmsg ()#line:343
    tl =[]#line:344
    for cg in klydconfig :#line:345
        print ('*'*50 )#line:346
        print (f'开始执行{cg["name"]}')#line:347
        api =WXYD (cg )#line:348
        t =threading .Thread (target =api .run ,args =())#line:349
        tl .append (t )#line:350
        t .start ()#line:351
        time .sleep (0.5 )#line:352
    for t in tl :#line:353
        t .join ()#line:354
    print ('全部账号执行完成')#line:355
    time .sleep (15 )#line:356
