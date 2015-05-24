# django-third-party - Third party code made easy

django-third-party is a simple django app for allowing you to add third party javascript and css based on a python regular expression.

##Features
###Current
* Add javascript based on url
* URL matching with python regex
* Add JavaScript to either Header or Footer

### Future
* Add support for CSS

##Quickstart
Install django-third-party

```bash
$ pip install django-third-party
```

Add `django-third-party` to `INSTALLED_APPS`:

```python
INSTALLED_APPS += (
  "djthirdparty",
)
```

Add `djthirdparty.context_processors.custom_content` to `template_context_processors`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'djthirdparty.context_processors.custom_content',
            ],
        },
    },
]
```

Add javascript header and footer to your base templates:

```jinja
    {% if custom_javascript_header %}
    <script type="text/javascript" charset="utf-8">
      {{ custom_javascript_header|safe }}
    </script>
    {% endif %}
  </head>
```
```jinja
    {% if custom_javascript_footer %}
    <script type="text/javascript" charset="utf-8">
      {{ custom_javascript_footer|safe }}
    </script>
    {% endif %}
  </body>
</html>
```
