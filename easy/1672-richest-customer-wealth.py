class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0

        # Loop through each account in the list getting the sum and comparing to current max
        for account in accounts: 
            sum1 = sum(account)
            if sum1 > wealth: 
                wealth = sum1

        return wealth
