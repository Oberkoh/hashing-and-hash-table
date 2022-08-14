"""
You've built an inflight entertainment system
with on-demand movie streaming.

So you're building a feature for choosing two movies 
whose total runtimes will equal the exact flight length.
"""

# one possibility, using 2 loops
# brute force with time complexity of O(n*n) and O(1) space complexity
def inflight_entertainment(flight_length, movie_lengths):
    for first in range(len(movie_lengths)):
        for second in range(len(movie_lengths)):
            if first == second:
                continue
            if movie_lengths[first] + movie_lengths[second] == flight_length:
                return True
    return False   

# print(inflight_entertainment(10, [1, 2, 4, 7]))