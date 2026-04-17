import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        while nums:
            val = nums.pop()
            if val not in freq:
                freq[val] = 0
            freq[val] += 1
        heap_queue = []
        for item in freq.items():
            heapq.heappush(heap_queue, (-item[1], item))
        result = []
        for _ in range(k):
            _, r = heapq.heappop(heap_queue)
            result.append(r[0])
        return result