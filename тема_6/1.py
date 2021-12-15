import time
class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(5)
            i += 1

traffic_light1 = TrafficLight()
traffic_light1.running()


