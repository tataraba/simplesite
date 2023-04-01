# :sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:

### Table of Contents
| Chapter | Title | Branch
| --- | --- | --- |
| Preface | [Getting Started](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) | [`main`](https://github.com/tataraba/simplesite) |
| Chapter 1 | [Using Jinja Templates to Render HTML](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md) | [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) |
| Chapter 2 | [Harnessing TailwindCSS for Consistent Design](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md) | [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) |
| Chapter 3 | [A Thin Database Layer](https://github.com/tataraba/simplesite/blob/main/docs/03_Chapter_3.md) | [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) |
| Chapter 4 | [Modern Browser Features Directly from HTML](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md) | [`04_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx)  |

## 📚 Chapter 1: Using Jinja Templates to Render HTML

This chapter focuses on how to use Jinja templates within your FastAPI application.

First things first, if you haven't already, make sure that Jinja is installed.

> Note: If you're using Codespaces, you will not need to install dependencies

```
python -m pip install Jinja2
```

Create two new directories within your `app`.
- `static`
- `templates`

Templates will create the foundation of your web application's html pages. You _could_ create templates for each url endpoint (view), and each of these views would have access to Python objects passed from your application.

But Jinja templates allow you to nest pieces together, giving you a powerful mechanic that reduces the need to rewrite a lot of redundant html code.

For example, it is likely that the `<head>` content between all your views remains the same, with the exception of maybe title or description elements.

> Note: If you're coming from Django or Flask, much of this will be familiar to you. Skip ahead if you're already comfortable with template mechanics.

To get started, create a `shared` folder within your `templates` directory, and create a `_base.html` file in the `shared` folder.

Within that file, create a basic html file (it might look a little like this):

```
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
  <title>{{ page_title }}</title>
  <meta name="description" content="{{ page_description }}"/>
</head>
<body>
    {% block content %}
    <h1>Hello, there!</h1>
    {% endblock %}
</body>
</html>
```

Don't worry about the `{% %}` and `{{ }}` just yet.

### Rendering Templates in FastAPI

Once you have created a template, you can render it through your FastAPI route.

In your `routes.py` file, create a route that renders the template you just created.

The FastAPI documentation provides instructions on how to use Jinja.
- Import Jinja2Templates.
- Create a templates object that you can re-use later.
- Declare a Request parameter in the path operation that will return a template.
- Use the templates you created to render and return a TemplateResponse, passing the request as one of the key-value pairs in the Jinja2 "context".

In practice, it looks something like this:

```
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="path/to/templates")
router = APIRouter()

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("shared/_base.html", {"request": request})
```

Add this code to `routes.py`. You wil need to supply the correct path to your templates directory.

> Hint: It should be defined in your config file.

### Mounting Static Files

If you want to serve certain assets (images, css, etc...), you need to "mount" these to your FastAPI application.

Within your `static` directory, create a new `css` folder, and within it, create a `main.css` file.

Write some basic css (this will be overwritten later). Here's an example:

```
html {
    background-color: #00539f;
  }

  body {
    width: 600px;
    margin: 0 auto;
    background-color: #ff9500;
    padding: 0 20px 20px 20px;
    border: 5px solid black;
  }
```

Now, mount your static directory to your FastAPI application (in `main.py`), so the content can be served.

```
app.mount("/static", StaticFiles(directory="path/to/static"), name="static")
```

Again, change the "path/to/static" to match your app structure.

### Back to Templates

Lastly, let's include the CSS file in the `_base.html` template. Since it is now mounted to your app, Jinja can access it with a special method (`url_for()`).

Add this line within the `<head>` element in `_base.html`:
```
<link rel="stylesheet" href="{{ url_for('static', path='css/main.css') }}" type="text/css" />
```
The `url_for()` method looks for a static directory called `static` which has already been registered with the FastAPI application, and follows the directory path starting from where it was defined in `main.py`.

> **Note**
> Sometimes, containers may be a little finicky with the way they treat mounted static files. In these cases, you may want to hard code the path to your static files instead [this is what is done in this repo to ensure compatibility with some of the containerization options].
>
> The stylesheet element above would be written like this: `<link rel="stylesheet" href="/static/css/main.css" type="text/css" />`
>
> Since the "static" directory is mounted by your app (and appended to your root url path), this should still work within your application.

Lastly, in the `templates` directory, create a `main.html` file. This is where you can harness the real power of Jinja templates. In this file, write the following:

```
{% extends "/shared/_base.html" %}

{% block content %}

    <h1>Simple Site</h1>
    <p>This is just a simple site for you</p>
{% endblock %}
```

By using the `{% extends "/shared/_base.html" %}` line, you are invoking the `_base.html` file. But now, you have the ability to "change" anything within the `{% block %}` elements.

Above, you are overwriting the `{% block content %}` contained in `_base.html` with new data.

To see this working, go back to the `route.py` file and change the `TemplateResponse` to point to `main.html` instead of `_base.html`.

> Note: When you run your app, you should no longer see "Hello, There!" Instead, the page should render with the CSS you created earlier and the heading of "Simple Site".

### Jinja Syntax and Context

I want to touch on three important items you will want to remember when working with templates.

#### Statements

Jinja statements are expressed with `{% ... %}`

Within these delimiters, you can use control structures (like "for" loops, "if/then" statements, etc..), as well as other special functions (such as the `{% include ... %}`) shown above.

#### Expressions

Expressions are contained within the `{{ ... }}` delimiters.

Ordinarily, you will be passing Python objects from your FastAPI app into your template, and these objects can be accessed through these expressions. (There are also helpful filters and other neat tricks you can do within the delimiters.)

One thing to note is that you can actually pass a _method_ object from your app and access it through these expressions. We'll see some of that later.

#### The Context

Above, there was a bullet point from the FastAPI documentation which talks about the "context". Here is that point again:

- Use the templates you created to render and return a TemplateResponse, passing the request as one of the key-value pairs in the Jinja2 "context".

The "context" here is very important. Think of it as the data that you want to pass from your application to your templates as _key:value_ pairs. These objects can then be accessed through the Jinja Expressions.

For example, look at this template response:

```
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
      "shared/_base.html",
      {
        "request": request,
        "age": 42
      }
    )
```

The dictionary that includes the `request` and `age` keys is considered the "context". Per the FastAPI docs, you _always_ have to send the `request` as part of the context. In addition, we are passing the `age` key.

In a Jinja template, you can then access the _value_ of `age` using an expression.

```
<p>The answer is {{ age }}.<p>
```
Which would ultimately be rendered as:
```
The answer is 42.
```

There's much more to Jinja templates, but it's vital to understand those three key points.


### Run Your App

You can run your app at any time to see if everything is working as intended. However, `uvicorn` can watch for changes in your app and restart the server automatically, so you don't have to keep running the command.

```
uvicorn app.main:app --reload
```

The `--reload` option restarts the server every time a change is made (and saved) to a `.py` file, so you can see changes reflected in your browser right away.

If the command is successful, you can visit [127.0.0.1:8000](http://127.0.0.1:8000) to see your app in action.

If you change/save a `.py` file in your app, the server will restart automatically.

> Note: The only files that are "watched" by default are `.py` files. If you want to restart the server when changes are saved to other file types, you can use the `--reload-include TEXT` option. The TEXT is a glob pattern.
>
> To include html files, for example, you would use the following command: `uvicorn app.main:app --reload --reload-include *.html`

### Extras

Take some time to flesh out your templates. You can start by including `<meta>` tags to your `_base.html` file. Think about which of those tags may need to have dynamic data, such as the `<title>` tag. How could you display a different title for each page that a user might visit?

For reference, here are some common meta tags:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
  <title>Simple Site</title>
  <meta name="description" content="Built with TailwindCSS and htmx"/>

  <!-- Facebok Open Graph: https://developers.facebook.com/docs/sharing/opengraph -->
  <meta property="og:site_name" content="Simple Site"/>
  <meta property="og:type" content="Demo site for TailwindCSS and htmx"/>
  <meta property="og:title" content="Simple Site - Home"/>
  <meta property="og:description"  content="Look, ma! No JavaScript!"/>
  <meta property="og:url" content="https://wwww.example.com"/>

  <!-- Favicon! -->
  <link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', path='favicon/apple-touch-icon.png') }}">
  <link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', path='favicon/favicon-32x32.png') }}">
  <link rel="icon" type="image/png" sizes="16x16" href="{{ url_for('static', path='favicon/favicon-16x16.png') }}">
  <link rel="manifest" href="/site.webmanifest">

  <!-- CSS -->
  <link rel="stylesheet" href="{{ url_for('static', path='css/main.css') }}" type="text/css" />
</head>
```

> Note: Favicons are great! Why not [use a generator](https://favicon.io) and create some for your project? Where will you put them?

Once you've had your fun with templates, it's time to[ move on to TailwindCSS](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md)!