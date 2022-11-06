# CLI Keyboard

Python module for handling keyboard event.

> **Note**
> This module supports only Windows.

# Usage

```python
from keyboard import Keys, on_press

def on_press_a() -> None:
   print('Pressed "a"')

def on_press_ctrl_c() => None:
   print('Pressed "Ctrl+C"')

on_press('a', on_press_a)
on_press(Keys.CTRL_C, on_press_ctrl_c)
```
