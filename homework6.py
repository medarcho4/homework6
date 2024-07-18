my_dict={"Real Madrid": 15, "barcelona": 5}
print(my_dict)
print(my_dict["Real Madrid"])
print(my_dict.get("Manchester City"))
my_dict.update({"Bayern Munich": 6, "Milan": 7})
x=my_dict.pop("barcelona")
print(x)

my_set={1,1,"a","a"}
print(my_set)
my_set.add("b")
my_set.add(2)
my_set.discard(2)
print(my_set)
