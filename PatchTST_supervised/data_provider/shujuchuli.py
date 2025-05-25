#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :shujuchuli.py
# @Time      :2025/5/23 下午5:00
# @Author    :LiXiaolong


import pandas as pd
from datetime import datetime


def filter_excel_by_dates(input_file, output_file, date_ranges):
    """
    从Excel文件中筛选多个日期范围内的数据并保存到新文件

    参数:
    input_file (str): 输入Excel文件路径
    output_file (str): 输出Excel文件路径
    date_ranges (list): 日期范围列表，每个范围为(start_date, end_date)元组
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(input_file)

        # 确保日期列存在
        if 'Calculated Date' not in df.columns:
            print(f"错误: 数据中不存在名为'date_column'的列。")
            return False

        # 将日期列转换为datetime类型
        df['Calculated Date'] = pd.to_datetime(df['Calculated Date'])

        # 创建空的筛选结果DataFrame
        filtered_df = pd.DataFrame()

        # 筛选每个日期范围内的数据并合并
        for start_date, end_date in date_ranges:
            # 转换输入日期为datetime对象
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')

            # 筛选当前日期范围内的数据
            current_range_df = df[(df['Calculated Date'] >= start) & (df['Calculated Date'] <= end)]

            # 合并到结果DataFrame
            filtered_df = pd.concat([filtered_df, current_range_df])

        # 保存筛选结果到新Excel文件
        filtered_df.to_excel(output_file, index=False)
        print(f"成功筛选并保存 {len(filtered_df)} 条记录到 {output_file}")
        return True

    except Exception as e:
        print(f"处理Excel文件时出错: {e}")
        return False


if __name__ == "__main__":
    # 配置参数
    INPUT_FILE = "2013_2018_SYMH_month.xlsx"  # 替换为你的输入文件路径
    OUTPUT_FILE = "2013_2018_test.xlsx"  # 替换为你的输出文件路径

    # 定义多个日期范围，格式为[(start1, end1), (start2, end2), ...]

    DATE_RANGES = [
        ("2013-05-28", "2013-06-04"),  # 替换为你图片中的日期范围3
        ("2013-06-26", "2013-07-04"),  # 替换为你图片中的日期范围1
        ("2015-03-11", "2015-03-21"),  # 替换为你图片中的日期范围2
        ("2018-08-22", "2018-09-03"),  # 替换为你图片中的日期范围3
    ]



    # 执行筛选
    filter_excel_by_dates(INPUT_FILE, OUTPUT_FILE, DATE_RANGES)
'''

          ("2012-09-10", "2012-10-05"),  # 替换为你图片中的日期范围3
       
'''