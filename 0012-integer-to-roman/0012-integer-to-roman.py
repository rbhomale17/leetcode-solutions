class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
        { "value": 1000, "symbol": 'M' },
        { "value": 900, "symbol": 'CM' },
        { "value": 500, "symbol": 'D' },
        { "value": 400, "symbol": 'CD' },
        { "value": 100, "symbol": 'C' },
        { "value": 90, "symbol": 'XC' },
        { "value": 50, "symbol": 'L' },
        { "value": 40, "symbol": 'XL' },
        { "value": 10, "symbol": 'X' },
        { "value": 9, "symbol": 'IX' },
        { "value": 5, "symbol": 'V' },
        { "value": 4, "symbol": 'IV' },
        { "value": 1, "symbol": 'I' }
    ]
        res = []
        for sym in roman:
            print(sym, sym.get('value'), sym.get('symbol'))
            while num >= sym.get('value'):
                res.append(sym.get('symbol'))
                num -= sym.get('value')
        print(res)
        return "".join(res)
        

