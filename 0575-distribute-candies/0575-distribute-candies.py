class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set_candyType=set(candyType)
        diffrnt_type=len(set_candyType)
        can_eat=min((len(candyType)//2),diffrnt_type)
        return can_eat
