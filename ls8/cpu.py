"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [bin(0)] * 256
        self.pc = 0
        self.reg = [bin(0)] * 8

        #create a branchtable
        self.branchtable = {}
        self.branchtable["ldi"] = self.handle_ldi
        self.branchtable["prn"] = self.handle_prn
        self.branchtable["hlt"] = self.handle_hlt
        self.branchtable["mul"] = self.handle_mul

        #create push and pop
        self.sp = 255
        self.branchtable["push"] = self.handle_push
        self.branchtable["pop"] = self.handle_pop

        #create call, ret and add
        self.branchtable["call"] = self.handle_call
        self.branchtable["ret"] = self.handle_ret
        self.branchtable["add"] = self.handle_add

    def handle_call(self):
        pass

    def handle_ret(self):
        pass

    def handle_add(self):
        pass

    def handle_pop(self):
        self.sp += 1
        num_pop = self.ram[self.sp]
        index = int(operand_a, 2)
        self.reg[index] = num_pop

        self.pc += 2

    def handle_push(self):
        index = int(operand_a, 2)
        num_push = self.reg[index]
        self.ram[self.sp] = num_push
        self.pc += 2
        self.sp -= 1


    def handle_ldi(self, operand_a, operand_b):
        self.reg[int(operand_a, 2)] = operand_b
        self.pc += 3

    def handle_prn(self, operand_a):
        print(int(self.reg[int(operand_a, 2)], 2))
        self.pc += 2

    def handle_htl(self):
        sys.exit(1)
        print("Halt!")

    def handle_mul(self, operand_a, operand_b):
        num1 = self.reg[int(operand_a, 2)]
        num2 = self.reg[int(operand_b, 2)]
        answer_mul = int(num1, 2) * int(num2, 2)

        self.reg[int(operand_a, 2)] = bin(answer_mul)
        self.pc += 3

    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        ldi = bin(0b10000010)

        prn = bin(0b01000111)

        hlt = bin(0b00000001)

        mul = bin(0b10000010)

        push = bin(0b01000101)

        pop = bin(0b1000110)

        call = bin(0b0101000)

        ret = bin(0b00010001)

        add = bin(0b10100000)

        run = True

        while run:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if ir == mul:
                self.branchtable['mul'](operand_a, operand_b)

            if ir == ldi:
                self.branchtable['mul'](operand_a, operand_b)

            if ir == prn:
                self.branchtable['prn'](operand_a)

            if ir == push:
                self.branchtable['push'](operand_a)

            if ir == pop:
                self.branchtable['pop'](operand_a)

            if ir == call:
                self.branchtable['call']()

            if ir == ret:
                self.branchtable['ret']()

            if ir == add:
                self.branchtable['add']()

            elif ir == hlt:
                self.branchtable['hlt']()
