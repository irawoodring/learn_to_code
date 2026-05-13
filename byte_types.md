| Type | Description | Example | Category |
|:-----|:------------|:--------|:---------|
| `str` | Immutable sequence of Unicode characters | `"hello"` | **Sequence** |
| `bytes` | Immutable sequence of bytes | `b"hello"` | **Sequence** |
| `bytearray` | Mutable sequence of bytes | `bytearray(b"hi")` | **Sequence** |
| `list` | Mutable ordered sequence | `[1, 2, 3]` | **Sequence** |
| `tuple` | Immutable ordered sequence | `(1, 2, 3)` | **Sequence** |
| `range` | Immutable sequence of integers | `range(0, 10)` | **Sequence** |
| `dict` | Mutable key-value pairs | `{"a": 1}` | **Mapping** |
| `set` | Mutable unordered collection of unique items | `{1, 2, 3}` | **Set** |
| `frozenset` | Immutable unordered collection of unique items | `frozenset({1, 2})` | **Set** |
| `memoryview` | Memory buffer interface to binary data | `memoryview(b"hi")` | **Binary** |
| `NoneType` | Represents the absence of a value | `None` | **Null** |
```