import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
# 数据
labels = ["高光", '亮面', '灰面', '暗面', '反光']
skin_values = [100, 95, 85, 73, 84]
hair_values = [100, 95, 87, 67, 80]

# 创建子图
fig, ax = plt.subplots()

# 绘制柱状图
x = range(len(labels))
ax.bar(x, skin_values, width=0.4, align='center', label="皮肤")
ax.bar([i + 0.4 for i in x], hair_values, width=0.4, align='center', label='头发')

# 添加详细的数值标注
for i, v in enumerate(skin_values):
    ax.text(i, v + 1, str(v), ha='center', va='bottom', color='black', fontsize=8)
for i, v in enumerate(hair_values):
    ax.text(i + 0.4, v + 1, str(v), ha='center', va='bottom', color='black', fontsize=8)

# 添加图例、标题和轴标签
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.title('皮肤和头发材质评估')
plt.xlabel('要素')
plt.ylabel('评分')

# 显示图形
plt.grid(True)
plt.show()
