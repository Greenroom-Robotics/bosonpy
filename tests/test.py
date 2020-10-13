from bosonpy.boson import Boson
from bosonpy.core import Core

camera = Boson()
camera.setup_video(
    device_id="/dev/video0"
)
print(camera.get_camera_serial())