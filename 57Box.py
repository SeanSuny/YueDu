"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
57Box_0.3
微信小程序  57Box   玩法：完成基础任务抽免费箱子
登录微信小程序授权手机号然后下载APP设置密码
export BOX_data=手机号@密码
多账号用'===='隔开 例 账号1====账号2
cron: 12 8 * * *

免费矿石箱 ID：586  80矿石
小块巧克力 ID：590  120矿石
泡面搭档 ID：588  199矿石  
饮料盒子 ID：589  199矿石
"""

lottery = 0  # 抽盒开关 1开启 0关闭
box_id = 586  #箱子id
import os
import time
import execjs
import hashlib
import requests
from notify import send

accounts = os.getenv("BOX_data")
if accounts is None:
    print('你没有填入BOX_data，咋运行？')
    exit()
accounts_list = accounts.split('====')
num_of_accounts = len(accounts_list)
print(f"获取到 {num_of_accounts} 个账号")
result_list = []  # 存储所有账号的签到和分享结果
for i, account in enumerate(accounts_list, start=1):
    values = account.split('@')
    mobile, password = values[0], values[1]
    print(f"\n{'=' * 8}开始执行账号[{mobile}]{'=' * 8}")
    url = "https://www.57box.cn/app/index.php?i=2&t=0&v=1&from=wxapp&c=entry&a=wxapp&do=login&m=greatriver_lottery_operation"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/47) uni-app",
    }

    data = {
        "mobile": mobile,
        "password": password,
        "password2": "",
        "code": "",
        "invite_uid": "0",
        "source": "app"
    }

    response = requests.post(url, headers=headers, data=data).json()
    if response['errno'] == 0:
        print(f"{response['message']}")
        token = response['data']['token']
        print(f"{'=' * 12}开始每日答题{'=' * 12}")
        time.sleep(3)
        url = "https://www.57box.cn/app/index.php"
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/47) uni-app",
        }
        params = {
                "i": "2",
                "t": "0",
                "v": "1",
                "from": "wxapp",
                "c": "entry",
                "a": "wxapp",
                "do": "getuserinfo",
                "m": "greatriver_lottery_operation",
                "token": token,
                "source": "app",
                
            }
        response = requests.get(url, headers=headers, params=params).json()
        id = response['data']['id']
        print(id)
        time.sleep(5)
        jsstr = '''
                function add() {
                    s = new Date,
                    l = s.getFullYear(),
                    c = s.getMonth() + 1,
                    r = s.getDate(),
                    d = s.getHours(),
                    u = s.getMinutes(),
                    g = (s.getSeconds(), l + "-" + c + "-" + r + " " + d + ":" + u),
                    p = new Date(g.replace(/-/g, "/")).getTime();
                    p = p / 1e3
                return p;
            }'''
        
        js = execjs.compile(jsstr)
        
        result = js.call('add')
        str_to_encrypt = f'{result}{id}box57'
        md5 = hashlib.md5()
        md5.update(str_to_encrypt.encode())
        result = md5.hexdigest()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/47) uni-app",
        }
        params = {
                "i": "2",
                "t": "0",
                "v": "1",
                "from": "wxapp",
                "c": "entry",
                "a": "wxapp",
                "do": "uptaskinfo",
                "m": "greatriver_lottery_operation",
                "radomstr": result,
                "id": "30",
                "answer": "用于商城和折扣商城兑换商品",
                "token": token,
                "source": "app",
                
            }
        response = requests.get(url, headers=headers, params=params).json()
        state = "每日答题一"
        if response['errno'] == 999:
            print(f"{state}---{response['message']}")
        elif response['errno'] == 0:
            print(f"{state}---{response['message']}")
        else:
            print(f"{state}错误未知{response}")
            break
        time.sleep(5)
        jsstr = '''
                function add() {
                    s = new Date,
                    l = s.getFullYear(),
                    c = s.getMonth() + 1,
                    r = s.getDate(),
                    d = s.getHours(),
                    u = s.getMinutes(),
                    g = (s.getSeconds(), l + "-" + c + "-" + r + " " + d + ":" + u),
                    p = new Date(g.replace(/-/g, "/")).getTime();
                    p = p / 1e3
                return p;
            }'''
        
        js = execjs.compile(jsstr)
        
        result = js.call('add')
        str_to_encrypt = f'{result}{id}box57'
        md5 = hashlib.md5()
        md5.update(str_to_encrypt.encode())
        result = md5.hexdigest()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/47) uni-app",
        }
        params = {
                "i": "2",
                "t": "0",
                "v": "1",
                "from": "wxapp",
                "c": "entry",
                "a": "wxapp",
                "do": "uptaskinfo",
                "m": "greatriver_lottery_operation",
                "radomstr": result,
                "id": "42",
                "answer": "通过开盒获得每1000能量石可以兑换1水晶",
                "token": token,
                "source": "app",
                
            }
        response = requests.get(url, headers=headers, params=params).json()
        state = "每日答题二"
        if response['errno'] == 999:
            print(f"{state}---{response['message']}")
        elif response['errno'] == 0:
            print(f"{state}---{response['message']}")
        else:
            print(f"{state}错误未知{response}")
            break
        print(f"{'=' * 12}获取账号信息{'=' * 12}")
        url = f"https://www.57box.cn/app/index.php?i=2&t=0&v=1&from=wxapp&c=entry&a=wxapp&do=getuserinfo&&token={token}"
        data = {
            "m": "greatriver_lottery_operation",
            "title": "",
        }
        response = requests.post(url, headers=headers, data=data).json()
        if response['errno'] == 999:
            print(f"{response['message']}")
        elif response['errno'] == 0:
            nickname = response['data']['nickname']
            integral_str = response['data']['integral']
            try:
                integral = int(float(integral_str))
                print(f"Name:{nickname}---矿石余额:{integral}")
                result_list.append(f"用户:{nickname}---矿石余额:{integral}")
            except ValueError:
                print(f"无效的integral值: {integral_str}")
        else:
            print(f"错误未知{response}")
            break
        if lottery == 1:  # 开始抽奖
            print(f"{'=' * 12}执行开盒{'=' * 12}")
            for i in range(10):
                url = "https://www.57box.cn/app/index.php"
                params = {
                    "i": "2",
                    "t": "0",
                    "v": "1",
                    "from": "wxapp",
                    "c": "entry",
                    "a": "wxapp",
                    "do": "openthebox",
                    "token": token,
                    "m": "greatriver_lottery_operation",
                    "box_id": box_id,
                    "paytype": "1",
                    "answer": "",
                    "num": 1
                }
                response = requests.post(url, headers=headers, data=params).json()
                if response['errno'] == 0:
                    complete_prize_title = response['data']['prizes_data'][0]['complete_prize_title']
                    prize_market_price = response['data']['prizes_data'][0]['prize_market_price']
                    print(f"{response['message']}---{complete_prize_title}  市场价:{prize_market_price}")
                elif response['errno'] == 999:
                    print(f"{response['message']}")
                    break
                else:
                    print(f"错误未知{response}")
                    break
            print(f"开盒完毕")
            url = f"https://www.57box.cn/app/index.php?i=2&t=0&v=1&from=wxapp&c=entry&a=wxapp&do=uptaskinfo&&token={token}"
            data = {
                "m": "greatriver_lottery_operation",
                "id": "39",
                "answer": ""
            }
            response = requests.post(url, headers=headers, data=data).json()
            state = "开盒看视频领矿石"
            if response['errno'] == 999:
                print(f"{state}---{response['message']}")
            elif response['errno'] == 0:
                print(f"{state}---{response['message']}")
            else:
                print(f"{state}错误未知{response}")
                break

        elif lottery == 0:
            print(f"{'=' * 12}不执行开鞋盒{'=' * 12}")
        print(f"当前奖品:")
        url = "https://www.57box.cn/app/index.php"

        params = {
            "i": "2",
            "t": "0",
            "v": "1",
            "from": "wxapp",
            "c": "entry",
            "a": "wxapp",
            "do": "getmemberprizes",
            "token": token,
            "m": "greatriver_lottery_operation",
            "page": "0",
            "type": "1",
            "prize_level": "1",
        }

        response = requests.get(url, headers=headers, params=params).json()

        all_prizes = response['data']

        for prize in all_prizes:
            prize_title = prize['prize']['complete_prize_title']
            prizes_count = prize['prizes_count']
            prize_market_price = prize['prize']['prize_market_price']
            print(f"{prize_title} 市场价:{prize_market_price}元 数量:x{prizes_count}")
            result_list.append(f"用户:{nickname}---当前奖品:{prize_title} 数量:x{prizes_count}")
    elif response['errno'] == 999:
        print(f"{response['message']}")
        break
    else:
        print(f"错误未知{response}")
        break
title = '57Box'
result_str = '\n'.join(result_list)
send(title, result_str)
