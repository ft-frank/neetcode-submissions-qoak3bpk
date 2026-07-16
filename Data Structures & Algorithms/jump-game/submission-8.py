class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1

        current = 0

        while current < last_index:
            longest_jump_avaliable = nums[current]
            if current + longest_jump_avaliable >= last_index:
                return True
            best_jump_avaliable = 0
            best_jump_index_offset = 0
            for j in range(1, longest_jump_avaliable + 1):
                jump_value = nums[current + j] + j if nums[current + j] > 0 else 0 #how far it can reach. 3, 0, 8. Starting at 3, going to 8 can reach 10
                if jump_value > best_jump_avaliable:
                    best_jump_avaliable = jump_value
                    best_jump_index_offset = j
            if best_jump_index_offset == 0:
                return False
            else:
                current = current + best_jump_index_offset

                
        return True

                