import sys

if __name__ == "__main__":

    n = int(sys.stdin.readline())
    student = list(map(int, sys.stdin.readline().split()))
    main_dir, sub_dir = list(map(int, sys.stdin.readline().split()))
    num_of_dirs = 0

    for stu in student:
        stu -= main_dir
        num_of_dirs += 1

        if stu > sub_dir:
            quot, left = stu // sub_dir, stu % sub_dir

            num_of_dirs += quot
            if left != 0:
                num_of_dirs += 1
        elif 0 < stu <= sub_dir:
            num_of_dirs += 1

    print(num_of_dirs)
