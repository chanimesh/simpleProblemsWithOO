class ReverseSentence:

    def __splitSentence(self,sentence):
        return sentence.split()

    def __reverse_list(self, stringList):
        stringList.reverse()
        return stringList

    def __join_list(self,stringList):
        return " ".join(stringList)

    def reverseSentence(self,sentence_string):
        sentence_list = self.__splitSentence(sentence_string)
        sentence_list = self.__reverse_list(sentence_list)
        return self.__join_list(sentence_list)
