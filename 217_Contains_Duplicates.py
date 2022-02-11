class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using hashset
        tabela = set()
        
        for i in nums:
            if i in tabela:
                return True
            else:
                tabela.add(i)
        return False
