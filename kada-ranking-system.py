# Maddie Reed
# Aug 23 2026

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def inc_progress(self, to_rank):

        if to_rank == 0 or to_rank < -8 or to_rank > 8: # Rank out of bounds
                raise Exception((f"To Rank {to_rank} Not Allowed"))
        else:
            if to_rank > 0 and self.rank > 0:
                d = to_rank - self.rank

            elif to_rank < 0 and self.rank < 0:
                d = abs(self.rank) - abs(to_rank)

            elif self.rank < 0 and to_rank > 0:
                d = to_rank - self.rank - 1

            elif to_rank < 0 and self.rank > 0:
                d = to_rank - self.rank + 1

            else: # rank > 0, to_rank < 0
                d = to_rank - self.rank - 1

            # Calculate points
            if d == -1:
                points = 1 + self.progress
            elif d <= -2:
                points = 0 + self.progress
            elif d == 0:
                points = 3 + self.progress
            else:
                points = 10 * d * d + self.progress

            # Rank up
            while points >= 100:
                self.rank += 1
                points = points - 100
                if self.rank == 0:
                    self.rank += 1

            # no more ranking needed
            if self.rank >= 8: 
                points = 0
                self.progress = 0
                self.rank=8
                
            self.progress = points
            return self

user = User()

# Tests these challenges: -8, 2, -8, -2, -5, -4, -7, -1, 8, 5, 7, -2

def test_it(params):
    user = User()
    for param in params:          
        user.inc_progress(param)
        
        print("----------------")
        print(f"For ({param}):")
        print(f"rank: {user.rank}")
        print(f"progress: {user.progress}")
        
test_it((-8, 2, -8, -2, -5, -4, -7, -1, 8, 5, 7, -2))
