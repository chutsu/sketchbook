# Slice

A slice (&[T]) is a borrowed reference to a contiguous sequence
of elements. It does not own data -- it borrows it.


BASIC SLICE SYNTAX
------------------

```
let arr = [1, 2, 3, 4, 5];

let whole  = &arr[..];    // [1, 2, 3, 4, 5]
let first3 = &arr[..3];   // [1, 2, 3]  (exclusive end)
let last3  = &arr[2..];   // [3, 4, 5]
let middle = &arr[1..4];  // [2, 3, 4]
```

STRING SLICES (&str)
--------------------

```
let s = String::from("hello world");

let hello = &s[..5];    // "hello"
let world = &s[6..];    // "world"
let full: &str = &s;    // borrow the whole string
```


IN FUNCTION SIGNATURES
----------------------
Prefer slices over &Vec or &String -- they are more flexible.

```
fn sum(nums: &[i32]) -> i32 {   // accepts Vec, arrays, or slices
    nums.iter().sum()
}

fn greet(name: &str) {          // accepts String or &str
    println!("Hello, {name}!");
}
```


COMMON SLICE METHODS
--------------------
```
let s = &[1, 2, 3, 4, 5];

s.len()               // 5
s.is_empty()          // false
s.first()             // Some(&1)
s.last()              // Some(&5)
s.get(2)              // Some(&3)  -- safe indexing, no panic
s.get(99)             // None
s.contains(&3)        // true
s.iter()              // iterator over &T
s.windows(3)          // [1,2,3], [2,3,4], [3,4,5]
s.chunks(2)           // [1,2], [3,4], [5]
s.split_at(2)         // (&[1,2], &[3,4,5])
s.starts_with(&[1,2]) // true
```

MUTABLE SLICES
--------------
```
let mut arr = [3, 1, 4, 1, 5];
let s = &mut arr[1..4];

s.sort();
s[0] = 99;
s.iter_mut().for_each(|x| *x *= 2);
```


SLICES FROM VEC
---------------
```
let v = vec![1, 2, 3];
let s: &[i32] = &v;          // deref coercion
let s: &[i32] = v.as_slice();
```


KEY RULE
--------
```
&Vec<T>  -->  use &[T]
&String  -->  use &str
```

Slices are always the more general and idiomatic choice
in function parameters.
