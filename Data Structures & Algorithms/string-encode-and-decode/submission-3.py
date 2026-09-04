class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for strsss in strs:
            s+=strsss
            s+="@$^^$#$#^##$%@%&^"
        return s

    def decode(self, s: str) -> List[str]:
        l = list(s.split("@$^^$#$#^##$%@%&^"))
        return l[:-1]