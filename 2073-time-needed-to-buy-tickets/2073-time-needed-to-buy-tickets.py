class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        position = k
        total_time = 0
        while tickets:
            front_tickets = tickets.pop(0)
            total_time += 1
            front_tickets -= 1
            if front_tickets > 0:
                tickets += [front_tickets]
            
            if position == 0:
                if front_tickets == 0:
                    return total_time
                else:
                    position = len(tickets) - 1
                    if position == 0:
                        return total_time + tickets[0]
            else:
                position -= 1
