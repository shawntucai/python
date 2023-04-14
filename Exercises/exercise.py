weight = input("Weight: ")
metric = input(f'(L)bs or (K)gs: ')
if metric == "L" or "l":
    weight_lbs = float(weight) * 0.45
    print(f'You are {weight_lbs} kgs')
elif metric == "K" or "k":
    weight_kgs = float(weight) * 2.2
    print(f'You are {weight_kgs} lbs')