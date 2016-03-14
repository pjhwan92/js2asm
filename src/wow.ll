; ModuleID = 'top'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
target triple = "asmjs-unknown-emscripten"

define float @__1(i32 %i1, float %i2) {
function_init:
  %0 = alloca i32
  store i32 %i1, i32* %0
  %1 = alloca float
  store float %i2, float* %1
  %2 = load i32* %0
  %3 = load float* %1
  %4 = bitcast i32 %2 to float
  %5 = fmul float %4, %3
  ret float %5
}

define float @main() {
function_init:
  %f = alloca float
  store float 0.000000e+00, float* %f
  %a = alloca i32
  store i32 2, i32* %a
  %0 = alloca float, i32 4
  %arrayinit.elem = getelementptr inbounds float* %0, i32 0
  store float 6.000000e+00, float* %arrayinit.elem
  %arrayinit.elem1 = getelementptr inbounds float* %0, i32 1
  store float 0x4010666660000000, float* %arrayinit.elem1
  %arrayinit.elem2 = getelementptr inbounds float* %0, i32 2
  store float 0x4018CCCCC0000000, float* %arrayinit.elem2
  %arrayinit.elem3 = getelementptr inbounds float* %0, i32 3
  store float 0x4020CCCCC0000000, float* %arrayinit.elem3
  %1 = load float* %0
  %b = alloca float
  store float %1, float* %b
  %c = alloca float
  store float 2.000000e+00, float* %c
  %array.elem = getelementptr inbounds float* %b, i32 0
  %2 = load float* %array.elem
  %3 = fcmp oeq float %2, 2.000000e+00
  br i1 %3, label %if_then, label %if_else

if_then:                                          ; preds = %function_init
  %array.elem4 = getelementptr inbounds float* %b, i32 1
  %4 = load float* %c
  %5 = fmul float %4, 2.000000e+00
  %6 = load float* %array.elem4
  store float %5, float* %array.elem4
  %i = alloca i32
  store i32 0, i32* %i
  %7 = load i32* %i8
  store i32 1, i32* %i8
  store i32 2, i32* %i8
  store i32 3, i32* %i8
  br label %iter_cond

if_else:                                          ; preds = %function_init
  %8 = load float* %c
  %9 = fcmp oeq float %8, 2.000000e+00
  br i1 %9, label %if_then5, label %if_else6

if_then5:                                         ; preds = %if_else
  %10 = load float* %c
  %11 = fsub float %10, 2.000000e+00
  store float %11, float* %c
  %i7 = alloca i32
  store i32 0, i32* %i7
  %12 = load i32* %i8
  store i32 1, i32* %i8
  store i32 2, i32* %i8
  store i32 3, i32* %i8
  br label %iter_cond9

if_else6:                                         ; preds = %if_else
  %i8 = alloca i32
  store i32 0, i32* %i8
  store i32 1, i32* %i8
  store i32 2, i32* %i8
  store i32 3, i32* %i8
  br label %iter_cond12

iter_cond:                                        ; preds = %iter_body, %if_then
  %13 = load i32* %i8
  %14 = icmp slt i32 %13, 10
  br i1 %14, label %iter_body, label %elem

iter_body:                                        ; preds = %iter_cond
  %array.elem15 = getelementptr inbounds float* %b, i32 3
  %15 = load float* %array.elem15
  %16 = load i32* %i8
  %17 = sitofp i32 %16 to float
  %18 = fadd float %15, %17
  store float %18, float* %array.elem15
  %19 = add i32 %16, 1
  store i32 %19, i32* %i8
  br label %iter_cond

elem:                                             ; preds = %iter_cond
  %20 = load i32* %i8
  %21 = add i32 10, %20
  %array.elem18 = getelementptr inbounds float* %b, i32 2
  %22 = load float* %array.elem18
  %23 = fadd float 2.000000e+01, %22
  %24 = call float @__1(i32 %21, float %23)
  %25 = load float* %f
  store float %24, float* %f
  %array.elem21 = getelementptr inbounds float* %b, i32 1
  %26 = load float* %array.elem21
  %27 = fmul float %26, 4.000000e+00
  %28 = load float* %c
  %29 = fmul float %28, 2.550000e+02
  %30 = fadd float %27, %29
  ret float %30

iter_cond9:                                       ; preds = %iter_body10, %if_then5
  %31 = load i32* %i8
  %32 = icmp slt i32 %31, 10
  br i1 %32, label %iter_body10, label %elem11

iter_body10:                                      ; preds = %iter_cond9
  %array.elem16 = getelementptr inbounds float* %b, i32 3
  %33 = load float* %array.elem16
  %34 = load i32* %i8
  %35 = sitofp i32 %34 to float
  %36 = fadd float %33, %35
  store float %36, float* %array.elem16
  %37 = add i32 %34, 1
  store i32 %37, i32* %i8
  br label %iter_cond9

elem11:                                           ; preds = %iter_cond9
  %38 = load i32* %i8
  %39 = add i32 10, %38
  %array.elem19 = getelementptr inbounds float* %b, i32 2
  %40 = load float* %array.elem19
  %41 = fadd float 2.000000e+01, %40
  %42 = call float @__1(i32 %39, float %41)
  %43 = load float* %f
  store float %42, float* %f
  %array.elem22 = getelementptr inbounds float* %b, i32 1
  %44 = load float* %array.elem22
  %45 = fmul float %44, 4.000000e+00
  %46 = load float* %c
  %47 = fmul float %46, 2.550000e+02
  %48 = fadd float %45, %47
  ret float %48

iter_cond12:                                      ; preds = %iter_body13, %if_else6
  %49 = load i32* %i8
  %50 = icmp slt i32 %49, 10
  br i1 %50, label %iter_body13, label %elem14

iter_body13:                                      ; preds = %iter_cond12
  %array.elem17 = getelementptr inbounds float* %b, i32 3
  %51 = load float* %array.elem17
  %52 = load i32* %i8
  %53 = sitofp i32 %52 to float
  %54 = fadd float %51, %53
  store float %54, float* %array.elem17
  %55 = add i32 %52, 1
  store i32 %55, i32* %i8
  br label %iter_cond12

elem14:                                           ; preds = %iter_cond12
  %56 = load i32* %i8
  %57 = add i32 10, %56
  %array.elem20 = getelementptr inbounds float* %b, i32 2
  %58 = load float* %array.elem20
  %59 = fadd float 2.000000e+01, %58
  %60 = call float @__1(i32 %57, float %59)
  %61 = load float* %f
  store float %60, float* %f
  %array.elem23 = getelementptr inbounds float* %b, i32 1
  %62 = load float* %array.elem23
  %63 = fmul float %62, 4.000000e+00
  %64 = load float* %c
  %65 = fmul float %64, 2.550000e+02
  %66 = fadd float %63, %65
  ret float %66
}
