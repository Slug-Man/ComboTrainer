module problemapi;

import std.string;
import std.random;

struct Problem {
    string flop;
    string range;
    int[string] combohash;
}

Problem getProblem(int pid) {
    switch (pid) {
        case 1: return Problem("2h2d2s", "utg", ["Trips: Board Trips": 92, "Full House: Pocket Pair, Board Trips": 48]);
        case 2: return Problem("2h2d3d", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 3: return Problem("2h2d3s", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 4: return Problem("2h2d4d", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 5: return Problem("2h2d4s", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 6: return Problem("2h2d5d", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 7: return Problem("2h2d5s", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 8: return Problem("2h2d6d", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 9: return Problem("2h2d6s", "utg", ["Pair: Two Overcards with Ace, Pair on Board": 92, "Two Pair: Over Pocket Pair, Board Pair": 48]);
        case 10: return Problem("2h6dJd", "utg", ["Pair: 2nd Pocket Pair": 24, "Pair: Over Pocket Pair": 18, "High Card": 32, "Trips: Set": 3, "Pair: Pair on Board": 21, "High Card: Two Overcards with Ace": 32]);
        case 11: return Problem("2h8hAh", "utg", ["Pair: 2nd Pocket Pair": 30, "Flush: Nut": 3, "High Card": 33, "Pair: 3rd Pocket Pair": 6, "Flush": 4, "Trips: Set": 6, "Pair: Pair on Board": 39]);
        case 12: return Problem("3h4h5h", "utg", ["Flush: Nut": 4, "High Card": 33, "Pair: Over Pocket Pair": 42, "Two Pair: Over Pocket Pair, Board Pair": 6, "Flush": 7, "High Card: Two Overcards with Ace": 48]);
        case 13: return Problem("8hThKh", "utg", ["Pair: 2nd Pocket Pair": 12, "Flush: Nut": 2, "High Card": 33, "Pair: 3rd Pocket Pair": 6, "Pair: Over Pocket Pair": 6, "Flush": 1, "Two Pair: Two Different Pocket Cards": 3, "Trips: Set": 9, "Pair: Under Pocket Pair": 6, "Pair: Pair on Board": 39]);
        case 14: return Problem("ThJhAh", "utg", ["Pair: 2nd Pocket Pair": 12, "Straight": 15, "Straight Flush": 1, "Two Pair: Two Different Pocket Cards": 15, "Trips: Set": 9, "Pair: Under Pocket Pair": 18, "Pair: Pair on Board": 39]);
        default: return Problem();
    }
}
interface IProblemAPI {
	// GET /problem?pid=:id
    @property Problem problem(int pid);
    
    // GET /random
    Problem getRandom();
}

class ProblemAPI : IProblemAPI {
    @property Problem problem(int pid) { return getProblem(pid); }
    Problem getRandom() { return getProblem(uniform(1, 15)); }
}