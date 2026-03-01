# Ownership

THE 3 RULES

1. Every value has a single owner
2. Only one owner at a time
3. Value dropped when owner goes out of scope

# Move (Non-Copy types: String, Vec, Box...)

```
let a = String::from("hi");
let b = a;  // a is moved, now invalid
println!("{}", a); // ✗ compile error
```

## Copy (ints, floats, bool, char, fixed tuples)

```
let x = 5;
let y = x;   // x is COPIED → both valid
println!("{} {}", x, y); // ✓
```

## Clone (explicit deep copy)

```
let a = String::from("hi");
let b = a.clone(); // both valid, heap data duplicated
```

## Borrowing &T  (immutable reference)

```
let s = String::from("hi");
let r = &s;            // borrow, s still owns
println!("{}", r);     // ✓  s still valid after
-> many immutable refs allowed at once
```

## Borrowing &mut T  (mutable reference)

```
let mut s = String::from("hi");
let r = &mut s;        // mutable borrow
r.push_str(" world");  // ✓
-> only ONE &mut ref allowed; no & refs simultaneously
```

## Reference Rules Summary

```
 &T            many at once, read-only
 &mut T        exactly one, read+write
 &T + &mut T   NOT allowed simultaneously
```

## Lifetimes (when compiler needs a hint)

```
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str { ... }
'a = "both inputs and output live at least this long"
```

## Common Smart Pointers

```
Box<T>      heap allocation, single owner
Rc<T>       shared ownership, single thread
Arc<T>      shared ownership, multi-thread safe
RefCell<T>  interior mutability, runtime borrow checks
```


