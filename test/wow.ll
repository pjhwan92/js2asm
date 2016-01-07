; ModuleID = 'top'
target datalayout = "e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128"
target triple = "asmjs-unknown-emscripten"

%struct.main = type { i32, i32, i32 }

define %struct.main @main() {
function_init:
  %a = alloca i32 ()*
  store i32 ()* @__1, i32 ()** %a
  %b = alloca i32
  store i32 10, i32* %b
  %c = alloca i32
  store i32 100, i32* %c
  %d = alloca i32
  store i32 3, i32* %d
}

define i32 @__1() {
function_init:
  ret i32 3
}
