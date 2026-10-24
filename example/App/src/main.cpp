/*
 * Copyright (c) 2026 Yoon-Ki Hong
 *
 * This file is subject to the terms and conditions of the MIT License.
 * See the file "LICENSE" in the main directory of this archive for more details.
 */

#include <stdio.h>
#include <yss.h>
#include <bsp.h>
#include <util/runtime.h>

void thread_blinkRed();
void thread_blinkGreen();
void thread_blinkYellow();

int main(void) 
{
	initializeYss();

	initializeBoard();

	thread::add(thread_blinkRed, 4 * 1024);
	thread::add(thread_blinkGreen, 4 * 1024);
	thread::add(thread_blinkYellow, 4 * 1024);

    while (1)
    {
		thread::yield();
    }
}

void thread_blinkRed()
{
	while(1)
	{
		led::setRed(true);
		thread::delay(500);

		led::setRed(false);
		thread::delay(500);
	}
}

void thread_blinkGreen()
{
	while(1)
	{
		led::setGreen(true);
		thread::delay(250);

		led::setGreen(false);
		thread::delay(250);
	}
}

void thread_blinkYellow()
{
	while(1)
	{
		led::setYellow(true);
		thread::delay(125);

		led::setYellow(false);
		thread::delay(125);
	}
}


