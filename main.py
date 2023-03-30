def file_to_map(filename):
    dict = {}
    with open(filename) as f:
        for line in f:
            trimed = line.strip()
            dict[trimed] = dict.get(trimed, 0) + 1
    return dict

def most_common(map, output, count):
    with open(output, 'w') as f:
        for idx, key in enumerate(sorted(map, key=map.get, reverse=True)):
            if idx >= count:
                break
            f.write(f'{key}={map[key]}\n')

def main():
    filename_input = "./data/input.txt"
    filename_output = "./data/output.txt"
    select_num = 10
    try:
        most_common(file_to_map(filename_input), filename_output, select_num)
        print("Success")
    except Exception as E:
        print(f"Oops, Error: {E}")

if __name__ == "__main__":
    main()
