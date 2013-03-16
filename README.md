A utility for generating names and email addresses.

The names are taken from the [1990 U.S.
Census](http://www.census.gov/genealogy/www/data/1990surnames/names_files.html).
Names are chosen at random, weighted by infrequency.

If you want to be more boring (though you'll still get many entertaining
results), use `weirdOrder=False` in the constructor.

# Examples

From the shell, optional arg specifies how many names to generate:

```shell
% python namegen.py 3
Pasty Stash <pstash@verizon.net>
Altagracia Kotula <altagraciakotula7344@live.nl>
Len Putzer <lputzer@live.ca>
```

From the python repl:

```python
>>> import namegen
>>> n = namegen.NameGen()
>>> ['%(first)s %(last)s %(email)s' % (n.next()) for i in range(10)]
['Stormy Miska smiska@yahoo.com.au',
 'Mozella Kopet mkopet5619@tlen.pl',
 'Mardell Varrato mvarrato3345@rochester.rr.com',
 'Lynsey Weader lynseyweader3648@email.com',
 'Alpha Klena alpha.klena@centrum.cz',
 'Boyce Interiano boyce.interiano@yahoo.com.au',
 'Malcom Filipek malcom.filipek@mozilla.com',
 'Jeanetta Pizzini jeanetta.pizzini@sporktronics.com',
 'Chanelle Schilk chanelle-schilk@tut.by',
 'Ike Muyskens ikemuyskens@nym.hush.com']
```

There is also a little `web.py` server for serving lists of names to networked
applications.  It returns json.

```shell
% python server.py &
% curl http://localhost:8080/42
[ ... list of 42 awesome names ... ]
```

# Requirements

- `numpy` (`pip install numpy`)
- `web` (`pip intall web.py`)

