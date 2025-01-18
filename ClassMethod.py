class Person:
    species = "Homo Sapiens"# this is a class attribute

    @classmethod
    def get_species(cls):#class methods use cls 
        
        print(cls)
        return cls.species
   


print(Person.get_species())