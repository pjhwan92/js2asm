; ModuleID = 'top'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
target triple = "asmjs-unknown-emscripten"

define i32 @__1(i32 %a, i32 %b) {
function_init:
  %0 = alloca i32
  store i32 %a, i32* %0
  %1 = alloca i32
  store i32 %b, i32* %1
  br label %loop

loop:                                             ; preds = %if_else, %if_then, %function_init
  %2 = load i32* %0
  %3 = srem i32 %2, 2
  %4 = icmp eq i32 %3, 0
  br i1 %4, label %if_then, label %if_else

if_then:                                          ; preds = %loop
  %5 = load i32* %0
  %6 = mul i32 %5, %5
  store i32 %6, i32* %0
  %7 = icmp slt i32 %6, 1000
  br i1 %7, label %loop, label %elem

if_else:                                          ; preds = %loop
  %8 = load i32* %0
  %9 = sdiv i32 %8, 10
  store i32 %9, i32* %0
  %10 = icmp slt i32 %9, 1000
  br i1 %10, label %loop, label %elem1

elem:                                             ; preds = %if_then
  %11 = load i32* %1
  %12 = mul i32 10, %11
  %13 = load i32* %0
  %14 = add i32 %13, %12
  ret i32 %14

elem1:                                            ; preds = %if_else
  %15 = load i32* %1
  %16 = mul i32 10, %15
  %17 = load i32* %0
  %18 = add i32 %17, %16
  ret i32 %18
}

define i32 @__2(i32 %a) {
function_init:
  %0 = alloca i32
  store i32 %a, i32* %0
  br label %loop

loop:                                             ; preds = %if_else, %if_then, %function_init
  %1 = load i32* %0
  %2 = srem i32 %1, 2
  %3 = icmp eq i32 %2, 0
  br i1 %3, label %if_then, label %if_else

if_then:                                          ; preds = %loop
  %4 = load i32* %0
  %5 = mul i32 %4, %4
  store i32 %5, i32* %0
  %6 = icmp slt i32 %5, 100
  br i1 %6, label %loop, label %elem

if_else:                                          ; preds = %loop
  %7 = load i32* %0
  %8 = icmp slt i32 %7, 100
  br i1 %8, label %loop, label %elem1

elem:                                             ; preds = %if_then
  %9 = load i32* %0
  %10 = add i32 %9, 10
  ret i32 %10

elem1:                                            ; preds = %if_else
  %11 = load i32* %0
  %12 = add i32 %11, 10
  ret i32 %12
}

define i32 @main() {
function_init:
  %c = alloca i32
  store i32 2, i32* %c
  br i1 false, label %ter_if, label %ter_else

ter_if:                                           ; preds = %function_init
  %a = alloca i32
  store i32 1, i32* %a
  %0 = call i32 @__1(i32 1, i32 3)
  %1 = load i32* %c
  %2 = add i32 %1, %0
  store i32 %2, i32* %c
  %3 = call i32 @__2(i32 2)
  %4 = add i32 %2, %3
  store i32 %4, i32* %c
  %5 = load i32* %a1
  %6 = mul i32 %5, %4
  store i32 %6, i32* %c
  ret i32 %6

ter_else:                                         ; preds = %function_init
  %a1 = alloca i32
  store i32 2, i32* %a1
  %7 = call i32 @__1(i32 1, i32 3)
  %8 = load i32* %c
  %9 = add i32 %8, %7
  store i32 %9, i32* %c
  %10 = call i32 @__2(i32 2)
  %11 = add i32 %9, %10
  store i32 %11, i32* %c
  %12 = mul i32 2, %11
  store i32 %12, i32* %c
  ret i32 %12
}
