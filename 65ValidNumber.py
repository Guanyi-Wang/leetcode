class Solution:
    def isNumber(self, s: str) -> bool:
        voc = {'0','1','2','3','4', '5','6','7','8','9','0','-','+','e','.'}
        # remove white space in start and tail
        str = s.strip()
        # null
        if not str:
            return False
        # set flag
        sign_flag = 0
        e_flag = 0
        dot_flag = 0
        num_flag = 0
        for i in range(len(str)):
            if str[i] not in voc:
                return False
            if str[i].isdigit():
                num_flag = 1
            # sign appears
            if str[i] in ['-','+']:
                # more than one sign on the same side of 'e'
                if sign_flag !=0 and e_flag ==0:
                    return False
                if sign_flag !=0 and e_flag< sign_flag:
                    return False
                # sign appears in the middle and not  behind 'e'
                if i != 0 and str[i-1] != 'e':
                    return False
                # '-e' or '+e'appears
                if i != len(str)-1 and str[i+1] =='e':
                    return False
                # sign appears in the end
                if i ==len(str)-1:
                    return False
                sign_flag = i
            # e appears:
            if str[i] == 'e':
                # no number before e
                if num_flag == 0:
                    return False
                if e_flag !=0:
                    return False
                # e appears at start or tail
                if i==0 or i==len(str)-1:
                    return False
                e_flag =i
            # dot appears:
            if str[i] == '.':
                # string is '.'
                if len(str) ==1:
                    return False
                if dot_flag ==1:
                    return False
                # appears after e:
                if e_flag !=0:
                    return False
                dot_flag  = 1
        # no digit
        if not num_flag:
            return False
        return True