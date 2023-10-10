# main - By: ruanasaduakhas - Tue Oct 03 2023

import sensor, image, time
from tensorflow import lite

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

model = lite.load('model_path.tflite')

while(True):
    img = sensor.snapshot()
    predictions = model.predict(img)

    if predictions[0] > 0.5:
        print("Occupied")
        # Turn on RED LED
    else:
        print("Unoccupied")
        # Turn on GREEN LED

    time.sleep(1)
