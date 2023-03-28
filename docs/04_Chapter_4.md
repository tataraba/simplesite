# :sparkles:Building a Python-Backed Frontend with HTMX and TailwindCSS:sparkles:

## 📚 Chapter 4

If you're here, you're probably curious about htmx and what it can do. You may have even heard that it can eliminate your need to learn JavaScript!

Is this true?

The answer is... Mostly? Maybe? Yes?

For a real world case, I would look no further than this DjangoCon EU 2022 talk, titled [From React to htmx on a real-world SaaS product: we did it, and it's awesome!](https://youtube.com/watch?v=3GObi93tjZI&si=EnSIkaIECMiOmarE)

I'm not going to reiterate everything contained in the video, but I think it becomes quite clear that it's not only _possible_ to build without a JavaScript front end, but in many ways, it is _beneficial_!

Just in case, though, I do want to address some common questions that may come up when considering an htmx-centric approach.

What are some of the tradeoffs when using this type of "multi-page application" (MPA) versus a JavaScript driven "single-page application" (SPA)?

There is an [excellent essay over at htmx.org](https://htmx.org/essays/a-response-to-rich-harris/) which talks about this in detail, but a couple kep points here:

- On having to load content on every request: If you're having consistent calls on every request, you could cache that content. But for the most part, with htmx, requests are generally light-weight replacements of Document Object Model (DOM) elements. (How web pages are represented internally to a browser.)
- On network latency issues: an MPA may suffer if the server is experiencing latency. However, with optimizations like database tuning, Redis caching, and so on, quick responses are easily achievable. The problem with latency is that it makes an app feel laggy&mdash;and this is not really a solved problem in the JavaScript world.
- On ✨ pizzaz ✨: Transitions and animations are much nicer with JavaScript. However, adding these elements doesn't mean much in respect to long-term accessibility and usability. In any respect, using clever CSS design, as well as with the htmx support for standard CSS transitions, a lot of that sparkle can be replicated.

Okay with all that out of the way, let's get to it.

### Installing?

There's a question mark there because you don't actually _have_ to install anything. Htmx is a dependency-free, browser-oriented JavaScript library. Using it is as simple as adding it to a `<script>` tag in your HTML document head.

To test it out, you could just use a CDN. To do so, just add this to within your document head:

```
<script src="https://unpkg.com/htmx.org@1.8.6" integrity="sha384-Bj8qm/6B+71E6FQSySofJOUjA/gq330vEqjFx9LakWybUySyI1IQHwPtbTU7bNwx" crossorigin="anonymous"></script>
```

But perhaps the next easiest way (and what I recommend) is to copy it into your project.

Within your `static` directory, create a new folder and call it `js`. You can get the file from [unpkg.com](https://unpkg.com/htmx.org@1.8.6/dist/htmx.min.js). Either download it, or copy the contents and create a file in your `js` directory. (I've called my file `htmx.min.js`).

Now, add to your document head. You can use the Jinja `url_for()` method to access it, since it is contained within your static directory.

```
<script src="{{ url_for('static', path='js/htmx.min.js') }}"></script>
```

And that's it!

### The Python Stuff

You actually don't _need_ any additional Python packaging to use htmx. There is one library, however, that I use in order to ease the building of templates. I'll get into that later, but for now, let's go ahead and install it.

```
python -m pip install jinja2-fragments
```
> Note: Update your requirements.txt file!

This creates a drop-in replacement for the FastAPI `Jinja2Templates` object. To use it, use `Jinja2Blocks` instead.

Open your `routes.py` file and make the substitution noted above. The top of your module will look something like this:

```
from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks

from app.config import Settings

templates = Jinja2Blocks(directory="path/to/templates")
```

This will enable to render "template fragments." (You can [read more about this paradigm](https://htmx.org/essays/template-fragments/) on the htmx.org website).

Without getting into the details (yet), this means that a `TemplateResponse` can find a defined section _within_ an existing template, and only send that content over to the DOM.

But before delving into that, let's findout how to actuall use htmx!

### Using htmx

At the core, htmx contains a set of attributes that allow you to issue AJAX requests directly within your HTML.

Here are a few of those:

- `hx-get` - issues `GET` request to given URL
- `hx-post` - issues `POST` request to given URL
- `hx-delete` - issues `DELETE` request to given URL

(Same applies for `PUT` and `PATCH`)

While these events are triggered by the "natural" event of an element (usually a "click" event), htmx also allows you to define which behavior will trigger the AJAX request. These are defined with an `hx-trigger` attribute.

And very importantly, you can also define the element where the response will be loaded. By default, the response will be loaded into the element that triggered the AJAX request.

But if you want the response to be loaded elsewhere, you can use the `hx-target` attribute to specify which element (this attributes takes a CSS selector as its value).

This makes more sense with an example (taken from [htmx.org](https://htmx.org/docs/)):

```
<button hx-post="/clicked"
    hx-trigger="click"
    hx-target="#parent-div"
    hx-swap="outerHTML"
>
    Click Me!
</button>
```

When a user clicks (`hx-trigger`) on this button, a `POST` request is sent to the "/clicked" endpoint (`hx-post`). The response will be sent back looking for an element with the id of "#parent-div" (`hx-target`), and the entire element will be replaced (`hx-swap`).

As you can see, htmx is very declarative with its intentions!

One of the attributes introduced above is `hx-swap`. This defines how the response is swapped into the existing DOM.

A few examples:

- "innerHTML" - the default, puts the content inside the target element
- "outerHTML" - replaces the entire target element with the returned content
- "afterbegin" - prepends the content before the first child inside the target
- "afterend" - appends the content after the target in the targets parent element

### Exercise

1.  Create a `<div>` element that contains artist name. On clicking the element, it only updates the information within that element.
2.  Active search (more details coming)



### Extras

- will need to install python-multipart to receive form data (search)
  - python -m pip install python-multipart