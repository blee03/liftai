import tensorflow as tf 

#output the sum of all of the values in a vector
def vectorSum(vector):
    sum = 0
    for i in vector.len:
        sum += vector[i]
    return sum
#determine the sum of 6 vectors,
def dotSum(v1,v2,v3,v4,v5,v6):
    result = int[v1.len]
    for i in v1.len:
        result[i] = v1[i] + v2[i] + v3[i] + v4[i] + v5[i] + v6[i]
    return result-1

def model_fn(v1,v2,v3,v4,v5,v6):
    return tf.minimize(dotSum)
