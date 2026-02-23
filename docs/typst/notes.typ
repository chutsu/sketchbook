#import "@preview/rubber-article:0.4.2": *

//#show: article.with(
//  lang: "en",
//  header-display: true,
//  eq-numbering: "(1.1)",
//  eq-chapterwise: true,
//  margins: 2in,
//  cols: 1,
//)
//
//#maketitle(
//  title: "Reprojection Error",
//  authors: ("Christopher Choi",),
//  date: datetime.today().display("[day]. [month repr:long] [year]"),
//)

#show math.equation: html.frame

// Maths Macros
#let skew(val) = $(#val)^(times)$
#let tf(to, from) = $bold(T)_(#to #from) #h(0.3em)$
#let tfinv(to, from) = $bold(T)_(#to #from)^(-1) #h(0.3em)$
#let rot(to, from) = $bold(C)_(#to #from)$
#let dtheta(to, from) = $delta bold(theta)_(#to #from)$
#let dthetainv(to, from) = $delta bold(theta)_(#to #from)^(-1)$
#let dpos(expin, to, from) = $delta ""_(#expin)bold(r)_(#to #from)$
#let pos(expin, to, from) = $""_(#expin)bold(r)_(#to #from)$
#let point(frame) = $""_(#frame)bold(p)$


= Reprojection Error

$
  bold(r) &= bold(z) - bold(pi) (
    tfinv(B, C_i) #h(0.2em)
    tf(B, T_j) #h(0.2em)
    point(T_j)
  ) \
  &= bold(z) - bold(pi) (
    point(C_i)
  ) \
  &= bold(z) - bold(k)(bold(d)(bold(p)(
      point(C_i)
    ))) \
$

$
  point(C_i) =
    tfinv(C_0, C_i) #h(0.5em)
    tf(C_0, S) #h(0.5em)
    tfinv(W, S) #h(0.5em)
    tf(W, T_0) #h(0.5em)
    tf(T_0, T_j) #h(0.5em)
    point(T_j)
$

$
  underbrace(
    frac(partial bold(r), partial bold(h)),
    -1
  )
  underbrace(
    frac(partial bold(h), partial bold(x'))
    frac(partial bold(x'), partial bold(x))
    frac(partial bold(x), partial point(C_i)),
    bold(J)_(h)
  )
$

== Jacobian with respect to camera extrinsic $tf(C_0, C_i)$:

$
  point(C_i)
    &= tfinv(C_0, C_i) point(C_0) \
    &= rot(C_0, C_i)^(T) (point(C_0) - pos(C_0, C_0, C_i)) \
$

$
  frac(partial point(C_i), partial tf(C_0, C_i))
  frac(partial tf(C_0, C_i), partial tfinv(C_0, C_i))
$

$
  frac(partial point(C_i), partial dpos(C_0, C_0, C_i)) &=
    -rot(B, C_i)^(T) \
  frac(partial point(C_i), partial dtheta(C_0, C_i)) &=
    frac(partial point(C_i), partial dthetainv(C_0, C_i)) #h(0.3em)
    frac(partial dthetainv(C_0, C_i), partial dtheta(C_0, C_i)) \
  &=
    (-rot(C_0, C_i)^(T) skew(point(C_0) - pos(C_0, C_0, C_i)))
    dot #h(0.3em)
    (-rot(C_0, C_i))
$


== Jacobian with respect to IMU extrinsic $tf(C_0, S)$:

$
  point(C_0)
    &= tf(C_0, S) point(S) \
    &= rot(C_0, S) point(S) + pos(C_0, C_0, S) \
$

$
  frac(partial point(C_i), partial tf(C_0, S)) &=
    frac(partial point(C_i), partial point(C_0))
    frac(partial point(C_0), partial tf(C_0, S)) \
  &=
    frac(partial point(C_i), partial point(C_0))
    [
      frac(partial point(C_0), partial dtheta(C_0, S))
      #h(1em)
      frac(partial point(C_0), partial dpos(C_0, C_0, S))
    ] \
  &=
  ( rot(C_i, C_0))
  [
    -rot(C_0, S) dot skew(point(S))
    #h(1em)
    bold(1)_(3 times 3)

  ]
$


== Jacobian with respect to IMU pose $tf(W, S)$:

$
  point(S)
    &= tfinv(W, S) point(W) \
    &= rot(W, S)^(T) (point(W) - pos(W, W, S)) \
$

$
  frac(partial point(C_i), partial tf(W, S)) &=
    frac(partial point(C_i), partial point(S))
    frac(partial point(S), partial tf(W, S)) \
  &=
    frac(partial point(C_i), partial point(S))
    [
      frac(partial point(S), partial dthetainv(W, S))
      frac(partial dthetainv(W, S), partial dtheta(W, S))
      #h(1.5em)
      frac(partial point(S), partial dpos(W, W, S))
    ]

    \
  &=
  ( rot(C_i, S))
  [
    {(-rot(W, S)^(T) dot skew(point(W) - pos(W, W, S))) dot -rot(W, S)}
    #h(1em)
    -rot(W, S)^(T)
  ]
$


== Jacobian with respect to target pose $tf(W, T_0)$:

$
  point(W)
    &= tf(W, T_0) #h(0.5em) point(T_0) \
    &= rot(W, T_0) #h(0.5em) point(T_0) + pos(W, W, T_0) \
$

$
  frac(partial point(C_i), partial tf(W, T_0)) &=
    frac(partial point(C_i), partial point(W))
    frac(partial point(W), partial tf(W, T_0)) \
  &=
    frac(partial point(C_i), partial point(W))
    [
      frac(partial point(W), partial dtheta(W, T_0))
      #h(1em)
      frac(partial point(W), partial dpos(W, W, T_0))
    ] \
  &=
  ( rot(C_i, W))
  [
    -rot(W, T_0) dot skew(point(T_0))
    #h(1em)
    bold(1)_(3 times 3)
  ]
$


== Jacobian with respect to target extrinsic $tf(T_0, T_j)$:

$
  point(T_0)
    &= tf(T_0, T_j) #h(0.5em) point(T_j) \
    &= rot(T_0, T_j) #h(0.5em) point(T_j) + pos(T_0, T_0, T_j) \
$

$
  frac(partial point(C_i), partial tf(T_0, T_j)) &=
    frac(partial point(C_i), partial point(T_0))
    frac(partial point(T_0), partial tf(T_0, T_j)) \
  &=
    frac(partial point(C_i), partial point(T_0))
    [
      frac(partial point(T_0), partial dtheta(T_0, T_j))
      #h(1em)
      frac(partial point(T_0), partial dpos(T_0, T_0, T_j))
    ] \
  &=
  ( rot(C_i, T_0))
  [
    -rot(T_0, T_j) dot skew(point(T_j))
    #h(1em)
    bold(1)_(3 times 3)
  ]
$


== Jacobian with respect to target point $point(T_j)$:

$
  point(C_i)
    &= tf(C_i, T_j) #h(0.5em) point(T_j) \
    &= rot(C_i, T_j) #h(0.5em) point(T_j) + pos(C_i, C_i, T_j) \
$

$
  frac(partial point(C_i), partial point(T_j)) &=  rot(C_i, T_j)
$
