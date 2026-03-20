import argparse
import csv
from collections import defaultdict
from statistics import median
from tabulate import tabulate


def read_files(file_paths):
    data = []
    for path in file_paths:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data


def median_coffee_report(data):
    students = defaultdict(list)

    for row in data:
        name = row["student"]
        spent = float(row["coffee_spent"])
        students[name].append(spent)

    result = []
    for name, values in students.items():
        result.append((name, median(values)))

    result.sort(key=lambda x: x[1], reverse=True)

    print(tabulate(result, headers=["Student", "Median Coffee"], tablefmt="grid"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    data = read_files(args.files)

    if args.report == "median-coffee":
        median_coffee_report(data)
    else:
        print("Неизвестный отчет")


if __name__ == "__main__":
    main()