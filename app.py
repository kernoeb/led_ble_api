import json
import random

from flask import Flask, request, jsonify

from ble_led import Led

app = Flask(__name__)


# Get random color
def random_color():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


print("Hello!")

leds = []
with open('leds.json') as json_file:
    data = json.load(json_file)
    for d in data:
        print(d['mac'] + ' | ' + d['uuid'] + ' | ' + d['address'])
        leds.append(Led(d['mac'], d['uuid'], d['address']))


@app.route('/colors', methods=['GET', 'POST'])
def color():
    if request.method == 'GET':
        tmp = []
        for led in leds:
            tmp.append({'mac': led.address, 'color': led.currentColor, 'brightness': led.currentBrightness})
        return jsonify(tmp)
    elif request.method == 'POST':
        try:
            req = request.get_json(silent=True)
            if req is not None and req.get('color') is not None and req.get('color').startswith('#') and len(
                    req.get('color')) == 7:
                tmp_color = req.get('color')
            else:
                tmp_color = random_color()
            if req is not None and req.get('brightness') is not None and 0 <= int(req.get('brightness')) <= 100:
                for led in leds:
                    led.set_brightness(int(req.get('brightness')))
            for led in leds:
                led.set_color(tmp_color)
            return jsonify({'status': 'ok'}), 200
        except Exception as e:
            print(e)
            return jsonify({'status': 'fail'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')