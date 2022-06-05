"""

"""
from __future__ import annotations
import numbers
from abc import ABC
from typing import Optional, overload, Type

import numpy

__all__ = (
    "BaseVector",
    "V2f",
    "V3f",
)


class BaseVector(ABC, numpy.ndarray):
    @property
    def x(self) -> float:
        return self[0]

    @property
    def y(self) -> float:
        return self[1]


class V2f(BaseVector):
    @overload
    def __new__(cls, x: numbers.Number, y: numbers.Number) -> V2f:
        ...

    @overload
    def __new__(cls, array: Optional[numpy.ndarray]) -> V2f:
        ...

    @overload
    def __new__(cls, v2f: Optional[V2f]) -> V2f:
        ...

    @overload
    def __new__(cls) -> V2f:
        ...

    def __new__(cls, *args, **kwargs) -> V2f:

        if not args and not kwargs:
            return cls(0.0, 0.0)

        elif args and kwargs:
            raise ValueError(
                f"Mix of kwargs and args is not supported : {args} ; {kwargs}"
            )

        elif args and not kwargs:

            if len(args) == 1 and isinstance(args[0], cls):
                return args[0].copy()

            if (
                len(args) == 2
                and isinstance(args[0], numbers.Number)
                and isinstance(args[1], numbers.Number)
            ):
                return cls(numpy.array((args[0], args[1])))

            if isinstance(args[0], numpy.ndarray):
                return args[0].view(cls)

        # kwargs just call back to above args
        elif not args and kwargs:

            k = kwargs.get("v2f")
            if isinstance(k, cls):
                return cls(k)

            k1 = kwargs.get("x")
            k2 = kwargs.get("y")
            if isinstance(k1, numbers.Number) and isinstance(k2, numbers.Number):
                return cls(k1, k2)

            k = kwargs.get("array")
            if isinstance(k, numpy.ndarray):
                return cls(k)

            if not kwargs.get("v2f", True) or not kwargs.get("array", True):
                return cls()

        raise ValueError(
            f"The given arguments doesn't resolve to a new instance:\n"
            f"{args} ; {kwargs}"
        )

    def to_v3f(self, third_axis: float) -> V3f:
        return V3f(self.x, self.y, third_axis)


class V3f(BaseVector):
    @overload
    def __new__(cls, x: numbers.Number, y: numbers.Number, z: numbers.Number) -> V3f:
        ...

    @overload
    def __new__(cls, array: Optional[numpy.ndarray]) -> V3f:
        ...

    @overload
    def __new__(cls, v3f: Optional[V3f]) -> V3f:
        ...

    @overload
    def __new__(cls) -> V3f:
        ...

    def __new__(cls: Type[V3f], *args, **kwargs) -> V3f:

        if not args and not kwargs:
            return cls(0.0, 0.0, 0.0)

        elif args and kwargs:
            raise ValueError(
                f"Mix of kwargs and args is not supported : {args} ; {kwargs}"
            )

        elif args and not kwargs:

            if len(args) == 1 and isinstance(args[0], cls):
                return args[0].copy()

            if (
                len(args) == 3
                and isinstance(args[0], numbers.Number)
                and isinstance(args[1], numbers.Number)
                and isinstance(args[2], numbers.Number)
            ):
                return cls(numpy.array((args[0], args[1], args[2])))

            if isinstance(args[0], numpy.ndarray):
                return args[0].view(cls)

        # kwargs just call back to above args
        elif not args and kwargs:

            k = kwargs.get("v3f")
            if isinstance(k, cls):
                return cls(k)

            k1 = kwargs.get("x")
            k2 = kwargs.get("y")
            k3 = kwargs.get("z")
            if (
                isinstance(k1, numbers.Number)
                and isinstance(k2, numbers.Number)
                and isinstance(k3, numbers.Number)
            ):
                return cls(k1, k2, k3)

            k = kwargs.get("array")
            if isinstance(k, numpy.ndarray):
                return cls(k)

            if not kwargs.get("v3f", True) or not kwargs.get("array", True):
                return cls()

        raise ValueError(
            f"The given arguments doesn't resolve to a new instance:\n"
            f"{args} ; {kwargs}"
        )

    @property
    def z(self) -> float:
        return self[2]
