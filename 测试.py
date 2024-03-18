# # 计算相邻元素之间的差值并命名
#
# labels = ["高光", '亮面', '灰面', '暗面', '反光']
# skin_values = [100, 95, 85, 73, 84]
# hair_values = [100, 95, 87, 67, 80]
#
#
# skin_diff_names = ['高光亮面差', '亮面灰面差', '灰面暗面差', '暗面反光差', '亮面暗面差']
# skin_diff = [skin_values[i] - skin_values[i+1] for i in range(len(skin_values)-1)]
# a =[skin_diff[1] - skin_diff[3]]
# skin_diff = skin_diff + a
# hair_diff_names = ['高光亮面差', '亮面灰面差', '灰面暗面差', '暗面反光差', '亮面暗面差']
# hair_diff = [hair_values[i] - hair_values[i+1] for i in range(len(hair_values)-1)]
# b =[hair_diff[1] - hair_diff[3]]
# hair_diff = hair_diff + b
#
# print(skin_diff)
# print(hair_diff)
#
#
# # 打印表格
# print("| 皮肤差值名称 | 皮肤差值 | 头发差值名称 | 头发差值 |")
# print("|-------------|---------|-------------|---------|")
# for skin_name, skin, hair_name, hair in zip(skin_diff_names, skin_diff, hair_diff_names, hair_diff):
#     print("|   {}   |   {}   |   {}   |   {}   |".format(skin_name, skin, hair_name, hair))




# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']
# # 数据
# labels = ['高光亮面差', '亮面灰面差', '灰面暗面差', '暗面反光差', '亮面暗面差']
# skin_diff_values = [5, 10, 12, -11, 21]
# hair_diff_values = [5, 8, 20, -13, 21]
#
# # 绘制折线图
# plt.plot(labels, skin_diff_values, marker='o', label='皮肤')
# plt.plot(labels, hair_diff_values, marker='o', label='头发')
#
# # 添加图例、标题和轴标签
# plt.legend()
# plt.title('皮肤和头发材质差值')
# plt.xlabel('差值名称')
# plt.ylabel('差值')
#
# # 显示图形
# plt.grid(True)
# plt.show()









