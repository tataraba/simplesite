# :sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:

### Table of Contents
| Chapter | Title | Branch
| --- | --- | --- |
| Preface | [Getting Started](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) | [`main`](https://github.com/tataraba/simplesite) |
| Chapter 1 | [Using Jinja Templates to Render HTML](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md) | [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) |
| Chapter 2 | [Harnessing TailwindCSS for Consistent Design](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md) | [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) |
| Chapter 3 | [A Thin Database Layer](https://github.com/tataraba/simplesite/blob/main/docs/03_Chapter_3.md) | [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) |
| Chapter 4 | [Modern Browser Features Directly from HTML](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md) | [`04_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx)  |

## 📚 Chapter 4: Modern Browser Features Directly from HTML

If you're here, you're either curious about htmx and what it can do, or ready to ditch unneeded complexity in your web stack. You may have even heard that this could eliminate your need to learn JavaScript!

Is this true?

The answer is...

Mostly? Maybe? Yes?

For a real world case, I would look no further than this DjangoCon EU 2022 talk, titled [From React to htmx on a real-world SaaS product: we did it, and it's awesome!](https://youtube.com/watch?v=3GObi93tjZI&si=EnSIkaIECMiOmarE)

I'm not going to reiterate everything contained in the video, but I think it makes a compelling case that it's not only _possible_ to build without a JavaScript front end, but in many ways, it is _beneficial_!

Just in case, though, I do want to address some common questions that may come up when considering an htmx-centric approach.

What are some of the tradeoffs when using this type of "multi-page application" (MPA) versus a JavaScript driven "single-page application" (SPA)?

There is an [excellent essay over at htmx.org](https://htmx.org/essays/a-response-to-rich-harris/) which talks about this in detail, but here are a few key points:

- On having to load content on every request: If you're having consistent calls on every request, you could cache that content. But for the most part, with htmx, requests are generally light-weight replacements of Document Object Model (DOM) elements. (How web pages are represented internally to a browser.)
- On network latency issues: an MPA may suffer if the server is experiencing latency. However, with optimizations like database tuning, Redis caching, and so on, quick responses are easily achievable. The problem with latency is that it makes an app feel laggy&mdash;and this is not really a solved problem in the JavaScript world.
- On ✨ pizzaz ✨: Transitions and animations are much nicer with JavaScript. However, adding these elements doesn't mean much in terms of long-term accessibility and usability concerns. In any respect, using clever CSS design, as well as with the htmx support for standard CSS transitions, a lot of that sparkle can be replicated.

Okay with all that out of the way, let's get to it.

### Installing?

There's a question mark there because you don't actually _have_ to install anything. Htmx is a dependency-free, browser-oriented JavaScript library. Using it is as straightforward as adding it to a `<script>` tag in your HTML document head.

To test it out, you could just use a CDN. To do so, add this line within your document:

```html
<script src="https://unpkg.com/htmx.org@1.8.6" integrity="sha384-Bj8qm/6B+71E6FQSySofJOUjA/gq330vEqjFx9LakWybUySyI1IQHwPtbTU7bNwx" crossorigin="anonymous"></script>
```

But perhaps the next easiest way (and what I recommend) is to copy it into your project.

Within your `static` directory, create a new folder and call it `js`. You can get the file from [unpkg.com](https://unpkg.com/htmx.org@1.8.6/dist/htmx.min.js). Either download it, or copy the contents and create a new file in your `js` directory. (I've called my file `htmx.min.js`).

Now, add the script element to your document head. You can use the Jinja `url_for()` method to access it, since it is contained within your static directory.

```html
<script src="{{ url_for('static', path='js/htmx.min.js') }}"></script>
```

And that's it!

### The Python Stuff

You actually don't _need_ any additional Python packaging to use htmx.

There is one library, however, that I use in order to ease the building of templates. I'll get into that later, but for now, let's go ahead and install it.

```
python -m pip install jinja2-fragments
```
> Note: Okay, you should already know by now...

This creates a drop-in replacement for the FastAPI `Jinja2Templates` object. To use it, use `Jinja2Blocks` instead.

Open your `routes.py` file and make the substitution noted above. The top of your module will look something like this:

```py
from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks

from app.config import Settings

templates = Jinja2Blocks(directory="path/to/templates")
```

This will enable you to render "template fragments." (You can [read more about this paradigm](https://htmx.org/essays/template-fragments/) on the htmx.org website).

Without getting into the details (yet), this means that a `TemplateResponse` can find a defined section _within_ an existing template file, and only send that content over to the DOM.

But before delving into that, let's find out how to actually use htmx!

### Using htmx

At the core, htmx contains a set of attributes that allow you to issue AJAX requests directly within your HTML.

Here are a few of those:

- `hx-get` - issues `GET` request to given URL
- `hx-post` - issues `POST` request to given URL
- `hx-delete` - issues `DELETE` request to given URL

(Same applies for `PUT` and `PATCH`)

While these events are triggered by the "natural" event of an element (usually a "click" event), htmx also allows you to define which behavior will trigger the AJAX request. These are defined with an `hx-trigger` attribute. (i.e., mouseover, keypress, etc...)

And very importantly, you can also define the element where the response will be loaded. By default, the response will be loaded into the element that triggered the AJAX request.

But if you want the response to be loaded elsewhere, you can use the `hx-target` attribute to specify which element should receive the response (this attributes takes a CSS selector as its value).

This makes more sense with an example (taken from [htmx.org](https://htmx.org/docs/)):

```html
<button hx-post="/clicked"
    hx-trigger="click"
    hx-target="#parent-div"
    hx-swap="outerHTML"
>
    Click Me!
</button>
```

When a user clicks (`hx-trigger`) on this button, a `POST` request is sent to the "/clicked" endpoint (`hx-post`). The response will be sent back looking for an element with the CSS `id` "#parent-div" (`hx-target`), and the entire element will be replaced (`hx-swap`).

As you can see, htmx is very declarative with its intentions!

One of the attributes introduced above is `hx-swap`. This defines how the response is swapped into the existing DOM.

A few examples:

- "innerHTML" - the default, puts the content inside the target element
- "outerHTML" - replaces the entire target element with the returned content
- "afterbegin" - prepends the content before the first child inside the target
- "afterend" - appends the content after the target in the targets parent element

### Request Headers

There are times where a request is made to a specific route/view/endpoint, but the response should vary based on whether it's a "regular" request, or one coming from htmx.

For example, a regular request expects the entire web page to refresh. However, an `hx-get` request only expects a response specific to the element being replaced.

In order for your web app to understand what kind of request it is receiving, htmx sends data within the Request Header.

FastAPI has access to this request object, and you can parse it in order to obtain specific Header information.

**All htmx requests will send an HX-Request header with its value set to `true`.**

This is extremely important, as you are able to write logic within your route/view/endpoint to handle that kind of request.

Additionally, htmx also sends relevant data through other Headers. Two important ones are:
- `HX-Target` - the `id` of the target element if it exists
- `HX-Trigger` - the `id` of the triggered element if it exists
- `HX-Current-URL` - the current URL of the browser

There are more, but these will suffice for now.

### Using With FastAPI

Let's take a look at how an htmx request might be handled in your app:

```py
@router.get("/page")
def some_page(request: Request):

    template = "full_content.html"

    if request.headers.get("HX-Request"):
        template = "partial_content.html"

    return template.TemplateResponse(
        template,
        {
            "request": request,
        }
    )
```

Since we've learned that `HX-Request` is a boolean, the conditional checks to see if it can be retrieved from the Request Headers. If so, the name of the template changes from `full_content.html` to `partial_content.html`.

Then, the `TemplateResponse` sends the corresponding response based on how the request was made.

### Let's Try It Out

You can also use the same pattern above to differentiate what gets sent through the template context, or to isolate what kind of database call should be made. Either way, you have full control of what gets sent back to the client.

It's now time to put it all together.

In the `routes.py` file, create an endpoint for `/catalog`.

When a user navigates to this endpoint, we want to display "cards" corresponding to each of the artists that are in the "artist_details" table of TinyDB.

Make a call to the database that gets all artist data, and send that data to your template.

```py
db = CRUD().from_table("artist_details")
artists = db.all_items()
```

In your template, you can iterate over that list of artists and extract the artist name.

> Note: You are iterating over a `list` of `dict` items. The `key` containing the `value` we want is "name".

Create `<div>` elements using Tailwind to resemble square or rectangular "cards".

Using Jinja, iterate over the artist data sent to the template in order to display a `<div>` element for each artist in the database.

Once you have that part working, create an htmx request on the `<div>` element that displays the artist card.

The htmx request should obtain the artist profile (it should be contained within the same `dict` object used for artist name).

> Note: The `key` containing the `value` is called... "profile"

And for extra credit, make it so that when you click the card again, it returns to the artist name.

### Active Search

For the final exercise, we're going to implement active search.

For this, we're going to need an html element for the user to input their search. This can be from within a `<form>` element or an `<input>` element.

This will require the last dependency used throughout this guide. (HTML forms send data to the server with a special encoding different than the usual JSON).

```
python -m pip install python-multipart
```
> Note: Obligatory comment about only needing dependency if building from scratch...

This allows FastAPI to gather the request submitted from the form.

Here's an example of a search element:

```html
 <div>
    <input name="search" type="search" placeholder="Search..."
           class="border w-60 py-1 px-4 h-10 font-mono" />
</div>
```

You can choose where you want this search to happen. I've placed it within my site header, or you may choose to have a dedicated route/endpoint where users conduct a search.

Style it however you want using Tailwind and think about where you will want the search content to be generated.

We know that we want to use htmx to send the request, but we want the search content to be generated in a different `<div>` element.

We know that we can target any element by using a CSS selector, so create a `<div>` element where you want the search results to generate, and give it a meaningful `id`. It can remain empty, or contain a message that will be replaced by search elements.

```html
<div id="search-results">No results</div>
```

Now, we can introduce the htmx into the `<input>` element. Try to accomplish the following:

-   Send a `POST` request
-   Make it trigger on a keypress ("keyup changed")
-   Load the response into the "#search-results" `<div>` element

Once your html is ready, head over to your `route.py` file and create the appropriate endpoint.

Perhaps you've built a `/search` endpoint. In order to receive the form data from the request, FastAPI needs to know about it.

```py
@router.post("/search")
def search_post(request: Request, search: Annotated[str, Form()]):
    ...
```

Note that the `search` argument matches the `name` of the `<input>` element from your template.

So now that you've gotten this part, you have a request that will be posted to this endpoint everytime it's triggered ("keyup changed").

Use the `search` value to look in the database for any artist name that contains that value.

If you're using the TinyDB helper class (`CRUD`), you can use the following method:

```py
search_results = db.search(key="name", value=search)
```

Remember, the object passed to the `value` argument is equivalent to the `POST` request sent by htmx.

Once you have your `search_results`, you can send these back to your template for display.

But wait, where will these results be generated?

Make sure your `TemplateResponse` is pointing to the correct template file. That template file should have a Jinja expression that loops through the `search_results` and displays the data that you choose to display. It can be just the artist name, or it can be an entire `<div>` element with additional data from the search results.

Try to generate a few different things using an HTML and Tailwind tricks you may have up your sleeve.

Once you get the search working on "keyup changed", you'll notice how jittery it might feel to have nearly instant searches hitting the server. One way to smooth things out is by adding a modifier to delay the search.

```
hx-trigger="keyup changed delay:500ms"
```
The attribute above delays the search by 500ms, meaning that if someone types a few letters quickly into the search bar, the search will not execute until 500ms have passed.

This makes for a smoother experience.

If you got the active search working, give yourself a nice pat on the back, and if you're feeling a bit cheeky, bid a fond farewell to JavaScript.

### Extra

There are a few more tips and tricks to make your htmx experience even better.

I mentioned the `jinja2-fragments` package earlier, but so far, the functionality has been the same as the regular `Jinja2Templates` included with FastAPI.

One feature that is unlocked by using the `Jinja2Blocks` class instead is the idea of template fragments.

As of now, we've seen that if we want to send a separate response from an htmx request, it's often a snippet of HTML code that we want to insert somewhere.

If you're using htmx a lot (and why wouldn't you!), you'll eventually have a lot of these snippets hanging out somewhere, and you would have to make sure to render _those_ files instead of the template you use for the main page content.

Your routes might end up looking something like the example we saw earlier:

```py
@router.get("/page")
def some_page(request: Request):

    template = "full_content.html"

    if request.headers.get("HX-Request"):
        template = "partial_content.html"

    return template.TemplateResponse(
        template,
        {
            "request": request,
        }
    )
```

Note that the `partial_content.html` file has to be set explicitly for the `HX-Request`.


But... _what if you could use **one** template file, and only render specific blocks of code as needed?_

Take a look at this HTML, for example:

```html
<html>
    <body>
        <h1>Search Results</h1>
        <div hx-target="search-results">
            <p>No results found</p>
            <!-- content from partial_content.html -->
            <!-- htmx request would replace everything here -->
        </div>
    </body>
</html>
```
