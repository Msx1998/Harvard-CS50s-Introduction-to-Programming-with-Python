"""
Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

Dear Potter, Harry,

Rather than with, for instance:

Dear Harry,

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""
import csv
import sys


def main():
    if len(sys.argv) != 3 or not all(arg.endswith('.csv') for arg in sys.argv[1:]):
        sys.exit('Usage: python script.py input.csv output.csv')
    with open(sys.argv[1], 'r') as input_file, open(sys.argv[2], 'w') as output_file:
        reader = csv.DictReader(input_file)
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        while True:
            rows = [row for row in reader]
            if not rows:
                break
            processed_rows = process_rows(rows)
            writer.writerows(processed_rows)


def process_rows(rows):
    processed_rows = []
    for row in rows:
        split_name = row["name"].split(",")
        processed_rows.append({'first': split_name[1].strip(), 'last': split_name[0], 'house': row['house']})
    return processed_rows


if __name__ == "__main__":
    main()
