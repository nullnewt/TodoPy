import sys

txt = "todolist.txt"
tdl = open(txt, "r")
line_count = len(tdl.readlines())
user_args = ["-tm", "--taskmake", "-tp", "--taskprint", "-h", "--help", "-tc", "--taskcomplete", "-ct", "--cleartasks"]

if sys.argv[1] not in user_args:
    print("The argument you specified does not exist, try -h, --help.")

elif sys.argv[1].lower() == user_args[0] or sys.argv[1] == user_args[1]:
    line_count += 1
    tdl = open(txt, "a")
    task = input("Task #%i: " % line_count)
    if 1 == line_count:
        tdl.write(str(line_count) + ": " + task)
    elif line_count >= 1:
        tdl.write("\n" + str(line_count) + ": " + task)
    tdl.close()

elif sys.argv[1].lower() == user_args[2] or sys.argv[1] == user_args[3]:
    tdl = open(txt, "r")
    print(tdl.read())
    tdl.close()

elif sys.argv[1] == user_args[4] or sys.argv[1] == user_args[5]:
    print("\t-tm, --taskmake - Creates a new task for your todolist. \n\t-tp, --taskprint - Prints your current "
           "tasks. \n\t-tc tasklinenumber, --taskcomplete tasklinenumber - Marks the selected task number as complete.")

elif sys.argv[1].lower() == user_args[6] or sys.argv[1] == user_args[7]:
    try:
        line_count += 1
        user_num = sys.argv[2]
        line_range = range(1, line_count)
        if int(sys.argv[2]) in line_range:
            sys.argv[2] = int(sys.argv[2]) - 1
            with open(txt, "r") as file:
                data = file.readlines()
                if " ✔" in data[sys.argv[2]]:
                    print("Task %i is already completed. Keep it up!" % int(sys.argv[2] + 1))
                    exit()
                elif " ✔" not in data[sys.argv[2]]:
                    line_count -= 1
                    tmp = data[sys.argv[2]].split()
                    data[sys.argv[2]] = ' '.join(tmp)
                    if int(user_num) == line_count:
                        data[sys.argv[2]] = data[sys.argv[2]] + " ✔"
                    elif int(user_num) <= line_count:
                        data[sys.argv[2]] = data[sys.argv[2]] + " ✔\n"
            with open(txt, "w") as file:
                file.writelines(data)
                tdl.close()
                print("Task %i has been marked as complete. Nice one!" % int(sys.argv[2] + 1))
        elif sys.argv[2] not in line_range:
            print("The line number you entered does not exist.")
    except ValueError:
        print("You entered %s. That is not a number." % sys.argv[2])
    except IndexError:
        print("Please enter a number to be marked as completed.")

elif sys.argv[1] == user_args[8] or sys.argv[1] == user_args[9]:
    yn = input("Are you sure you would like to clear your tasks? Enter y/n: ")
    if yn.lower() == "y":
        print("Clearing tasks")
        tdl = open(txt, "r+")
        tdl.truncate(0)
        tdl.close()
    elif yn.lower() == "n":
        print("Nothing has been cleared.")

