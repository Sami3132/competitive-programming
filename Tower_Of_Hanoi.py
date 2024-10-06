class Solution:
    def toh(self, n, fromm, to, aux):
        self.count = 0
        
        def solve(n, fromm, to, aux):
            if n == 1:
                print(f"move disk 1 from rod {fromm} to rod {to}")
                self.count += 1
                return
            
            solve(n - 1, fromm, aux, to)
            print(f"move disk {n} from rod {fromm} to rod {to}")
            self.count += 1
            solve(n - 1, aux, to, fromm)
        
        solve(n, fromm, to, aux)
        
        return self.count
