import collections
class Solution:
    def countOfAtoms(self, formula):
        def parse():
            N = len(formula)
            count = collections.Counter()
            while (self.i < N and formula[self.i] != ')'):
                if (formula[self.i] == '('):
                    self.i += 1
                    for name, v in parse().items():
                        count[name] += v
                else:
                    i_start = self.i
                    self.i += 1
                    while (self.i < N and formula[self.i].islower()):
                        self.i += 1
                    name = formula[i_start: self.i]
                    i_start = self.i
                    while (self.i < N and formula[self.i].isdigit()):
                        self.i += 1
                    count[name] += int(formula[i_start: self.i] or 1)
            self.i += 1
            i_start = self.i
            while (self.i < N and formula[self.i].isdigit()):
                self.i += 1
            if (i_start < self.i):
                multiplicity = int(formula[i_start: self.i])
                for name in count:
                    count[name] *= multiplicity

            return count

        self.i = 0
        ans = []
        count = parse()
        for name in sorted(count):
            ans.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)
z=Solution()
print(z.countOfAtoms("H2O"))
print(z.countOfAtoms("Mg(OH)2"))
print(z.countOfAtoms("K4(ON(SO3)2)2"))
print(z.countOfAtoms("C10H16O"))
print(z.countOfAtoms("Zn(NO3)2"))
print(z.countOfAtoms("NaOH"))
print(z.countOfAtoms("F2"))

