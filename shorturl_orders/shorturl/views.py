from django.shortcuts import render,redirect ,render_to_response
from shorturl.models import Url
from django.http import JsonResponse ,HttpResponse
import random ,string
import re

#短網址頁面
def short_url_page(request):
    if request.method == 'POST':
        longUrl = request.POST.get('longUrl')
        
        #判斷是否為網址格式
        if not re.match(r'^https?:/{2}\w.+$', longUrl):
            return JsonResponse({'status':0,'info':'非合法網址'})
        
        #資料庫取資料
        Short_url_Data = Url.objects.select_related()
        
        #篩選相符長連結
        findData = Short_url_Data.filter(ori_url=longUrl)
        
        #篩選相符
        if findData.exists():
            #回傳相對應短連結
            return JsonResponse({'status':1,'info':str(findData.first().short_url)})
        #不相符
        else:
            
            #賦予此長連結的短連結
            randomString = ''.join(random.choice(string.ascii_letters) for x in range(10))
            #重覆迴圈
            while Short_url_Data.filter(short_url=randomString).exists():
                randomString = ''.join(random.choice(string.ascii_letters) for x in range(10))
            #新增資料
            Url(
               ori_url =  longUrl,
               short_url = randomString
            ).save()
            #回傳相對應短連結
            return JsonResponse({'status':1,'info': randomString})
    
    return render(request,'shortUrl/shortUrl.html')

#短網址跳轉
def short_url_redrict(request ,urlCode):

    Redirect_Data = Url.objects.all()
    #篩選資料
    findData = Redirect_Data.filter(short_url=urlCode)
    #資料相符
    if findData.exists():
        #進行跳轉
        return redirect(findData.first().ori_url)
    else:
        #不相符提示
        return HttpResponse('無此紀錄')
    
    return render(request,'shortUrl/shortUrl.html')

#==============================================================================================================================#
#order頁面
def order_page(request):
    #產出資料
    if request.method == 'POST':
        return JsonResponse({
            'orders': [
                {
                    'name': 'Livi優活 抽取式衛生紙(100抽x10包x10串/箱)',
                    'logo': 'https://static.oopocket.com/store/iconTreemall@3x.png',
                    'status': {
                        'code': 3,
                        'type': '已取消'
                    },
                    'date': '107/6/12'
                },
                {
                    'name': 'BALMUDA The Toaster 百慕達烤麵包機-黑色',
                    'logo': 'https://static.oopocket.com/store/iconTreemall@3x.png',
                    'status': {
                        'code': 2,
                        'type': '已成立'
                    },
                    'date': '108/7/21'
                },
                {
                    'name': '贈-短慧萬用鍋HD2133+三合一濾網「LG樂金」韓國原裝...',
                    'logo': 'https://static.oopocket.com/store/iconTreemall@3x.png',
                    'status': {
                        'code': 1,
                        'type': '處理中'
                    },
                    'date': '108/6/2'
                },
                {
                    'name': 'Apple AirPds 2',
                    'logo': 'https://static.oopocket.com/store/iconTreemall@3x.png',
                    'status': {
                        'code': 4,
                        'type': '已送達'
                    },
                    'date': '108/3/02'
                }
            ]
        })
    return render(request,'order/order_page.html')