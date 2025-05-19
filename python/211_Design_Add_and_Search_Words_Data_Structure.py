class WordDictionary:

    def __init__(self):
        self.root = dict()
        
    def addWord(self, word: str) -> None:
        curr_status = self.root
        for char in word:
            if char not in curr_status:
                curr_status[char] = dict()
            curr_status = curr_status[char]

        curr_status["END"] = ""

    def search(self, word: str) -> bool:
        curr_status = self.root
        for char in word:
            if "END" in curr_status:
                return False
            if char == '.':
                key = curr_status.keys()
                for c in key:
                    curr_status = curr_status[c]
            elif char in curr_status:
                curr_status = curr_status[char]
            else:
                return False

        return "END" in curr_status


obj = WordDictionary()
word = "a"
obj.addWord(word)
param_2 = obj.search(".a")