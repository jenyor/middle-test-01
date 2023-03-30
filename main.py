def string_to_map(text):
    dict = {}
    for line in text.splitlines():
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
        with open(filename_input, 'r') as f:
            input_text = f.read()
        write_list_to_file(most_common(string_to_map(input_text), select_num), filename_output)
        print("Success")
    except Exception as E:
        print(f"Oops, Error: {E}")


if __name__ == "__main__":
    main()
