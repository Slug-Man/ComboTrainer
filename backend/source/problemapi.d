module problemapi;

import std.string;
import std.conv;
import std.random;
import dpq2;

import std.process;
import vibe.vibe;


struct Problem {
    string flop;
    string range_label;
    string range_desc;
    int range_id;
    int[string] combohash;
}

Problem getProblem(int rangeid, string flop) {
	auto conn = new Connection("");
    
    QueryParams p;
    p.sqlCommand = "select * from combohashes where rangeid=$1::integer and flop=$2::text";
    p.argsFromArray = [to!string(rangeid), flop];
    auto result = conn.execParams(p);
        
    QueryParams p2;
    p2.sqlCommand = "select * from ranges where id=$1::integer";
    p2.argsFromArray = [to!string(rangeid)];
    auto ranges_res = conn.execParams(p2);
    
    if (result.length > 0) { // && ranges_res.length > 0?
        auto r = result[0];
        int[string] combohash;
        for (auto column = 2; column < result.columnCount; column++) {
            combohash[result.columnName(column)] = to!int(r[column].as!PGinteger);
        }

        return Problem(r["flop"].as!string, ranges_res[0]["range_label"].as!PGtext,
                                            ranges_res[0]["range_desc"].as!PGtext,
                                            to!int(ranges_res[0]["id"].as!PGinteger),
                                            combohash);
    }
    else {
        return Problem();
    }
}

interface IProblemAPI {
	// GET /problem?pid=:id
    //@property Problem problem(int pid);
    
    // GET /problem?rangeid=:rangeid&flop=:flop
    @property Problem problem(int rangeid, string flop);
    
    // GET /random
    //Problem getRandom();
}

class ProblemAPI : IProblemAPI {
    //@property Problem problem(int pid) { return getProblem(pid); }
    @property Problem problem(int rangeid, string flop) { return getProblem(rangeid, flop); }
    //Problem getRandom() { return getProblem(uniform(1, 15)); }
}