def solution(n, r):
    # Write your answer here
    # status: "passed", "failed", "timeout", "error"
    # 测试用例按照连续自然数编号分组
    # 每组测试用例必须都通过才可得分
    # 如果一组只有一个测试用例，命名为 [任务名称]+[组号]
    # 如果一组有多个测试用例，命名为 test1a
    # 组数 * 100 / 组数
    # 如果是小书，四舍五入保留整数
    # 2 * 100 / 3 = 66
    """
    根据测试用例数据算出最终得分

    Args:
        n(list[str]): 测试用例的名称列表
        r(list[str]): 测试用例对应的通过情况
    Returns:
        (int): 最终的得分
    """
    import re
    # 输入数据校验
    assert len(n) == len(r), "input data error"
    # 用例状态字典
    is_int = re.compile(r"^[0-9]$")

    group_name_list = []
    for case_name in n:
        group_name = ""
        idx = 0
        while (not is_int.search(case_name[idx])) and (idx+1) <= len(case_name):
            group_name = group_name + case_name[idx]
            idx = idx + 1
        group_name_list.append(group_name)
    # 去重
    group_name_list = list(set(group_name_list))
    # 组数
    group_number = len(group_name_list)
    group_name_dict = {i: 1 for i in group_name_list}

    # 通过数
    for status_idx, status in enumerate(r):
        g_name = ""
        for _name in group_name_dict:
            if status.startswith(_name):
                g_name = _name
                break
        if status != "passed":
            group_name_dict[g_name] = 0
    print(group_name_dict)

    passed_num = 0
    for k, v in group_name_dict.items():
        if v == 1:
            passed_num = passed_num + 1
    final_score = group_number * 100 // passed_num
    print(group_number)
    print(passed_num)
    return final_score


if __name__ == "__main__":
    n = ["test1", "jack1a", "jack1b"]
    r = ["passed", "passed", "error"]
    print(solution(n, r))
