from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            atIdx = email.find("@")
            locName = email[:atIdx]
            domName = email[atIdx + 1:]
            plus = locName.find("+")
            if plus != -1:
                locName = locName[:plus]
            locName = locName.replace(".", "")

            unique.add("%s@%s" % (locName, domName))
        return len(unique)
