Rtype={
    "add":("000","0110011","0000000"),
    "sub":("000","0110011","0100000"),
    "sll":("001","0110011","0000000"),
    "slt":("010","0110011","0000000"),
    "sltu":("011","0110011","0000000"),
    "xor":("100","0110011","0000000"),
    "srl":("101","0110011","0000000"),
    "or":("110","0110011","0000000"),
    "and":("111","0110011","0000000")
}

Itype={
    "lw":("010","0000011"),
    "addi":("000","0010011"),
    "sltiu":("011","0010011"),
    "jalr":("000","1100111")
}

Stype={
    "sw":("010","0100011")
}

Btype={
    "beq": ("000", "1100011"),
    "bne": ("001", "1100011"),
    "blt": ("100", "1100011"),
    "bge": ("101", "1100011"),
    "bltu": ("110", "1100011"),
    "bgeu": ("111", "1100011")
}

Utype={
    "lui":("0110111"),
    "auipc":("0010111")
}

Jtype={
    "jal":("1101111"),
}


register_address= {
    "zero": "00000",    
    "ra": "00001",     
    "sp": "00010",     
    "gp": "00011",     
    "tp": "00100",    
    "t0": "00101",     

    "t1": "00110",     
    "t2": "00111",

    "s0": "01000",      
    "fp": "01000",
    "s1": "01001",      

    "a0": "01010",     
    "a1": "01011",

    "a2": "01100",    
    "a3": "01101",
    "a4": "01110",     
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",

    "s2": "10010",    
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",

    "t3": "11100",     
    "t4": "11101",
    "t5": "11110",
    "t6": "11111"
}



labels={"start":0,"end":1}


program_memory=["00000000","00000004","00000008","0000000c","00000010","00000014","00000018","0000001c","00000020","00000024","00000028","0000002c","00000030","00000034","00000038","0000003c","00000040","00000044","00000048","0000004c","00000050","00000054","00000058","0000005c","00000060","00000064","00000068","0000006c","00000070","00000074","00000078","0000007c","00000080","00000084","00000088","0000008c","00000090","00000094","00000098","0000009c","000000a0","000000a4","000000a8","000000ac","000000b0","000000b4","000000b8","000000bc","000000c0","000000c4","000000c8","000000cc","000000d0","000000d4","000000d8","000000dc","000000e0","000000e4","000000e8","000000ec","000000f0","000000f4","000000f8","000000fc"]
stack_memory=["00000100","00000104","00000108","0000010c","00000110","00000114","00000118","0000011c","00000120","00000124","00000128","0000012c","00000130","00000134","00000138","0000013c","00000140","00000144","00000148","0000014c","00000150","00000154","00000158","0000015c","00000160","00000164","00000168","0000016c","00000170","00000174","00000178","0000017c"]
data_emory=["00100000","00100004","00100008","0010000c","00100010","00100014","00100018","0010001c","00100020","00100024","00100028","0010002c","00100030","00100034","00100038","0010003c","00100040","00100044","00100048","0010004c","00100050","00100054","00100058","0010005c","00100060","00100064","00100068","0010006c","00100070","00100074","00100078","0010007c"]


def imm_to_bin(immediate, bits):
    """Convert the immediate value to a binary string with the specified number of bits."""
   
    if not isinstance(immediate, int):
        raise ValueError("Immediate must be an integer")
    if not isinstance(bits, int) or bits <= 0:
        raise ValueError("Bits must be a positive integer")

  
    if immediate < -(1 << (bits - 1)) or immediate >= (1 << (bits - 1)):
        raise ValueError(f"Immediate value {immediate} is out of range for {bits}-bit binary")

  
    binary = ['0'] * bits  
    if immediate < 0:
       
        immediate = (1 << bits) + immediate

    
    for i in range(bits - 1, -1, -1):
        binary[i] = str(immediate & 1) 
        immediate >>= 1  

    return ''.join(binary) 




def extend_to_20_bits(number):
    """Extend the given number to a 20-bit binary representation."""

    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

  
    if number < -(1 << 19) or number >= (1 << 19):
        raise ValueError("Input value is out of range for a 20-bit binary")

    # Convert to binary
    if number >= 0:
   
        binary_str = format(number, '020b')
    else:
     
        binary_str = format((1 << 20) + number, '020b')

    return binary_str



def extend_to_16_bits(number):
    """Extend the given number to a 16-bit binary representation."""
 
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

  
    if number < -(1 << 15) or number >= (1 << 15):
        raise ValueError("Input value is out of range for a 16-bit binary")


    if number >= 0:
      
        binary_str = format(number, '016b')
    else:
     
        binary_str = format((1 << 16) + number, '016b')

    return binary_str





