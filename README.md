# lxMath

Math library for graphics and image-processing.

Based on [ASWF Imath](https://github.com/AcademySoftwareFoundation/Imath) attempting at having a similar API **but not strictly identical.**

>  This is not considered production-ready.

> Features implementation are based on my needs and doesn't attempt to cover the average use-cases.

```python
import lxMath

matrix = lxMath.M33f()
vector = lxMath.V2f(0.33, 0.69)
matrix.scale(vector)
```

`lxMath` is using Numpy at his core (only dependency). Objects are subclasses of `numpy.ndarray` which make implementation into existing code easier.
