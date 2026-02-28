
class rovar:

    def __init__(self) -> None:
        self._LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz" #missed g
        self._UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ" #missed D
 
    def enrove(self, normal: str)-> str: 
        '''
        Encode the string in rovarspraket.
        Args:
            normal (str): Normal string
        Returns:
            (str) Encoded String
        '''
        #if normal is None:
             #return None 
        #This is returning none instead of raising an exception
        if normal is None: #or not isinstance(normal, str):
           raise TypeError("Input must be a non-empty string")
        
        encoded = []
        for char in normal:
            if char in self._LOWER_CONSTANTS:
                encoded.append(char + 'o' + char)
            elif char in self._UPPER_CONSTANTS:
                encoded.append(char + 'O' + char) #used lowercase o instead of uppercase O
            else:
                encoded.append(char)
        return ''.join(encoded)
 
    def derove(self, rov:str)->str:
        """ 
            Decode a string from rovarspraket.
            Args:
                normal (str): Encoded string
            Returns:
                (str) Normal string
        """
        if rov is None:
            #return None: returning none instead of raising error
            raise TypeError("Input must be a non-empty string")
       
        for c in self._LOWER_CONSTANTS:
            find = c+'o'+c
            rov = rov.replace(find, c)
       
        for c in self._UPPER_CONSTANTS:
            find = c+'O'+c
            rov = rov.replace(find, c)
 
        return rov
