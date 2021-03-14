# ble_led_api

## Usage

Create a file named `leds.json`, with this content (replace MAC addresses with yours).  
You can find theses MAC addresses with something like [bettercap](https://github.com/bettercap/bettercap).

```json
[
  {
    "mac": "XX:XX:XX:XX:XX:XX",
    "uuid": "fff0",
    "address": "0000fff3-0000-1000-8000-00805f9b34fb"
  },
  {
    "mac": "XX:XX:XX:XX:XX:XX",
    "uuid": "fff0",
    "address": "0000fff3-0000-1000-8000-00805f9b34fb"
  }
]
```



## Acknowledgements

[arduino12/ble_rgb_led_strip_controller](https://github.com/arduino12/ble_rgb_led_strip_controller)