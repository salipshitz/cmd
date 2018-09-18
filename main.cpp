using namespace std;

enum nestingLevel {
	IF_COND, ELSE_IF_COND, ELSE_COND,
	FOR_LOOP, WHILE_LOOP,
	FUNC, CLASS
};

class mth {
	
}

map<string, mth> methods = {};
map<string, cls> classes = {};
