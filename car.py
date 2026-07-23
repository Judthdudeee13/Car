from gpiozero import PWMOutputDevice as PWM
from gpiozero import OutputDevice as Pin
import time

#socket setup
import socket

HOST = '0.0.0.0'
PORT = 1313

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print("Connected:", addr)

class Motor:
        def __init__(self, forward, backward, ena):
                self.ena_pin = PWM(ena)
                self.forward_pin = Pin(forward)
                self.backward_pin = Pin(backward)
                self.forward_pin.off()
                self.backward_pin.off()
                self.ena_pin.value = 0.5

        def forward(self):
                self.backward_pin.off()
                self.forward_pin.on()

        def backward(self):
                self.forward_pin.off()
                self.backward_pin.on()

        def stop(self):
                self.backward_pin.off()
                self.forward_pin.off()

class DriveTrain:
        def __init__(self, motor1, motor2):
                self.motor1 = motor1
                self.motor2 = motor2

        def set_speed(self, left, right):
                self.motor1.ena_pin.value = left/100
                self.motor2.ena_pin.value = right/100

        def forward(self, speed):
                self.set_speed(speed, speed)
                self.motor1.forward()
                self.motor2.forward()

        def backward(self, speed):
                self.set_speed(speed, speed)
                self.motor1.backward()
                self.motor2.backward()

        def left(self, left, right):
                self.set_speed(left, right)
                self.motor1.forward()
                self.motor2.forward()

        def right(self, left, right):
                self.set_speed(left, right)
                self.motor1.forward()
                self.motor2.forward()

        def stop(self):
                self.motor1.stop()
                self.motor2.stop()

motor1 = Motor(19, 13, 6) #left
motor2 = Motor(17, 27, 22) #right

car = DriveTrain(motor1, motor2)
# time.sleep(3)
# car.forward(70)
# time.sleep(2)
# car.backward(50)
# time.sleep(2)
# car.left(80)
# time.sleep(2)
# car.right(60)
# time.sleep(2)
# car.stop()

while True:
        try:
                data = client.recv(1024)

                if not data:
                    print('no data')
                    break
            
                command = data.decode().strip()

                if command == "forward":
                        car.forward(70)

                elif command == "backward":
                        car.backward(70)

                elif command == "left":
                        car.left(100, 30)

                elif command == "right":
                        car.right(30, 100)

                elif command == "stop":
                        car.stop()

        except Exception as e:
                print(e)
                break
client.close()
server.close()