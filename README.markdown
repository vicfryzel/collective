collective: blog engine with minimal core feature set
Written by [Vic Fryzel](http://www.vicfryzel.com/)

# Introduction and features

collective is a blog engine with a small core feature set.  It is intended
to be used with other hosted services by embedding them into articles.
By itself, collective is able to manage articles and static pages, but has
no support for comments, file uploads, etc.  It also doesn't have a GUI-based
installer, and requires a command-line installation process.

Out of the box, collective has support for:

* Articles and static pages in [Markdown](http://daringfireball.net/projects/markdown/) syntax
* Archives
* RSS and Atom feeds
* HTML5 and CSS3, [Google Fonts API](http://code.google.com/webfonts)
* Themes
* Full page caching
* Search via [Google Custom Search](http://www.google.com/cse/)
* Comments via [Disqus](http://disqus.com/)

Out of the box, collective does _not_ support:

* Automatic imports from other blog services
* File uploads, image uploads
* Categories, tags
* Article drafts, revisions, future publishing, private articles
* OpenID authentication


# Intended audience

To use this blog software, you should probably be at least a bit technical,
and have some experience deploying web applications on a web server.  If you
are not familiar with programming at all, then you may want to try a hosted
blog engine, like [Posterous](http://posterous.com),
[Tumblr](http://tumblr.com), [Blogger](http://www.blogger.com/), etc.


# Dependencies

You must have the following dependencies installed and available on the
PYTHONPATH of your server.  Your startup script must also know where these
are.

* [Python 2.5 or greater](http://www.python.org/) (does not work with Python 3)
* [Django 1.2](http://www.djangoproject.com/)
* [PyMarkdown 2.0](http://www.freewisdom.org/projects/python-markdown/)
* [Pygments 1.3](http://www.pygments.org)

You'll also need a web server capable of running a Django (Python) application
behind a web server.  Examples include Apache 2 with FastCGI or Passenger.
This can be a bit difficult in a shared hosting environment, but this
application is known to work on [DreamHost](http://www.dreamhost.com/).


# Configuration

To get going, you must create a database and edit three files.  Once you've
done this, collective should work.  Expected configuration and deployment time
is about two hours, depending on how familiar you are with configuring a
Django application.

All fields you should edit are marked EDIT_ME.  To find everything you should
edit to get going, run:

    grep -R EDIT_ME ./*

## Create a database

The type of database you use is up to you.  This blog engine supports all
databases that are supported natively in Django, as listed
[here](http://docs.djangoproject.com/en/1.2/ref/databases/).

## Edit settings.py

Copy settings.py.template to settings.py.

    cp settings.py.template settings.py

In settings.py, edit the DATABASES, SECRET_KEY, TEMPLATE_DIRS, CACHE_BACKEND,
and CACHE_MIDDLEWARE_KEY_PREFIX variables.  For help, see
[the documentation](http://docs.djangoproject.com/en/1.2/ref/settings/).

## Edit feeds.py

Copy feeds.py.template to feeds.py.

    cp feeds.py.template feeds.py

In feeds.py, you must edit the various options to configure your feeds to your
liking.

## Edit themes/minimalbw-yourname/base.html or create your own theme

Copy themes/minimalbw to themes/minimalbw-yourname.

    cp -R themes/minimalbw themes/minimalbw-yourname

In themes/minimalbw-yourname/base.html, you'll need to configure that base HTML
template so that it reflects your blog.  This includes things like page title,
[Disqus](http://disqus.com/) keys, etc.

Speaking of Disqus, make sure you register a Disqus account, and use the
appropriate unique identifiers when editing base.html.


# Deployment

You must first create your database schema.

    python manage.py syncdb

When prompted, be sure to create an admin user.

To deploy this application locally (e.g. while developing a theme,) just run

    python manage.py runserver

This is documented [here](http://docs.djangoproject.com/en/1.2/ref/django-admin/#runserver-port-or-ipaddr-port).
You may have to edit settings.py appropriately to enable development settings.

To deploy this application to a Passenger instance, place a link to
contrib/passenger_wsgi.py in the appropriate location on your web server.
This will vary from server to server.  To do this, you must first copy the
script template, and then edit its settings so that the paths match your setup.

    cp contrib/passenger_wsgi.py.template contrib/passenger_wsgi.py
    # Edit contrib/passenger_wsgi.py
    ln -s /path/to/collective/contrib/passenger_wsgi.py /path/to/passenger/scripts/passenger_wsgi.py

To deploy this application with Apache 2 and mod_python, see
[here](http://docs.djangoproject.com/en/1.2/howto/deployment/modpython/).

Also, setup your web server to serve themes/minimalbw/static/ in a public
directory.  You can do this by creating a symlink to that directory in your
public directory on your web server.

Besides the static directory, you will also need to copy relevant admin media
to the directory that is configured for admin media in your settings.py.  This
is documented [here](http://docs.djangoproject.com/en/1.2/howto/deployment/modpython/#serving-the-admin-files).

The static directory also contains a .htaccess file that will enable useful
caching operations on an Apache 2 web server.


# Importing existing data

You are more or less on your own here at this time.  You can look at the
database schema, and import from your existing data source accordingly.
Obviously this will require a bit of work on your part.


# Usage

After deploying collective, you should have an empty blank page.  To add
articles or static pages, login to http://yourdomain.com/admin with the
username and password created previously, and add an Article.

Articles should be written in
[Markdown](http://daringfireball.net/projects/markdown/) with optional raw
HTML for the cases in which Markdown does not have an appropriate syntax.

Based on the value of CACHE_MIDDLEWARE_SECONDS in your settings.py, pages will
be cached until the cache clears.  This is important to note, because if you
edit an article or flatpage, you will not see the updates reflected until you
either clear your cache or the given number of seconds has elapsed.

After collective is deployed, you must also add search support via
[Google Custom Search](http://www.google.com/cse/).  To do this, create a new
flatpage, and add the embed code that Google Custom Search gives you after
creating a custom search engine.  The flatpage must have the URI /search/.


# Creating your own theme

Everything you need to create your own theme is in the themes/ directory.  You
could get going with a new theme pretty quickly just by copying
themes/minimalbw to themes/mytheme, and starting from there.  Once you do
this, edit settings.py, and change your TEMPLATE_DIRS setting accordingly.


# Modifying/extending collective

collective itself only really manages static pages and articles.  Even then, the
amount of data managed is very minimal.  Most of the features of collective are
provided in the UI.  [Disqus](http://disqus.com/) is used for comments by
default.  File upload mechanisms are not provided by collective on purpose,
in favor of using other hosted mechanisms.  Some examples are:

* [Picasa Web Albums](http://picasaweb.google.com/)
* [Flickr](http://www.flickr.com/)
* [Google Docs](http://docs.google.com/)
* [Baconfile](http://baconfile.com/)
* [Dropbox](http://www.dropbox.com/)
* etc.

The justification for this when writing collective was that all of
those services already do an amazing job in their specific focus areas, and
nothing added here would rival them without a substantial amount of work.

To extend collective, you essentially need to know how to embed a hosted
service into your posts or theme, or implement whichever service you need in
Django.

For instance, if you wanted to change Article syntax to
[Textile](http://textile.thresholdstate.com/), you would need to edit
themes/yourtheme/articles/article.html and apply a Textile filter to the
article body instead of the Markdown filter.

Adding a WYSIWYG editor would be a bit more involved.  You'd have to edit
admin templates, and also accept an article body format produced by the
editor.


# Why another blog engine?

There aren't many stable, "complete" Django-based blog engines.  This is rather
ironic, given how amazingly fast it is to build a blog in Django.  For more
information on this topic, see my
[blog post](http://www.vicfryzel.com/2011/01/06/finally-blog-software-doesnt-suck).


# Where did the name _collective_ come from?

At first, I had wanted to name this blog engine 'picard', as a tribute to
[Patrick Stewart](http://en.wikipedia.org/wiki/Patrick_Stewart) as
[Jean-Luc Picard](http://en.wikipedia.org/wiki/Jean-Luc_Picard).  However,
there are already some existing applications/libraries named picard, and I
didn't want to polute the open-source namespace.  collective works well
because just as Jean-Luc was assimilated by the Borg, he is forever part of
the collective.  That's right, a little piece of Jean-Luc/Locutus is in this
blog engine.

Also, this blog engine can stand on its own, but does much better when used in
conjunction with other hosted services.


# Further development

I may make changes here as I am able, but I don't have
official plans to actively develop collective over time.  That said, I'd be
weary of anyone considering this a "dead" project, as it is stable and works
great.  Don't let the fact that it is not actively maintained deter you from
using it!  If you need help, I'm always [available](http://www.vicfryzel.com).
