import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
def plot_line_chart(data):
    x = list(range(1, len(data) + 1))
    plt.plot(x, data, marker='o', linestyle='-')
    plt.title('Line Chart')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def main():
    data = input("请输入数据 (以空格分隔): ").split()
    try:
        data = [float(x) for x in data]
    except ValueError:
        print("请输入有效的数字！")
        return

    if len(data) > 20:
        print("最多只能输入20个数据！")
        return

    if data:
        plot_line_chart(data)
    else:
        print("没有提供数据，无法生成图表。")

if __name__ == "__main__":
    main()