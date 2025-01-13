# coding: utf8

def calculate_total_size(file_content, target_lib):
    """
    统计指定 .a 文件的总体积，支持模糊匹配（如 libJVerification.a*）
    :param file_content: 文件内容字符串
    :param target_lib: 目标库名称（如 "libJVerification.a"）
    :return: 总体积大小（单位：M）
    """
    total_size = 0.0  # 总体积
    lines = file_content.splitlines()  # 按行分割文件内容

    for line in lines:
        # 检查行中是否包含以 target_lib 开头的模块
        if any(part.startswith(target_lib) for part in line.split()):
            # 提取体积部分（假设体积在行末，格式为 "X.XXM"）
            size_part = line.split()[-1]  # 获取行末的体积部分
            size = float(size_part[:-1])  # 去掉末尾的 'M' 并转换为浮点数
            total_size += size  # 累加体积

    return total_size


def read_file_content(file_path):
    """
    从本地文件读取内容
    :param file_path: 文件路径
    :return: 文件内容字符串
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# 示例使用
if __name__ == "__main__":
    # 本地文件路径
    file_path = "BaseLinkMapResult.txt"  # 替换为你的文件路径

    # 从本地文件读取内容
    file_content = read_file_content(file_path)

    # 统计 libJVerification.a* 的总体积
    target_lib = "OAuth"
    total_size = calculate_total_size(file_content, target_lib)
    print(f"{target_lib}* 的总体积为: {total_size:.2f}M")

# BC* 的总体积为: 0.63M
# libJ* 的总体积为: 2.35M
# UM* 的总体积为: 1.32M
# libWechat* 的总体积为: 0.38M
# libS(s)peech* 的总体积为: 0.98M
# OAuth* 的总体积为: 0.14M
#
