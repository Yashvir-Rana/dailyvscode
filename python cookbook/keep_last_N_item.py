"""you want to keep a limited history of the last few items seen 
during iteration or during some other kind of processing"""

from collections import deque 

def search(lines, pattern, history=5):
    pr_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, pr_lines
        pr_lines.append(line)
