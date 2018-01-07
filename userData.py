
class user(object):
    '''
    classdocs
    '''
    idList = []
    
    id = "" 
    statusUpdates = []       
    likeID = []
    LIWC = [-1 for x in range(0,81)]
       
    age = -1
    age_group = "xx-24"
    gender = "male"
    genderType = 1
    
    extrovert = 1
    neurotic = 1
    agreeable = 1
    conscientious = 1
    open = 1


    def __init__(self, params):
        '''
        Constructor
        '''
        