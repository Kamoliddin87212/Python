## Exercise 1: Convert List to 1D Array
import numpy as np
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print(arr)

## Exercise 2: Create 3x3 Matrix (2 to 10)
import numpy as np
arr = np.arange(2, 11).reshape(3,3)
print(arr)

## Exercise 3: Null Vector & Update Sixth Value
import numpy as np
arr = np.zeros(10)
arr[5] = 11
print(arr)

## Exercise 4: Array from 12 to 38
import numpy as np
arr = np.arange(12, 38)
print(arr)

## Exercise 5: Convert Array to Float Type
import numpy as np
arr = np.array([1,2,3,4])
arr = arr.astype(float)
print(arr)

## Exercise 6: Celsius to Fahrenheit Conversion
import numpy as np
c = np.array([0, 12, 45.21, 34, 99.91])
f = c * 9/5 + 32
print(f)

## Exercise 7: Append Values to Array
import numpy as np
arr = np.array([10,20,30])
arr = np.append(arr, [40,50,60,70,80,90])
print(arr)

## Exercise 8: Array Statistical Functions
import numpy as np
arr = np.random.rand(10)
print(np.mean(arr), np.median(arr), np.std(arr))

## Exercise 9: Find min and max in 10x10
import numpy as np
arr = np.random.rand(10,10)
print(np.min(arr), np.max(arr))

## Exercise 10: 3x3x3 random
import numpy as np
arr = np.random.rand(3,3,3)
print(arr)
