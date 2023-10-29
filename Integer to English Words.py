class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def convert_to_words(num):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + convert_to_words(num % 10)
            else:
                return below_20[num // 100] + " Hundred " + convert_to_words(num % 100)

        result = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                result = convert_to_words(num % 1000) + thousands[i] + " " + result
            num //= 1000

        return result.strip()
