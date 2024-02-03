def split_list(list: str) -> list[str]:
    new_list = []
    for rec in list:
        new_list.append(rec.split(','))
    return new_list

def strip_array(array: list) -> list:
    for i in range(len(array)):
        if type(array[i]) == str:
            array[i] = array[i].strip()
        else:
            strip_array(array[i])
    return array