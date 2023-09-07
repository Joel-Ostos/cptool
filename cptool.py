#!/usr/bin/env python3
import subprocess
import sys
import os

def are_files_equal(file1_path, file2_path, executable_file):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read().rstrip('\n')
        content2 = file2.read().rstrip('\n')
        lines1 = content1.split('\n')
        lines2 = content2.split('\n')
        
        if content1 == content2:
            print("\033[32mTest passed\033[0m")
            a = input("Do you want to delete:\nType the number\n1 Test file\n2 Output file\n3 Compiled file\n4 All\n5 None\n")
            if a == '1':
                os.remove("test.txt")
            elif a == '2':
                os.remove("output.txt")
            elif a == '3':
                os.remove(f"{executable_file}")
            elif a == '4':
                os.remove("output.txt")
                os.remove("test.txt")
                os.remove(f"{executable_file}")
        else:
            print("Test not passed\nBecause:")
            for index, (line1, line2) in enumerate(zip(lines1, lines2)):
                if line1 != line2:
                    print(f"On file 1(output) line {index+1}: \n", line1)
                    print(f"On file 2(test) line {index+1}: \n", line2)


def main():
    if len(sys.argv) < 2:
        print("Use: python cptool <name of the .cpp (without cpp extension) file>")
        print("Make sure that your .cpp program writes the output on a file called output.txt")
        sys.exit(1)

    filename = sys.argv[1]

    if ".cpp" in filename:
        print("Don't use .cpp extension, run the program this way:\ncptool <filename>")
        sys.exit(1)  

    compile_command = f"g++ {filename}.cpp -o {filename}"
    compile_process = subprocess.run(compile_command, shell=True, text=True, capture_output=True)

    if compile_process.returncode == 0:
        print("\033[32m Successful compilation!\033[0m")

        run_command = f"./{filename}"
        run_process = subprocess.run(run_command, shell=True, text=True, capture_output=True)

        if run_process.returncode == 0:
            print("\033[34m Successfully executed program\033[0m")
            print(run_process.stdout)
        else:
            print("\033[31mError running program:\033[0m")
            print(run_process.stderr)
    else:
        print("\033[31mError compiling program:\033[0m")
        print(compile_process.stderr)
        print("Use: python cptool <name of the .cpp (without cpp extension) file>")
        sys.exit(1)  

    print("\033[32mScanning...\033[0m")
    are_files_equal("output.txt", "test.txt", filename)


if __name__ == "__main__":
    main()

