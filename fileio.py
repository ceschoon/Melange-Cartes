import numpy,pandas

def storevec(vec, filename):
    
    M = len(vec)
    
    data = list(zip(vec))
    df = pandas.DataFrame(data = data,columns = ["vec"])
    df.to_csv(filename,index=False,header=True)
    
    
def readvec(filename):
    
    data = pandas.read_csv(filename)
    [vec] = numpy.transpose(data.as_matrix(["vec"]))
    
    return vec


def mat2vec(mat):
    
    N = len(mat[0,:])
    M = len(mat[:,0])
    
    vec = numpy.zeros(N*M)
    for i in range(N):
        vec[i*M:i*M+M] = mat[i,:]
        
    return vec


def vec2mat(vec,M):
    
    N = int(len(vec)/M)
    
    mat = numpy.zeros((N,M))
    for i in range(N):
        mat[i,:] = vec[i*M:i*M+M]
        
    return mat

def storemat(mat, filename):
    
    M = len(mat[0,:])
    vec = mat2vec(mat)
    
    data = list(zip(vec))
    df = pandas.DataFrame(data = data,columns = ["vec"])
    df.to_csv(filename,index=False,header=True)
    
    
def readmat(filename,M):
    
    data = pandas.read_csv(filename)
    [vec] = numpy.transpose(data.as_matrix(["vec"]))
    
    mat = vec2mat(vec,M)
    return mat