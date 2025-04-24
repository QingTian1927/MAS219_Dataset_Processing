import csv

current_row = None

def parsePrice(priceString: str) -> int:
    tokens = priceString.split(" ")
    result = 0
    temp = 0

    for token in tokens:
        if token.isnumeric():
            temp = int(token)
            continue

        token = token.lstrip().rstrip().lower()
        if token == "billion":
            temp *= 1_000_000_000
        elif token == "million":
            temp *= 1_000_000

        result += temp

    return result

try:
    with (
        open("data/car_detail_en.csv", mode="r", newline="", encoding="utf-8") as csvfile,
        open("data/car_detail_en_new.csv", mode="w", encoding="utf-8") as new_csvfile,
    ):
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()

        for row in reader:
            current_row = row['ad_id']
            print()

            priceStr = row['price']
            priceNum = parsePrice(priceStr)

            print(f"[CONVERT] {priceStr} -> {priceNum}")
            row['price'] = priceNum

            writer.writerow(row)
except KeyboardInterrupt:
    print(f"\n[STOPPED] Script stopped at id {current_row}\n")
except Exception as err:
    print("[FATAL] Script stopped due to exception:\n")
    print(err)
