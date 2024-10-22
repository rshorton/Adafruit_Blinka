"""CELERON J41X5 pin names"""

from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

# gpiochip0
GPIO_60  = Pin((0, 60))
GPIO_61  = Pin((0, 61))

UART0_RXD = GPIO_60
UART0_TXD = GPIO_61

#gpiochip 1
GPIO_79   = Pin((1, 3))
GPIO_80   = Pin((1, 4))
GPIO_81   = Pin((1, 5))
GPIO_82   = Pin((1, 6))
GPIO_83   = Pin((1, 7))
GPIO_88   = Pin((1, 12))
GPIO_110  = Pin((1, 34))
GPIO_111  = Pin((1, 35))
GPIO_112  = Pin((1, 36))
GPIO_113  = Pin((1, 37))
GPIO_114  = Pin((1, 38))
GPIO_115  = Pin((1, 39))
GPIO_134  = Pin((1, 58))
GPIO_136  = Pin((1, 60))
GPIO_137  = Pin((1, 61))
GPIO_139  = Pin((1, 63))
GPIO_140  = Pin((1, 64))
GPIO_141  = Pin((1, 65))
GPIO_143  = Pin((1, 67))
GPIO_145  = Pin((1, 69))
GPIO_146  = Pin((1, 70))

I2C5_SDA = GPIO_110
I2C5_SCL = GPIO_111

SDA = I2C5_SDA
SCL = I2C5_SCL

SPI0_MOSI = GPIO_83
SPI0_MISO = GPIO_82
SPI0_CLK  = GPIO_79

FS0  = GPIO_80
FS1  = GPIO_81

I2C6_SDA  = GPIO_112
I2C6_SCL  = GPIO_113

#gpiochip 2
GPIO_161    = Pin((2, 5))
GPIO_162   = Pin((2, 6))
GPIO_163   = Pin((2, 7))
GPIO_164   = Pin((2, 8))
GPIO_165   = Pin((2, 9))

# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((0, SPI0_CLK, SPI0_MISO, SPI0_MOSI),)

# ordered as uartId, txId, rxId
uartPorts = ((0, UART0_TXD, UART0_RXD),)

# ordered as i2cId, sclId, sdaId
i2cPorts = (
    # It was found that on some power cycles/reboots, I2C 2 would be
    # linked to the wrong hardware module.  Specifically, "i2c_designware.1"
    # is used for the I2C interface on pins I2C5_SCL/SDA.  To avoid this,
    # a udev rule was created to link "i2c_designware.1" to I2C bus 10.  Bus 10 was
    # used to avoid the bus numbers typically used.
    # In: /etc/udev/rules.d/71-i2c.odyssey.rules
    #    SUBSYSTEM=="i2c-dev", KERNELS=="i2c_designware.1", SYMLINK+="i2c-10"
    (10, I2C5_SCL, I2C5_SDA)
#    (6, I2C6_SCL, I2C6_SDA),
)