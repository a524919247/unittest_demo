import xlrd


# 从excal获取到需要sheet表的所有数据
def excal_list(data_file,sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)   # 打开文件
    sh = wb.sheet_by_name(sheet)   # 打开sheet表
    header = sh.row_values(0)   #获取到第一行数据

    for i in range(1,sh.nrows):     # 从第二行开始获取数据
        d = dict(zip(header,sh.row_values(i)))
        data_list.append(d)     # 获取到的数据放在list中
    return data_list

# 从获取到的数据中根据case_name选择想要的用例数据
def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data

# if __name__ == '__main__':   # 测试代码
#     data_list = excal_list("/Users/bytedance/Desktop/test/unittest_demo/unittest_demo_one/data/test_user_data.xlsx", "TestUserLogin")  # 读取excel，TestUserLogin工作簿的所有数据
#     case_data = get_test_data(data_list, 'test_type_error')  # 查找用例'test_user_login_normal'的数据
#     print(case_data)

