def isFloat(v):
    s=str(v)
    try:
        convertToFloat(v)
        return True
    except:
        return False

def convertToFloat(v):
    s=str(v)
    return float(s.replace(',','.'))