import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 
from picamera2 import Picamera2
import time


class Device:

    def __init__(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name
        self.status='off'

        #sherkat dade beman
        self.mqtt_broker='jasdhash'
        self.port=37362 

        #on dastgahe pini -->
        self.mqtt_client=pin

        self.connect_mqtt()
        self.setup_gpio()

        # agar device az noe camera bood
        if self.device_type=='camera':
            self.cam = Picamera2()



    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)


    def setup_gpio(self):

        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)

        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
        # camera GPIO nemikhad


    def turn_on(self):
        print('Done!!!')
        self.status='on'
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')



    def turn_off(self):
        print('off')
        self.status='off'
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')



    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False

    # ===============================
    # >>> تابع برای گرفتن عکس با دوربین
    def take_picture(self, name='image.jpg'):
        if self.device_type!='camera':
            print('In device camera nist!')
            return

        self.cam.start()
        time.sleep(1)
        self.cam.capture_file(name)
        self.cam.stop()
        print('aks save shod:', name)


    # >>> تابع برای ضبط ویدیو با دوربین
    def record_video(self, name='video.mp4', duration=5):
        if self.device_type!='camera':
            print('In device camera nist!')
            return

        print('record start shod...')
        self.cam.start_recording(name)
        time.sleep(duration)
        self.cam.stop_recording()
        print('video save shod: ‘,name)


# نمونه استفاده از دوربین
cam1 = Device('home','room','camera','cam1001','topic/camera')
cam1.take_picture('test.jpg')
cam1.record_video('video.mp4',10)