def scan_labels(text):
    """Scan labels from the given text and store them in the labels dictionary."""
    lines = text.split("\n")

    for line in lines:
        line = line.strip()
        if not line:  
            continue

        parts = line.split()
        if not parts:  
            continue

        instruction = parts[0].strip('"')
        if instruction[-1] == ':': 
            label = instruction[:-1]  
            labels[label] = None  


def parse_instruction(line):
    """Parse an instruction line and extract the instruction and operands."""
    parts = line.strip().split()
    instruction = parts[0].strip('"')

    if instruction[-1] == ':': 
        if len(parts) == 1:  
            return None, None
        else:
            instruction = parts[1].strip('"')  

    if len(parts) >= 2:
        if '(' in parts[1] and ')' in parts[1]:
            rd, rest = parts[1].split(",", 1)
            imm, rs1 = rest.split("(")
            rs1 = rs1.strip(')').strip('"')
            operands = [rd, rs1, imm]
        else:
            operands = parts[1].strip('"').split(",")


        operands.extend([None] * (3 - len(operands)))
    else:
        operands = [None, None, None]

    return instruction, operands

def format_code(text):
    """Format assembly-like code into machine code."""
    lines = text.split("\n")
    output = ''

    for line in lines:
        instruction, operands = parse_instruction(line)

        if instruction is None: 
            continue

        output += assembly_language(instruction, operands)

    return output


def is_virtual_halt(last_line):
    """Checks if the given line represents a virtual halt instruction."""

    last_line = last_line.strip()

    if ':' in last_line:
        last_instruction = last_line.split(':')[-1].strip()
    else:
        last_instruction = last_line


    return last_instruction == "beq zero,zero,0"

def virtualhalt(file_path):
    """Checks if the last line of the file represents a virtual halt instruction."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            last_line = lines[-1].strip()
            
            return is_virtual_halt(last_line)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False

# ********************************************************************************

def assembly_language(instruction, operands):
 
    if instruction in Rtype:
        funct3, opcode, funct7 = Rtype[instruction]
    elif instruction in Itype:
        funct3, opcode = Itype[instruction]
    elif instruction in Stype:
        funct3, opcode = Stype[instruction]
    elif instruction in Btype:
        funct3, opcode = Btype[instruction]
    elif instruction in Utype:
        opcode = Utype[instruction]
    elif instruction in Jtype:
        opcode = Jtype[instruction]
    else:
        return "Error: Instruction not in ISA"
    
    binary_operand = [register_address[op] if op in register_address else op for op in operands]

    if instruction in ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]:
        rd, rs1, rs2 = binary_operand
        return funct7 + rs2 + rs1 + funct3 + rd + opcode
    elif instruction in ["lw", "addi", "sltiu", "jalr"]:
        rd, rs1, imm = binary_operand
        return imm_to_bin(int(imm), 12) + rs1 + funct3 + rd + opcode
    elif instruction == "sw":
        rs2, rs1, imm = binary_operand
        return imm_to_bin(int(imm), 12)[0:7] + rs2 + rs1 + funct3 + imm_to_bin(int(imm), 12)[7:12] + opcode
    elif instruction in ["beq", "bne", "blt", "bge", "bltu", "bgeu"]:
        if operands == ["zero", "zero", "0"] and instruction == "beq":
         
            return "0000000000000000000000000" + opcode
        rs1, rs2, imm = binary_operand
        return extend_to_16_bits(int(imm))[0] + extend_to_16_bits(int(imm))[5:11] + rs2 + rs1 + funct3 + \
               extend_to_16_bits(int(imm))[11:] + opcode
    elif instruction in ["lui", "auipc"]:
        rd = binary_operand[0]
        imm = binary_operand[1]
        return imm_to_bin(int(imm), 32)[0:20] + rd + opcode
    elif instruction == "jal":
        rd = binary_operand[0]
        imm = binary_operand[1]
        return extend_to_20_bits(int(imm))[0] + extend_to_20_bits(int(imm))[9:19] + extend_to_20_bits(int(imm))[0:9] + rd + opcode


def give_output(input_file, output_file):
    
    if virtualhalt(input_file):
        
        with open(output_file, "w") as output:
            
            with open(input_file, 'r') as input:
                lines = input.readlines() 

                
                for line in lines:
                    
                    line = line.strip()
                    if not line:
                        continue
                    
                    formatted_output = format_code(line)
                    print(formatted_output)
                    output.write(formatted_output + "\n")
        print("Conversion completed successfully.")
    else:
        print("Virtual Halt instruction not found in the last line. Conversion aborted.")


input_file = "input.txt"
output_file = "output.txt"


give_output(input_file, output_file)
