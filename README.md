A utility for generating names and email addresses.

The names are taken from the [1990 U.S.
Census](http://www.census.gov/genealogy/www/data/1990surnames/names_files.html).
Names are chosen at random, weighted by frequency.

The results are plausible and sometimes even entertaining.

# Examples

From the shell, optional arg specifies how many names to generate:

```shell
% python namegen.py 3
Kathyrn Hanneman khanneman@tlen.pl
Blanch Gravatt bgravatt@aim.com
Sterling Otremba sotremba8711@ya.rux
```

From the python repl:

```python
>>> import namegen
>>> n = namegen.NameGen()
>>> [n.next() for i in range(10)]
['Chin Leong chinleong6194@live.com',
 'Erika Ripperger erikaripperger@centrum.cz',
 'Helaine Rollinson helaine.rollinson9355@lavabit.com',
 'Leeanna Sarnicola leeanna.sarnicola@hotmail.fr',
 'Lindsey Min lmin4691@yahoo.ca',
 'Iris Lisle ilisle@yahoo.de',
 'Ignacia Nealy ignacianealy@arcor.de',
 'Meryl Cluff merylcluff@mailinator.com',
 'Wilson Holtzer wilson.holtzer@hushmail.com',
 'Luke Poser luke-poser@yahoo.com.au']
```

There is also a little `web.py` server for serving lists of names to networked
applications.

```shell
% python server.py &
% curl http://localhost:8080/42
[ ... list of 42 names ... ]
```

# Requirements

- `numpy` (`pip install numpy`)
- `web` (`pip intall web.py`)

