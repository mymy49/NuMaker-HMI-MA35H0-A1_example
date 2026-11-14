/*
 * Copyright (c) 2026 Yoon-Ki Hong
 *
 * This file is subject to the terms and conditions of the MIT License.
 * See the file "LICENSE" in the main directory of this archive for more details.
 */

#include <bsp.h>
#include <yss/instance.h>
#include <yss/debug.h>

void initializeBoard()
{

}

void initializeSystem()
{
    __disable_irq();

    CLK->SYSCLK1 |= CLK_SYSCLK1_GPGCKEN_Msk;
    SYS->GPG_MFPH = (SYS->GPG_MFPH & ~0xFFFFF000UL) | 0x33333000UL;
    
	while (1)
    {
        __NOP();
	}
}

void initializeSystem1()
{
    __disable_irq();
    SYS->CA35WRBADR1 = 0;
    while (1)
    {
        uintptr_t bootAddr = SYS->CA35WRBADR1;
        if (bootAddr != 0)
        {
            void (*jumpToReset)(void) = (void (*)(void))bootAddr;
            jumpToReset();
        }
        __NOP();
    }
}
