def file_to_map(filename):
    dict = {}
    with open(filename) as f:
        for line in f:
            trimed = line.strip()
            dict[trimed] = dict.get(trimed, 0) + 1
    return dict


def most_common(map, count):
    freq = []
    for idx, key in enumerate(sorted(map, key=map.get, reverse=True)):
        if idx >= count:
            break
        freq.append(f'{key}={map[key]}')
    return freq


def write_list_to_file(list, output):
    with open(output, 'w') as f:
        f.write('\n'.join(list))


def main():
    filename_input = "./data/input.txt"
    filename_output = "./data/output.txt"
    select_num = 10
    try:
        write_list_to_file(most_common(file_to_map(filename_input), select_num), filename_output)
        print("Success")
    except Exception as E:
        print(f"Oops, Error: {E}")


if __name__ == "__main__":
    main()
