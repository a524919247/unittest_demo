import xlrd


def excal_list(data_file,sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)

    for i in range(1,sh.nrows):
        d = dict(zip(header,sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data

if __name__ == '__main__':   # 测试一下自己的代码
    data_list = excal_list("/Users/bytedance/Desktop/test/unittest_demo_one/data/test_user_data.xlsx", "TestUserLogin")  # 读取excel，TestUserLogin工作簿的所有数据
    case_data = get_test_data(data_list, 'test_type_error')  # 查找用例'test_user_login_normal'的数据
    print(case_data)

