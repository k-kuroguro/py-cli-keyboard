# CLI Keyboard

Python module for handling keyboard event.

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
