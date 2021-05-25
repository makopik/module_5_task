import sys


#def show_size(x, level=0):
#    print('\t' * level,  f' type= {x.__class__}, size={sys.getsizeof(x)}, object={x}')
#    
#    if hasattr(x, '__inter__'):
#        if hasattr(x, 'items'):
#            for xx in x.items():
#                show_size(xx, level + 1)
#        elif not isinstance(x, str):
#            for xx in x:
#                show_size(xx, level + 1)
#

def show_size(loc, level=0):
    size = 0
     
    for obj in loc.values():
        
        size += sys.getsizeof(obj)
    print('#'*50)
    print('Memory used:',size)   