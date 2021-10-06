import keyboard, time

print("[*] Beginning pin cracker in 5 seconds")
time.sleep(5)

for x in range(1111, 10000):
    print("[*] Trying pin: " + str(x))
    keyboard.write(str(x)[0])
    time.sleep(0.1)
    keyboard.write(str(x)[1])
    time.sleep(0.1)
    keyboard.write(str(x)[2])
    time.sleep(0.1)
    keyboard.write(str(x)[3])
    time.sleep(0.1)
