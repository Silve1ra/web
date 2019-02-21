import one

print("top level two")

one.func()

if __name__ == '__main__':
    print("two being run directly")
else:
    print("two is being imported")