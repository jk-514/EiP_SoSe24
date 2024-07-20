from os import listdir


def calculate_avg(file):
    speeds = []

    with open(file) as file_:
        for index, line in enumerate(file_):
            if index == 0:
                continue

            info = [int(e) for e in line.split()]
            heart = info[0]
            if heart <= 150:
                continue
            speeds.append(info[1]/10)

    return sum(speeds) / len(speeds)


def calculate_avg2(file):
    speeds = []

    with open(file) as file_:
        for index, line in enumerate(file_):
            if index == 0:
                continue

            info = [int(e) for e in line.split()]
            speeds.append(info[1]/10)

    return sum(speeds) / len(speeds)


# a
print(calculate_avg("Training.hrm"))

# b
with open("average_speed", "w") as current_file:
    sessions = listdir('sessions')
    for folder in sessions:
        current_values = []
        files = listdir("sessions/"+folder)
        for training in files:
            current_values.append(calculate_avg2("sessions/"+folder+"/"+training))
        current_file.write(str(sum(current_values) / len(current_values))+"\n")
