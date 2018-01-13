# `makeTable.py`

This is a simple python program to print pretty tables using the following 3 characters: `|-+`. I initially kept trying to use libraries I found online, but they all seemed over-complicated, and _none_ of them supported unicode characters, which were quite important in the data I was trying to print. (I was scraping Spanish conjugation tables from spanishdict.com, if you must know)

## How do I use it?

I find example code the easiest way to learn, so here's a simple program:
```
import makeTable
mytable = [[u'Apple',u'Banana'],[u'CÄT',u'Dóg'],[u'¡Eskimø!',u'Flówer']]
print(makeTable.drawTable(mytable).encode('utf-8'))
```

Output:
```
+--------+------+
| Apple  |Banana|
+--------+------+
|  CÄT   | Dóg  |
+--------+------+
|¡Eskimø!|Flówer|
+--------+------+


```

And that's pretty much it. `drawTable()` is the only function defined by `makeTable`. It accepts a an array of arrays as rows of columns, and prints them accordingly.

## Notes

So, as of now, this program only works in `python2`. Evidently `python3` handles unicode somewhat differently, but hopefully that'll be an easy fix.
