## PYTHON VS. RUST VS. GO (GOLANG) VS. JAVASCRIPT EQUIVALENTS
## WORK-IN-PROGRESS
## CHECK BACK SOON FOR UPDATES; PLEASE COME BACK AGAIN SOON
## www.JerusalemProgramming.com

## DECLARE VARIABLES

## PYTHON
AnyVariableName = "Whatever String, Number, or other Object"

## JAVASCRIPT
var AnyVariableName = "Whatever String, Number, or other Object";
let AnyVariableName = "Whatever String, Number, or other Object";
const AnyVariableName = "ES6 - Whatever String, Number, or other Object in ES6";

## GO (GOLANG) - INTEGERS - VERSION 1 - THE LONG WAY
var AnyVariableName int
AnyVariableName = 700

## GO (GOLANG) - INTEGERS - VERSION 2 - ASSIGN VALUE ON SAME LINE
var AnyVariableName int = 700

## GO (GOLANG) - INTEGERS - VERSION 3 - SHORTCUT INFERS TYPE
AnyVariableName := 700

## GO (GOLANG) - FLOAT64 - VERSION 1 - THE LONG WAY
var AnyVariableName float64
AnyVariableName = 700.00

## GO (GOLANG) - FLOAT64 - VERSION 2 - ASSIGN VALUE ON SAME LINE
var AnyVariableName float64 = 700.00

## GO (GOLANG) - FLOAT64 - VERSION 3 - SHORTCUT INFERS TYPE
AnyVariableName := 700.00

## GO (GOLANG) - STRING - VERSION 1 - THE LONG WAY
var AnyVariableName string
AnyVariableName = "700"

## GO (GOLANG) - STRING - VERSION 2 - ASSIGN VALUE ON SAME LINE
var AnyVariableName string = "700"

## GO (GOLANG) - STRING - VERSION 3 - SHORTCUT INFERS TYPE
AnyVariableName := "700"

## RUST

## RUST

## RUST

## RUST

## RUST

## RUST
// Basic printing with newline (equivalent to Python's print())
println!("Hello, world!");

// Print with formatting (similar to Python's f-strings or .format())
let name = "Rust";
println!("Hello, {}!", name);

// Print without adding a newline at the end
print!("This doesn't add a newline");

// Print to standard error instead of standard output
eprintln!("This is an error message");

// Create an empty vector
let mut empty_vec: Vec<i32> = Vec::new();

// Create a vector with initial values
let mut numbers = vec![1, 2, 3, 4, 5];

// Adding elements
numbers.push(6);
numbers.push(7);

// Insert at specific position
numbers.insert(0, 0);  // Insert 0 at index 0

// Access elements
let third = numbers[2];  // Zero-indexed like Python
let maybe_value = numbers.get(10);  // Safe access that returns Option<&T>

// Remove elements
let last = numbers.pop();  // Removes and returns the last element
numbers.remove(0);  // Remove element at index 0

// Iterate over elements
for num in &numbers {
    println!("{}", num);
}

// Vector length
let length = numbers.len();

// Check if empty
if numbers.is_empty() {
    println!("Vector is empty");
}

// Clear all elements
// numbers.clear();

// Key differences from Python lists:

// Rust vectors are homogeneous (all elements must be the same type)
// You need to specify the type (Vec<T> where T is the element type)
// To modify a vector, it must be declared as mutable with mut
// Rust has both unchecked access (vec[i]) which will panic if out of bounds, and safe access (vec.get(i)) which returns an Option
// The vector operations tend to be more explicit than Python's list operations

// Vectors in Rust provide similar functionality to Python lists but with Rust's added safety guarantees around memory management and type safety.


In Rust, the equivalent of Python dictionaries are HashMap and BTreeMap from the standard library. HashMap is more similar to Python dictionaries in terms of performance characteristics (average O(1) lookups), while BTreeMap keeps keys sorted.
Here's how to create and use a HashMap in Rust:


use std::collections::HashMap;

