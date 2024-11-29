import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list)
    b = a.reshape(3,3)
    
    mean_vals = [np.mean(b,axis=0).tolist(), np.mean(b,axis=1).tolist(), np.mean(b)]
    variance_vals = [np.var(b,axis=0).tolist(), np.var(b,axis=1).tolist(), np.var(b)]
    stddev_vals = [np.std(b,axis=0).tolist(), np.std(b,axis=1).tolist(), np.std(b)]
    max_vals = [np.max(b,axis=0).tolist(), np.max(b,axis=1).tolist(), np.max(b)]
    min_vals = [np.min(b,axis=0).tolist(), np.min(b,axis=1).tolist(), np.min(b)]
    sum_vals = [np.sum(b,axis=0).tolist(), np.sum(b,axis=1).tolist(), np.sum(b)]

    calculations = dict([('mean', mean_vals), 
                            ('variance', variance_vals),
                            ('standard deviation', stddev_vals),
                            ('max', max_vals),
                            ('min', min_vals),
                            ('sum', sum_vals)])
    
    return calculations