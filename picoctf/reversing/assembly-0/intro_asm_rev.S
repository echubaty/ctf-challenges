
asm0: args: (0x2a,0x4f)
	push	ebp
	mov	ebp,esp ;prologue
	mov	eax,DWORD PTR [ebp+0x8] ; 0x2a to eax
	mov	ebx,DWORD PTR [ebp+0xc] ; 0x4f to ebx
	mov	eax,ebx ; squash eax with ebx
	mov	esp,ebp
	pop	ebp	
	ret

therefore the flag is just 0x4f
