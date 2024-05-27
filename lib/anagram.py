# your code goes here!
class Anagram:
    def __init__(self,anagram):
        self.anagram = anagram
    def test_instantiates_with_word(self):
        return(self.anagram)
    def match(self,list):
        for each_word in list:
            our_second_sort = sorted(each_word)
            if our_second_sort == sorted(self.anagram):
                print(our_second_sort)
                return
            else:
                print("Okay")
                
    pass        
    
neno = Anagram('google')
neno.match(['enlists', 'google', 'inlets', 'banana'])