class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if not magazine:
            return False
        r_counts = collections.Counter(ransomNote)
        m_counts = collections.Counter(magazine)
        for letter, counts in r_counts.items():
            if letter not in m_counts or m_counts[letter]<counts:
                return False
        return True