# latexify

A plot "latexifyer" for Python. This is a combination of pieces of code found in [this blog](https://nipunbatra.github.io/blog/visualisation/2014/06/02/latexify.html) and in [this post](https://stackoverflow.com/questions/25210898/matplotlib-log-scale-tick-labels-minus-sign-too-long-in-latex-font)

### How to use

```python
from latexify import latexify, MyLogFormatter, format_labels, _example
```
Run `example()` to print out an example. If you want to format a `list_of_labels`, just do `list(map(format_labels, list_of_labels))`.
