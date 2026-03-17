import random

# 骰子 ASCII 圖形
DICE_ART = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    # ... 依此類推，補上3~6的骰子圖
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def display_dice(dice_values):
    for value in dice_values:
        for line in DICE_ART[value]:
            print(line)
        print()

if __name__ == "__main__":
    print("歡迎來到擲骰子程式！")
    while True:
        try:
            num_dice = int(input("請輸入要擲幾顆骰子（1~6）："))
            if 1 <= num_dice <= 6:
                results = roll_dice(num_dice)
                display_dice(results)
                again = input("是否繼續擲骰子？(yes/no): ").lower()
                if again not in ("yes", "y"):
                    print("遊戲結束！")
                    break
            else:
                print("請輸入1到6之間的數字！")
        except ValueError:
            print("請輸入有效的數字！")
