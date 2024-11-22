import smbus2
import time

# I2C Address of LTR390
LTR390_ADDR = 0x53

# I2C bus initialization
bus = smbus2.SMBus(1)

def read_uv_and_light():
    # Read UV and ALS values (6 bytes of data)
    try:
        data = bus.read_i2c_block_data(LTR390_ADDR, 0x0D, 6)
        als = (data[0] << 16) | (data[1] << 8) | data[2]
        uvs = (data[3] << 16) | (data[4] << 8) | data[5]
        return als, uvs
    except Exception as e:
        print(f"Error reading data: {e}")
        return None, None

def setup_sensor():
    try:
        # Activate UV/ALS mode
        bus.write_byte_data(LTR390_ADDR, 0x00, 0x02)
        # Set measurement rate (100ms) and gain (default 3x)
        bus.write_byte_data(LTR390_ADDR, 0x04, 0x22)
        bus.write_byte_data(LTR390_ADDR, 0x05, 0x02)
        print("LTR390 initialized successfully!")
    except Exception as e:
        print(f"Error initializing sensor: {e}")

if __name__ == "__main__":
    setup_sensor()
    while True:
        als, uvs = read_uv_and_light()
        if als is not None and uvs is not None:
            uv_index = uvs / 2300.0  # Convert UV raw data to approximate UV index
            print(f"Ambient Light: {als}, UV Index: {uv_index:.2f}")
        time.sleep(1)
