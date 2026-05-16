from pathlib import Path

current_file = Path(__file__)
print(current_file)

parent_directory = current_file.parent
print(parent_directory)

absolute_path = current_file.resolve()
print(absolute_path)


data_file = parent_directory / 'data' / 'example.txt'
print(data_file)


print("Does file exist?", data_file.exists())