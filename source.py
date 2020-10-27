import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):

    ans = {} # name : hash dictionary
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            ans[row[0]] = row[1]

    d = {} # hash : password dictionary
    for i in range(0, 10000):
        result = hashlib.sha256(str(i).encode())
        number = result.hexdigest()
        d[number] = i

    final = {}  # name:password dictionary
    for name, value in ans.items():
        if ans[name] in d:
            final[name] = d[ans[name]]

    with open(output_file_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in final.items():
            writer.writerow([key, value])
