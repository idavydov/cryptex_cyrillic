This is supporting code for a remix of
[10 letter Cryptex v2 by VortyZA](https://www.printables.com/model/231458-10-letter-cryptex-v2).

Here I select of 10 rings with Cyrillic letters which can be used to spell
all of the 5000 most common Russian words. The
[frequency dictionary](https://bokrcorpora.narod.ru/frqlist/frqlist-en.html) is
based on corpus of modern Russian and created by Serge Sharoff. I include a
version converted to UTF-8 into this repository.

Note: to check if a word can be spelled I used a greedy algorithm which is
relatively faster but has a high probability of not finding a way to spell
a particular word. Given that every ring can fit ~80% of the letters of the
alphabet even given this limitation the solution can be found quickly. A
more efficient approach probably would be using a bipartade graph.

This code can be easily applied to other alphabets.

The [OpenSCAD](https://openscad.org/) file can be used to deboss letters
onto the ring; ring 0 is an empty ring which just has a circle indicating
the correct position.

