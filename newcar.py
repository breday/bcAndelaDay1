class Car(object):
	def __init__(self, name='General', model='GM', vehicle_type=None, speed = 0):
		self.name = name
		self.model = model
		self.vehicle_type = vehicle_type
		self.speed = speed

		if (name=='porsh') or (name =='Koenigsegg'):
            self.num_of_doors = 2
        else:
        	self.num_of_doors = 4

        if vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4


    def is_saloon(self):
    	if self.vehicle_type =='saloon':
    		return True
    	else:
            return False

     def drive(self,movivng_speed):
     	if self.vehicle_type == 'MAN':
     		self.speed = moving_speed * 11
     	else:
     		self.speed =10* moving_speed



  










		





