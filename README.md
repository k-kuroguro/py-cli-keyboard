# CLI Keyboard

Python module for handling keyboard event.

This module is sample code for [my article](https://zenn.dev/k_kuroguro/articles/e8437cdf6d804f) (Japanese).

> **Note**
> This module supports only Windows.

# Usage

```python
from clikeyboard import KeyEvent, Keys, on_press

def on_event(event: KeyEvent) -> None:
    print(f'Pressed "{event.key}"')

on_press('a', on_event)
on_press(Keys.CONTROL_D, on_event)

while 1:
    pass
```
