/*
 * Copyright (c) 2026 Yoon-Ki Hong
 *
 * This file is subject to the terms and conditions of the MIT License.
 * See the file "LICENSE" in the main directory of this archive for more details.
 */

#include <bsp.h>
#include <yss/instance.h>
#include <yss/debug.h>

void initializeBoard(void)
{
	led::initialize();
	
	// EMAC
	gpioE.lock();
	gpioE.setAsAltFunc(0, Gpio::PE0_RMII0_MDC, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(1, Gpio::PE1_RMII0_MDIO, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(2, Gpio::PE2_RMII0_TXEN, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(3, Gpio::PE3_RMII0_TXD0, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(4, Gpio::PE4_RMII0_TXD1, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(5, Gpio::PE5_RMII0_REFCLK, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(6, Gpio::PE6_RMII0_CRSDV, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(7, Gpio::PE7_RMII0_RXD0, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(8, Gpio::PE8_RMII0_RXD1, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.setAsAltFunc(9, Gpio::PE9_RMII0_RXERR, Gpio::AF_PUSH_PULL, Gpio::SLEWRATE_FAST);
	gpioE.unlock();

	Ethernet::config_t eth0Config = 
	{
		{0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF},	// uint8_t macAddress[6];
		8,										//uint16_t rxDescriptorCount;
		8,										//uint16_t txDescriptorCount;
	};
	
	emac0.lock();
	emac0.enableClock();
	emac0.initialize(eth0Config);
	emac0.setPhysicalLayerAddress(1);
	emac0.enableInterrupt();
	emac0.unlock();
}
