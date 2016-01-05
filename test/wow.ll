; ModuleID = 'top'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
target triple = "asmjs-unknown-emscripten"

define i32 @__0(i32 %a, i32 %b) {
function_init:
  %0 = alloca i32
  store i32 %a, i32* %0
  %1 = alloca i32
  store i32 %b, i32* %1
  br label %loop

loop:                                             ; preds = %loop, %loop, %function_init
  %2 = load i32* %0
  %3 = srem i32 %2, 2
  %4 = icmp eq i32 %3, 0
  br i1 %4, label %if_then, label %if_else
  br i1 %7, label %loop, label %elem
  br i1 %7, label %loop, label %elem1

if_then:                                          ; preds = %loop
  %5 = load i32* %0
  %6 = mul i32 %5, %5
  store i32 %6, i32* %0
  %7 = icmp slt i32 %6, 1000

if_else:                                          ; preds = %loop
  %8 = load i32* %0
  %9 = sdiv i32 %8, 10
  store i32 %9, i32* %0
  %10 = icmp slt i32 %9, 1000

elem:                                             ; preds = %loop
  %11 = load i32* %1
  %12 = mul i32 10, %11
  %13 = add i32 %6, %12
  %14 = bitcast i32 %13 to float
  ret float %14

elem1:                                            ; preds = %loop
  %15 = load i32* %1
  %16 = mul i32 10, %15
  %17 = add i32 %9, %16
  %18 = bitcast i32 %17 to float
  ret float %18
}

define i32 @__1(i32 %a) {
function_init:
  %0 = alloca i32
  store i32 %a, i32* %0
  br label %loop

loop:                                             ; preds = %loop, %loop, %function_init
  %1 = load i32* %0
  %2 = srem i32 %1, 2
  %3 = icmp eq i32 %2, 0
  br i1 %3, label %if_then, label %if_else
  br i1 %6, label %loop, label %elem
  br i1 %6, label %loop, label %elem1

if_then:                                          ; preds = %loop
  %4 = load i32* %0
  %5 = mul i32 %4, %4
  store i32 %5, i32* %0
  %6 = icmp slt i32 %5, 100

if_else:                                          ; preds = %loop
  %7 = load i32* %0
  %8 = icmp slt i32 %7, 100

elem:                                             ; preds = %loop
  %9 = add i32 %5, 10
  %10 = bitcast i32 %9 to float
  ret float %10

elem1:                                            ; preds = %loop
  %11 = add i32 %7, 10
  %12 = bitcast i32 %11 to float
  ret float %12
}

define i32 @main() {
function_init:
  %c = alloca i32
  store i32 2, i32* %c
  %a = alloca i32
  store i32 1, i32* %a
  %0 = call i32 @__0(i32 1, i32 3)
  %1 = load i32* %c
  %2 = add i32 %1, %0
  store i32 %2, i32* %c
  %3 = call i32 @__1(i32 2)
  %4 = add i32 %2, %3
  store i32 %4, i32* %c
  %5 = load i32* %a
  %6 = mul i32 %5, %4
  %7 = bitcast i32 %4 to float
  ret float %7
}
