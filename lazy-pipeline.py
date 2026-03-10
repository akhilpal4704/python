import sys
import json

def read_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)

def filter_logs(logs, level=None, message_substring=None):
    for log in logs:
        if (level is not None and log.get("level", "").lower() != level.lower()):
            continue
        if (message_substring is not None and message_substring.lower() not in log.get("message", "").lower()):
            continue
        yield log

def extract_fields(logs, field = None):
    for log in logs:
        if field is None:
            yield log
        else:
            yield log.get(field, "" ).strip()

def get_first_n_logs(logs, n):
    count = 0
    for log in logs:
        if count >= n:
            break
        yield log
        count += 1

logs_gen = read_logs('logs.txt')
filtered_logs = filter_logs(logs_gen,level = "error",message_substring="login")
extracted_logs = extract_fields(filtered_logs, )

for log in get_first_n_logs(extracted_logs, 15):
    print(log)
