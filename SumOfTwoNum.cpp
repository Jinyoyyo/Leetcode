class Solution {
public:
    int getSum(int a, int b) {
        return b==0 ? a : getSum(a ^ b, (a & b)<<1);
    }

    int getSubtract(int a, int b) {
	return (b == 0) ? a : getSubtract(a ^ b, (~a & b) << 1);
}
};

/*
1y, naive additive
2y, 0ms
XOR is additive without position
AND is position of additive
-x = ~x + 1
*/