## Static/ Media

`static`은 정적 파일들을 모아놓은 폴더이며 `media`폴더에는 사용자를 통해 사이트에 업로드되는 파일들이 모인다.

## 1. Static

static load 시 `<app_name>/static` 경로를 탐색하기 때문에 그 외 경로는 `settings.py`에 `STATICFILES_DIRS`을 추가하여야한다.  :warning: **오타 조심** 

- `settings.py`

  ```python
  STATICFILES_DIRS = [
      BASE_DIR/ 'static',
  ]
  ```

  

static 파일을 사용할 html 파일에 static을 load한다.

- `--.html`

  ```html
  {% load static %}
  
  ...
  
  <img src="{% static 'images/default-imag.jpg' %}" alt="" width="100px">
  ```

  최상단에 `load` 태그 작성. `extends` 태그 존재 시 `extends` 태그 다음 작성. `img` 태그 안 `src`에 `static` 폴더 다음 부터 이미지 경로 작성.

  `app` 폴더 안에 `static` 파일 저장 시 `static/<app_name>` 경로에 넣어준다. (다른 `app`의 `static` 파일들과 이름이 동일한 경우를 대비하여 위와 같이 설정해준다.)

  

## 2. Media

프로젝트 폴더 내부 `uploaded_files`폴더로 업로드 파일 저장하고자 할 때 설정

- `settings.py`

  ```python
  MEDIA_ROOT = BASE_DIR / 'media'
  MEDIA_URL = '/media/'
  ```

  

1.  `model`에 `image` 관련 필드 추가하기

   - `models.py`

     ```python
     class MyApp(models.Model):
         ...
         image = models.ImageField(blank=True, upload_to='img/')
     ```

     `blank=True` 속성은 기존  `model`에 `image` 추가 시 기존 있던 `record`의 `image` field 값을 `blank` 처리하여 오류없이 생성하기 위해서 이며, `upload_to='img/'` 속성은 `media`폴더 내의 `image`파일 추가 경로를 설정해준다.

     ** `upload_to`  설정 방법

     ```python
     # 1. 날짜로 하위 폴더 설정
     image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
     
     # 2. 함수로 폴더 설정
     def image_path(instance, filename):
         return f'user_{instance.pk}/{filename}'
     
     
     image = models.ImageField(blank=True, upload_to=image_path)
     ```

      

     ** `ImageField` 사용 시 `migration`을 하면 `Pillow`를 설치하라는 에러 메세지가 발생한다. `pytyon -m pip install Pillow` 실행 후 `migration`을 완료해준다.

2. `image` 데이터 받기

   1. `form` 태그에서 `image` /`file`데이터 전송 시 파일에 대한 내용도 함께 전송하기 위해 `enctype="multipart/form-data"` 속성을 사용하여야 한다.

      ```django
        <form action="" method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="BUTTON">
        </form>
      ```

      **해당 속성에 따른 `Request information`  비교**

      - 미 적용 시 : <img src="Static, Media.assets/image-20210926215136673.png" alt="image-20210926215136673" style="width:250px;" />

      - 적용 시 :  <img src="Static, Media.assets/image-20210926215336822.png" alt="image-20210926215336822" style="width:305px;" />

   2.  위와 연결되어 `FILES`에 `image` 데이터가 담겨 오기때문에 `request.POST` 데이터 뿐만 아니라 `request.FILES`의 files 내용도 받아와야 한다.

      ```python
      form = MyForm(data=request.POST, files=request.FILES)
      ```

    

   위 과정을 통해 `database`의 `image` 필드에  image 경로가 저장 되고 지정한 `media`폴더 경로에 image 파일이 저장된다.

3. `image` 데이터 보여주기

   `2`번 과정을 통해 우리 server에는 사용자가 upload한 image 데이터가 저장되어 있다. `database`에는 `media`폴더 경로 하위 image 경로가 저장되어 있으며, **이 경로를 `url`로 보내 image를 요청할 것이다.** 

   이를 위해 설정해야 할 것 

   1. `project`의 `urlpatterns`에 `media`폴더 관련 `url`도 등록한다.

      - `urls.py`

      ```python
      from django.contrib import admin
      from django.urls import path, include
      from django.conf import settings
      from django.conf.urls.static import static
      
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          ...,
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```

      `settings.py` 에서 `MEDIA`관련 등록했던 값들을 통해 url 주소를 설정한다.

   2. `image` 의 `src`를 설정 시 url 주소를 사용해주면 된다.

      `settings.py`를 통해 url 주소를 `/media/`로 사용한 것을 알고 있기때문에 이를 이용해서 명시적으로 설정할 수도 있다.

      ```django
      <img src="/media/{{ myrecord.image }}" alt="">
      ```

      `MyApp` 클래스의 instance `myrecord`의 `image` 필드에 저장되어 있는 경로 값을 이용하여 `media` url을 생성하여 이미지를 불러올 수 있다.

      하지만 `MEDIA_URL`값은 `settings.py`를 통해 변경 가능하므로 해당 값을 저장하고 있는 url 속성을 사용할 수 있다.  

      ```django
      <img src="{{ myrecord.image.url }}" alt="">
      ```

      ** [장고 문서 : How do I use image and file fields?](https://docs.djangoproject.com/en/3.2/faq/usage/#how-do-i-use-image-and-file-fields)



