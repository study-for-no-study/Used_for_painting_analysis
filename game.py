import time

def introduction():
    print("欢迎来到小冒险游戏！")
    time.sleep(1)
    print("你将要进入一个神奇的世界...")
    time.sleep(2)
    print("你的任务是找到宝藏并带回来！")
    time.sleep(2)

def choose_path():
    print("\n你来到了一个岔路口，你要往左走还是往右走？")
    choice = input("输入左或右: ").lower()
    if choice == "左":
        print("\n你选择了向左走...")
        time.sleep(1)
        left_path()
    elif choice == "右":
        print("\n你选择了向右走...")
        time.sleep(1)
        right_path()
    else:
        print("无效的选择，请输入左或右。")
        choose_path()

def left_path():
    print("\n你走着走着，发现了一只巨大的食人花！")
    time.sleep(2)
    print("它看起来很饥饿，你会：")
    time.sleep(1)
    print("1. 试图逃跑")
    print("2. 继续接近并尝试与它对话")
    choice = input("输入1或2: ")
    if choice == "1":
        print("\n你试图逃跑，但是食人花太快了，它抓住了你！")
        time.sleep(2)
        game_over()
    elif choice == "2":
        print("\n你走向食人花，开始与它交谈...")
        time.sleep(2)
        print("令人惊讶的是，食人花居然是友好的！它告诉你宝藏的所在。")
        time.sleep(2)
        print("你继续前进，找到了宝藏！恭喜你，任务完成！")
        time.sleep(2)
        play_again()
    else:
        print("无效的选择，请输入1或2。")
        left_path()

def right_path():
    print("\n你沿着右边的路走着...")
    time.sleep(2)
    print("你看见了一个宝箱，但是周围有一条巨大的蛇！")
    time.sleep(2)
    print("你会：")
    time.sleep(1)
    print("1. 尝试打开宝箱")
    print("2. 尝试诱导蛇离开")
    choice = input("输入1或2: ")
    if choice == "1":
        print("\n你试图打开宝箱，但是蛇被惊醒了，它攻击了你！")
        time.sleep(2)
        game_over()
    elif choice == "2":
        print("\n你试图诱导蛇离开...")
        time.sleep(2)
        print("你成功地诱导了蛇离开，你打开了宝箱，里面有宝藏！")
        time.sleep(2)
        print("恭喜你，任务完成！")
        time.sleep(2)
        play_again()
    else:
        print("无效的选择，请输入1或2。")
        right_path()

def game_over():
    print("\n游戏结束，你失败了！")
    play_again()

def play_again():
    choice = input("\n你想再玩一次吗？ (是/否): ").lower()
    if choice == "是":
        start_game()
    elif choice == "否":
        print("谢谢你玩这个游戏，再见！")
    else:
        print("无效的选择，请输入是或否。")
        play_again()

def start_game():
    introduction()
    choose_path()

start_game()
