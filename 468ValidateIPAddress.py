class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validIPv4(IP)
        if IP.count(':') == 7:
            return self.validIPv6(IP)
        else:
            return 'Neither'

    def validIPv4(self, IP):
        nums = IP.split('.')
        for n in nums:
            if len(n) == 0 or len(n) >= 4:  # no. of digits
                return 'Neither'
            if not n.isdigit() or int(n) > 255:
                return 'Neither'
            if n[0] == '0' and len(n) != 1:
                return 'Neither'
        return 'IPv4'

    def validIPv6(self, IP):
        h = '0123456789abcdefABCDEF'
        string = IP.split(':')
        for s in string:
            if not len(s) or len(s) > 4:
                return 'Neither'
            if not all(i in h for i in s):
                return 'Neither'
        return 'IPv6'
