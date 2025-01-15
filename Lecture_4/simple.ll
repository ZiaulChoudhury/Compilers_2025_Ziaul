; ModuleID = 'simple.cpp'
source_filename = "simple.cpp"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx12.0.0"

; Function Attrs: mustprogress noinline nounwind optnone ssp uwtable(sync)
define noundef i32 @_Z3fooi(i32 noundef %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %0, ptr %3, align 4
  store i32 3, ptr %4, align 4
  store i32 6, ptr %5, align 4
  %6 = load i32, ptr %3, align 4
  %7 = icmp sgt i32 %6, 2
  br i1 %7, label %8, label %12

8:                                                ; preds = %1
  %9 = load i32, ptr %4, align 4
  %10 = load i32, ptr %5, align 4
  %11 = add nsw i32 %9, %10
  store i32 %11, ptr %2, align 4
  br label %16

12:                                               ; preds = %1
  %13 = load i32, ptr %4, align 4
  %14 = load i32, ptr %5, align 4
  %15 = sub nsw i32 %13, %14
  store i32 %15, ptr %2, align 4
  br label %16

16:                                               ; preds = %12, %8
  %17 = load i32, ptr %2, align 4
  ret i32 %17
}

attributes #0 = { mustprogress noinline nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+complxnum,+crc,+dotprod,+fp-armv8,+fp16fml,+fullfp16,+jsconv,+lse,+neon,+pauth,+ras,+rcpc,+rdm,+sha2,+sha3,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"uwtable", i32 1}
!3 = !{i32 7, !"frame-pointer", i32 1}
!4 = !{!"clang version 18.1.8 (https://github.com/llvm/llvm-project.git 3b5b5c1ec4a3095ab096dd780e84d7ab81f3d7ff)"}
