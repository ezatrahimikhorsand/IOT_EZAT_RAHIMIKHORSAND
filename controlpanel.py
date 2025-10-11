#--------TASK  2, 3-----------------

class Device:
   
    def __init__(self, location, group, device_type, device_name):
        self.location = location
        self.group = group
        self.device_type = device_type
        self.device_name = device_name
        self.status = 'off'

    def turn_on(self):
        print(f'دستگاه {self.device_name} روشن شد!')
        self.status = 'on'

    def turn_off(self):
        print(f'دستگاه {self.device_name} خاموش شد!')
        self.status = 'off'
       
    def get_status(self):
        if self.status == 'on':
            return True
        else:
            return False

class Sensor:
   
    def __init__(self, location, group, sensor_type, sensor_name):
        self.location = location
        self.group = group
        self.sensor_name = sensor_name
        self.sensor_type = sensor_type
               
    def read_data(self):
        return 25

class ControlPanel:
   
    def __init__(self):
        self.groups = {}
        self.sensors = []
       
    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'گروه {group_name} با موفقیت ایجاد شد!')
        else:
            print(f'گروه {group_name} از قبل وجود دارد!')
   
    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'دستگاه {device.device_name} به گروه {group_name} اضافه شد!')
        else:
            print(f'گروه {group_name} وجود ندارد!')
       
    def create_device(self, group_name, device_type, device_name):
        if group_name in self.groups:
            location = 'home'
            new_device = Device(location, group_name, device_type, device_name)
            self.groups[group_name].append(new_device)
            print(f'دستگاه {device_name} با موفقیت ایجاد شد!')
        else:
            print(f'گروه {group_name} وجود ندارد!')
       
    def create_multiple_device(self, group_name, device_type, device_number):
        if group_name in self.groups:
            for i in range(1, device_number + 1):
                dv_name = f'{device_type}_{i}'
                self.create_device(group_name, device_type, dv_name)
            print(f'{device_number} دستگاه از نوع {device_type} ایجاد شد!')
        else:
            print(f'گروه {group_name} وجود ندارد!')
           
    def get_devices(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f'گروه {group_name} وجود ندارد!')
            return []
       
    def turn_on_in_group(self, group_name):
        if group_name in self.groups:
            devices = self.get_devices(group_name)
            for device in devices:
                device.turn_on()
            print(f'تمام دستگاه‌های گروه {group_name} روشن شدند!')
        else:
            print(f'گروه {group_name} وجود ندارد!')
           
    def turn_off_in_group(self, group_name):
        '''
        تمام دستگاه‌های گروه مورد نظر را خاموش می‌کند
        '''
        if group_name in self.groups:
            devices = self.get_devices(group_name)
            for device in devices:
                device.turn_off()
            print(f'تمام دستگاه‌های گروه {group_name} خاموش شدند!')
        else:
            print(f'گروه {group_name} وجود ندارد!')
   
    def turn_on_all(self):
        '''
        تمام دستگاه‌ها را در همه گروه‌ها روشن می‌کند
        '''
        device_count = 0
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_on()
                device_count += 1
        print(f'تمام {device_count} دستگاه در همه گروه‌ها روشن شدند!')
   
    def turn_off_all(self):
        '''
        تمام دستگاه‌ها را در همه گروه‌ها خاموش می‌کند
        '''
        device_count = 0
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_off()
                device_count += 1
        print(f'تمام {device_count} دستگاه در همه گروه‌ها خاموش شدند!')
   
    def get_status_in_group(self, group_name):
        '''
        وضعیت تمام دستگاه‌های یک گروه را نمایش می‌دهد
        '''
        if group_name in self.groups:
            devices = self.get_devices(group_name)
            print(f'وضعیت دستگاه‌های گروه {group_name}:')
            for device in devices:
                status = "روشن" if device.get_status() else "خاموش"
                print(f'دستگاه {device.device_name} - {status}')
        else:
            print(f'گروه {group_name} وجود ندارد!')
       
    def get_status_in_device_type(self, device_type):
        '''
        وضعیت تمام دستگاه‌های یک نوع خاص را نمایش می‌دهد
        '''
        found_devices = []
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    found_devices.append(device)
        
        if found_devices:
            print(f'وضعیت دستگاه‌های نوع {device_type}:')
            for device in found_devices:
                status = "روشن" if device.get_status() else "خاموش"
                print(f'گروه: {device.group} - دستگاه: {device.device_name} - {status}')
        else:
            print(f'هیچ دستگاه از نوع {device_type} یافت نشد!')
   
    def create_sensor(self, location, group, sensor_type, sensor_name):
        '''
        ایجاد یک سنسور جدید
        '''
        new_sensor = Sensor(location, group, sensor_type, sensor_name)
        self.sensors.append(new_sensor)
        print(f'سنسور {sensor_name} با موفقیت ایجاد شد!')
        return new_sensor
   
    def create_multiple_sensor(self, location, group, sensor_type, sensor_number):
        
        '''
        ایجاد چندین سنسور از یک نوع
        '''
        created_sensors = []
        for i in range(1, sensor_number + 1):
            sensor_name = f'{sensor_type}_{i}'
            new_sensor = self.create_sensor(location, group, sensor_type, sensor_number)
            created_sensors.append(new_sensor)
        
        print(f'{sensor_number} سنسور از نوع {sensor_type} ایجاد شد!')
        return created_sensors


if __name__ == "__main__":
    # ایجاد پنل کنترل
    panel = ControlPanel()
    
    # ایجاد گروه‌ها
    panel.create_group("living_room")
    panel.create_group("bedroom")
    
    # ایجاد دستگاه‌ها
    panel.create_device("living_room", "lamp", "lamp_1")
    panel.create_device("living_room", "tv", "tv_1")
    panel.create_multiple_device("bedroom", "lamp", 3)
    
    # تست توابع
    panel.turn_on_in_group("living_room")
    panel.get_status_in_group("living_room")
    panel.get_status_in_device_type("lamp")
    