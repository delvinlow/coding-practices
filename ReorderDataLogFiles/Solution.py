class Solution:
    def reorderLogFiles(self, logs):
        digit_logs = []
        letter_logs = []
        for log in logs:
            first_word = log.split(" ")[1]
            if first_word.isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        return sorted(letter_logs, key=self.get_log_entry_and_identifier) + digit_logs 

    def get_log_entry_and_identifier(self, log):
        words = log.split(" ")
        return (" ".join(words[1:]), words[0])