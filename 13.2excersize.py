from sys import argv as arguments

script = arguments
#script = str(script)
print(f"name: {script}", script)

for value in script:
	print(value)