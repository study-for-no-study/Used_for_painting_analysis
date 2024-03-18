import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

def calculate_differences(data):
    differences = []
    for i in range(0, len(data) - 1, 2):
        differences.append(data[i] - data[i + 1])
    return differences


def plot_line_chart(data):
    x = list(range(1, len(data) + 1))
    plt.plot(x, data, marker='o', linestyle='-')
    plt.title('不同材质的明度差值')
    plt.xlabel('组别')
    plt.ylabel('明度差值')
    plt.grid(True)

    # 添加注释
    for i, txt in enumerate(data):
        plt.annotate(txt, (x[i], data[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.show()


def main():
    data = input("请输入数字串 (以空格分隔): ").split()
    try:
        data = [float(x) for x in data]
    except ValueError:
        print("请输入有效的数字！")
        return

    if len(data) < 2:
        print("至少需要提供两个数字！")
        return

    differences = calculate_differences(data)
    plot_line_chart(differences)


if __name__ == "__main__":
    main()