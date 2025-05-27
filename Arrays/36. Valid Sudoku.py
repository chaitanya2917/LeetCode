#python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r // 3) * 3 + c // 3]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + c // 3].add(val)
        return True


#C++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9), cols(9), boxes(9);
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char val = board[r][c];
                if (val == '.') continue;
                int boxIndex = (r / 3) * 3 + c / 3;
                if (rows[r].count(val) || cols[c].count(val) || boxes[boxIndex].count(val))
                    return false;
                rows[r].insert(val);
                cols[c].insert(val);
                boxes[boxIndex].insert(val);
            }
        }
        return true;
    }
};



#Java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] boxes = new HashSet[9];
        
        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.') continue;
                int boxIndex = (r / 3) * 3 + c / 3;
                if (rows[r].contains(val) || cols[c].contains(val) || boxes[boxIndex].contains(val))
                    return false;
                rows[r].add(val);
                cols[c].add(val);
                boxes[boxIndex].add(val);
            }
        }
        return true;
    }
}


Optimal Approach
Use sets to track seen numbers for rows, columns, and boxes.

Time Complexity: O(1) (since the board size is always 9x9).

Space Complexity: O(1) for the same reason.