
in1=123
in2=-123
in3=120
in4=1534236469

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31 :
            return 0;

        if x < 0 :
            return -self.reverse(-x);
        else :
            rev = 0;
            while x>0 :
                rev = rev * 10;
                rev = x%10 + rev;
                x   = x/10;
            if rev >= 2**31 :
                return 0;
            return rev;

a=Solution();

print a.reverse(in1);
print a.reverse(in2);
print a.reverse(in3);
print a.reverse(in4);

