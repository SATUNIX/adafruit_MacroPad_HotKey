# Modified By SATUNIX / Tony, BASED ON WORK BY PHILLIP BURGESS / ADAFRUIT
# LICENSED UNDER THE MIT LICENSE:

# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
A macro/hotkey program for Adafruit MACROPAD. Macro setups are stored in the
/macros folder (configurable below). Plug into computer's USB port, use dial
to select an application macro set, press MACROPAD keys to send key sequences
and other USB protocols.
"""
import os
import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

MACRO_FOLDER = '/macros'

class App:
    """Class representing a host-side application, for which we have a set
    of macro sequences. Project code was originally more complex and
    this was helpful, but maybe it's excessive now?
    """
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']

    def switch(self):
        """Activate application settings; update OLED labels and LED colors."""
        group[13].text = self.name 
        if self.name:
            rect.fill = 0xFFFFFF
        else:  
            rect.fill = 0x000000

        for i in range(12):
            if i < len(self.macros): 
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  
                macropad.pixels[i] = 0
                group[i].text = ''

        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

# INITIALIZATION
macropad = MacroPad()

# BOOT SCREEN GROUP
boot_group = displayio.Group()

boot_label_1 = label.Label(
    terminalio.FONT,
    text="SATUNIX",
    color=0xFFFFFF,
    anchored_position=(macropad.display.width // 2, macropad.display.height // 2 - 10),
    anchor_point=(0.5, 0.5)
)
boot_group.append(boot_label_1)

boot_label_2 = label.Label(
    terminalio.FONT,
    text="",
    color=0xFFFFFF,
    anchored_position=(macropad.display.width // 2, macropad.display.height // 2 + 10),
    anchor_point=(0.5, 0.5)
)
boot_group.append(boot_label_2)

macropad.display.root_group = boot_group
macropad.display.refresh()
time.sleep(0.5)

boot_message = "Hack The Planet!"
for i in range(1, len(boot_message) + 1):
    boot_label_2.text = boot_message[:i]
    macropad.display.refresh()
    time.sleep(0.1) 

# CONTINUE
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(
        label.Label(
            terminalio.FONT,
            text='',
            color=0xFFFFFF,
            anchored_position=((macropad.display.width - 1) * x / 2,
                               macropad.display.height - 1 - (3 - y) * 12),
            anchor_point=(x / 2, 1.0)
        )
    )

rect = Rect(0, 0, macropad.display.width, 13, fill=0xFFFFFF)
group.append(rect)

group.append(
    label.Label(
        terminalio.FONT,
        text='',
        color=0x000000,
        anchored_position=(macropad.display.width // 2, 0),
        anchor_point=(0.5, 0.0)
    )
)

# Set the real group after display screens
macropad.display.root_group = group

apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py') and not filename.startswith('._'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError, IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[13].text = 'OOPS, NO MACRO FILES!!!'
    macropad.display.refresh()
    while True:
        pass

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()

# MAIN LOOP ----------------------------
while True:
    position = macropad.encoder
    if position != last_position:
        app_index = position % len(apps)
        apps[app_index].switch()
        last_position = position

    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue 
        key_number = 12
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            continue
        key_number = event.key_number
        pressed = event.pressed

    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        if key_number < 12:
            macropad.pixels[key_number] = 0xFFFFFF
            macropad.pixels.show()

        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.press(item)
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                macropad.keyboard_layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    elif isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.press(item['buttons'])
                    else:
                        macropad.mouse.release(-item['buttons'])
                macropad.mouse.move(
                    item['x'] if 'x' in item else 0,
                    item['y'] if 'y' in item else 0,
                    item['wheel'] if 'wheel' in item else 0
                )
                if 'tone' in item:
                    if item['tone'] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item['tone'])
                    else:
                        macropad.stop_tone()
                elif 'play' in item:
                    macropad.play_file(item['play'])
    else:
        for item in sequence:
            if isinstance(item, int) and item >= 0:
                macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if 'buttons' in item and item['buttons'] >= 0:
                    macropad.mouse.release(item['buttons'])
                if 'tone' in item:
                    macropad.stop_tone()

        macropad.consumer_control.release()
        if key_number < 12:
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
