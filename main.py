'''
Author: Little Weak-duck
Date: 2023-10-08 18:27:43
LastEditors: Little Weak-duck
LastEditTime: 2023-10-08 19:18:12
FilePath: /main.py
Description: get data from csv and generate response from openAI
'''
import openai
import os
import pandas as pd


# Set up OpenAI API credentials
openai.api_key = '' # 替换为你的 OpenAI API 密钥

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-4', # 替换为你的模型名称
        messages=[{"role": "user", "content": prompt}]
    )
    # print(response)
    return response['choices'][0]['message']['content'].strip()

def csv_to_2d_array(file_name):
    # 读取 CSV 文件
    data = pd.read_csv(file_name, encoding='utf-8')
    # 获取二维数组
    array = data.values
    return array

def write_data_to_csv(data, file_name):
    # 创建一个 DataFrame
    df = pd.DataFrame(data)
    # 将 DataFrame 写入 CSV 文件
    df.to_csv(file_name, index=False, header=False, encoding='utf-8-sig')

if __name__ == "__main__":
    file_name = ''  # 替换为你的 CSV 文件名
    csvData = csv_to_2d_array(file_name)
    result = [[]] # 保存结果的 title
    # for data in csvData:
    for data in csvData:    
        prompt = '' # 替换为你的问题
        generated_response = generate_response(prompt)
        this_result = [data[0],data[1],generated_response]
        result.append(this_result)
        print(generated_response)
    
    print(result)
    # 保存结果
    write_data_to_csv(result, './result.csv')
    