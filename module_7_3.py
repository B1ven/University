class WordsFinder:
    file_name = []

    def __init__(self, *args):
        self.args = args
        for q in args:
            self.file_name.append(q)

    def get_all_words(self):
        all_words = {}
        bad_value = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for c in WordsFinder.file_name:
            with open(c, 'r+', encoding='utf-8') as file:
                temp = file.read().lower().split()
                for q in range(len(temp)):
                    for v in temp[q]:
                        if v in bad_value:
                            temp[q] = temp[q].replace(v, '')
                all_words[c] = temp
        return all_words

    def find(self, word):
        result = self.get_all_words()
        answer = {}
        for c in result:
            for q in result[c]:
                if q == word.lower():
                    answer[c] = result[c].index(q) + 1
        return answer

    def count(self, word):
        result = self.get_all_words()
        answer = {}
        for c in result:
            count = 0
            for q in result[c]:
                if q == word.lower():
                    count += 1
            answer[c] = count
        return answer
