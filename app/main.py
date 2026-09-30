from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    now = datetime.now()
    hours = now.strftime("%H")
    minutes = now.strftime("%M")
    seconds = now.strftime("%S")

    file_name = f"app-{hours}_{minutes}_{seconds}.log"

    text = f"{now.date()} {now.strftime("%H:%M:%S")}"
    with open(file_name, "a") as f:
        f.write(text)


if __name__ == "__main__":
    main()

while True:
    main()
    sleep(1)
