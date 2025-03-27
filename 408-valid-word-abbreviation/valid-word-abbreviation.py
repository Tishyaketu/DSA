class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = 0
        abbr_index = 0
        word_length = len(word)
        abbr_length = len(abbr)
        while word_index < word_length and abbr_index<abbr_length:
            if word[word_index] == abbr[abbr_index]:
                word_index += 1
                abbr_index += 1
                continue
            if not abbr[abbr_index].isdigit():
                return False
            num_start_index = abbr_index
            while abbr_index < abbr_length and abbr[abbr_index].isdigit():
                abbr_index += 1
            num_str = abbr[num_start_index:abbr_index]
            if num_str[0] == '0':
                return False
            word_index += int(num_str)
        return word_index == word_length and abbr_index == abbr_length
