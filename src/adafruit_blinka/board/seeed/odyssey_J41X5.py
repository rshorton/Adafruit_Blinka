"""Pin definitions for 40-pin Seeed Odyessy models."""

from adafruit_blinka.microcontroller.celeron.j41X5 import pin

D3 = pin.GPIO_110
D5 = pin.GPIO_111
D7 = pin.GPIO_161
D8 = pin.GPIO_61
D10 = pin.GPIO_60
D11 = pin.GPIO_88
D12 = pin.GPIO_162
D13 = pin.GPIO_136
D15 = pin.GPIO_137
D16 = pin.GPIO_145
D18 = pin.GPIO_146
D19 = pin.GPIO_83
D21 = pin.GPIO_82
D22 = pin.GPIO_114
D23 = pin.GPIO_79
D24 = pin.GPIO_80
D26 = pin.GPIO_81
D27 = pin.GPIO_112
D28 = pin.GPIO_113
D29 = pin.GPIO_139
D31 = pin.GPIO_140
D32 = pin.GPIO_115
D33 = pin.GPIO_141
D35 = pin.GPIO_163
D36 = pin.GPIO_134
D37 = pin.GPIO_143
D38 = pin.GPIO_164
D40 = pin.GPIO_165

SDA = pin.I2C5_SDA
SCL = pin.I2C5_SCL

ID_SD = pin.I2C6_SDA
ID_SCL = pin.I2C6_SCL

MOSI = pin.SPI0_MOSI
MOSO = pin.SPI0_MISO
SCLK = pin.SPI0_CLK

TXD = pin.UART0_TXD
RXD = pin.UART0_RXD

CE0 = pin.FS0
CE1 = pin.FS1