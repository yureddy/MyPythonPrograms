# Pychling is the process whereby a python object strcture.  is converted into a byte 
#stream. Unpickling is a inverse operation whereby a byte stream from a binary file 
# or bytes like object is converted back to a object hierarchy. 
''' Picklin and unpicklin is alternatively known as serialization, marshin, flattening,
non python programs may not reconstruct pickeled objects .
There are currenly 5 different protocols for pickling , the higher the protocol used the 
most recent version of python is need to read the pickle protocols
Protocol version 0 is a original human readable format 
Protocal version 1 is and old binary format 
protocal version 2 is effcity pcilcing with new stlye class PEP 307 for 
Protocol version 3 added in Python 3.0 it has explicit support for bytes objects cant 
					unpickled by Python 2.0
Protocal version 4 added in Python 3.4 it adds support for very large objects , pickling
					more kind of objects and format optimization 9refer PEP 3154) 
To serialise an object hierarchy you call dumps()
siniliiraly to de-serialize a data stream you call loads()
for more control you can call Pickler and Unpickler

Constants provided by Pickle module
pickle. HIGHEST_PROTOCOL - int of highest version of protocol versoin availble, value 
					passed as protocol value to funcitons dump() and sumps() as well 
					Pickler constructor
pickle.DEFAULT_PROTOCOL - the deault protocol version is less than HIGHEST_PROTOCOL.
					Current default protocol is 3 '''

import pickle

myData = {'foo': 'bar'}

handle2 = open("output.txt", 'rb')
Serial_data = pickle.load(handle2)

with open('..\output.txt','wb') as handle:
	pickle.dump(Serial_data, handle, protocol = pickle.HIGHEST_PROTOCOL)


# pICKLE AND Unpickle works only for binary files not any regular text files