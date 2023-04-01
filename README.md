<h1 align="center">Simple Site</h1>
<h2 align="center">Featuring htmx and TailwindCSS</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/tataraba/simplesite)](https://github.com/tataraba/simplesite/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/tataraba/simplesite)](https://github.com/tataraba/simplesite/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Create a Python-backed frontend with FastAPI, htmx, and TailwindCSS. Build it from scratch and follow the guide. Alternatively, clone the repo/use the template, or better yet, spin up a Codespace and start right away!
    <br>
</p>
<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=400px src="https://github.com/tataraba/simplesite/blob/main/assets/simple-site-demo.gif" alt="Project demo"></a>
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
    - [Using Codespaces](#using-codespaces)
    - [Locally](#locally)
- [🔧 Running the tests ](#-running-the-tests-)
- [🚗 💨 Need to Catch Up?](#--need-to-catch-up)
- [🎈 Guide ](#-guide-)
  - [:sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:](#sparklesbuild-a-python-backed-frontend-with-htmx-and-tailwindcsssparkles)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

Build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Harness the power of Jinja templates and server-side rendering to create a dynamic, REST-ful web app.

## 🏁 Getting Started <a name = "getting_started"></a>

This repository was prepared for a workshop on how to create a python-backed frontend, featuring Jinja templates for HTML rendering, TailwindCSS for style, and htmx for pizzazz! 😎

The workshop consists of [four chapters](#-guide-), each introducing an additional tool on the road to creating a beautiful* Python-backed frontend.

> *Note: Beauty is in the eye of the beholder.

### Prerequisites

The example app was created with **Python 3.11**, but it is likely compatible with earlier versions. However, I would highly recommend using the latest version of Python. The rest of the dependencies are listed in the `requirements.txt` file.

```
fastapi[all]
jinja2
jinja2-fragments
python-multipart
pytest
pytailwindcss
tinydb
```

The `fastapi[all]` dependency installs some other optional dependencies and features. It also includes `uvicorn`, which is used as the server to run your code. (You could choose to just use `fastapi` and `uvicorn[standard]` separately, if you prefer.)

> Why is there a `pyproject.toml` file? If you use a package manager (i.e., I use `pdm`), you can use your package manager to install dependencies. Otherwise, you can go the more traditional route using the `requirements.txt` file. If you use Codespaces, you won't need to worry about dependencies!

### Installing

#### Using Codespaces
Press the `<> Code` button above and select `Create a Codespace on main`. This will open a new window in your browser, where you can run the code in a virtual environment.

https://user-images.githubusercontent.com/8632637/228152014-a73297f5-dfd7-400c-96b1-17239dcdb633.mp4

#### Locally
Create a copy of the repo using the `Use this template` button above. Select `Create a new repository`.

> **Warning**
> Be sure to select **`Include all branches`** when cloning the repo.

After cloning or using this template, you will need to create a virtual environment. Navigate to the location where you have cloned the project (your project root) and run the following command in your terminal:

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

## 🚗 💨 Need to Catch Up?
If you are using Codespaces, there is a script you can use to catch up to the current chapter. Just run the following command in your terminal and choose the section we're on:

```shell
. catchup.sh
```

https://user-images.githubusercontent.com/8632637/228153775-a3ca38fa-c467-402d-bf60-5c55b0f9b9e9.mp4

Or (if you're developing locally) to catch up **manually**...


Checkout the branch that corresponds to the appropriate section (see below).

## 🎈 Guide <a name="guide"></a>

This repo was created primarily to aid in a workshop setting, so your mileage may vary. Feel free to clone it and make it your own. But most of all, have fun! 🥳

To take a more structured approach, you can follow sequentially with the accompanying markdown files for each branch of the repo.

These Chapters are all located in the "docs" directory. The direct links to the corresponding chapters are listed here for convenience.

### :sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:

| Chapter | Title | Branch
| --- | --- | --- |
| Preface | [Getting Started](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) | [`main`](https://github.com/tataraba/simplesite) |
| Chapter 1 | [Using Jinja Templates to Render HTML](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md) | [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) |
| Chapter 2 | [Harnessing TailwindCSS for Consistent Design](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md) | [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) |
| Chapter 3 | [A Thin Database Layer](https://github.com/tataraba/simplesite/blob/main/docs/03_Chapter_3.md) | [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) |
| Chapter 4 | [Modern Browser Features Directly from HTML](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md) | [`04_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx)  |

## ⛏️ Built Using <a name = "built_using"></a>

- FastAPI
- Jinja2
- TailwindCSS
- TinyDB
- htmx

## ✍️ Authors <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- [@kjaymiller](https://github.com/kjaymiller) - Jay Miller, _Senior Cloud Advocate-Python_, Microsoft
