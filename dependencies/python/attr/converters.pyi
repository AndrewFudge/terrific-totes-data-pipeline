from typing import Callable, Any, overload

from attrs import _ConverterType, _CallableConverterType

@overload
def pipe(*validators: _CallableConverterType) -> _CallableConverterType: ...
@overload
def pipe(*validators: _ConverterType) -> _ConverterType: ...
@overload
def optional(converter: _CallableConverterType) -> _CallableConverterType: ...
@overload
def optional(converter: _ConverterType) -> _ConverterType: ...
@overload
def default_if_none(default: Any) -> _CallableConverterType: ...
@overload
def default_if_none(
    *, factory: Callable[[], Any]
) -> _CallableConverterType: ...
def to_bool(val: str | int | bool) -> bool: ...
