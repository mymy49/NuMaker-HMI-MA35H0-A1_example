#include "led.h"
#include <yss/instance.h>

namespace led
{
	void initialize()
	{
		gpioN.setAsOutput(6); // Red
		gpioN.setAsOutput(7); // Green
		gpioN.setAsOutput(10); // Yellow

		setRed(false);
		setGreen(false);
		setYellow(false);
	}

	void setRed(bool on)
	{
		gpioN.setOutput(6, !on);
	}

	void setGreen(bool on)
	{
		gpioN.setOutput(7, !on);
	}

	void setYellow(bool on)
	{
		gpioN.setOutput(10, !on);
	}
}