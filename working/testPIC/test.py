import subprocess

# Example function to call the PIE executable
def call_wrap_function(*args):
    result = subprocess.run(['./wrap'] + list(args), capture_output=True, text=True)
    return result.stdout.strip()

# Call the functions
result1 = call_wrap_function('test_function', 'Hello, World!')
print("Result1:", result1)

result2 = call_wrap_function('non_pic_function', 'Hello, World!')
print("Result2:", result2)
