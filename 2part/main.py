lst_of_info = []
i = 1
while i < 4:
    num_str = 0
    file_name = ''
    lst_of_str = ''

    with open(f'{i}.txt', encoding="utf-8") as f:
        lines = [line.strip() for line in f]
        file_name = f.name
        num_str = len(lines)
        lst_of_str = lines
        lst_of_info.append([num_str, file_name, lst_of_str])
        i += 1
        f.close()
    lst_of_info.sort()

with open('4.txt', 'w', encoding="utf-8") as f:
    for lst in lst_of_info:
        for el in lst:
            if not isinstance(el, list):
                f.write(f'{str(el)}\n')
            else:
                f.write("\n".join(el))
                f.write('\n')
    f.close()
