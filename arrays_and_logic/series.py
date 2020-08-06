import re

def slices(series, length):
    if re.search('\D', series):
        raise ValueError('Series must be made up of digits only.')
    len_s = len(series)
    if (length < 1) | (len_s < length):
        raise ValueError('Slice and series lengths must be greater than 0.')
    return [series[i:i+length] for i in range(len_s+1-length)]
