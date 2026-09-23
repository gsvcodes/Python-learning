def main():
    reading = []
    elevated_count = 0

    while True:
        blood_pressure = input("Enter a systolic reading or done: ")
        if blood_pressure == "done":
            break
        else:
            reading.append(int(blood_pressure))
            print(reading)
    for bp in reading:
         if bp >= 130:
            elevated_count += 1

    line = ""
    for _ in range (20):
        line += "-"

    print(line)

    print(f"Total readings: {len(reading)}")
    print(f"Elevated (>=130): ", elevated_count)
main()
