<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h2 align="center">Simple Site</h2>
<h3 align="center">Featuring htmx and TailwindCSS</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/tataraba/simplesite)](https://github.com/tataraba/simplesite/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/tataraba/simplesite)](https://github.com/tataraba/simplesite/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Creating a Python-backed front end, featuring FastAPI, htmx, and TailwindCSS.
    <br>
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
- [📚 Chapter 1: Templates](#-chapter-1-templates)
  - [Rendering Templates in FastAPI](#rendering-templates-in-fastapi)
  - [Mounting Static Files](#mounting-static-files)
  - [Back to Templates](#back-to-templates)
  - [Run Your App](#run-your-app)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

Build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Harness the power of Jinja templates and server-side rendering to create a dynamic, REST-ful web app.

## 🏁 Getting Started <a name = "getting_started"></a>

You can clone this branch and install dependencies from the `requirements.txt` file (make sure you've created a virtual environment and activated it first).

More detailed instructions are available on the [main branch](https://github.com/tataraba/simplesite/tree/main).

## 📚 Chapter 1: Templates

This chapter focuses on how to use Jinja templates within your FastAPI application.

First things first, if you haven't already, make sure you install Jinja.

```
python -m pip install Jinja2
```
> Note: You may want to keep your requirements file up to date. You can either use `pip freeze > requirements.txt` or adding manually. (I recommend using `pip freeze`).

Create two new directories within your `app`.
- `static`
- `templates`

Starting with templates, you will want to create the foundation of your web applications html pages. You could create templates for each url endpoint (view), and each of these views would have access to Python objects passed from your application.

> Note: If you're coming from Django or Flask, much of this will be familiar to you. Skip ahead if you're already comfortable with templating mechanics.

But Jinja templates allow you to nest pieces together, giving you a powerful mechanic that reduces the need to rewrite a lot of redundant html code.

For example, it is likely that the `<head>` content between all your views would not change, with the exception of maybe meta title or description elements.

To get started, create a `shared` directory, and create a `_base.html` file.

Within that file, create a basic html file that looks a little like this:

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

FastAPI documentation provides instructions on how to use Jinja.
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

Lastly, let's include the CSS file in the `_base.html` template. Since it is now mounted to your app, Jinja can access it with a special methode (`url_for()`).

Add this line within your `_base.html`:
```
<link rel="stylesheet" href="{{ url_for('static', path='css/main.css') }}" type="text/css" />
```
The `url_for()` method looks for a static directory called `static` which has already been registerd with the FastAPI application, and follows the directory path starting from where it was defined in `main.py`.

Lastly, in the `templates` directory, create a `main.html` file. This is where you can harness the real power of Jinja templates. In this file, write the following:

```
{% extends "/shared/_base.html" %}

{% block content %}

    <h1>Simple Site</h1>
    <p>This is just a simple site for you</p>
{% endblock %}
```

By using the {% extends "/shared/_base.html" %} line, you are invoking the `_base.html` file. But now, you have the ability to "change" anything within the `{% block %}` elements.

Above, you are overwriting the {% block content %} contained in `_base.html` with new data.

To see this working, go back to the `route.py` file and change the `TemplateResponse` to point to `main.html` instead of `_base.html`.

### Run Your App

Every so often, you will want to run your FastAPI application. You can do that with the following command on the command line (make sure you have activated your virtual environment).

```
uvicorn app.main:app --reload
```
This is a `uvicorn` CLI command. The argument is looking for a path and a FastAPI app object. The path is `app.main`, followed by `:`, which signals that you will be providing an app object (defined as `app = get_app()` in `main.py`).

The `--reload` option restarts the server every time a change is made to a `.py` file, so you can see changes reflected in browser right away.

If the command is successful, you can visit [127.0.0.1:8000](http://127.0.0.1:8000) to see your app in action.



## ✍️ Authors <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Coming soon
