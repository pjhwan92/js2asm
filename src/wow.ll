; ModuleID = 'top'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
;target triple = "asmjs-unknown-emscripten"
target triple = "x86_64-unknown-linux-gnu"

define i32 @main() {
function_init:
  %p1 = alloca i32
  %p2 = alloca i32
  %tmp = alloca i32
  store i32 0, i32* %tmp
  %i = alloca i32
  store i32 0, i32* %i
  %j = alloca i32
  store i32 0, i32* %j
  br label %loop

loop:                                             ; preds = %function_init
  br label %loop1

loop1:                                            ; preds = %loop
  %0 = load i32* %p1
  %1 = load i32* %p2
  %2 = add i32 %0, %1
  store i32 %2, i32* %p1
  br label %loop2

loop2:                                            ; preds = %loop2, %loop1
  %3 = load i32* %p1
  %4 = sdiv i32 %3, 10
  store i32 %4, i32* %p1
  %5 = icmp sgt i32 %4, 10
  br i1 %5, label %loop2, label %elem

elem:                                             ; preds = %loop2
  %6 = load i32* %p2
  %7 = load i32* %tmp
  store i32 %7, i32* %p2
  br label %loop3

loop3:                                            ; preds = %loop3, %elem
  %8 = load i32* %p2
  %9 = sdiv i32 %8, 10
  store i32 %9, i32* %p2
  %10 = icmp sgt i32 %9, 10
  br i1 %10, label %loop3, label %elem4

elem4:                                            ; preds = %loop3
  %11 = load i32* %tmp
  %12 = load i32* %p1
  store i32 %12, i32* %tmp
  %13 = load i32* %j
  %14 = add i32 %13, 1
  store i32 %14, i32* %j
  %15 = icmp slt i32 %14, 100000
	ret i32 0
}
