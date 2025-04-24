OLD_FILE_PATH = "data/car_detail_en_new.csv"
NEW_FILE_PATH = "data/cars.csv"

try:
    with (
        open(OLD_FILE_PATH, mode="r", encoding="utf-8") as old_file,
        open(NEW_FILE_PATH, mode="w+", encoding="utf-8") as new_file
    ):
        line_count = 0
        current_row = ""

        for line in old_file:
            line_count += 1
            current_row = line

            if not line or line.isspace():
                continue
            new_file.write(line)
except KeyboardInterrupt:
    print(f"\n[STOPPED] Script stopped at line [{line_count}]: {current_row}\n")
except Exception as err:
    print("[FATAL] Script stopped due to exception:\n")
    print(err)