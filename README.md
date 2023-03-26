<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h2 align="center">Simple Site</h2>
<h3 align="center">Featuring htmx and TailwindCSS</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
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
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [🔧 Running the tests ](#-running-the-tests-)
- [🎈 Usage ](#-usage-)
- [📚 Preface](#-preface)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

Build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Harness the power of Jinja templates and server-side rendering to create a dynamic, REST-ful web app.

## 🏁 Getting Started <a name = "getting_started"></a>

This repository was prepared as part of a workshop on how to create a python-backed front end, featuring Jinja templates for HTML rendering, TailwindCSS for style, and htmx for pizzazz! 😎

The workshop consists of four **Chapters**, each introducing an additional tool on the road to making a beautiful* front end. More info below.

> *Note: Beauty is in the eye of the beholder.

### Prerequisites

Your only requirement is to have **Python 3.11** (or later) installed locally. The rest of the dependencies are in the `pyproject.toml` file, as well as the `requirements.txt` file.

> Why both? If you use a package manager (i.e., I use `pdm`), you can use your package manager to install dependencies from the `pyproject.toml`. Otherwise, you can go the more traditional route using the `requirements.txt` file.

### Installing

If you have a package manager, you can use that to install directly from the `pyproject.toml` file. Otherwise, you can go the traditional route (see below).

After cloning or using this template, you will need to create a virtual environment. Navigate to the location where you have cloned the project (your project root) and run the following command:

```
python -m venv .venv
```

This will create a `.venv` directory within your project.

Next, activate your environment:

```
# On Windows
.\.venv\Scripts\activate

# On MacOS/Linux
$ source .venv/bin/activate
```

Then, install the requirements:
```
python -m pip install -r requirements.txt
```


## 🔧 Running the tests <a name = "tests"></a>

After activating your virtual environment, you can run tests by typing `pytest` on the command line. This makes sure that your application runs and can generate a "Hello World" message.

```
pytest
```

If everything has gone well so far, all tests should pass.

## 🎈 Usage <a name="usage"></a>

This repo was created primarily to aid in a workshop setting, so your mileage may vary. Feel free to clone the repo and make it your own. But most of all, have fun! 🥳

This repo is split into four branches, representing different Chapters. Each chapter will set the stage for the next.


## 📚 Preface

The first step to get going is to build a minimal FastAPI application. If you have used other web frameworks before, you should be able to follow along. I recommend starting from scratch, but if you feel like skipping the formalities, you can also clone this template to get going.

Otherwise, you'll want to follow these steps.

Create a project directory and create your virtual environment.

`python -m venv .venv`

Next, create an `app` directory and a `test` directory.

Also, create these files:
- `requirements.txt` - to keep track of your dependencies
- `.gitignore` - you should really plan to use version control, because why not?
- `README.md` - Write down some things you may want to remember later

Within your `app` directory, create the following files:
- `__init__.py` - makes your app a "package"
- `main.py` - where your FastAPI application will live
- `config.py` - for app configuration
- `routes.py` - here we will define our url endpoints or "views"

Now that you have your structure set, create a basic FastAPI application within `main.py`
- It's okay, you can look at the code here and copy/paste

For all intents and purposes, you can go through this thing without a `config.py`. I have kept it here because it may be useful if you build out your app in the future. The most important pieces in there are the `STATIC_DIR` and `TEMPLATE_DIR` attributes that point to where our html templates and static files will live. But we'll touch more on that in Chapter 1.

The `FASTAPI_PROPERTIES` are just key:value pairs that we can pass to the `FastAPI` object. The most important piece in there is the `defaulet_response_class` that changes the default response type of your FastAPI application.

While most "Hello World" style FastAPI tutorials include their routes/views within the context of the application (i.e., in `main.py`), in practice, it's better to keep these elsewhere, which is why you created a `routes.py` file.

Routes in FastAPI look something like this:

```
@app.get("/")
def index_page():
  return SomeResponse
```

You'll notice that the `routes.py` file has a different decorator. This is what allows us to link our routes back to the app that we defined in `main.py`.

At the top of `routes.py`, we include `router = APIRouter()`. Now, all the routes that we define with the `@router` decorator will get added to the `APIRouter()` object defined here.

And in `main.py`, you can register all those routes directly to your application:

```
app.include_router(router)
```

Once you're comfortable with this starter application, it is time to move on to Chapter 1.




## ⛏️ Built Using <a name = "built_using"></a>

- FastAPI
- Jinja2
- TailwindCSS
- HTMX


## ✍️ Authors <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Coming soon
