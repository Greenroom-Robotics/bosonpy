# bosonpy
Flir Boson for python (linux) compatible with docker

## Install globally with 
```
python3 -m pip install -e /path/to/bosonpy
```

## Use
```
from bosonpy.boson import Boson
from bosonpy.core import Core

camera = Boson()
camera.setup_video(
    device_id="/dev/video0"
)
camera.grab()
print(camera.get_camera_serial())
```

## Use with docker
You will need to pass the usb and video device, the use uses video for linux V4l. 

docker-compose
```
container:
    devices: 
      - /dev/ttyACM0:/dev/ttyACM0 # USB DEVICE
      - /dev/video0:/dev/video0 # V4L video device for opencv
```