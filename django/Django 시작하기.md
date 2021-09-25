# Django 시작하기

- 가상 환경 설정

  ```bash
  python -m venv venv
  ```

  프로젝트 시작 폴더에서 해당 명령어 실행 시 프로젝트 폴더 안에 `venv` 폴더 생성 및 가상환경 설정

- vs code에서 가상 환경 활성화

  ```bash
  source venv/Scripts/activate
  ```

- 설치 항목 확인하기

  ```bash
  pip list
  ```

- `requirements.txt` 파일 제공 시 설치하기

  ```bash
  pip install -r requirements.txt
  ```

- `django` 프로젝트 생성하기

  ```bash
  django-admin startproject <project-name> .
  ```

  `.`  사용 시 해당 폴더 안에 프로젝트 생성됨. `.` 생략 시 폴더 안에 <project-name>폴더 안에 프로젝트 생성됨.

- `app` 생성하기

  ```bash
  python manage.py startapp <app-name>
  ```

  `app`은 `project` 의 기능별로 구분하여 생성한다. 

  `app` 생성 후 `<project-name>/settings.py`의 `INSTALLED_APPS`에 등록해준다.

  ```python
  # Application definition
  
  INSTALLED_APPS = [
      '<app-name>',	# 사용자 정의 app
      
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```



- 서버 실행하기

  ```bash
  python manage.py runserver
  ```

  

- `admin` 계정 생성하기

  ```bash
  python manage.py createsuperuser
  ```

  `Username` 입력, `Email address`  입력하지 않아도 됨. `Password` 입력. 

  `http://127.0.0.1:8000/admin`  url에서 로그인 가능



- `app`에서 `model` 생성 후 `database`에  적용하기

  ```bash
  python manage.py makemigrations
  ```

  `model`의 변경점들을 `000x.py` 파일로 생성한다.

  ```bash
  python manage.py migrate
  ```

  `migration`들을 `database`에 적용시킨다.



# Django App 작성하기

1. `<project-name>/urls.py` 

   `urlpatterns`는 `views`로 `URLs`을 라우팅하는 리스트이다. 

   나의 `app`의 `URLconf`도 프로젝트의 `urls.py`에 등록해준다.  다른 `URLconf`를 포함시키는 방법은 다음과 같다. 

   ```python
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('accounts/', include('accounts.urls')),
   ]
   ```

2. `<my-app>/urls.py` 에 `<my-app>`에서 