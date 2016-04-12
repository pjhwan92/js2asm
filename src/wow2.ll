; ModuleID = 'wow.ll'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
target triple = "x86_64-unknown-linux-gnu"

; Function Attrs: nounwind readnone
define float @main() #0 {
function_init:
  br label %loop

loop:                                             ; preds = %loop, %function_init
  %i.0 = phi i32 [ 0, %function_init ], [ %3, %loop ]
  %x.0 = phi i32 [ 1, %function_init ], [ %2, %loop ]
  %0 = add i32 %i.0, -1
  %1 = add i32 %0, %x.0
  %2 = ashr i32 %1, 10
  %3 = add i32 %i.0, 1
  %exitcond = icmp eq i32 %3, 100000000
  br i1 %exitcond, label %elem, label %loop

elem:                                             ; preds = %loop
  %4 = bitcast i32 %2 to float
  %5 = fcmp ogt float %4, 1.000000e+00
  br i1 %5, label %if_then.i, label %__1.exit

if_then.i:                                        ; preds = %elem
  %6 = fadd float %4, 1.000000e+00
  br label %__1.exit

__1.exit:                                         ; preds = %elem, %if_then.i
  %7 = phi float [ %6, %if_then.i ], [ %4, %elem ]
  %8 = fadd float %7, 1.000000e+00
  ret float %8
}

; Function Attrs: nounwind readnone
define float @__0(float %a) #0 {
function_init:
  %0 = fcmp ogt float %a, 1.000000e+00
  br i1 %0, label %if_then, label %if_else

if_then:                                          ; preds = %function_init
  %1 = fadd float %a, 1.000000e+00
  ret float %1

if_else:                                          ; preds = %function_init
  ret float %a
}

; Function Attrs: nounwind readnone
define float @__1(i32 %a) #0 {
function_init:
  %0 = bitcast i32 %a to float
  %1 = fcmp ogt float %0, 1.000000e+00
  br i1 %1, label %if_then, label %if_else

if_then:                                          ; preds = %function_init
  %2 = fadd float %0, 1.000000e+00
  ret float %2

if_else:                                          ; preds = %function_init
  ret float %0
}

attributes #0 = { nounwind readnone }
