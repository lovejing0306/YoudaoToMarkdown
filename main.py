# coding=utf-8

def convert(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        lines = infile.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            # line = line.replace(' ', '')
            if '_' in line:
                line = line.replace('_', ' _ ')
            if '`$' in line:
                # line = line.replace('`$', ' `$')
                line = line.replace('`$', '$')
                if '_' in line:
                    line = line.replace('_', ' _ ')
            if '$`' in line:
                # line = line.replace('$`', '$` ')
                line = line.replace('$`', '$')
            if '```math' in line:
                #outfile.write('\n')
                line = line.replace('```math', '$$')
                outfile.write(line)
                i += 1
                while i < len(lines):
                    line = lines[i]
                    if '```' in line:
                        line = line.replace('```', '$$')
                        outfile.write(line)
                        #outfile.write('\n')
                        break
                    i += 1
                    outfile.write(line)
                i += 1
                continue
            if '==' in line:
                count = line.count('==')
                if count % 2 == 0:
                    line = line.replace('==', '')
            i += 1
            outfile.write(line)


def main():
    input_path = '/Users/littlebei/Downloads/优化算法_费马定理(解析解).md'
    output_path = '/Users/littlebei/Downloads/优化算法_费马定理(解析解)2.md'
    convert(input_path, output_path)


if __name__ == '__main__':
    main()
