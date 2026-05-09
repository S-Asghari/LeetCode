class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        task_exclusive_time = [0 for i in range(0, n)]
        stack = []
        last_task = -1
        last_timestamp = -1
        
        for log in logs:
            id = int(log.split(':')[0])
            mode = log.split(':')[1]
            timestamp = int(log.split(':')[2])
            
            if mode == 'start':
                if last_task >= 0:
                    task_exclusive_time[last_task] += timestamp - last_timestamp
                    stack.append(last_task)
                last_task = id
                last_timestamp = timestamp
            
            else: # mode = 'end'
                task_exclusive_time[last_task] += timestamp - last_timestamp + 1
                last_timestamp = timestamp + 1
                if stack:
                    last_task = stack.pop()

        return task_exclusive_time
