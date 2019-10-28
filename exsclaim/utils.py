import sys
import json
import yaml
import collections

def labelbox_to_patch(lb,img):
    x1,y1=lb[0]["x"],lb[0]["y"]
    x2,y2=lb[2]["x"],lb[2]["y"]
    return img[y1:y2,x1:x2]

def is_disjoint(l1,l2) -> bool:
    """
    Determines if two lists share any common elements

    :param l1: List 1
    :param l2: List 2

    :return: A bool determining if lists overlap at all
    """
    return len(set(l1).intersection(set(l2))) == 0

def load_json(filename):
    with open(filename, 'r') as fp:
        try:
            return json.load(fp)
        except:
            print("JSON load error")
            return

def load_yaml(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
    
def flatten(items: list) -> list:
    """
    Yield items from any nested iterable; 

    :param items: A nested iterable (list)

    :return: A flattened list
    """
    for x in items:
        if isinstance(x, collections.Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

def exist_common_member(a: list, b: list) -> bool: 
    """Return bool indicating if variable length lists share common member"""
    if len(set(a).intersection(set(b))) > 0: 
        return(True)  
    return(False)


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self,data):
        sys.stdout.write("\r\x1b[K"+data.__str__())
        sys.stdout.flush()
