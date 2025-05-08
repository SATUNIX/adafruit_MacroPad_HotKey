# Adafruit Macropad Quickstart

## About

This is a customizable macro/hotkey launcher for the **Adafruit MACROPAD**.
Rotate the encoder to switch between macro sets. Press any key to send
custom keystrokes, commands, or strings over USB to the connected host.

Based on original code by Phillip Burgess / Adafruit
With my modifications to code.py and custom macros.
should be good for circuitpy 9.x firmware. 
If you get any issues such as import error, use the lib and requirements from Adafruit. 

---

## File Structure

```
/code.py           # Main runtime script
/macros/*.py       # Folder of user-defined macro sets
/lib/              # Required CircuitPython libraries
/requirements/     # Optional extras, support tools, or scripts
```

---

## How to Use

1. Install [CircuitPython](https://circuitpython.org/board/macropad_rp2040/) on your MACROPAD (if not already installed).
2. Copy the included `uf2` firmware file to the MACROPAD while in bootloader mode.

   * It will automatically reboot after flashing. This may take a few minutes.
3. Once rebooted, copy the following items to the root of the `CIRCUITPY` drive:

   * `code.py`
   * `/macros/` folder
   * `/lib/` folder
   * `/requirements/` folder (optional extras if included)
4. Add `.py` macro files inside `/macros/` to define custom key layouts.
5. Plug the MACROPAD into your computer.
6. Use the rotary encoder to scroll through available macro profiles.
7. Press any key to send its configured action over USB.

---

## Macro File Format

Each file in `/macros/` should contain a dictionary like this:

```python
app = {
    'name': 'ExampleApp',
    'macros': [
        (0xHEX, 'LABEL', ['Command or keystrokes']),
        ...
    ]
}
```

* `0xRRGGBB`: RGB color for key lighting (hex format)
* `'LABEL'`: Text (≤5 characters) shown on the MACROPAD display
* `['...']`: List of actions (strings, delays, keycodes, etc.)

---

## Color Codes

Colors are specified in hex format:
`0xFF0000` → Red
`0x00FF00` → Green
`0x0000FF` → Blue

You can use any valid RGB hex.

---

## Author

**BY Satunix**
*Based on original code by Phillip Burgess / Adafruit*

---

## License

[MIT License](LICENSE) — Free to use, modify, and redistribute.
