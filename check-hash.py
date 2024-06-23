import os

# 最新 hash
LAST_HASH = [
    # 莫娜
    "515f3ce6",
    "bad2731b",
    "e543af5d",
    "c814ad67",
    "d5ad8084",
    "8991360f",
    "8e116301"
]


def main():
    """
    检查是否存在已过时 hash
    """
    for e in scan_ini("D:/game/原神 mod/需要修复的 MOD/莫娜-全裸"):
        print("open", e)
        fs = open(e, "r")
        ini_content: list[str] = fs.readlines()
        fs.close()

        check_hash(ini_content)

        fs = open(e, "w")
        fs.writelines(ini_content)
    input("按任意键退出程序")
    pass


def check_hash(ini_content: list[str]):
    for line_index in range(len(ini_content)):
        line = ini_content[line_index]
        index = line.find("=")
        if index == -1 or index == len(line) - 1:
            continue
        key = line[0: index].strip().lower()
        value = line[index + 1: len(line)].strip().lower()
        # 输出已过时的 HASH
        if key == "hash" and value not in LAST_HASH:
            print("unknown hash:", value)
            pass
    return


def scan_ini(directory) -> list[str]:
    """
    扫描 ini 文件
    """
    e: str
    ini_files = []
    for f in os.listdir(directory):
        f = f"{directory}/{f}"
        if os.path.isdir(f):
            ini_files.extend(scan_ini(f))
            pass
        else:
            suffix = f[len(f) - 4: len(f)]
            if suffix == ".ini":
                ini_files.append(f)
            pass
    return ini_files


if __name__ == '__main__':
    main()
