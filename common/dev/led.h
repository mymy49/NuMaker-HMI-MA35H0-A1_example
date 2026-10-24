/*
 * Copyright (c) 2026 Yoon-Ki Hong
 *
 * This file is subject to the terms and conditions of the MIT License.
 * See the file "LICENSE" in the main directory of this archive for more details.
 */

#ifndef DEV_LED__H_
#define DEV_LED__H_

namespace led
{
	void initialize();

	void setRed(bool on);

	void setGreen(bool on);

	void setYellow(bool on);
}

#endif

