text = "kskngwhg-1rthrh+2rhrh0rhrh122rhr500rhr"
my_list = []
num = ""

for i in range(0, len(text)):
    if text[i].isdigit():
        num += f"{text[i - 1]}{text[i]}" if text[i - 1] == "-" else f"{text[i]}"
    else:
        if num:
            my_list.append(int(num))
            num = ''

print(f"Min = {min(my_list)}, Max = {max(my_list)}")
