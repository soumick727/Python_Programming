# marks = {
#     "debendra": 78,
#     "pritam": 76,
#     "soumick": 90
# }

# print(marks)
# print(marks["pritam"])
# print(marks.get("soumick"))
# print(marks.get("unknown", "Not Found"))
# print(marks.values())
# print(marks.keys())
# print(marks.items())


desc_1 = {"name":"pritam","roll_no":"26","roll_no":"21","stream":"BCA"}
print(desc_1)
print(desc_1.values())
print(desc_1.keys())
print(desc_1.items())
print(type(desc_1))
print(desc_1["stream"])
print(desc_1["roll_no"])
desc_1.update({"year":"2025"})
desc_1.update({"name":"debendra"})
print(desc_1)

value = desc_1.pop("year")
print(value)
print(desc_1)