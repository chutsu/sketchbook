# TYPES OF STRUCTS

```
// Named Field Struct
struct Point {
  x: f64,
  y: f64,
}

let p = Point {
  x: 1.0,
  y: 2.0,
};
let x = p.x;

// Tuple Struct
struct Color(
    u8, u8, u8
);

let c = Color(255,0,0);
let red = c.0;

// Unit Struct
struct Marker;
let m = Marker;
// no fields, no ()
```

# INSTANTIATION

```
// Shorthand (when var name == field name)
let x = 1.0; let y = 2.0;
let p = Point { x, y };                    // x: x, y: y shorthand

// Struct update syntax
let p2 = Point { x: 5.0, ..p };           // copy remaining fields from p

// Destructuring
let Point { x, y } = p;
let Point { x: px, y: py } = p;           // rename while destructuring
```

# IMPL BLOCKS & METHODS

```
impl Point {
    // Associated function (no self) — called like Point::new()
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    // Immutable method
    fn distance(&self, other: &Point) -> f64 { ... }

    // Mutable method
    fn translate(&mut self, dx: f64, dy: f64) {
        self.x += dx; self.y += dy;
    }

    // Takes ownership
    fn into_tuple(self) -> (f64, f64) { (self.x, self.y) }
}

let mut p = Point::new(1.0, 2.0);         // associated fn
p.translate(1.0, 1.0);                    // method call
```

# DERIVE MACROS (Common)

```
#[derive(Debug)]          // println!("{:?}", p)  or  "{:#?}" pretty print
#[derive(Clone)]          // p.clone()
#[derive(Copy)]           // copy instead of move (requires Clone)
#[derive(PartialEq)]      // p1 == p2
#[derive(Eq)]             // full equality (requires PartialEq)
#[derive(Hash)]           // use in HashMap/HashSet (requires Eq)
#[derive(Default)]        // Point::default()  →  zeroed fields
#[derive(PartialOrd, Ord)]// comparison and sorting

#[derive(Debug, Clone, PartialEq)]
struct Point { x: f64, y: f64 }
```

# TRAITS ON STRUCTS

```
// Implement a trait
impl std::fmt::Display for Point {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// Implement Default manually
impl Default for Point {
    fn default() -> Self { Self { x: 0.0, y: 0.0 } }
}
```

# GENERICS & LIFETIMES

```
// Generic struct
struct Pair<T> { first: T, second: T }

impl<T: std::fmt::Debug> Pair<T> {
    fn show(&self) { println!("{:?} {:?}", self.first, self.second); }
}

// Struct with lifetime
struct Important<'a> {
    part: &'a str,         // borrowed data, lives at least as long as 'a
}
```

# VISIBILITY

```
pub struct Foo {           // public struct
    pub x: i32,            // public field
        y: i32,            // private field (module-only)
    pub(crate) z: i32,     // visible within the crate
}

// Private fields force use of constructors (good for invariants)
```

# COMMON PATTERNS

```
// Builder pattern                       // Newtype pattern
struct Builder { val: i32 }              struct Meters(f64);
impl Builder {                           impl Meters {
    fn val(mut self, v: i32) -> Self {       fn value(&self) -> f64 {
        self.val = v; self                       self.0
    }                                        }
    fn build(self) -> Foo { ... }        }
}

// Type state pattern
struct Locked;   struct Unlocked;
struct Safe<State> { _state: std::marker::PhantomData<State> }
impl Safe<Locked>   { fn unlock(self) -> Safe<Unlocked> { ... } }
impl Safe<Unlocked> { fn open(&self)  { ... } }
```

# QUICK REFERENCE

```
struct Foo { .. }   Named  │  impl Foo { fn method(&self) }
struct Bar(..);     Tuple  │  Self = the type itself inside impl
struct Baz;         Unit   │  &self = borrow  │  &mut self = mut borrow
#[derive(..)]       Auto   │  self  = consume │  Foo::func() = assoc fn
```
