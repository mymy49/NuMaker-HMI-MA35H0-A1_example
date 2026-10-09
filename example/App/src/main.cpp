/*
 * Copyright (c) 2026 Yoon-Ki Hong
 *
 * This file is subject to the terms and conditions of the MIT License.
 * See the file "LICENSE" in the main directory of this archive for more details.
 */

#include <stdio.h>
#include <yss.h>
#include <util/runtime.h>

triggerId_t gId;

void thread_test1()
{
	while(1)
	{
		if(runtime::getMsec() > 5000)
			return;
	}
}

void thread_test2()
{
	while(1)
	{
		thread::delay(100);
		trigger::run(gId);
	}
}

void trigger_test()
{
	printf("%d\r", (uint32_t)runtime::getMsec());
}

int main(void) 
{
	initializeYss();

	gId = trigger::add(trigger_test, 10 * 1024);

	thread::add(thread_test1, 10 * 1024);
	thread::add(thread_test2, 10 * 1024);

    while (1)
    {
		thread::yield();
    }
}
