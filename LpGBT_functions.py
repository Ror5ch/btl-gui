import sys # For sys.argv and sys.exit
sys.path.append('/opt/rh/python210/root/usr/lib64/python2.10/lib-tk')
import os
import random # For randint
import time
#from __future__ import division, with_statement, print_function
import sys
import binascii

import logging
from lpgbt_control_lib import LpgbtV1

#############################################################################
# low level access to control pins
GPIO_MAP = [
#    LpgbtV0.CTRL_RSTB: 0,
#    LpgbtV0.CTRL_ADDR: 1,
    # ... add a mapping to your hardware GPIOs for all control pins
    LpgbtV1.CTRL_RSTB,
    LpgbtV1.CTRL_LOCKMODE,
    LpgbtV1.CTRL_PORDIS
]

def write_lpgbt_ctrl_pin(pin_name, value):
    gpio_id = GPIO_MAP[pin_name]
    # TODO: write 'value' to your hardware GPIO

def read_lpgbt_ctrl_pin(pin_name):
    gpio_id = GPIO_MAP[pin_name]
    gpio_val = # TODO read value of hardware GPIO
    return gpio_val

# low level access to I2C interface
def write_lpgbt_regs_i2c(reg_addr, reg_vals):
    some_i2c_master.write_regs(
        device_addr=0x70
        addr_width=2,
        reg_addr=reg_addr,
        data=reg_vals
    )

def read_lpgbt_regs_i2c(reg_addr, read_len):
    values = some_i2c_master.read_regs(
        device_addr=0x70,
        addr_width=2,
        reg_addr=reg_addr,
        read_len=read_len
    )
    return values

def main(types, lpgbt_num, bit_num, lpgbt_version):
	# get a logger for lpGBT library logging
    lpgbt_logger = logging.getLogger("lpgbt")

    # instantiate lpGBT class
    lpgbt = LpgbtV1(logger=lpgbt_logger)
    if (lpgbt_version == "LpgbtV0"):
        from lpgbt_control_lib import LpgbtV0
        lpgbt = LpgbtV0(logger=lpgbt_logger)

    # register communications interface(s)
    lpgbt.register_comm_intf(
        name="I2C",
        write_regs=write_lpgbt_regs_i2c,
        read_regs=read_lpgbt_regs_i2c,
        default=True
    )

    # register access methods to control pins
    lpgbt.register_ctrl_pin_access(
        write_pin=write_lpgbt_ctrl_pin,
        read_pin=read_lpgbt_ctrl_pin
    )

    # communicate with your chip
    lpgbt.generate_reset_pulse()
    lpgbt.clock_generator_setup()

    if (types == "on"):
        lpgbt.gpio_set_dir(dir_) # needs direction sent
        #lpgbt.gpio_set_dir_bit(bit, value) # needs bit and value sent
        lpgbt.gpio_set_drive(drive_strength) # needs drive strength sent
        #lpgbt.gpio_set_drive_bit(bit, drive_strength) # needs bit and drive_strength sent

        # need to do read_write command



    # in order to use a different communication interface
    #lpgbt.adc_convert(..., comm_intf="I2C")
    #lpgbt.adc_convert(..., comm_intf="EC")
    #lpgbt.adc_convert(..., comm_intf="IC")


if __name__ == "__main__":
    	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

