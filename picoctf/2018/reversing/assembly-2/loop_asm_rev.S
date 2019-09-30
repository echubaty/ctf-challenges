.intel_syntax noprefix
.bits 32
	
.global asm2

; asm2(0x7,0x28)

; ebp + val -> args
; ebp - val -> local vars

asm2:
	push   	ebp
	mov    	ebp,esp						; function prologue
	sub    	esp,0x10					; reserve 16 bytes on stack (0x10 = 16) 
	mov    	eax,DWORD PTR [ebp+0xc]		
	mov 	DWORD PTR [ebp-0x4],eax		; set ebp-0x4 to 0x28
	mov    	eax,DWORD PTR [ebp+0x8]		
	mov	DWORD PTR [ebp-0x8],eax			; set ebp-0x8 to 0x7
	jmp    	part_b						; jump to part b
part_a:			1					; iterator
	add    	DWORD PTR [ebp-0x4],0x1 	; ebp-0x4 is a counter (initially 0x28)
	add		DWORD PTR [ebp+0x8],0x76	; add 0x76 to ebp+0x8 (initially 0x7)
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0xa1de 
	jle    	part_a						; loop if ebp+0x8 is less than 0xa1de
	mov    	eax,DWORD PTR [ebp-0x4]		; this loop happens 351 times, 351 + 1 + 0x28 = 0x188 (FLAG)
	mov	esp,ebp
	pop	ebp
	ret
