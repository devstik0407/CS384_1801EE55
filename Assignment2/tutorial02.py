# All decimal 3 places

# Function to compute mean
import math
def mean(first_list):
    # mean Logic 
    if len(first_list)==0:
        return 0
    else:
        for x in first_list:
            if(not isinstance(x,(float, int))):
                return 0
        mean_value=summation(first_list)/len(first_list)
        return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    median_value=0
    if(len(first_list)==0):
        return 0
    for x in first_list:
        if(not isinstance(x,(float, int))):
            return 0
    # Sorting function has been defined later
    # We can assume that sorting(sample_list) returns a list containing the elements of sample_list in non-decreasing order
    temp_list=sorting(first_list.copy())
    if(len(first_list)%2==0):
        pos=len(first_list)//2
        median_value=(temp_list[pos]+temp_list[pos-1])/2
    else:
        pos=len(first_list)//2
        median_value=temp_list[pos]
    return median_value

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    # Checking for errors has been done in variance(first_list)
    standard_deviation_value=math.sqrt(variance(first_list))
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    for x in first_list:
        if(not isinstance(x,(float, int))):
            return 0
    if(len(first_list)==0):
        return 0
    mean_value=mean(first_list)
    temp_list=[]
    for x in first_list:
        temp_list.append((x-mean_value)*(x-mean_value))
    variance_value=summation(temp_list)/len(first_list)
    return variance_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    # The function mse has been defined later
    # Checking for errors has been done in mse(first_list,second_list)
    rmse_value=math.sqrt(mse(first_list,second_list))
    return rmse_value

'''
# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    return summation_value
'''