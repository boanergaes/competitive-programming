def split_and_join(line):
    # write your code here
    new_str = ''
    for i in line:
        new_str += i if i != ' ' else '-'
    return new_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)