fn main() {
    // Create an empty HashMap (key type: String, value type: i32)
    let mut scores: HashMap<String, i32> = HashMap::new();
    
    // Insert key-value pairs
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Red"), 50);
    
    // Create from tuples with collect
    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 25];
    let mut scores: HashMap<_, _> = teams.into_iter().zip(initial_scores.into_iter()).collect();
    
    // Access values
    let blue_score = scores.get("Blue");  // Returns Option<&i32>
    
    // Access with default value if key doesn't exist
    let green_score = scores.get("Green").copied().unwrap_or(0);
    
    // Check if key exists
    if scores.contains_key("Yellow") {
        println!("Yellow team exists!");
    }
    
    // Update a value
    scores.insert(String::from("Blue"), 25);  // Overwrites existing value
    
    // Update only if key doesn't exist
    scores.entry(String::from("Green")).or_insert(50);
    
    // Update based on old value
    let text = "hello world wonderful world";
    let mut word_count = HashMap::new();
    
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);
        *count += 1;
    }
    
    // Iterate over key-value pairs
    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
    
    // Remove a key-value pair
    scores.remove("Blue");
    
    // Get the number of elements
    let size = scores.len();
    
    // Check if empty
    if scores.is_empty() {
        println!("HashMap is empty");
    }
}

Key differences from Python dictionaries:

You need to import HashMap with use std::collections::HashMap
You must specify both key and value types when creating a HashMap
String keys are typically String type rather than string literals (&str)
get() returns an Option<&V> rather than the value directly
Iteration patterns and mutability rules follow Rust's ownership system
The .entry() API provides more explicit control over insertion logic

If you need ordered keys (like Python's OrderedDict), use BTreeMap instead, which has a similar API but maintains keys in sorted order.

The main advantages of BTreeMap over HashMap:

Keys are always sorted (lexicographically for strings)
Supports ordered operations like first_key_value(), last_key_value(), and range()
Provides consistent iteration order
Offers logarithmic time complexity (O(log n)) for operations, which is slower than HashMap's average O(1) but has more predictable worst-case performance

Use BTreeMap when you need ordered keys or when you want to perform range queries on your map. Use HashMap when you prioritize raw lookup and insertion speed and don't care about key ordering.

use std::collections::BTreeMap;

fn main() {
    // Create an empty BTreeMap (key type: String, value type: i32)
    let mut scores: BTreeMap<String, i32> = BTreeMap::new();
    
    // Insert key-value pairs (will be stored in sorted key order)
    scores.insert(String::from("Zebra"), 10);
    scores.insert(String::from("Apple"), 50);
    scores.insert(String::from("Banana"), 25);
    
    // Create from tuples with collect
    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 25];
    let mut ordered_scores: BTreeMap<_, _> = teams.into_iter().zip(initial_scores.into_iter()).collect();
    
    // Access values
    let apple_score = scores.get("Apple");  // Returns Option<&i32>
    
    // Access with default value if key doesn't exist
    let missing_score = scores.get("Missing").copied().unwrap_or(0);
    
    // Check if key exists
    if scores.contains_key("Banana") {
        println!("Banana team exists!");
    }
    
    // Update a value
    scores.insert(String::from("Apple"), 55);  // Overwrites existing value
    
    // Update only if key doesn't exist
    scores.entry(String::from("Cherry")).or_insert(30);
    
    // Update based on old value
    let text = "hello world wonderful world";
    let mut word_count = BTreeMap::new();
    
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);
        *count += 1;
    }
    
    // Iterate over key-value pairs (will be in sorted key order)
    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
    
    // Get first and last entries (not available in HashMap)
    if let Some((first_key, first_value)) = scores.first_key_value() {
        println!("First entry: {}: {}", first_key, first_value);
    }
    
    if let Some((last_key, last_value)) = scores.last_key_value() {
        println!("Last entry: {}: {}", last_key, last_value);
    }
    
    // Range operations (not available in HashMap)
    for (key, value) in scores.range("Apple".."Zebra") {
        println!("Range value: {}: {}", key, value);
    }
    
    // Remove a key-value pair
    scores.remove("Banana");
    
    // Get the number of elements
    let size = scores.len();
    
    // Check if empty
    if scores.is_empty() {
        println!("BTreeMap is empty");
    }
}








































## PRINT TO CONSOLE

## PYTHON
print(AnyVariableName)

## RUST

## JAVASCRIPT
console.log(AnyVariableName);

## GO (GOLANG)
fmt.Println(AnyVariableName)

## CHECK TYPE OF OBJECT

## PYTHON
type(AnyVariableName)

## JAVASCRIPT
typeof(AnyVariableName);

## GO (GOLANG)
reflect.TypeOf(AnyVariableName)

## RETURN LENGTH OF OBJECT

