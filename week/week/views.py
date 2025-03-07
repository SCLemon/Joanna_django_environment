from django.shortcuts import render
from datetime import datetime

def index(request):
    current_time = datetime.now().strftime('%Y 年 %m 月 %d 日 %H:%M')
    messages = [
        '生活就是一場無法預測的旅程，每一步都充滿了無限的可能性，雖然很多時候，這些可能性也只是未知的選擇。',
        '每當你走過街角，世界似乎就會向你展開一個全新的面貌，無論你是否準備好去迎接。',
        '有時候，靜下來思考，也許會發現，自己一直在走一條循環的路，但這也並不意味著不值得走。',
        '生活中的每一個小細節，都似乎在告訴我們，未來並不是一條直線，而是充滿了曲折的岔路。',
        '我們都在追求一個看似無法觸及的目標，但也許那個目標根本就不存在，只是我們自己心中的一個影像。'
    ]
    return render(request, 'index.html',{'current_time': current_time, 'messages': messages})
