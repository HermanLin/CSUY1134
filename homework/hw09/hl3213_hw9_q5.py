from ChainingHashTableMap import ChainingHashTableMap

class InvertedFile:
    def __init__(self, fname):
        file = open(fname, "r")
        txt = file.read()
        wrds = txt.split()
        self.invert = ChainingHashTableMap()
        for i in range(len(wrds)):
            wrd = wrds[i].strip(",")
            wrd = wrd.lower()
            try:
                inverse = self.invert[wrd]
                inverse.append(i)
            except:
                self.invert[wrd] = [i]

    def indices(self, wrd):
        print(self.invert[wrd])
        try:
            return self.invert[wrd]
        except:
            return []
