import sys
import os


def check_file(filename):
    if not os.path.isfile(filename):
        print(f"{filename} do not exist")
        sys.exit(1)
    if not os.access(filename, os.R_OK):
        print(f"{filename} is not readable")
        sys.exit(1)


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    packages = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 4:
            packages.append({
                'category': parts[0],
                'name': parts[1],
                'description': parts[2],
                'size': int(parts[3])
            })
    return packages


def option_a(packages):
    if len(packages) == 0:
        print("No packages installed")
    else:
        print("Installed packages:")
        for pkg in packages:
            print(pkg['name'])

def option_s(packages):
    total_size = sum(pkg['size'] for pkg in packages)
    print(f"Total size in kilobytes: {total_size}")

def option_l(packages, package_name):
    found = False
    for pkg in packages:
        if pkg['name'] == package_name:
            print(f"Package: {pkg['name']}")
            print(f"Category: {pkg['category']}")
            print(f"Description: {pkg['description']}")
            print(f"Size in kilobytes: {pkg['size']}")
            found = True
            break
    if not found:
        print(f"No installed package with this name")

# 处理 -v 选项，输出作者信息
def option_v():
    print("Package information command-line tool")
    print("Version: 1.0")

# 主程序入口
def main():
    if len(sys.argv) < 3:
        print("It misses the argument file")
        sys.exit(1)
    
    option = sys.argv[1]
    argument_file = sys.argv[2]
    if option == '-a':
        check_file(argument_file)
        packages = read_file(argument_file)
        option_a(packages)
    elif option == '-s':
        check_file(argument_file)
        packages = read_file(argument_file)
        option_s(packages)
    elif option == '-l':
        if len(sys.argv) < 4:
            print("It misses an argument")
            sys.exit(1)

        package_name = sys.argv[2]
        argument_file = sys.argv[3]
        check_file(argument_file)
        packages = read_file(argument_file)
        option_l(packages, package_name)
    elif option == '-v':
        check_file(argument_file)
        option_v()
    else:
        print("This option doesn't exist")
        sys.exit(1)

if __name__ == "__main__":
    main()