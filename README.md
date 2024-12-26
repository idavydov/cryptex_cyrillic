This is supporting code for
[10 letter Cryptex v2 with Cyrillic letters](https://www.printables.com/model/1121460-10-letter-cryptex-v2-with-cyrillic-letters),
which is a remix of
[10 letter Cryptex v2](https://www.printables.com/model/231458-10-letter-cryptex-v2)
by VortyZA.

Here I select of 10 rings with Cyrillic letters which can be used to spell
all of the 5000 most common Russian words. The
[frequency dictionary](https://bokrcorpora.narod.ru/frqlist/frqlist-en.html) is
based on corpus of modern Russian and created by Serge Sharoff. I include a
version converted to UTF-8 into this repository.

Note: to check if a word can be spelled I used a greedy algorithm which is
relatively quick but has a high probability of not finding a way to spell
a particular word. Every ring can fit 26 out of 33 (~80%) letters of the
alphabet. Therefore the problem is relatively simple and even using this
simplstic approach a solution can be found quickly. There are multiple ways to
improve the search.

This code can be easily applied to other alphabets.

The [OpenSCAD](https://openscad.org/) file can be used to deboss letters
onto the ring; ring 0 is an empty ring which just has a circle indicating
the correct position.

