from solution import *

file_path = input("Enter absolute path to file: ")


with open(file_path) as file:
    captured_data = json.load(file).get("message")

result = sniff(captured_data)

result_file_name = (file_path.split("/")[-1]).replace("data", "schema")

with open(f"./schema/{result_file_name}", "w+") as result_file:
    result_file.write(json.dumps(result))

