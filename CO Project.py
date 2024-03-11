#dictionary -->  instruction:(opcode,func 3,func7)
R_type={
    "add":("0110011","000","0000000"),
    "sub":("0110011","000","0100000"),
    "sll":("0110011","001","0000000"),
    "slt":("0110011","010","0000000"),
    "sltu":("0110011","011","0000000"),
    "xor":("0110011","100","0000000"),
    "srl":("0110011","101","0000000"),
    "or":("0110011","110","0000000"),
    "and":("0110011","111","0000000")}

#dictionary -->  instruction:(opcode,func 3)
I_type={
    "lw":("0000011","010"),
    "addi":("0010011","000"),
    "sltiu":("0010011","011"),
    "jalr":("1100111","000")}

#dictionary -->  instruction:(opcode,func 3)
S_type={
    "sw":("0100011","010")}

#dictionary -->  instruction:(opcode,func 3)
B_type={
    "beq": ("1100011","000"),
    "bne": ("1100011","001"),
    "blt": ("1100011","100"),
    "bge": ("1100011","101"),
    "bltu": ("1100011","110"),
    "bgeu": ("1100011","111")}

#dictionary -->  instruction:(opcode)
U_type={
    "lui":("0110111"),
    "auipc":("0010111")}

#dictionary -->  instruction:(opcode)
J_type={
    "jal":("1101111")}

#register address according to the info given
register_address= {
    "zero": "00000",    #zero   Hard-wired zero 
    "ra": "00001",      #ra     Return address
    "sp": "00010",      #sp     Stack Pointer
    "gp": "00011",      #gp     Global Pointer
    "tp": "00100",      #tp     Thread Pointer
    "t0": "00101",      #t0     Temporary/ alternate link register

    "t1": "00110",      #t1-2   Temporaries
    "t2": "00111",

    "s0": "01000",      #s0     Saved register
    "fp": "01000",      #fp     Frame pointer
    "s1": "01001",      #s1     Saved register

    "a0": "01010",     #a0-1    Function arguments/ return values
    "a1": "01011",

    "a2": "01100",     #a2-7    Function arguments
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",

    "s2": "10010",     #s2-11   Saved registers
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",

    "t3": "11100",     #t3-6    Temporatries
    "t4": "11101",
    "t5": "11110",
    "t6": "11111"
}

