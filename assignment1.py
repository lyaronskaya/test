#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import unittest


def factorize_range(n):
    '''
        The function factorizes numbers in the range (1, n) on prime factors.
        
        Input:
        n : Integer, size of the range.
        Output:
        prime_factors_dict: Dictionary with pairs of the form (number, it's prime factors)
    '''
    prime_factors_dict = {}
    
    def factorize(n):
        prime_factors = []
        d = 2
        is_prime = True
        while d * d <= n:
            if n % d == 0:
                prime_factors += prime_factors_dict[d]
                prime_factors += prime_factors_dict[n//d]
                is_prime = False
                break
            d += 1
        if is_prime and n != 1:
            prime_factors.append(n)
        prime_factors_dict[n] = prime_factors
    
    for x in range(1, n + 1):
        factorize(x)
    
    for x, prime_factors in prime_factors_dict.items():
        prime_factors = list(map(str, prime_factors))
        print('{}: {}'.format(x, ' '.join(prime_factors)))
    return prime_factors_dict


class TestFactorizeRange(unittest.TestCase):
    def test_tokenize(self):
        n = 8
        expected_factors_dict = {1:[], 2: [2], 3: [3], 4: [2, 2], 5: [5], 6: [2, 3], 7: [7], 8: [2, 2, 2]}
        self.assertEqual(factorize_range(n), expected_factors_dict)
    
    def test_not_raises_when_zero(self):
        try:
            factorize_range(0)
        except ExceptionType:
            self.fail("The function factorize_range \
                      raised ExceptionType unexpectedly!")


if __name__ == '__main__':
    unittest.main()
