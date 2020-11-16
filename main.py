import data
import gui


if __name__ == '__main__':
    results = data.read_data("data.txt")
    print(results)
    print(data.format_State("data.txt"))
    print(data.format_Vote("data.txt"))
    print(data.format_Lean("data.txt"))
    print(data.list_Democratic("data.txt"))
    print(data.list_Republican("data.txt"))
    print(data.list_Swing("data.txt"))
    data.Move_States("data.txt", "Florida", "swing", "red")
    print(data.blue)
    print(data.red)
    print(data.swing)

