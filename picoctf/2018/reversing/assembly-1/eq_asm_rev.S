.intel_syntax noprefix
.bits 32
	
.global asm1

; asm(0xcd)
 
asm1:
	push	ebp
	mov	ebp,esp				; function prologue
	cmp	DWORD PTR [ebp+0x8],0xde	; 0xcd > 0xde = false	
	jg 	part_a	
	cmp	DWORD PTR [ebp+0x8],0x8		; 0xcd != 0x8 = true
	jne	part_b				; goto b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x4e
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]		; move 0xcd to eax
	sub	eax,0x3				; subtract 0x3 from 0xcd = 0xca
	jmp	part_d				; goto d
	cmp	DWORD PTR [ebp+0x8],0xee
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp				; exit, 0xca is eax = FLAG
	ret
