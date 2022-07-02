#1
def hello():
    print('hello world')
#2
def pack(a, b, c):
    return [a, b, c]
#3
def eat_lunch(str):
  if len(str) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(str)):
      if i == 0:
        print(f"First I eat {str[0]}")
      else:
        print(f"Next I eat {str[i]}")
        
#printing
hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])