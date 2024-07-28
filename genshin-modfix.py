import os

v46_hash = {
    # 莫娜
    "ee5ed1dc": "7a1dc890",
    "41f18240": "8991360f",
    "ed79ea5b": "d75308d8"
}

v47_hash = {
    # 莫娜
    "7a1dc890": "515f3ce6",
    "b043715a": "bad2731b",
    "a8191396": "e543af5d",
    "00741928": "c814ad67",
    "d75308d8": "d5ad8084",
    "8991360f": "c814ad67"
}


def main():
    for e in scan_ini("."):
        fs = open(e, "r")
        ini_content: list[str] = fs.readlines()
        fs.close()

        mod_fix(e, ini_content, v46_hash)
        mod_fix(e, ini_content, v47_hash)

        fs = open(e, "w")
        fs.writelines(ini_content)
    input("按任意键退出程序")
    pass


def mod_fix(file_name: str, ini_content: list[str], hash_map: dict[str, str]):
    for line_index in range(len(ini_content)):
        line = ini_content[line_index]
        index = line.find("=")
        if index == -1 or index == len(line) - 1:
            continue
        key = line[0: index].strip().lower()
        value = line[index + 1: len(line)].strip().lower()

        # 将旧 hash 替换为新 hash
        if key == "hash" and value in hash_map.keys():
            new_hash: str = hash_map[value]
            new_hash = new_hash.strip()
            print(f"{file_name}: {value} -> {new_hash}")
            ini_content[line_index] = f"{key} = {new_hash}\n"
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
