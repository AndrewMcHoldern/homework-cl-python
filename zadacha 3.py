postcards = {
    "Maria":"London",
    "Lorenzo":"Milan",
    "Oleg":"Canberra",
    "Hans":"Calgary",
    "Mark":"Milan",
    "Alex":"Krakow",
    "Julia":"Murmansk"
}
others = {"Petra":"Paris", "Ivan":"Moscow"}
postcards.update(others)
print(postcards)
postcards["Oleg"] = 'Sydney'
print(postcards)
print(set(postcards.values()))
print(len(set(postcards.values())))


