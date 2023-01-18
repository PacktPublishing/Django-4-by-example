


# Django 4 by Example

[<img src="https://djangobyexample.com/static/v4/img/django_by_example_4_cover.png" style="width:200px;"  align="left">](https://djangobyexample.com/)

[![GitHub stars](https://img.shields.io/github/stars/PacktPublishing/Django-4-by-example)](https://github.com/PacktPublishing/Django-4-by-example/stargazers)

This is the code repository for [Django 4 by Example](https://djangobyexample.com/), written by [Antonio Melé](https://antoniomele.es/) and published by [Packt](https://www.packtpub.com/product/django-4-by-example/9781801813051). It contains all the supporting project files necessary to work through the book from start to finish.



## Instructions
The code is organised into directories with the chapter number. For example, `Chapter02` contains the source code for chapter 2. Each chapter folder has a `requirements.txt` file that includes all packages required to run the code of that chapter. These can be installed with the command `pip install -r requirements.txt`.


## About the Book

**Django 4 by Example** (4th edition) will guide you through the entire process of developing professional web applications with Django. The book not only covers the most relevant aspects of the framework, but it will also teach you how to integrate other popular technologies into your Django projects.

The book will walk you through the creation of four real-world applications, solving common problems, and implementing best practices, using a step-by-step approach that is easy to follow.

After reading this book, you will have a good understanding of how Django works and how to build practical, advanced web applications.

## Requirements

This book requires Python 3.10+ and Django 4.1.

## Django Projects

The book covers a wide range of web app development topics divided into four different Django projects:

- **Blog Application** (chapters 1-3): Create a complete blog application
  - Build data models, views, and URLs
  - Implement an administration site for your blog
  - Use canonical URLs for modles and implement SEO-friendly URLs for posts
  - Build post pagination and learn how to create class-based views
  - Use forms to allow readers to share posts via email and implement a comment system using model forms
  - Add tags to posts using [django-taggit](https://github.com/jazzband/django-taggit) and recommend similar posts based on shared tags
  - Implement custom template tags to display latest posts and most commented posts
  - Implement a custom template filter to render [Markdown](https://github.com/Python-Markdown/markdown)
  - Create a sitemap and a RSS feed for your blog
  - Implement a full-text search engine using PostgreSQL

- **Social Website** (chapters 4-7): Create a website to bookmark and share images
  - Implement authentication using the Django authentication framework
  - Extend the user model with a custom profile model
  - Use the Diango messages framework
  - Build a custom authentication backend
  - Implement social authentication (OAuth2) with Facebook, Twitter, and Google using [Python Social Auth](https://github.com/python-social-auth/social-app-django)
  - Use [django-extensions](https://github.com/django-extensions/django-extensions) to run the development server through HTTPS
  - Generate image thumbnails with [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails)
  - Implement many-to-many relationships in models
  - Build a JavaScript bookmarklet with JavaScript and Django
  - Add asynchronous HTTP requests with the JavaScript Fetch API and Django
  - Implement infinite scroll pagination
  - Build a user follow system
  - Create a user activity stream and optimize QuerySets
  - Learn to use Django signals
  - Use [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) to obtain relevant debug information
  - Count image views with [Redis](https://redis.io/)
  - Build an image ranking with Redis

- **Ecommerce Application** (chapters 8-11): Create a fully-featured on-line shop
  - Build the models of the product catalog
  - Create a shopping cart using Django sessions
  - Create custom context processors
  - Manage customer orders
  - Send asynchronous notifications using [Celery](https://docs.celeryq.dev/) and [RabbitMQ](https://www.rabbitmq.com/)
  - Monitory Celery using [Flower](https://github.com/mher/flower)
  - Integrate [Stripe](https://stripe.com/) to process payments
  - Implement a webhook to receive payment notifications from Stripe
  - Build custom views in the Django administration site
  - Create admin actions and generate CSV files
  - Generate PDF invoices dynamically using [Weasyprint](https://weasyprint.org/)
  - Create a coupon system to apply disconts to orders
  - Integrate discounts with Stripe payments
  - Build a product recommendation engine using Redis
  - Add internationalization to the shop
  - Generate and manage translation files
  - Use [Rosetta](https://github.com/mbi/django-rosetta) to manage translations
  - Translate URL patterns and build a language selector
  - Translate models using [django-parler](https://github.com/django-parler/django-parler)
  - Localize forms using [django-localflavor](https://github.com/django/django-localflavor)

- **eLearning Platform** (chapters 12-17): Create an eLearning platform including a CMS
  - Build course models
  - Create and use data fixtures
  - Use model inheritance to create polymorphic Content
  - Create a custom model field to order course contents
  - Implement authentication views
  - Build a content management system using class-based views and mixins
  - Restrict access using groups and permissions
  - Build formsets to manage course contents
  - Create drag-and-drop functionality to reorder content in-place using JavaScript and Django
  - Using generic mixins from [django-braces](https://github.com/brack3t/django-braces)
  - Implement public views and student enrolment views
  - Render different type of contents and use [django-embed-video](https://github.com/jazzband/django-embed-video)
  - Cache content using the cache framework
  - Use the [Memached](https://memcached.org/) and Redis cache backends
  - Monitor Redis using [django-redisboard](https://github.com/ionelmc/django-redisboard)
  - Build an API using [Django REST Framework](https://www.django-rest-framework.org/)
  - Create serializers for models and custom API views
  - Handle API authentication and permissions
  - Build API viewsets and routers
  - Consume your API using Python [requests](https://github.com/psf/requests)
  - Create a real-time chat server using Django [Channels](https://github.com/django/channels)
  - Implement a WebSocket consumer/client using Django and JavaScript
  - Use Redis to set up a channel layer
  - Make your WebSocket fully-asynchronous
  - Create settings for multiple environments
  - Configure a production environment using [Docker Compose](https://docs.docker.com/compose/) with PostgreSQL, Redis, [Nginx](https://www.nginx.com/), [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) and [Daphne](https://github.com/django/daphne)
  - Serve your project securely through HTTPS
  - Use the Django system check framework
  - Build a custom middleware
  - Create custom management commands

## Code Snippets for Intermediate Steps
[Work in progress] Main chapter directories contain only the finished code for each chapter. The [Snippets](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Snippets) directory contains code files as they appear for a given stage of each chapter.

Where there are interim files for the chapter, you can find those files in the `chXX` folder within a sub-folder for each section. Where the edit to a particular file brings it in line with the final version, that file is not included in the interim tree.

Changed lines are marked with a comment. Where an entire block is new or changed, there is a hashtag on the line following the end of changed lines.

Filenames like `filename_00.py` are the auto-generated files before any edits are applied, they exist for informational purposes only.

## Community & Support

Join the book [Discord Community](https://discord.gg/PQ7UYX9VTx) to participate in the ongoing discussions or/and initiate a new one. You will find other developers reading the book alongside and helping each other with questions.

## Source Code for Previous Editions
- [Django 3 by Example](https://github.com/PacktPublishing/Django-3-by-Example)
- [Django 2 by Example](https://github.com/PacktPublishing/Django-2-by-Example)
- [Django by Example](https://github.com/PacktPublishing/Django-by-Example)

## Editions in Other Languages
While the 4th edition of the book is translated to other languages, you can find translations for the previous editions:
- Simplified Chinese: [Django 3项目实例精解](http://www.tup.tsinghua.edu.cn/wap/tsxqy.aspx?id=08886201)
- Brazilian Portuguese: [Aprenda Django 3 com Exemplos](https://novatec.com.br/livros/aprenda-django3-com-exemplos/)
- Polish: [Django 3. Praktyczne tworzenie aplikacji sieciowych. Wydanie III](https://helion.pl/ksiazki/django-3-praktyczne-tworzenie-aplikacji-sieciowych-wydanie-iii-antonio-mel,dj3pt3.htm#format/d)
- Serbo-Croatian-Bosnian: [Django 3 kroz primere, prevod III izdanja](https://knjige.kombib.rs/django-3-kroz-primere-prevod-iii-izdanja)
- Spanish: [Django 2](https://www.amazon.es/Django-2-Antonio-Mel%C3%A9/dp/8426727484)
- Russian: [Django 2 в примерах](https://dmkpress.com/catalog/computer/programming/python/978-5-97060-746-6/)

## Download a free PDF
If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost. Simply click on the link to claim your free PDF: [https://packt.link/free-ebook/9781801813051](https://packt.link/free-ebook/9781801813051)

## Errata
- Chapter 1, in *Figure 1.4* the `body` field should be `TextField` instead of `ForeignKey`.
- Chapter 16, page 647 line `ASGI_APPLICATION = 'educa.routing.application'` should be `ASGI_APPLICATION = 'educa.asgi.application'`.
