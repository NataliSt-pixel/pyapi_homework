import os


def merge_files(input_files, output_file):
    files_info = []
    for filename in input_files:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            files_info.append({
                'name': filename,
                'line_count': len(lines),
                'content': lines
            })
    files_info.sort(key=lambda x: x['line_count'])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_info in files_info:
            out_file.write(f"{file_info['name']}\n")
            out_file.write(f"{file_info['line_count']}\n")
            out_file.writelines(file_info['content'])


if __name__ == "__main__":
    input_files = ['/Users/natalastupnickaa/Desktop/pyapi_homework/exercise3/1.txt',
                   '/Users/natalastupnickaa/Desktop/pyapi_homework/exercise3/2.txt',
                   '/Users/natalastupnickaa/Desktop/pyapi_homework/exercise3/3.txt']
    output_file = 'merged.txt'
    merge_files(input_files, output_file)

