# 초간단 홈페이지 만들기_ver.django

> 빠르게 홈페이지 아웃라인을 만드는 법을 정리한 문서입니다. 

해당 문서는 **Atom**과 **django**의 설치가 필요하며, **Python** 기반으로 진행됩니다. 

<img width="240" alt="atom" src="https://user-images.githubusercontent.com/58945760/98442653-2ca0d880-2149-11eb-9db0-e429a6750dfd.png" style="zoom: 67%;" >

<img src="https://user-images.githubusercontent.com/58945760/98442657-39253100-2149-11eb-81d4-77ab2bb254d6.png" alt="unnamed" style="zoom:20%;" />

## 0. 사전 설치

Atom 설치는 생략합니다. 이하의 내용에서는 웹 서비스를 개발할 수 있는 최소한의 환경을 세팅하는 법부터 설명합니다. 앞의 프로그램 외 아무것도 설치가 되어있지 않은 상황이라면 1번으로, 이미 work_django 폴더, 가상환경이 설치되어 있다면 2번으로 GO!

## 1. 초기 환경 세팅

```shell
$ cd / # 한 방에 C:까지 나갈 수 있다!
$ mkdir work_django # work_django 폴더 만들기
$ cd work_django 
$ mkdir django_mldl # django_mldl 폴더 만들기
$ cd django_mldl
$ pip install virtualenv==16.7.7 # 가상환경을 만들어주는 라이브러리 설치
$ virtualenv django_env # django_env라는 이름의 가상 환경 생성
$ django_env\Scripts\activate # Scripts 폴더 내의 activate 파일 실행==가상환경 활성화
$ pip install django==2.2.6 # django 설치!
```

## 2. 새로운 프로젝트(홈페이지) 만들기

이미 가상환경과 django 설치 등 환경 세팅이 완료된 상태라면 아래의 코드부터 참고하면 된다. 

```shell
$ cd / # C:로 이동
$ cd work_django 
$ cd django_mldl # 작업 폴더로 이동
$ django_env\Scripts\activate # 가상 환경 활성화
```



```shell
$ django-admin startproject sample_page # sample_page라는 새로운 프로젝트(웹페이지) 생성, sample_page 폴더 생성
```



```
# sample_site 프로젝트 파일 구성도
├── 📂 work_django
└── 📂 django_mldl
└── 📂 sample_site
    ├── 📂 sample_page
    |    ├── 📂 templates
    |        ├── 📄 default.html
    |        └── 📄 index.html
    ├── 📂 static
    |    └── 📂 sample_page
    |         ├── 📄 style.js
    |         └── 📄 style.css
    |        
    ├── 📂 sample_site
    |   ├── 📄 settings.py
    |   ├── 📄 urls.py
    |   ├── 📄 __init__.py
    |   └── 📄 wsgi.py
    ├── 📄 db.sqlite3
    └── 📄 manage.py
```

### 2.1 기본 

- `settings.py` 수정 및 추가

```
LANGUAGE_CODE = 'en-us' -> 'ko-kr'로 수정
TIME_ZONE = 'UTC' -> 'Asia/Seoul'로 수정

STATIC_ROOT = os.path.join(BASE_DIR, 'static') 추가
```



```shell
$ cd sample_page # sample_page 폴더로 이동
$ python manage.py startapp sample_site 

# 앱이 여러 개인 경우
$ cd apps
$ django-admin startapp app1 # app2, app3...
```

- Atom에서 `settings.py` 수정

```shell
$ cd /
$ cd work_django
$ cd sample_site
$ django_env\Scripts\activate # 가상환경 열기 # 자동완성 가능
$ python manage.py runserver # 생성한 프로젝트 로컬에서 확인
```

### 2.2 기초

- Atom에서 `urls.py` 수정

```python
from django.contrib import admin
from django.urls import path
from sample_site import views # 추가!

urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지
    path('default/', views.result) # 추가! # 새로 만들 페이지
]
```



- `views.py` 수정

```python
from django.shortcuts import render

# Create your views here.
def result(request):
    return render(request, 'sample_site/default.html') # default.html 페이지로 이동
```



- Template 파일 만들기 => 📂sample_site 내 📂templates 폴더 생성 => 📂templates 폴더 안에 sample_site 생성 => default.html 생성

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Test Page</title>
  </head>
  <body>
    <h1>아직 페이지가 만들어지지 않았습니다.</h1>
  </body>
</html>

```

default 페이지를 이렇게 만들어 놓은 후 cmd로 돌아와 runserver를 실행한다.

```shell 
$ python manage.py runserver # 수정한 웹페이지 확인, 디버깅
```

이렇게 하고 http://127.0.0.1:8000/로 들어가면 404 에러가 나 있을 것이다.  http://127.0.0.1:8000/default/ 로 들어가야 default.html이 제대로 반영된 것을 볼 수 있다. 만약 원래 주소에 이 페이지가 뜨게 하고 싶다면 아래와 같이 urls.py를 수정하면 된다. 

```python
from django.contrib import admin
from django.urls import path
from sample_site import views 

urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지
    path('', views.result) # '' 따옴표 사이를 빈 공간으로 두면 http://127.0.0.1:8000/에 default.html이 그대로 표시된다. 
]
```





### 2.3 css, js 추가

📂sample_site 폴더 안에 📂static 폴더 생성=>📂static 폴더 안에 📂example_site 폴더를 만들고 그 안에 style.css 파일 생성(경로 example_site/static/example_site/style.css)

하고 싶은 디자인이나 스타일에 맞추어 css 파일을 채운다. 

javascript의 경우 똑같은 경로에 style.js파일을 만들어 저장하고 마찬가지로 바꾸고 싶은 스타일에 맞는 코드로 파일을 채워주면 된다.

### 2.4 css, js HTML 문서에 적용

먼저 해당 css와 js를 적용하고 싶은 html 파일을 찾는다. 그리고 맨 윗줄에 아래와 같이 적는다. 

**css**

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'sample_site/style.css' %}" />
```

**javascript**

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'sample_site/style.js' %}" />
```

그리고 cmd를 켠다. 만약 이미 서버가 켜져 있는 상황이라면 Ctrl + C로 서버를 종료한다. 그리고 cmd에서 아래와 같이 입력한다. 

```shell
$ python manage.py collectstatic # static 파일 적용
$ python manage.py runserver # 결과 확인
```

### 2.5 모든 페이지에 똑같은 디자인 씌우기

sample_site/template/sample_site에 base.html을 생성한다. 

**base.html**

```html
↑ 이 위로 적용될 디자인이나 속성 등을 추가하면 된다. ex) <link rel="stylesheet" type="text/css" href="{% static 'sample_site/style.css' %}" />
{% block content %}
'''
이 디자인이 적용될 html 파일들의 내용
'''
{% endblock %}
↓ 아래도 추가 가능
```

**타 html 파일들**

```html
{% extends 'sample_site/base.html' %}
{% block content %}

'''
파일별 코드
'''

{% endblock %}
```

이렇게 해준 후 cmd에서 python manage.py runserver로 디자인이 제대로 적용되었는지 확인해본다.

```shell
$ python manage.py collectstatic # static 파일 적용
$ python manage.py runserver # 결과 확인
```



