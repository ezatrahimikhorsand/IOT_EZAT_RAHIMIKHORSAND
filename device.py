import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 
from picamera2 import Picamera2

class Device:

    def __init__(self, location, group, device_type, device_name, pin):
        self.location = location
        self.group = group
        self.device_type = device_type
        self.device_name = device_name
        self.status = 'off'

        # تنظیمات MQTT
        self.mqtt_broker = 'jasdhash'
        self.port = 37362 
        self.mqtt_client = mqtt.Client()

        self.connect_mqtt()
        self.setup_gpio()

        # اگر دوربین هست، راه اندازی ساده
        if self.device_type == 'camera':
            self.cam = Picamera2()
            self.cam.configure(self.cam.create_still_configuration())
            self.is_recording = False  # وضعیت ضبط ویدیو

    def connect_mqtt(self):
        try:
            self.mqtt_client.connect(self.mqtt_broker, self.port)
            print(f'اتصال MQTT برای دستگاه {self.device_name} برقرار شد')
        except Exception as e:
            print(f'خطا در اتصال MQTT: {e}')

    def setup_gpio(self):
        if self.device_type == 'lights':
            GPIO.setup(17, GPIO.OUT)
        elif self.device_type == 'doors':
            GPIO.setup(27, GPIO.OUT)

    def turn_on(self):
        print(f'دستگاه {self.device_name} روشن شد!')
        self.status = 'on'
        self.mqtt_client.publish("devices", f'{self.device_name}:ON')

    def turn_off(self):
        # اگر در حال ضبط هست، اول ضبط رو متوقف کن
        if self.device_type == 'camera' and self.is_recording:
            self.stop_recording()
            
        print(f'دستگاه {self.device_name} خاموش شد!')
        self.status = 'off'
        self.mqtt_client.publish("devices", f'{self.device_name}:OFF')

    def get_status(self):
        return self.status == 'on'

    # تابع  برای دوربین - گرفتن عکس
    def take_picture(self, filename="photo.jpg"):
        """یک تابع برای گرفتن عکس با دوربین"""
        if self.device_type != 'camera':
            print("این دستگاه دوربین نیست!")
            return False
        
        if self.status != 'on':
            print("لطفا اول دوربین را روشن کنید!")
            return False

        try:
            self.cam.start()
            time.sleep(1)
            self.cam.capture_file(filename)
            self.cam.stop()
            print(f"عکس ذخیره شد: {filename}")
            return True
        except Exception as e:
            print(f"خطا در گرفتن عکس: {e}")
            return False

    # تابع برای دوربین - شروع ضبط ویدیو
    def start_recording(self, filename="video.mp4"):
        """یک تابع  برای شروع ضبط ویدیو"""
        if self.device_type != 'camera':
            print("این دستگاه دوربین نیست!")
            return False
        
        if self.status != 'on':
            print("لطفا اول دوربین را روشن کنید!")
            return False

        try:
            self.cam.start_recording(filename)
            self.is_recording = True
            print(f"ضبط ویدیو شروع شد: {filename}")
            return True
        except Exception as e:
            print(f"خطا در شروع ضبط ویدیو: {e}")
            return False

    def stop_recording(self):
        """تابع برای توقف ضبط دوربین"""
        if self.device_type != 'camera':
            print("این دستگاه دوربین نیست!")
            return False
        
        if not self.is_recording:
            print("دوربین در حال ضبط نیست!")
            return False

        try:
            self.cam.stop_recording()
            self.is_recording = False
            print("ضبط ویدیو متوقف شد")
   