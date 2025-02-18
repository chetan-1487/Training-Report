try:
    a=1/1
    print(a)
except ZeroDivisionError:
    print("zero Division error")



try:
    n = 0
    res = 100 / 1
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print("Result is", res)
finally:
    print("Execution complete.")


def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
try:
    set(-5)
except ValueError as e:
    print(e)
