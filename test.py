import numpy as np
import time

python_list = list(range(10_000_000))

start = time.time()
res = [x * 2 for x in python_list]
print(f"Python List: {time.time() - start:.4f}s")

numpy_array = np.array(10_000_000)
start = time.time()
res_np = numpy_array * 2
print(f"NumPy Array: {time.time() - start:.4f}s")
