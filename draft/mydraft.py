from LyPythonToolbox import lyprint_elapsed_time

@lyprint_elapsed_time
def print_howmanyhaha(times):
    for i in range(times):
        print("haha")
        result = i
    return result

result = print_howmanyhaha(2)
print(f"result={result}")