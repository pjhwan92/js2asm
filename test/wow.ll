; ModuleID = 'top'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
target triple = "asmjs-unknown-emscripten"

define float @__0(float %a) {
function_init:
  %0 = alloca float
  store float %a, float* %0
  %1 = load float* %0
  %2 = fcmp ogt float %1, 1.000000e+00
  br i1 %2, label %if_then, label %if_else

if_then:                                          ; preds = %function_init
  %3 = load float* %0
  %4 = fadd float %3, 1.000000e+00
  ret float %4

if_else:                                          ; preds = %function_init
  %5 = load float* %0
  ret float %5
}

define float @__1(i32 %a) {
function_init:
  %0 = alloca i32
  store i32 %a, i32* %0
  %1 = load i32* %0
  %2 = bitcast i32 %1 to float
  %3 = fcmp ogt float %2, 1.000000e+00
  br i1 %3, label %if_then, label %if_else

if_then:                                          ; preds = %function_init
  %4 = load i32* %0
  %5 = bitcast i32 %4 to float
  %6 = fadd float %5, 1.000000e+00
  ret float %6

if_else:                                          ; preds = %function_init
  %7 = load i32* %0
  %8 = bitcast i32 %7 to float
  ret float %8
}

define float @main() {
function_init:
  %i = alloca i32
  store i32 0, i32* %i
  %x = alloca i32
  store i32 1, i32* %x
  br label %loop

loop:                                             ; preds = %loop, %function_init
  %0 = load i32* %x
  %1 = load i32* %i
  %2 = add i32 %0, %1
  store i32 %2, i32* %x
  %3 = sub i32 %2, 1
  store i32 %3, i32* %x
  %4 = ashr i32 %3, 10
  store i32 %4, i32* %x
  %5 = add i32 %1, 1
  store i32 %5, i32* %i
  %6 = icmp slt i32 %5, 100000000
  br i1 %6, label %loop, label %elem

elem:                                             ; preds = %loop
  %7 = call float @__0(float 1.000000e+00)
  %8 = load i32* %x
  %9 = call float @__1(i32 %8)
  %10 = fadd float %7, %9
  ret float %10
}
