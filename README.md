# bosonpy
Flir Boson for python (linux) compatible with docker

# Install globally with 
```
python3 -m pip install -e /path/to/bosonpy
```

# Use
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