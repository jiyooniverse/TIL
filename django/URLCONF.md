## URLCONF

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

```

` urlpatterns`는 `URLPattern` 의 `List`

- URLPattern

```python
class URLPattern:
    def __init__(self, pattern, callback, default_args=None, name=None):
        self.pattern = pattern
        self.callback = callback  # the view
        self.default_args = default_args or {}
        self.name = name
        
        ...
```



`path` 함수는 `_path` 함수의 ` partial`(부분적으로 렌더링한것?, Pattern 인자에 `path`함수 두번째 값 넣어줌)로  `path` 함수의 `return` 값은 `URLPattern`

```python
def _path(route, view, kwargs=None, name=None, Pattern=None):
    if isinstance(view, (list, tuple)):
        # For include(...) processing.
        pattern = Pattern(route, is_endpoint=False)
        urlconf_module, app_name, namespace = view
        return URLResolver(
            pattern,
            urlconf_module,
            kwargs,
            app_name=app_name,
            namespace=namespace,
        )
    elif callable(view):
        pattern = Pattern(route, name=name, is_endpoint=True)
        return URLPattern(pattern, view, kwargs, name)
    else:
        raise TypeError('view must be a callable or a list/tuple in the case of include().')
```



`include` 함수의 return 값 (urlconf_module, app_name, namespace)

