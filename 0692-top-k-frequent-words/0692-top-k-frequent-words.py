import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        freq = [(-counts[word], word) for word in counts]
        heapq.heapify(freq)
        topk = []
        while k:
            _, word = heapq.heappop(freq)
            topk.append(word)
            k -= 1
        return topk