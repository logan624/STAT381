import math

def main():

    data = [ 0.53,1.08,1.25,2.17,1.54,1.01,1.08,1.06,1.82,2.03,0.93,0.80,1.41,0.60,1.52,1.04,1.12,1.78,1.00,1.13
 ]

    print("Size of dataset: ", str(len(data)))
    sum = calculateSum(data)
    print("The sum is: ", str(sum))
    mean = calculateMean(data, sum)
    print("The mean is: ", str(mean))
    variance_computational = varianceComputation(data, mean, sum)
    print("The variance (comp. method) is: ", str(variance_computational))
    standard_deviation = math.sqrt(variance_computational)
    print("The standard deviation is: ", str(standard_deviation))
    variance_shortcut = varianceShortcut(data, sum)
    print("The variance (comp. method) is: ", str(variance_shortcut))

def calculateSum(data):
    sum = 0
    for num in data:
        sum += num
    return sum

def calculateMean(data, sum):
    mean = sum / len(data)    
    return mean
    
def varianceComputation(data, mean, sum):
    square_sum = 0
    for num in data:
        square_sum = square_sum + num**2
    numerator = square_sum - sum**2 / len(data)
    
    denominator = len(data) - 1
    
    variance = numerator / denominator
    
    return variance
    
def varianceShortcut(data, sum):
    square_sum = 0
    for num in data:
        square_sum = square_sum + num**2
    
    numerator = ( len(data) * square_sum ) - sum**2
    denominator = len(data) * ( len(data) - 1 )  
    
    variance = numerator / denominator
    
    return variance
    
if __name__ == "__main__":
    main()