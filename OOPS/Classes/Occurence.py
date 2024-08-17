def check(k):
    my_dict = {}
    for name in k:
        my_dict[name] = my_dict.get(name, 0) + 1

    for w, i in my_dict.items():
        print(f"{w}, {i}")


st = input("")
k = st.split(" ")

check(k)
