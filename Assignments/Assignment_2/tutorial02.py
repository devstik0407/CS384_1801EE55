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
    # Checking for errors has been done in mse(first_list,second_list)
    rmse_value=math.sqrt(mse(first_list,second_list))
    return rmse_value

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    for x in second_list:
        if(not isinstance(x,(float,int))):
            return 0
    if(len(first_list)!=len(second_list) or len(first_list)==0):
        return 0
    temp_list=[]
    for i in range(0,len(first_list)):
        temp_list.append((first_list[i]-second_list[i])*(first_list[i]-second_list[i]))
    mse_value=summation(temp_list)/len(first_list)
    return mse_value

# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    for x in second_list:
        if(not isinstance(x,(float,int))):
            return 0
    if((len(first_list)!=len(second_list)) or len(first_list)==0):
        return 0
    temp_list=[]
    for i in range(0,len(first_list)):
        temp_list.append(abs(first_list[i]-second_list[i]))
    mae_value=summation(temp_list)/len(first_list)
    return mae_value

# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    # To avoid precision errors I have calculated variance and mse without using variance(first_list) and mse(first_list,second_list)
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
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    for x in second_list:
        if(not isinstance(x,(float,int))):
            return 0
    if(len(first_list)!=len(second_list) or len(first_list)==0):
        return 0
    temp_list=[]
    for i in range(0,len(first_list)):
        temp_list.append((first_list[i]-second_list[i])*(first_list[i]-second_list[i]))
    mse_value=summation(temp_list)/len(first_list)
    if(variance_value==0):
        return 0
    nse_value=1-mse_value/variance_value
    return nse_value

# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # pcc Logic
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    for x in second_list:
        if(not isinstance(x,(float,int))):
            return 0
    if(len(first_list) != len(second_list) or len(first_list)==0):
        return 0
    actual_mean=mean(first_list)
    predicted_mean=mean(second_list)
    temp_list=[]
    for i in range(0,len(first_list)):
        temp_list.append((first_list[i]-actual_mean)*(second_list[i]-predicted_mean))
    pcc_value=summation(temp_list)/len(first_list)
    if(standard_deviation(first_list)==0 or standard_deviation(second_list)==0):
        return 0
    pcc_value=pcc_value/(standard_deviation(first_list)*standard_deviation(second_list))
    return pcc_value

# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    if(len(first_list)==0):
        return 0
    mean_value=mean(first_list)
    sd=standard_deviation(first_list)
    if(sd==0):
        return 0
    temp_list=[]
    for i in range(0,len(first_list)):
        temp_list.append(((first_list[i]-mean_value)*(first_list[i]-mean_value)*(first_list[i]-mean_value))/(sd*sd*sd))
    skewness_value=summation(temp_list)/len(first_list)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    # Here is the implementation of merge sort algorithm
    for x in first_list:
        if(not isinstance(x,(float, int))):
            return 0
    if len(first_list)<=1:
        return first_list
    half1=[]
    half2=[]
    for i in range(0,len(first_list)//2):
        half1.append(first_list[i])
    for i in range(len(first_list)//2,len(first_list)):
        half2.append(first_list[i])
    half1=sorting(half1)
    half2=sorting(half2)
    h1=0
    h2=0
    sorted_list=[]
    while(h1<len(half1) or h2<len(half2)):
        if(h1<len(half1) and h2<(len(half2))):
            if(half1[h1]<half2[h2]):
                sorted_list.append(half1[h1])
                h1+=1
            else:
                sorted_list.append(half2[h2])
                h2+=1
        elif(h1<len(half1)):
            sorted_list.append(half1[h1])
            h1+=1
        else:
            sorted_list.append(half2[h2])
            h2+=1
    return sorted_list

def kurtosis(first_list):
    # Kurtosis Logic
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    if(len(first_list)==0):
        return 0
    mean_value=mean(first_list)
    sd=standard_deviation(first_list)
    if(sd==0):
        return 0
    temp_list=[]
    for x in first_list:
        temp_list.append(((x-mean_value)*(x-mean_value)*(x-mean_value)*(x-mean_value))/(sd*sd*sd*sd))
    kurtosis_value=summation(temp_list)/len(first_list)
    return kurtosis_value

# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    for x in first_list:
        if(not isinstance(x,(float,int))):
            return 0
    if(len(first_list)==0):
        return 0
    summation_value=0
    for x in first_list:
        summation_value+=x
    return summation_value