import datetime
import time

FILENAME = "bucket.txt"
meetings = []


def file_load():

    meetings.clear()
  
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if "," not in line:
                    continue
                title, timestr = line.split(",")
                time_obj = datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M")
                meetings.append({"title": title, "time": time_obj})
    except FileNotFoundError:
        pass 

def input_save():
    with open(FILENAME, "w") as file:
        for m in meetings:
            file.write(f"{m['title']},{m['time'].strftime('%Y-%m-%d %H:%M')}\n")

def menu():
    print("\nMEETING SCHEDULER")
    print("1.Add a meeting")
    print("2.View all meetings")
    print("3.Delete a meeting")
    print("4.Check reminders")
    print("5.Exit")

def add():
    print("\nADD NEW MEETING")
    title = input("Enter meeting Title: ")

    print("\n  ENTER DATE")
    yr = int(input("Year(YYYY): "))
    mon = int(input("Month(MM): "))
    day = int(input("Day(DD): "))

    print("\n  ENTER TIME")
    hr = int(input("Hour (0-23): "))
    min = int(input("Minute (0-59): "))

    try:
        current_datetime=datetime.datetime.now()
        user_datetime=datetime.datetime(yr, mon, day, hr, min)
        if user_datetime < current_datetime:
            print("Invalid date or time! (Meeting is in the past)")
        else:
            meetings.append({"title": title, "time": user_datetime})
            input_save()
            print("Meeting saved!")
    except ValueError:
        print("Invalid date or time!")

    input("Press Enter to continue...")

def show():
    print("\nALL MEETINGS")

    if not meetings:
        print("No meetings found.")
    else:
        sorted_list = sorted(meetings, key=lambda x: x["time"])
        for i, m in enumerate(sorted_list, 1):
            print(f"{i}. {m['title']}")
            print("Date:", m["time"].strftime("%Y-%m-%d"))
            print("Time:", m["time"].strftime("%H:%M"))
            print()

    input("Press Enter to continue...")

def remove():
    print("\nDELETE MEETING")

    if not meetings:
        print("No meetings to delete.")
        input("Press Enter to continue...")
        return

    for i, m in enumerate(meetings, 1):
        print(f"{i}. {m['title']} - {m['time'].strftime('%Y-%m-%d %H:%M')}")

    choice = input("Enter meeting number to delete (0 to cancel): ")

    if not choice.isdigit():
        print("Invalid input!")
        input("Press Enter...")
        return

    choice = int(choice)

    if choice == 0:
        return
    if 1 <= choice <= len(meetings):
        meetings.pop(choice - 1)
        input_save()
        print("Meeting deleted!")
    else:
        print("Invalid number!")

    input("Press Enter to continue...")
def upcoming():
    print("\n UPCOMING MEETINGS (NEXT 24 HOURS)")

    now = datetime.datetime.now()
    found = False

    for m in meetings:
        delta = m["time"] - now
        if datetime.timedelta(0) <= delta <= datetime.timedelta(days=1):
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            print(f"\n{m['title']}")
            print("At:", m["time"].strftime("%Y-%m-%d %H:%M"))
            print(f"In: {hours}h {minutes}m")
            found = True

    if not found:
        print("No upcoming meetings.")

    input("Press Enter to continue...")

def main():
    file_load()

    while True:
        menu()
        number = input("Enter your choice (1-5): ")

        if number == "1":
            add()
        elif number == "2":
            show()
        elif number == "3":
            remove()
        elif number == "4":
            upcoming()
        elif number == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            time.sleep(1)

main()