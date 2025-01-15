	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0
	.globl	__Z3fooi                        ; -- Begin function _Z3fooi
	.p2align	2
__Z3fooi:                               ; @_Z3fooi
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	mov	w8, #3                          ; =0x3
	stp	w8, w0, [sp, #8]
	mov	w8, #6                          ; =0x6
	str	w8, [sp, #4]
	mov	w0, #9                          ; =0x9
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
