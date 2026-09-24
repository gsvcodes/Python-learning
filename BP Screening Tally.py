def main():
    reading = []
    elevated_count = 0
    normal_count = 0
    high_count = 0

    while True:
        blood_pressure = input("Enter a systolic reading or done: ")
        if blood_pressure == "done":
            break
        else:
            reading.append(int(blood_pressure))
            print(reading)
    

    def categorize_bp(systolic):
        if systolic < 120:
            return "normal"
        elif 120 <= systolic <= 129:
            return "elevated"
        else:
            return "high"

    for bp in reading:
            category = categorize_bp(bp)
            if category == "elevated":
                elevated_count += 1
            elif category == "normal":
                normal_count += 1
            else:
                high_count += 1
    

    line = ""
    for _ in range (20):
        line += "-"

    print(line)

    print(f"Total readings: {len(reading)}")
    print(f"Elevated: ", elevated_count)
    print(f"Normal: ", normal_count)
    print(f"High: ", high_count)
main()
