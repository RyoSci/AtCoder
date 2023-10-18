
# https://xn--t8j715h0qi.jp/programming/38/

class Osa_k_Method:
    '''
    osa_k法で高速に素因数分解する(O(log(nmax)))
    https://osak.jp/diary/diary_201310.html#20131017
    '''
    def __init__(self, nmax):
        '''
        nmax: 素因数分解する可能性のある数の最大値
        '''
        self.min_factor = [i for i in range(nmax+1)]
        self.primes = [True for _ in range(nmax+1)]
        self.primes[0] = False
        self.primes[1] = False
        num = 2
        j = num*2
        while j <= nmax:
            self.primes[j] = False
            self.min_factor[j] = num
            j += num
        num = 3
        while num*num <= nmax:
            if self.primes[num]:
                j = num*num
                while j <= nmax:
                    self.primes[j] = False
                    self.min_factor[j] = num
                    j += num
            num += 2
        return

    def factorization(self, n):
        '''nを素因数分解する
        戻り値: factList = [[prime1, exp1], [prime2, exp2],...] 
                n=(prime1)**exp1 * (prime2)**exp2 * ...
        '''

        factDict=dict()
        while n > 1:
            fact = self.min_factor[n]
            if fact not in factDict:
                factDict[fact] = 1
            else:
                factDict[fact] += 1
            n //= fact

        factList = [(fact, order) for fact, order in factDict.items()]
        return factList