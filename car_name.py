import csv
import requests
from time import sleep
from bs4 import BeautifulSoup

NAME_COLUMN = "CarName"
inaccessible_urls = dict()
current_row = None

try:
    with (
        open("data/seller_en.csv", mode="r", newline="", encoding="utf-8") as csvfile,
        open("data/seller_en_new.csv", mode="w", encoding="utf-8") as new_csvfile,
    ):
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + [NAME_COLUMN]

        writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()

        for row in reader:
            current_row = row['ad_id']

            print()
            if not row["Website"]:
                print(f"[NO_LINK] {row['ad_id']}")
                continue

            url = row["Website"]
            if url in inaccessible_urls:
                if inaccessible_urls[url] >= 5:
                    print(f"[SKIPPED] {url}")
                    continue
            else:
                inaccessible_urls[url] = 0

            postUrl = f"{url}/chi-tiet-xe/id,{row['ad_id']}"
            print(f"[REQUEST] {postUrl}")

            request = requests.get(postUrl)
            soup = BeautifulSoup(request.content, "html.parser")
            container = soup.find(id="detail_title")

            if container is None:
                row[NAME_COLUMN] = "UNKNOWN"
                writer.writerow(row)

                inaccessible_urls[url] += 1
                print(f"[NO_DATA] {postUrl}")
                continue

            texts = [
                text
                for text in container.find("p").get_text().split(" ")
                if not text.isspace() and text != ""
            ]

            name = ""
            for word in texts:
                name += word + " "
                if word.endswith("\n"):
                    break

            row[NAME_COLUMN] = name
            writer.writerow(row)
            print(f"[DATA_OK] {name.rstrip()}")

            sleep(0.1)
except KeyboardInterrupt:
    print(f"\n[STOPPED] Script stopped at id {current_row}\n")
except Exception as err:
    print("[FATAL] Script stopped due to exception:\n")
    print(err)
