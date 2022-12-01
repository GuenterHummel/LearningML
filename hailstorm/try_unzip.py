import zipfile
import os
import shutil

DEST_DIR = '../data-out'


def extract_csv_file_from_zip(filename: str, destination_dir : str):
    print("extract_csv_file_from_zip")

    if filename.upper().endswith("ZIP"):
        with zipfile.ZipFile(filename, mode="r") as zip_file:
            for member in zip_file.namelist():
                filename = os.path.basename(member)

                if not filename:
                    continue

                if not filename.lower().endswith("csv"):
                    continue

                source = zip_file.open(member)
                target = open(os.path.join(destination_dir, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)


def main():
    extract_csv_file_from_zip("../data/1_99409999_kixai-data-extractor.zip", DEST_DIR)


if __name__ == "__main__":
    main()
