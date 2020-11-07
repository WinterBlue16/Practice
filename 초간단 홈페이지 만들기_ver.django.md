# 초간단 홈페이지 만들기_ver.django

> 빠르게 홈페이지 아웃라인을 만드는 법을 정리한 문서입니다. 

해당 문서는 **Atom**과 **django**의 설치가 필요하며, **Python** 기반으로 진행됩니다. 

<img width="240" alt="atom" src="https://user-images.githubusercontent.com/58945760/98442653-2ca0d880-2149-11eb-9db0-e429a6750dfd.png" style="zoom: 67%;" >

<img src="https://user-images.githubusercontent.com/58945760/98442657-39253100-2149-11eb-81d4-77ab2bb254d6.png" alt="unnamed" style="zoom:33%;" />

## 0. 사전 설치

Atom 설치는 생략합니다. 이하의 내용에서는 웹 서비스를 개발할 수 있는 최소한의 환경을 세팅하는 법부터 설명합니다. 앞의 프로그램 외 아무것도 설치가 되어있지 않은 상황이라면 1번으로, 이미 work_django 폴더, 가상환경이 설치되어 있다면 2번으로 GO!

## 1. 환경 세팅

```shell
$ cd / # 한 방에 C:까지 나갈 수 있다!
$ mkdir work_django # work_django 폴더 만들기
$ cd work_django 
$ mkdir django_mldl # django_mldl 폴더 만들기
$ cd django_mldl
$ pip install virtualenv==16.7.7 # 가상환경을 만들어주는 라이브러리 설치
$ virtual django_env # django_env라는 이름의 가상 환경 생성
$ django_env\Scripts\activate # Scripts 폴더 내의 activate 파일 실행==가상환경 활성화
$ pip install django==2.2.6 # django 설치!
```

## 2. 새로운 프로젝트(홈페이지) 만들기

```shell
$ django-admin startproject sample_site # sample_site이라는 새로운 프로젝트(웹페이지) 생성, sample_site 폴더 생성
```



```
# sample_site 프로젝트 파일 구성도
├── 📂 work_django
└── 📂 django_mldl
└── 📂 sample_site
    ├── 📂 sample_site
    |    ├── 📂 templates
    |        ├── 📄 default.html
    |        └── 📄 index.html
    ├── 📂 static
    |    └── 📂 sample_site
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

`settings.py` 수정

```shell
$ python manage.py startapp sample_site
```

Atom에서 `settings.py` 수정

```shell
$ cd /
$ cd work_django
$ cd sample_site
$ django_env\Scripts\activate # 가상환경 열기 # 자동완성 가능
$ python manage.py runserver # 생성한 프로젝트 로컬에서 확인
```

### 2.2 기초

Atom에서 `urls.py`, `views.py` 수정

Template 파일 만들기 => 📂sample_site 내 📂templates 폴더 생성 => 📂templates 폴더 안에 sample_site 생성 => default.html 생성

```shell 
$ python manage.py runserver # 수정한 웹페이지 확인, 디버깅
```

### 2.3 css, js 추가

📂sample_site 폴더 안에 📂static 폴더 생성=>📂static 폴더 안에 📂example_site 폴더를 만들고 그 안에 style.css 파일 생성(경로 example_site/static/example_site/style.css)

하고 싶은 디자인이나 스타일에 맞추어 css 파일을 채운다. 

javascript의 경우 똑같은 경로에 style.js파일을 만들어 저장하고 마찬가지로 바꾸고 싶은 스타일에 맞는 코드로 파일을 채워주면 된다.

### 2.4 css, js html에 적용

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



