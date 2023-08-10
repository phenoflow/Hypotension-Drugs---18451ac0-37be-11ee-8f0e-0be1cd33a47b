# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"G57y000","system":"readv2"},{"code":"G57y100","system":"readv2"},{"code":"G57y300","system":"readv2"},{"code":"R059.00","system":"readv2"},{"code":"4279PK","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypotension-drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypotension-drugs-sinus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypotension-drugs-sinus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypotension-drugs-sinus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
