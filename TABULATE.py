from tabulate import tabulate
headers=["name","age","department"]
data=[
    ["Ravi",25,"HR"],
]
print(tabulate(data,headers=headers,tablefmt="fancy_grid"))