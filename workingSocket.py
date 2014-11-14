import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import time 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#get python code for setting up each GPIO pin and put it here

#activating all gpio outputs
#gpio pins number 7 and 11 control the back motor pin 12 and 16 control the current that makes the car go back and forth
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

#gpio pin numbers 13 and 15 control the servo using pins 18 and 22 to change the current
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#activating the ENA ENB on the relay switch
GPIO.output(7, True)
GPIO.output(11, True)

GPIO.output(13, True)
GPIO.output(15, True)

#Handler for our WebSocket
class MotorFunctions(tornado.websocket.WebSocketHandler):
 
	def open(self):
		print "Connection Opened from: {}".format(self.request.remote_ip)
		self.write_message("Connection Opened")
		
	def on_close(self):
		print "Connection Closed"
		
	def stop(self): 
		GPIO.output(18, False)
		GPIO.output(22, False) 
		GPIO.output(12, False) 
		GPIO.output(16, False) 
	
	def forward(self):
		GPIO.output(12, False)
		GPIO.output(16, True) 
	
	def reverse(self): 
		GPIO.output(12, True)
		GPIO.output(16, False) 
	
	def left(self):
		GPIO.output(18, False)
		GPIO.output(22, True) 
	
	def right(self): 
		GPIO.output(18, True)
		GPIO.output(22, False) 

#This handles the incoming message and turns on the proper GPIO pins to make the car move. 		
	def on_message(self, message):
		print "Message Received: {}".format(message)
		
		if message == "upLeft": 
			print "I went up and left"
			forward() 
			left() 
			time.sleep(2) 
			stop()
			
		elif message == "forward": 
			print "I went forward"
			forward()
			time.sleep(3)
		 	stop() 
		elif message == "upRight": 
			print "I went up and right"
			forward() 
			right() 
			time.sleep(2) 
			stop()
 
		elif message == "downLeft":
			print "I went down and left"
			reverse()
			left()
			time.sleep(2)
			stop()
 
		elif message == "reverse": 
			print "I went backwards"
			reverse()
			time.sleep(3)
			stop() 
		elif message == "downRight":  
			print "I went down and right"
			reverse()
			right()
			time.sleep(2) 
			stop()
	
if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", MotorFunctions)])
	server = tornado.httpserver.HTTPServer(app)
	server.listen(8080)
	tornado.ioloop.IOLoop.instance().start() 