## PYTHON
len(AnyVariableName)

## JAVASCRIPT
AnyVariableName.length;

## GO (GOLANG)
len(AnyVariableName)

## IF / ELSE CONDITIONALS

## PYTHON
if WhateverCondition:
    print("If WhateverCondition is True, then do whatever conditional operation")
else:
    print("...else:  then do something else")

## RUST

## JAVASCRIPT
if (WhateverCondition) {
     console.log("If WhateverCondition is true");
} else {
     console.log("else AlternateCondition goes here");
}

## GO (GOLANG) // PARENTHESES AROUND CONDITION OPTIONAL
if WhateverCondition {
     fmt.Println("If WhateverCondition is true")
} else {
     fmt.Println("else AlternateCondition goes here")
}

## IF / ELSE IF / ELSE CONDITIONALS

## PYTHON
if WhateverCondition:
    return()
elif ElseIfCondition:
    return()
else:
    return()

## JAVASCRIPT
if (WhateverCondition) {
  return();
} else if (ElseIfCondition) {
  return();
} else {
  return();
}

## GO (GOLANG) // PARENTHESES AROUND CONDITION OPTIONAL
if WhateverCondition {
  return 
} else if ElseIfCondition {
  return
} else {
  return
}

## SWITCH CASE

## PYTHON
match WhateverCondition:
  case 1: pass
  case 2: pass
  case 3: pass

## JAVASCRIPT

## GO (GOLANG)
switch i {
    case 0: fmt.Println("Zero")
	case 1: fmt.Println("One")
	case 2: fmt.Println("Two")
	case 3: fmt.Println("Three")
	case 4: fmt.Println("Four")
	case 5: fmt.Println("Five")
	default: fmt.Println("Unknown Number")
}

## EQUIVALENCY OPERATOR

## PYTHON
if 1 == 1:  ## WhateverCondition
    print("If WhateverCondition is True, then do whatever conditional operation")
else:
    print("...else:  then do something else")

## JAVASCRIPT
if (1 == 1) { // WhateverCondition
     console.log("If WhateverCondition is true");
} else {
     console.log("else AlternateCondition goes here");
}

## GO (GOLANG) // PARENTHESES AROUND CONDITION OPTIONAL
if (1 == 1) {
     fmt.Println("If WhateverCondition is true")
} else {
     fmt.Println("else AlternateCondition goes here")
}

## CREATE LIST / ARRAY

## PYTHON
PythonList = []

# JAVASCRIPT
var JavascriptArray = [];
let JavascriptArray = [];

## GO (GOLANG)

## ADD ELEMENT TO LIST / ARRAY

## PYTHON
PythonList.append(AnyVariableName)

# JAVASCRIPT
var JavascriptArray.push(AnyVariableName);

## GO (GOLANG)

## POP ELEMENT FROM LIST / ARRAY

## PYTHON
PythonList.pop(AnyVariableName)

# JAVASCRIPT
var JavascriptArray.pop(AnyVariableName);

## GO (GOLANG)

## CREATE PYTHON DICTIONARY / JAVASCRIPT OBJECT

## PYTHON
PythonDictionary = {}

# JAVASCRIPT
var JavascriptObject = {};

## GO (GOLANG)

## FOR LOOPS

## PYTHON
i = 0   ## INITIALIZE COUNTER VARIABLE
PythonList = []  ## CREATE EMPTY PYTHON LIST
RangeOfIntegerNumbers = list(range(5)) ## SET RANGE OF INTEGERS FOR FOR LOOP
for each in RangeOfIntegerNumbers:
    PythonList.append(each)
    i += 1 ## i = i + 1  ## INCREMENT COUNTER

## JAVASCRIPT
var JavascriptArray = [];   ## CREATE EMPTY JAVASCRIPT ARRAY
for (var i = 0; i < 5; i++) {  ## INITIALIZE COUNTER; SET RANGE OF INTEGERS FOR FOR LOOP; INCREMENT COUNTER
  JavascriptArray.push(i);
}

## GO (GOLANG) - VERSION 1
i := 0
for i <= 5 {
     fmt.Println(i) // CHANGE THIS TO ARRAY LATER
     i = i + 1
}

## GO (GOLANG) - VERSION 2
for i := 1; i <= 5; i++ {
     fmt.Println(i) // CHANGE THIS TO ARRAY LATER
}

## GAME OVER
## www.JerusalemProgramming.com
