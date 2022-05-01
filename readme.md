# Uniforms

Low-code forms for small university purposes.

## Licence (MIT Licence)

Copyright (c) 2022 Tobias Thelen and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Setup

You need Python (3.8+) and Django (2.0+).

All sensitive credentials are to be  stored in a file `uniforms/credentials.py` that can be created by
copying and filling `uniforms/credentials.py.template`. In that file you can also override database settings etc. 

Default database is sqlite, do the typical command chain works for testing:

```
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver
```

## Usage

Each form lives as a separate app. Let's assume, there are two such apps:

1. schnupper
2. cogscinet

The forms can be display by using the url `/schnupper` and `/cogscinet` respectively.

A listing of data entered can be obtained from `/schnupper/list` and `/cogscinet/list`. User credentials (e.g. from the 
superuser created during setup) are needed to see this list.

TODO: limit user's acccess to a single app.

## Development

Each form is a separate app. 

To change an existing form (e.g. `schnupper`), you may:

1. Alter the data model in `schnupper/models.py`. After changing, don't forget to perform `python manage.py makemigrations` 
   and `python manage.py migrate`.
2. Change display texts in the various templates in `schnupper/templates/schnupper`, including the e-mail template.

