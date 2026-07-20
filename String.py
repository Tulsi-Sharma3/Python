str = "Tulsi"           # 'tulsi' or '''tulsi'''

print(str[0])           # T
print(str[-1])          # i
print(str[1:4])
print(str[ :5])
print(str[::-1])        # reverse string -> isluT

print(len(str))             # 5
print(str.find("ls"))       # 2
print(str.count("l"))       # 1
print(str.startswith("tu"))
print(str.endswith("Si"))


# Type Conversion
s = "hello shnaya. shnaya"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())

print("ha" * 3)
print("py" in s)            # False
print("el" in s)            # True

td  = s.strip()
print(td)
print(s.lstrip())
print(s.rstrip())

print("new")
ss = "A,B,C"
print(s.split(","))
