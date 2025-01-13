# coding: utf8

def summarize_module_sizes(file_content):
    """
    按 [ 前的名称汇总分类各个模块的代码大小
    :param file_content: 文件内容字符串
    :return: 字典，键为模块名称，值为模块的总体积
    """
    module_size_dict = {}  # 存储模块名称及其总体积
    lines = file_content.splitlines()  # 按行分割文件内容

    for line in lines:
        # 提取模块名称（[ 前的部分）
        if "[" in line:
            module_name = line.split("[")[0].strip()  # 获取 [ 前的名称并去掉空格
        else:
            module_name = line.split()[0].strip()  # 如果没有 [，则取第一个部分作为名称

        # 提取体积部分（假设体积在行末，格式为 "X.XXM"）
        size_part = line.split()[-1]  # 获取行末的体积部分
        size = float(size_part[:-1])  # 去掉末尾的 'M' 并转换为浮点数

        # 累加模块的总体积
        if module_name in module_size_dict:
            module_size_dict[module_name] += size
        else:
            module_size_dict[module_name] = size

    return module_size_dict


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

    # 汇总分类各个模块的代码大小
    module_size_dict = summarize_module_sizes(file_content)

    # 输出结果
    print("模块名称\t\t总体积 (M)")
    print("-----------------------------")
    for module_name, total_size in module_size_dict.items():
        print(f"{module_name}\t\t{total_size:.2f}M")
