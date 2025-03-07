## 建立虛擬環境（python 3.9）
Step 1. 於 VScode 安裝虛擬環境 .venv

```
開啟指令 Command+Shift+P

Python: Select Interpreter --> 建立虛擬環境 --> Python 3.9.21
```

Step 2. 安裝 Django 2.x
```

pip install "django>=2.2,<3.0"

```
Step 3. 開啟 Django 專案
```

django-admin startproject <專案名稱>
cd <專案名稱>

Ex.
django-admin startproject week
cd week

```
Step 4. 啟動伺服器
```

python manage.py runserver

```
## 渲染 index.html 步驟
Step 1. 於 setting.py 的 INSTALLED_APPS 中加入：
```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '專案名稱',  # 新增這一行
]

Ex.
INSTALLED_APPS = [
    ...,
    'week',  # 新增這一行
]

```
Step 2. 於與 setting.py 同級目錄下建立 templates 資料夾

Step 3. 於 templates 資料夾下建立 index.html

Step 4. 於 setting.py 同級目錄下建立 view.py (若無，則自行新增)
```

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

```
Step 5. 設定 URL，於 setting.py 同級目錄下的 urls.py (若無，則自行新增)
```

urlpatterns = [
    ...,
    path('', index, name='index'),
]

```
完成以上步驟，重啟伺服器
即可藉由 http://127.0.0.1:8000/ 訪問 index.html

