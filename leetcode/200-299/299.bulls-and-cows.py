class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sd = {}
        gd = {}
        bulls = cows = 0
        for sChar, gChar in zip(secret, guess):
            if sChar == gChar:
                bulls += 1
            else:
                sd.setdefault(sChar, 0)
                gd.setdefault(gChar, 0)
                sd[sChar] += 1
                gd[gChar] += 1
        for key, val in gd.items():
            if key in sd:
                cows += min(sd[key], val)
        return "%dA%dB" % (bulls, cows)
