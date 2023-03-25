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
- [🚀 Deployment ](#-deployment-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)
- [Chapter 3](#chapter-3)

## 🧐 About <a name = "about"></a>

Build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Harness the power of Jinja templates and server-side rendering to create a dynamic, REST-ful web app.

## 🏁 Getting Started <a name = "getting_started"></a>

This repository was prepared as part of a workshop on how to create a python-backed front end, featuring Jinja templates for HTML rendering, TailwindCSS for style, and htmx for pizzazz! 😎

The main branch contains the "starter" app, which lacks all of the features. It only contains a basic FastAPI "Hello, World!" application. Each subsequent branch contains more features. If you want the fully-featured application, switch to the appropriate branch and select "Use This Template" (make sure to only clone the "current" branch).

### Prerequisites

Your only requirement is to have **Python 3.11** (or later) installed locally. The rest of the dependencies are in the `pyproject.toml` file, as well as the `requirements.txt` file.

> Why both? If you use a package manager (i.e., I use `pdm`), you can use your package manager to install dependencies from the `pyproject.toml`. Otherwise, you can go the more traditional route using the `requirements.txt` file.

### Installing

If you have a package manager, you can use that to install directly from the `pyproject.toml` file. Otherwise, you can go the traditional rout (see below).

After cloning the repo locally, you will need to create a virtual environment. Navigate to the location where you have cloned the project and run the following command:

```
python -m venv .venv
```

This will create a `.venv` directory within your project.

Next, activate your environment:

```
# On Windows
.\.venv\Scripts\activate

# On MacOS/Linux
$ source myvenv/bin/activate
```

Then, install the requirements:
```
python -m pip install -r requirements.txt
```


## 🔧 Running the tests <a name = "tests"></a>

After activating your virtual environment, you can run tests by typing `pytest` on the command line.

```
pytest
```

If everything has gone well so far, all tests should pass.

## 🎈 Usage <a name="usage"></a>

This repo was created primarily to aid in a workshop setting, so your mileage may vary. Feel free to clone the repo and make it your own. But most of all, have fun! 🥳

## 🚀 Deployment <a name = "deployment"></a>

- Coming Soon

## ⛏️ Built Using <a name = "built_using"></a>

- FastAPI
- Jinja2
- TailwindCSS
- HTMX


## ✍️ Authors <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Coming soon


## Chapter 3

- `python -m pip install tinydb`
- add the `DATA_DIR` to config file and load data from github
  - create `data` directory in project root
  - add the `data.json` file obtained from github
- create `crud.py`
  - Basic helper class for `tinydb` operations
    - very basic - only has a few methods for sake of demo
  - use `CRUD` class to interface with the `data.json` file
  - two tables within `data.json` - "artist_info" and "artist_details"
  - instantiate a table (example)
    - `db = CRUD().with_table("artist_info")`
  - use class operations to access data (example)
    - get all artist records - `artists = db.all_items()`
    - search for an artist - `artist = db.search(key="artist", value="bandname")`
  - Create methods within `routes.py` to access db data
    - send to template through the template context
  - Practice sending data to templates from db